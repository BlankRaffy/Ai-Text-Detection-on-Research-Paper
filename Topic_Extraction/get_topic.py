import topic_extraction
import pandas as pd
import os
import tqdm

abstract = []
intro = []
conclusion = []

columns = ['file','abstract','introduction','conclusion']
df_yake = pd.DataFrame(columns= columns)



original_paper = 'Dataset/plagiated_paper' #change to do on the original paper or on the plagiated one

#extract all keyword in all file 
for file in tqdm.tqdm(os.listdir(original_paper)):
    path = original_paper+'/'+file
    abstract,intro,conclusion = topic_extraction.yake_extraction(path)
    new_row = {'file':file, 'abstract': abstract, 'introduction':intro, 'conclusion': conclusion}
    df_yake = pd.concat([df_yake, pd.DataFrame([new_row])], ignore_index=True)

#save the dataframe in csv
csv_file_path = 'Topic_Extraction/topic/plagiated_topic.csv'

# Salva il DataFrame nel file CSV
df_yake.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")

