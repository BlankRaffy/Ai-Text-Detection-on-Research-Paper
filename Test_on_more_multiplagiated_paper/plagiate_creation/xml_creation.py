import os
import xml.etree.ElementTree as ET
import get_text
from xml.dom import minidom


def find_passage_by_section_type(root, section_type):
    passages = root.findall(".//passage")
    for passage in passages:
        infon = passage.find(".//infon[@key='section_type']")
        if infon is not None and infon.text == section_type:
            return passage
    return None

def save_tree(intro_file_path, abstract_file_path, conclusion_file_path):
    # Load intro XML
    abstract_tree = ET.parse(abstract_file_path)
    intro_tree = ET.parse(intro_file_path)
    conclusion_tree = ET.parse(conclusion_file_path)
    
    abstract_text = get_text.extract_abstract(abstract_tree)
    intro_text = get_text.extract_intro(intro_tree)
    conclusion_text = get_text.extract_conclusion(conclusion_tree)

    # Create a new XML tree
    new_root = ET.Element("root")

    # TITLE
    title_passage_element = ET.SubElement(new_root, "passage")
    title_infon_element = ET.SubElement(title_passage_element, "infon", key="section_type")
    title_infon_element.text = "TITLE"
    title_text_element = ET.SubElement(title_passage_element, "text")
    title_text_element.text = get_text.get_title(abstract_tree)

    # ABSTRACT
    abstract_passage_element = ET.SubElement(new_root, "passage")
    abstract_infon_element = ET.SubElement(abstract_passage_element, "infon", key="section_type")
    abstract_infon_element.text = "ABSTRACT"
    abstract_text_element = ET.SubElement(abstract_passage_element, "text")
    abstract_text_element.text = abstract_text

    # INTRO
    intro_passage_element = ET.SubElement(new_root, "passage")
    intro_infon_element = ET.SubElement(intro_passage_element, "infon", key="section_type")
    intro_infon_element.text = "INTRO"
    intro_text_element = ET.SubElement(intro_passage_element, "text")
    intro_text_element.text = intro_text

    # CONCLUSION
    conclusion_passage_element = ET.SubElement(new_root, "passage")
    conclusion_infon_element = ET.SubElement(conclusion_passage_element, "infon", key="section_type")
    conclusion_infon_element.text = "CONCL"
    conclusion_text_element = ET.SubElement(conclusion_passage_element, "text")
    conclusion_text_element.text = conclusion_text

    # Convert tree to a string
    rough_string = ET.tostring(new_root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    output_string = reparsed.toprettyxml(indent="  ", encoding='utf-8').decode('utf-8')

    # Save the new XML tree to a file
    output_file_path = "combined_sections.xml"
    with open(output_file_path, "wb") as f:
        f.write(output_string.encode('utf-8'))

    return output_file_path

# Example usage:
intro_file_path = "Dataset/original_paper/PMC13901.xml"
abstract_file_path = "Dataset/original_paper/PMC29080.xml"
conclusion_file_path = "Dataset/original_paper/PMC32247.xml"
combined_file_path = save_tree(intro_file_path, abstract_file_path, conclusion_file_path)
print("Combined sections saved to:", combined_file_path)
