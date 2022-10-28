import json 
import datetime 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import uuid




def plot_top10(bars_top10GenesNames_dict, title):
    
    colorList = ['tab:blue', 'tab:cyan', 'tab:purple', 'tab:gray', 'tab:orange', 'tab:red',
    'lightcyan', 'salmon', 'wheat', 'fuchsia', 'tab:green', 'tab:brown','tab:pink',
    'midnightblue', 'tomato', 'yellow', 'goldenrod', 'indigo', 'violet']
    figure_path = Path("static/file_" + str(uuid.uuid4())+'.png')
    
    with open(bars_top10GenesNames_dict, 'r') as json_file:
        j =json_file.read()
        
        try: 
            data = json.loads(j)
            print(j)
        except json.decoder.JSONDecodeError as e: 
            print("deu ruim (json invalido)")
            print(e)
    
    _, ax = plt.subplots(figsize=(15, 8))

    bars = data["bars"]
    top10GenesNames = data["top10GenesNames"]

    npBars=np.array(bars)
    plotBars=[]

    ind = [9,8,7,6,5,4,3,2,1,0]
    plt.yticks(ind, top10GenesNames)

    for index in range(len(bars)):
        if(index==0):        
            plotBars.append(ax.barh(ind,bars[index],color=colorList[index]))
            sumPrevious=npBars[index]
        else:
            plotBars.append(ax.barh(ind,bars[index],left=sumPrevious,color=colorList[index]))
            sumPrevious+=npBars[index]

    ax.set_title(title)

    xmin, xmax = plt.xlim()
    plt.xlim(xmin, xmax+xmax*0.05)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  
    plt.tight_layout(h_pad=2.5, w_pad=1)

    plt.savefig(figure_path, format='png', dpi=250,bbox_inches='tight')


    filename = str(figure_path)

    return filename
