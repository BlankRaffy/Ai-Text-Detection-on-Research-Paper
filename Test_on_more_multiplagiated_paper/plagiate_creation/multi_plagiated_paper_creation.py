import multi_plagiated_function
import os
import xml.etree.ElementTree as ET
import tqdm
import pandas as pd

''' TEST ON A SINGLE FILE
file_path= 'original_paper\PMC13901.xml'

tree = ET.parse(file_path)

tree = plagiated_function.change_abstract(tree)
tree = plagiated_function.change_intro(tree)
tree = plagiated_function.change_conclusion(tree)

#save the final xml file with all the modified part:
plagiated_function.save_tree(file_path,tree)

folder = 'Dataset/original_paper'
for ele in tqdm.tqdm(os.listdir(folder)):

    absolute_path = folder+'/'+ele
    
    tree = ET.parse(absolute_path)

    tree = plagiated_function.change_abstract(tree)
    tree = plagiated_function.change_intro(tree)
    tree = plagiated_function.change_conclusion(tree)

    #save the final xml file with all the modified part:
    plagiated_function.save_tree(absolute_path,tree)
'''

df = pd.read_csv('Similarity_Compare/top_k_for_similarity/paper_topic_similarity_rank.csv') #ci stiamo basando su quelli che in precedenza avevano il final score più alto

columns=['input_file','list_of_source_file']
df_multi_plagiated_source=pd.DataFrame(columns=columns)

# Ordina per 'input_file' e 'final_score' in ordine decrescente
df_sorted = df.sort_values(by=['input_file', 'final_score'], ascending=[True, False])

# Prendi i primi 3 per ogni 'input_file'
df_top3 = df_sorted.groupby('input_file').head(3)


# Accedi ai primi 3 elementi del primo gruppo
first_input_file = df_top3['input_file'].unique()[0] #primo elemento 
df_first_input_file = df_top3[df_top3['input_file'] == first_input_file] #top_3 per il primo elemtno

file_list=[]

for i in range(len(df_first_input_file)): #iteriamo sui primi 3 elementi e ci salviamo i nomi dei file
    file_list.append(df_first_input_file.iloc[i]['compare_file'])

new_row = {'input_file':df_first_input_file.iloc[i]['input_file'],'list_of_source_file':file_list}

df_multi_plagiated_source = pd.concat([df_multi_plagiated_source, pd.DataFrame([new_row])], ignore_index=True)

original_dataset='Dataset/original_paper'

absolute_path_abstract = original_dataset+'/'+file_list[0]
    
abstract_tree = ET.parse(absolute_path_abstract)
'''
tree = multi_plagiated_function.change_abstract(tree)
tree = plagiated_function.change_intro(tree)
tree = plagiated_function.change_conclusion(tree)

#save the final xml file with all the modified part:
plagiated_function.save_tree(absolute_path,tree)

'''




