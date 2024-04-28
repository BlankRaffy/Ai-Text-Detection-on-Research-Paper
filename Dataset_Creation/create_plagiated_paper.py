import plagiated_function
import os
import xml.etree.ElementTree as ET


file_path= 'origianal_paper\PMC13901.xml'

tree = ET.parse(file_path)
#tree = plagiated_function.change_abstract(tree)
#plagiated_function.change_abstract(tree)
#plagiated_function.save_tree(file_path,tree)
tree = plagiated_function.change_intro(tree)
plagiated_function.save_tree(file_path,tree)
