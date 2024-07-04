import pandas as pd

df=pd.read_csv('AI_Detection/support_and_confidence/support_and_confidence_on_original.csv')
threshold_result_abstract=0
abstract_zero=0
threshold_result_intro=0
intro_zero=0
threshold_result_conclusion=0
conclusion_zero=0

columns=['input_file','abstact','intro','conclusion']
df_result=pd.DataFrame(columns=columns)

for ele in df.iterrows():
    abstract=False
    intro=False
    conclusion=False

    dic_abstract=eval(ele[1]['abstract_result'])
    #print(dic_abstract)
    if(dic_abstract['support'])>0.5 and (dic_abstract['confidence'])>0.6 :
        threshold_result_abstract+=1
        abstract=True
    if(dic_abstract['support'])==0:
        abstract_zero+=1

    dic_intro=eval(ele[1]['intro_result'])
    print(dic_intro)
    if(dic_intro['support'])>0.25 and (dic_intro['confidence'])>0.8:
        threshold_result_intro+=1
        intro=True
    if(dic_intro['support'])==0:
        intro_zero+=1

    dic_conclusion=eval(ele[1]['conclusion_result'])
    #print(dic_intro)
    if(dic_conclusion['support'])>0.5 and (dic_conclusion['confidence'])>0.6:
        threshold_result_conclusion+=1
        conclusion=True
    if(dic_conclusion['support'])==0:
        conclusion_zero+=1

    row={'input_file':ele[1]['plagiated_file'],
         'abstract':abstract,
         'intro':intro,
         'conclusion':conclusion}
    df_result=pd.concat([df_result, pd.DataFrame([row])], ignore_index=True)

print(f'Using a threshold for support set at 0.5 and confidence set at 0.6 for ABSTRACT we have {threshold_result_abstract/(len(df)-abstract_zero)}')
print(f'Number of file that pass detectio {threshold_result_abstract} on {len(df)}' )

print(f'Using a threshold for support set at 0.45 and confidence set at 0.6 for INTRO we have {threshold_result_intro/(len(df)-intro_zero)}')
print(f'Number of file that pass detectio {threshold_result_intro} on {len(df)}' )

print(f'Using a threshold for support set at 0.45 and confidence set at 0.6 for CONCLUSION we have {threshold_result_conclusion/(len(df)-conclusion_zero)}')
print(f'Number of file that pass detectio {threshold_result_conclusion} on {len(df)}' )

df_result.to_csv('AI_Detection/support_and_confidence/threshold_result.csv', index=None)
