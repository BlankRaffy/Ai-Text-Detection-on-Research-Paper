
def extract_intro(tree):
    introduction = ''
    root = tree.getroot()
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        section_type = passage.find(".//infon[@key='section_type']")

        if section_type is not None and section_type.text == 'INTRO':
            introduction = introduction + ' ' + passage.find('.//text').text
                
            

    return introduction

def extract_abstract(tree):
    
    root = tree.getroot()
    
    # Trova tutti gli elementi 'passage' nell'albero XML 
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'ABSTRACT'
        section_type = passage.find(".//infon[@key='section_type']")
        
        if section_type is not None and section_type.text == 'ABSTRACT':
            abstract = passage.find('.//text').text
            
    # Restituisci l'albero XML copiato e modificato
    return abstract

def extract_conclusion(tree):
    conclusion = ' '
    root = tree.getroot()
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'CONCL'
        section_type = passage.find(".//infon[@key='section_type']")
        
        if section_type is not None and section_type.text == 'CONCL':
            if passage.find('.//text').text != 'Conclusion':
                conclusion = conclusion + ' ' + passage.find('.//text').text
    
    return conclusion

def get_title(tree):
    root = tree.getroot()
    generated = True #boolean to to modify the first element of the introduction
    # Trova tutti gli elementi 'passage' nell'albero XML 
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'ABSTRACT'
        section_type = passage.find(".//infon[@key='section_type']")
        
        
        if section_type is not None and section_type.text == 'TITLE':
            # Trova l'elemento 'text' all'interno del 'passage' (abstract)
            title_element = passage.find('.//text')
            return title_element.text