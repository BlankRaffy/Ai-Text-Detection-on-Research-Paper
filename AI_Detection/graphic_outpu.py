import pandas as pd
import fitz
import ast  # Library to parse strings containing Python expressions
import annotation_on_pdf
import os
import tqdm

pastel_yellow = (1, 1, 0.8)
pastel_orange_yellow = (1, 0.85, 0.65)
pastel_orange = (1, 0.75, 0.5)
pastel_red_orange = (1, 0.65, 0.55)
pastel_red = (1, 0.6, 0.6)

# Load the CSV into a DataFrame
df = pd.read_csv('AI_Detection/results/Ai_Detection_result.csv')


#load document 

output_pdf = "output_highlighted.pdf"

pdf_folder='AI_Detection/pdf_plagiated_file'
i=0 #to iterate over dataset

for file in os.listdir(pdf_folder):

    input_pdf = pdf_folder+'/'+file 
    print(input_pdf)
    output_pdf='AI_Detection/pdf_plagiated_file'+'/'+file.replace('_demo.pdf','_highlight.pdf')
    print(output_pdf)



    string_data = df['abstract_sentence'][i] #all sentence of first element
    abstract_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['intro_sentence'][i] #all sentence of first element
    intro_data = ast.literal_eval(string_data) #convert to tuple to access them
    string_data = df['conclusion_sentence'][i] #all sentence of first element
    conclusion_data = ast.literal_eval(string_data) #convert to tuple to access them

    data= abstract_data + intro_data + conclusion_data






    pdf_document = fitz.open(input_pdf)

    for ele in data:


        
        if ele[1]>0.5:
            
            if ele[1]<0.6:
                color= pastel_yellow

            elif ele[1]<0.7:
                color= pastel_orange_yellow
            
            elif ele[1]<0.8:
                color=pastel_orange
            
            elif ele[1]<0.9:
                color=pastel_red_orange

            elif ele[1]>0.9:
                color=pastel_red
            
            sentence = [ele[0]]
            annotation_on_pdf.highlight_sentences(pdf_document, output_pdf, sentence, color)

    pdf_document.save(output_pdf)
    pdf_document.close()  

    i+=1 #increase count to move to next element on dataset to implement a match base on file name
