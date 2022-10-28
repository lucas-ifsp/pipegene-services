import json 
from pathlib import Path
import uuid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



def plot_snv(title, variantsPercentageDict):
    
    with open(variantsPercentageDict, 'r') as json_file:
        j =json_file.read()
        
        try: 
            data = json.loads(j)
            print(j)
        except json.decoder.JSONDecodeError as e: 
            print("deu ruim (json invalido)")
            print(e)

    
    colorList = ['tab:blue', 'tab:cyan', 'tab:purple', 'tab:gray', 'tab:orange', 'tab:red',
    'lightcyan', 'salmon', 'wheat', 'fuchsia', 'tab:green', 'tab:brown','tab:pink',
    'midnightblue', 'tomato', 'yellow', 'goldenrod', 'indigo', 'violet']

    _, ax = plt.subplots(figsize=(15, 15))
    

    variantsName  = [*data.keys()]
    variantsPercentage = [*data.values()]

    y_pos = np.arange(len(variantsName))

    ax.barh(y_pos, variantsPercentage, color=colorList[:5])
    ax.set_title(title)

    plt.yticks(y_pos, variantsName)

    for x, v in enumerate(variantsPercentage): 
        ax.text(v, x, str(v), color='black')

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  
    plt.tight_layout(h_pad=2.5, w_pad=1)

    figure_path = Path("static/file_" + str(uuid.uuid4())+'.png')
    plt.savefig(figure_path, format='png', dpi=250,bbox_inches='tight')
    
    filename = str(figure_path)
    #print(filename)
    return filename
    