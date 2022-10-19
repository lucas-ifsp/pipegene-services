import json 
# import datetime 
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import uuid
# import pandas as pd


def plot_maf(variants_percentage_dict, title):
    colors = ['tab:blue', 'tab:cyan', 'tab:purple', 'tab:gray', 'tab:orange', 'tab:red',
              'lightcyan', 'salmon', 'wheat', 'fuchsia', 'tab:green', 'tab:brown', 'tab:pink',
              'midnightblue', 'tomato', 'yellow', 'goldenrod', 'indigo', 'violet']

    with open(variants_percentage_dict, 'r') as json_file:
        j =json_file.read()
        
        try: 
            data = json.loads(j)
            print(j)
        except json.decoder.JSONDecodeError as e: 
            print("deu ruim (json invalido)")
            print(e)

    figure_path = Path("static/file_" + str(uuid.uuid4())+'.png')
    _, ax = plt.subplots(figsize=(15, 15))

    variants_name = [*data.keys()]
    variants_percentage = [*data.values()]

    y_pos = np.arange(len(variants_name))

    ax.barh(y_pos, variants_percentage, color=colors[:5])
    ax.set_title(title)

    plt.yticks(y_pos, variants_name)

    for x, v in enumerate(variants_percentage):
        ax.text(v, x, str(v)+'%', color='black')

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.tight_layout(h_pad=2.5, w_pad=1)
    
    plt.savefig(figure_path, format='png', dpi=250, bbox_inches='tight')

    filename = str(figure_path)
    print(filename)
    return filename
    


    