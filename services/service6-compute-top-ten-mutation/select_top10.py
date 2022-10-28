import json 
import datetime 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import uuid

def select_top10(maf_file_name):
    data = pd.read_csv(maf_file_name, sep="\t", comment="#", low_memory=False)

    top10GenesNames=[]
    variantClassificationType=[]
    for g in data['Hugo_Symbol'].value_counts()[:10].index.tolist():
        top10GenesNames.append(g)
        for v in data[data["Hugo_Symbol"]==g]["Variant_Classification"].value_counts().index.tolist():
            variantClassificationType.append(v)

    variantClassificationType=set(variantClassificationType)
    topGenesVariations_df = pd.DataFrame(0, index=top10GenesNames, columns=variantClassificationType)
    for g in data['Hugo_Symbol'].value_counts()[:10].index.tolist():
        for v in data[data["Hugo_Symbol"]==g]["Variant_Classification"].value_counts().items():
            topGenesVariations_df[v[0]][g]=v[1]
    topGenesVariations_df=topGenesVariations_df.append(topGenesVariations_df.agg(['sum']))
    topGenesVariations_df=topGenesVariations_df.sort_values(by ='sum', axis=1,ascending=False)

    bars=[]
    for c in topGenesVariations_df.columns:
        bars.append(list(topGenesVariations_df[c][:10]))
    
    dictionary = {
        "bars": bars,
        "top10GenesNames": top10GenesNames

    }
    result = dictionary
    filename = "static/file_{}.json".format(datetime.datetime.now().isoformat())
    with open(filename, "w+") as f: 
        json.dump(result, f)

    return filename

# maf = "BRCA1_data_mutations_extended.txt"
# select_top10(maf)