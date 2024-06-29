import pandas as pd

df=pd.read_csv('AI_Detection/support_and_confidence/support_and_confidence_plagiated_no_semantic_filter.csv')
threshold_result_abstract=0
abstract_zero=0
threshold_result_intro=0
intro_zero=0
threshold_result_conclusion=0
conclusion_zero=0


for ele in df.iterrows():
    dic_abstract=eval(ele[1]['abstract_result'])
    #print(dic_abstract)
    if(dic_abstract['support'])>0.5 and (dic_abstract['confidence'])>0.6 :
        threshold_result_abstract+=1
    if(dic_abstract['support'])==0:
        abstract_zero+=1

    dic_intro=eval(ele[1]['intro_result'])
    #print(dic_intro)
    if(dic_intro['support'])>0.45 and (dic_intro['confidence'])>0.6 :
        threshold_result_intro+=1
    if(dic_intro['support'])==0:
        intro_zero+=1

    dic_conclusion=eval(ele[1]['conclusion_result'])
    #print(dic_intro)
    if(dic_conclusion['support'])>0.4 and (dic_conclusion['confidence'])>0.6 :
        threshold_result_conclusion+=1
    if(dic_conclusion['support'])==0:
        conclusion_zero+=1

print(f'Using a threshold for support set at 0.5 and confidence set at 0.6 for ABSTRACT we have {threshold_result_abstract/(len(df)-abstract_zero)}')
print(f'Number of file that pass detectio {threshold_result_abstract} on {len(df)}' )

print(f'Using a threshold for support set at 0.45 and confidence set at 0.6 for INTRO we have {threshold_result_intro/(len(df)-intro_zero)}')
print(f'Number of file that pass detectio {threshold_result_intro} on {len(df)}' )

print(f'Using a threshold for support set at 0.45 and confidence set at 0.6 for CONCLUSION we have {threshold_result_conclusion/(len(df)-conclusion_zero)}')
print(f'Number of file that pass detectio {threshold_result_conclusion} on {len(df)}' )
