import os
import xml.etree.ElementTree as ET
import tqdm
import pandas as pd
import xml_creation_function


df = pd.read_csv('Similarity_Compare/top_k_for_similarity/paper_topic_similarity_rank.csv') #ci stiamo basando su quelli che in precedenza avevano il final score più alto

columns=['input_file','list_of_source_file']
df_multi_plagiated_source=pd.DataFrame(columns=columns)

# Ordina per 'input_file' e 'final_score' in ordine decrescente
df_sorted = df.sort_values(by=['input_file', 'final_score'], ascending=[True, False])

# Prendi i primi 3 per ogni 'input_file'
df_top3 = df_sorted.groupby('input_file').head(3)

output_folder='Test_on_more_multiplagiated_paper/multi_plagiated_paper'

for i in tqdm.tqdm(range (2)): #we divide 3 beacuse there are three occuorance of group (int(len(df_top3)/3))
# Accedi ai primi 3 elementi del primo gruppo
    first_input_file = df_top3['input_file'].unique()[i] #primo elemento 
    df_first_input_file = df_top3[df_top3['input_file'] == first_input_file] #top_3 per il primo elemtno

    file_list=[]

    for j in range(len(df_first_input_file)): #iteriamo sui primi 3 elementi e ci salviamo i nomi dei file
        file_list.append(df_first_input_file.iloc[j]['compare_file'])

    new_row = {'input_file':df_first_input_file.iloc[0]['input_file'],'list_of_source_file':file_list}

    df_multi_plagiated_source = pd.concat([df_multi_plagiated_source, pd.DataFrame([new_row])], ignore_index=True)

    original_dataset='Dataset/original_paper'

    absolute_path_abstract = original_dataset+'/'+file_list[0]
        
    abstract_tree = ET.parse(absolute_path_abstract)

    absolute_path_intro = original_dataset+'/'+file_list[1]
        
    absolute_path_conclusion = original_dataset+'/'+file_list[2]

    absolute_path_output=output_folder+'/'+df_first_input_file.iloc[0]['input_file'].replace('.xml','_multiplagiated.xml')

    xml_creation_function.save_tree(absolute_path_abstract,absolute_path_intro,absolute_path_conclusion,absolute_path_output)

df_multi_plagiated_source.to_csv('Test_on_more_multiplagiated_paper/multiplagiated_source.csv',index=False)



