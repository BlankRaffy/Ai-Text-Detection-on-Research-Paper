import pandas as pd
import ast

df_abstract= pd.read_csv('top_abstract_scores.csv').groupby('input_file')
df_source= pd.read_csv('Test_on_multiplagiated_paper\multiplagiated_source.csv')
df_source['list_of_source_file'] = df_source['list_of_source_file'].apply(ast.literal_eval)

i=0
result=0
for ele in df_abstract:
    for item in ele[1]['compare_file']:
        if (df_source.iloc[i]['list_of_source_file'][0]) == item:
            result +=1
    i+=1

print(f'precision on abstact with top-5 is {result/174}')   