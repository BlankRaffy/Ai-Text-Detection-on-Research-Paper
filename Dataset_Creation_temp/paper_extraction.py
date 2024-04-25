import xml.etree.ElementTree as ET

# File path
file_path = "PMC13900.xml"  # Replace "your_file.xml" with the actual file path

# Parse XML from file
tree = ET.parse(file_path)
root = tree.getroot()

# Find the abstract passage
'''
abstract_passage = None
for passage in root.findall(".//passage"):
    section_type = passage.find("infon[@key='section_type']")
    if section_type is not None and section_type.text == 'ABSTRACT':
        abstract_passage = passage
        break

if abstract_passage is not None:
    # Extract abstract text
    abstract_text = abstract_passage.find("text").text
    print(abstract_text)
else:
    print("Abstract passage not found.")
'''

passage = root.findall('.//passage')
for infon in passage:
    text = infon.find(".//infon[@key='section_type']")
    print(text.text)