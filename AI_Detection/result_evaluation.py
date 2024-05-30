import pandas as pd
import ast

df = pd.read_csv('AI_Detection/results/Ai_Detection_result.csv')

#check if in every part there is at least one plagiated sentence
abstract_count=0
intro_count=0
conclusion_count=0
complete_count=0

for i  in range(len(df)):
    
    string_data = df['abstract_sentence'][i] #all sentence of first element
    abstract_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['intro_sentence'][i] #all sentence of first element
    intro_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['conclusion_sentence'][i] #all sentence of first element
    conclusion_data = ast.literal_eval(string_data) #convert to tuple to access them

    #check if at least one sentence in abstract is AI GENERATED
    abstract_flag=False
    for ele in abstract_data:
        if ele[1]>0.5 and not abstract_flag:
            abstract_count +=1
            abstract_flag=True

    intro_flag=False
    for ele in intro_data:
        if ele[1]>0.5 and not intro_flag:
            intro_count +=1
            intro_flag=True    

    conclusion_flag=False
    for ele in conclusion_data:
        if ele[1]>0.5 and not conclusion_flag:
            conclusion_count +=1
            conclusion_flag=True 
    
    if abstract_flag or conclusion_flag or intro_flag:
        complete_count +=1
    else:
        print(df.iloc[i]['plagiated_file'])


print(f'the accuracy of AI detecion for ABSTRACT is {abstract_count/len(df)}')
print(f'the accuracy of AI detecion for INTRO is {intro_count/len(df)}')
print(f'the accuracy of AI detecion for CONCLUSION is {conclusion_count/len(df)}')
print(f'Without the intro part the accuracy of AI Detection on all the document is {complete_count/len(df)}')
#we not include the intro part because it a part of it is completly generated, also for future work test the model on longer abstract or conclusion, because the more the sentence
#the more the possibility of detection
#For future work we can use a different model for the AI Detection
#We have to computate how much the sentence are rephrase and how much they are keep the same

