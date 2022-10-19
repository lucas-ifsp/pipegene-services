import requests
import json 
import datetime 
import pandas as pd

def snvDict(parameter):
    maf_fields = ["Hugo_Symbol", "Chromosome", "Start_Position", "End_Position", "Reference_Allele", "Tumor_Seq_Allele2", "Variant_Classification", "Variant_Type", "Tumor_Sample_Barcode"]

    maf = pd.read_csv(parameter, sep="\t", usecols=maf_fields,comment="#")
    aux_df = maf[[ x in ('A', 'C', 'G', 'T') for x in maf['Reference_Allele']]]
    reference_Alleles_len =set(aux_df['Reference_Allele'])

    aux_df = maf[[ x in ('A', 'C', 'G', 'T') for x in maf['Tumor_Seq_Allele2']]]
    tumor_Seq_Allele2_len =set(aux_df['Tumor_Seq_Allele2'])

    reference_Alleles_len =sorted(reference_Alleles_len )
    tumor_Seq_Allele2_len =sorted(tumor_Seq_Allele2_len )

    snvClass={}
    for r in reference_Alleles_len :
        for t in tumor_Seq_Allele2_len :
            if(r != t):
                key=str(r)+'>'+str(t)
                snvClass[key]=len(maf.loc[(maf['Reference_Allele']==r) & (maf['Tumor_Seq_Allele2']==t)])

    snvToPlot={}
    for r in ['C','T']:
        for t in ['A', 'C', 'G', 'T']:
            if(r != t):
                key=str(r)+'>'+str(t)
                snvToPlot[key]=snvClass[key]

    snvToPlot['C>A']+=snvClass['G>T']
    snvToPlot['C>G']+=snvClass['G>C']
    snvToPlot['C>T']+=snvClass['G>A']
    snvToPlot['T>A']+=snvClass['A>T']
    snvToPlot['T>C']+=snvClass['A>G']
    snvToPlot['T>G']+=snvClass['A>C']

    # json_object = json.dumps(snvToPlot, indent = 4) 
    result = snvToPlot
    filename = "static/file_{}.json".format(datetime.datetime.now().isoformat())
    with open(filename, "w") as f: 
        json.dump(result, f)


   
    
    return filename

# # # maf = pd.read_csv("BRCA1_data_mutations_extended.txt", sep="\t")
# maf = "BRCA1_data_mutations_extended.txt"
# # print(snvDict(maf))

# json_file_path =  snvDict(maf)

# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())
#      print(contents)