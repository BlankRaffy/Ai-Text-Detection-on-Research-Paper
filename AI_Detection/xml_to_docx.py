from docx import Document
from xml.etree import ElementTree as ET
import get_text
from docx import Document

def save_text_to_docx(text, docx_file):
    doc = Document()
    
    doc.add_paragraph(text)
    
    doc.save(docx_file)
    print("Conversione completata!")

file_path = 'AI_Detection/PMC13901_plagiated.xml'

tree = ET.parse(file_path)

abstract_text = get_text.extract_abstract(tree)
intro_text = get_text.extract_intro(tree)
conclusion_text = get_text.extract_conclusion(tree)

text = 'ABSTRACT \n'+ abstract_text + '\n\n\n'+'INTRODUCTION \n'+ intro_text + '\n\n\n'+ 'CONCLUSION \n'+ conclusion_text

save_text_to_docx(text, 'PMC13901_plagiated.docx')
