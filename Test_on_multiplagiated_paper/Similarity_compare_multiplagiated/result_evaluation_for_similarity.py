import pandas as pd
import ast

df_abstract = pd.read_csv('Test_on_multiplagiated_paper/Similarity_compare_multiplagiated/top-k_rank/top_abstract_scores_LDA.csv').groupby('input_file')
df_intro = pd.read_csv('Test_on_multiplagiated_paper/Similarity_compare_multiplagiated/top-k_rank/top_intro_scores_LDA.csv').groupby('input_file')
df_conclusion = pd.read_csv('Test_on_multiplagiated_paper/Similarity_compare_multiplagiated/top-k_rank/top_conclusion_scores_LDA.csv').groupby('input_file')
df_source= pd.read_csv('Test_on_multiplagiated_paper\multiplagiated_source.csv')
df_source['list_of_source_file'] = df_source['list_of_source_file'].apply(ast.literal_eval)

i=0
abstrac_result=0
for ele in df_abstract:
    for item in ele[1]['compare_file']:
        if (df_source.iloc[i]['list_of_source_file'][0]) == item: #the first one is the one from we get the abstract
            abstrac_result +=1
    i+=1



i=0
intro_result=0
for ele in df_intro:
    for item in ele[1]['compare_file']:
        #test=df_source.iloc[i]['list_of_source_file'][1]
        #print(f'source file is : {test} the file on the group is {item}' )
        if (df_source.iloc[i]['list_of_source_file'][1]) == item: #the second one is the one from we get the intro
            intro_result +=1
    i+=1


i=0
conclusion_result=0
for ele in df_conclusion:
    for item in ele[1]['compare_file']:
        if (df_source.iloc[i]['list_of_source_file'][2]) == item: #the third one is the one from we get the abstract
            conclusion_result +=1
    i+=1

print(f'precision on abstact with top-5 is {abstrac_result/174}')   
print(f'precision on intro with top-5 is {intro_result/174}')  
print(f'precision on conclusion with top-5 is {conclusion_result/174}')  