import xml.etree.ElementTree as ET


def validate_paper(input_path):
    file_path =  input_path

# Parse XML from file
    tree = ET.parse(file_path)
    root = tree.getroot()

    abstract = False
    concl = False
    intro = False


    passages = root.findall('.//passage')
    for passage in passages:
        text = passage.find(".//infon[@key='section_type']")

        if(text.text=='CONCL'):
            concl=True          
    
        if(text.text=='INTRO'):
            intro= True

        if(text.text=='ABSTRACT'):
            abstract=True

    if(abstract and intro and concl):
        #print('nel paper sono presenti tutti gli elementi richiesti')
        return True
    else:
        #print('nel paper NON sono presenti tutti gli elementi richiesti')
        return False