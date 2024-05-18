import pandas as pd
import tqdm

data = pd.read_csv('Similarity_Compare/top_k_for_similarity/paper_topic_similarity_rank.csv')
similar = []
count = 0
for i in tqdm.tqdm(range(len(data))):
    #print(data.iloc[i]['input_file'])
    check_file = data.iloc[i]['input_file'].replace('_plagiated.xml', '.xml')
    if(check_file == data.iloc[i]['compare_file']):
        count += 1
        #similar.append(data.iloc[i]['input_file'] + ' ' + data.iloc[i]['compare_file'])
    else:
     similar.append(data.iloc[i]['input_file'] + ' ' + data.iloc[i]['compare_file'])
     

     

print('Using a top-3 we have an accuracy of :',count/174)
