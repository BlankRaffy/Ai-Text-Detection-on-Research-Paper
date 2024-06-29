import pandas as pd

df=pd.read_csv('AI_Detection/support_and_confidence/threshold_result.csv')
result=0

for i in range(len(df)):
    if(df.iloc[i]['abstract'] or df.iloc[i]['intro'] or df.iloc[i]['conclusion']):    
        result+=1

print('number of file with at least one section plagiated',result/174)
