import xml.etree.ElementTree as ET

file_path = "your_file.xml"  # Replace "your_file.xml" with the actual file path

# Parse XML from file
tree = ET.parse(file_path)
root = tree.getroot()

# Find the passage with section_type 'ABSTRACT'
abstract_passage = root.find(".//passage[infon[@key='section_type' and text()='ABSTRACT']]")

# Extract abstract text
abstract_text = abstract_passage.find("text").text

print(abstract_text)