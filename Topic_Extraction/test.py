import pandas as pd

def convert_to_list(string):
    if isinstance(string, str):
        return string.split(',')
    else:
        return []

# Carica il DataFrame dal file CSV, specificando la funzione di conversione per le colonne desiderate
df = pd.read_csv('Topic_Extraction/topic/original_topic.csv', converters={'abstract': convert_to_list, 'introduction': convert_to_list, 'conclusion': convert_to_list})

list = ['left sylvian artery' , 'auto-immune Guillain-Barrè syndrome', 'isolated vasculitis', 'sylvian artery', 'Guillain-Barrè syndrome', 'authors describe']

for item in df.iterrows():
    if item[1]['file']=='PMC29044.xml':
        print(item[1]['abstract'])