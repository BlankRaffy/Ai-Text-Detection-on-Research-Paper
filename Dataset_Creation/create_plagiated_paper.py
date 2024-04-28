import plagiated_function
import os
import xml.etree.ElementTree as ET
import tqdm

''' TEST ON A SINGLE FILE
file_path= 'original_paper\PMC13901.xml'

tree = ET.parse(file_path)

tree = plagiated_function.change_abstract(tree)
tree = plagiated_function.change_intro(tree)
tree = plagiated_function.change_conclusion(tree)

#save the final xml file with all the modified part:
plagiated_function.save_tree(file_path,tree)
'''
folder = 'Dataset/original_paper'
for ele in tqdm.tqdm(os.listdir(folder)):

    absolute_path = folder+'/'+ele
    
    tree = ET.parse(absolute_path)

    tree = plagiated_function.change_abstract(tree)
    tree = plagiated_function.change_intro(tree)
    tree = plagiated_function.change_conclusion(tree)

    #save the final xml file with all the modified part:
    plagiated_function.save_tree(absolute_path,tree)
