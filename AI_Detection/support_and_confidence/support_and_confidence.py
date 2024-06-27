import pandas as pd
import ast
 
df = pd.read_csv('AI_Detection/results/Ai_Detection_result_no_semantic_filter.csv')

intro_zero=0
for i  in range(len(df)):
    
    string_data = df['abstract_sentence'][i] #all sentence of first element
    abstract_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['intro_sentence'][i] #all sentence of first element
    intro_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['conclusion_sentence'][i] #all sentence of first element
    conclusion_data = ast.literal_eval(string_data) #convert to tuple to access them

    intro_confidence=[]
    intro_support=0
    
    for ele in intro_data:
        if ele[1] > 0.50:
            intro_confidence.append(ele[1])
            intro_support+=1

    print(f'Abstact support {intro_support/len(intro_data)}')
    if(sum(intro_confidence)==0):
        print(f'Abstact confidence is 0')
        intro_zero+=1
    else:
        print(f'Abstact confidence {sum(intro_confidence)/len(intro_confidence)}')

print('number of not detected abstact',intro_zero)
