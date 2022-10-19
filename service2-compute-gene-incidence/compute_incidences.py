import json 
import datetime 
import pandas as pd



def read_maf(maf_file_name):
    return pd.read_csv(maf_file_name, sep="\t", comment="#", low_memory=False)#filter
    

def computePercentageOfVariant(maf_file_name, variantColumnName):
    maf = read_maf(maf_file_name)
    variantsType = maf[variantColumnName] 
    numberOfMutations = len(variantsType)
    variantQuantityDic  = variantsType.value_counts().to_dict()
    
    variantPercentageDict = {}
    for k, v in variantQuantityDic.items():
        variantPercentageDict[k] = round(v/numberOfMutations*100)

    result = dict(sorted(zip(variantPercentageDict.keys(), variantPercentageDict.values()), reverse=True))
    filename = "static/file_{}.json".format(datetime.datetime.now().isoformat())
    with open(filename, "w+") as f: 
        json.dump(result, f)

    return filename

