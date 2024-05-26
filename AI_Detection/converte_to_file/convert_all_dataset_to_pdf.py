import xml_to_pdf
import os

plagiated_directory = 'Dataset\plagiated_paper'

for file in os.listdir(plagiated_directory):
    file_path= plagiated_directory+'/'+file
    output_path= 'AI_Detection/pdf_plagiated_file'+'/'+file.replace('.xml','_demo.pdf')
    xml_to_pdf.create_pdf(file_path,output_path)