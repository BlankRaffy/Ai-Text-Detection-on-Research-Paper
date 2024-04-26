import os
import shutil
import paper_extraction


folder = 'achivio_paper' #removed after the creation of dataset
destination = 'valid_paper_temp'

# Itera sugli elementi della cartella
for elemento in os.listdir(folder):
    final_path= os.path.join(folder, elemento)

    if paper_extraction.validate_paper(final_path):
        shutil.copyfile(final_path, os.path.join(destination,elemento))

