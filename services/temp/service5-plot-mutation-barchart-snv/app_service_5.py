import os

from flask import Flask, request, current_app, send_from_directory, jsonify
import tempfile
from task_queue import Tasks
import worker
from plot_mutations_barchart_snv import plot_snv
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = './static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


app.config['MAX_CONTENT_LENGTH'] = 5000 * 1024 * 1024


def processFile(file):
    # Aqui deve ser chamado os códigos/metodos de datascience para executar processamento usando o arquivo recebido via parametro file'
    # a função deve retornar o nome do arquivo, abaixo um exemplo
    return plot_snv("BRCA",file)


# Rota de upload utilizada pela pipegine
@app.route('/v1/pipegine/provider/process', methods=['POST'])
def upload():
    #Recupera parametros enviados pela pipegine
    execution_id = request.headers.get("x-pipegene-execution-id")
    step_id = request.headers.get("x-pipegene-step-id")

    # Criar arquivo temporário que sera usado para guardar conteúdo do arquivo que veio na request da pipegine pela rede
    file = tempfile.NamedTemporaryFile().name
    #Salva conteúdo do arquivo enviado pela pipegine pela rede no arquivo temporário
    request.files['file'].save(file)

    #Chama função para processar arquivo, a função deve retornar o nome do arquivo resultante.
    result = processFile(file)

    # adiciona nova tarefa para ser processada depois
    putNewTask(execution_id, step_id, result)

    # responde para a pipegine
    return jsonify({
        "urlToCheck": "http://localhost:5015/v1/pipegene/{}/status".format(step_id),
        "message": "IN_PROGRESS",
    })

def putNewTask(execution_id, step_id, result):
    Tasks.put({
        "execution_id": execution_id,
        "step_id": step_id,
        "filename": result.replace("static/", "")
    })

# Rota de download usada pela pipegine para baixar o resultado do processamento 
@app.route('/v1/uploads/<path:filename>', methods=['GET'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path=filename, )

if __name__ == '__main__':
    worker.start()
    address = "127.0.0.1"
    app.run(host=address, port=5015)
