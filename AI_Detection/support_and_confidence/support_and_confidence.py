import pandas as pd
import ast
import tqdm
 
df = pd.read_csv('AI_Detection/results/Ai_Detection_result_NO_semantic_filter.csv')
columns=['plagiated_file','abstract_result','intro_result','conclusion_result']
df_result=pd.DataFrame(columns=columns)

abstract_zero=0
intro_zero=0
conclusion_zero=0

for i  in tqdm.tqdm(range(len(df))):
    
    string_data = df['abstract_sentence'][i] #all sentence of first element
    abstract_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['intro_sentence'][i] #all sentence of first element
    intro_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['conclusion_sentence'][i] #all sentence of first element
    conclusion_data = ast.literal_eval(string_data) #convert to tuple to access them

    abstract_confidence=[]
    abstract_support=0
    intro_confidence=[]
    intro_support=0
    conclusion_confidence=[]
    conclusion_support=0
    
    #evaluation support and confidence on abstract
    for ele in abstract_data:
        if ele[1] > 0.50:
            abstract_confidence.append(ele[1])
            abstract_support+=1
        

    if(abstract_support>0):
        abstract_support=abstract_support/len(abstract_data)
        abstact_confidence_score=sum(abstract_confidence)/len(abstract_confidence)
    else:
        abstract_support=0
        abstact_confidence_score=0
        abstract_zero+=1


    #evaluation support and confidence on intro
    for ele in intro_data:
        if ele[1] > 0.50:
            intro_confidence.append(ele[1])
            intro_support+=1


    if(intro_support>0):
        intro_support=intro_support/len(intro_data)
        intro_confidence_score=sum(intro_confidence)/len(intro_confidence)
    else:
        intro_support=0
        intro_confidence_score=0
        intro_zero+=1



    #evaluation support and confidence on conclusion
    for ele in conclusion_data:
        if ele[1] > 0.50:
            conclusion_confidence.append(ele[1])
            conclusion_support+=1


    if(conclusion_support>0):
        conclusion_support=conclusion_support/len(conclusion_data)
        conclusion_confidence_score=sum(conclusion_confidence)/len(conclusion_confidence)
    else:
        conclusion_support=0
        conclusion_confidence_score=0
        conclusion_zero+=1


    

    new_row = {'plagiated_file':df.iloc[i]['plagiated_file'],
               'abstract_result':{'support':abstract_support,'confidence':abstact_confidence_score},
               'intro_result':{'support':intro_support,'confidence':intro_confidence_score},
               'conclusion_result':{'support':conclusion_support,'confidence':conclusion_confidence_score}}
    
    '''print(f'Abstact support {abstract_support}')
    print(f'Abstact confidence {sum(abstract_confidence)/len(abstract_confidence)}')
    print(f'Intro support {intro_support}')
    print(f'Intro confidence {sum(intro_confidence)/len(intro_confidence)}')
    print(f'Conclusion support {conclusion_support}')
    print(f'Conclusion confidence {sum(conclusion_confidence)/len(conclusion_confidence)}')'''

    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)
    

df_result.to_csv('AI_Detection/support_and_confidence/support_and_confidence_plagiated_no_semantic_filter.csv', index=None)
print('number of not detected abstract is', abstract_zero)
print('number of not detected intro is', intro_zero)
print('number of not detected conclusion is', conclusion_zero)
