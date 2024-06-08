import xml_to_pdf
import os

plagiated_directory = 'Test_on_multiplagiated_paper\multi_plagiated_paper'

for file in os.listdir(plagiated_directory):
    file_path= plagiated_directory+'/'+file
    output_path= 'Test_on_multiplagiated_paper\multiplagiated_pdf'+'/'+file.replace('.xml','_demo.pdf')
    xml_to_pdf.create_pdf(file_path,output_path)