import csv
from collections import defaultdict
import pandas as pd
import ast

# Input filename
input_filename = 'Test_on_multiplagiated_paper/semantic_similarity/semantic_rank/semantic_rank_conclusion.csv'
source_filename='Test_on_multiplagiated_paper/multiplagiated_source.csv'
count=0

df_source= pd.read_csv(source_filename)
df_source['list_of_source_file'] = df_source['list_of_source_file'].apply(ast.literal_eval)
# Read input CSV file
rows = []
with open(input_filename, 'r', newline='') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        rows.append(row)

# Group rows by input_file
grouped_rows = defaultdict(list)
for row in rows:
    grouped_rows[row['input_file']].append(row)

i=0
# Check if the first compare_file matches the input_file without "_plagiated"
for input_file, group in grouped_rows.items():
    first_compare_file = group[0]['compare_file']
    source_file= df_source['list_of_source_file'][i][2] # 0 for abstact, 1 for intro and 2 for conclusion
    i+=1
    if first_compare_file == source_file:
        count += 1
        #print(f"For input_file '{input_file}', the first compare_file matches: '{first_compare_file}'")
    else:
        print(f"For input_file '{input_file}', the first compare_file does not match. Found: '{first_compare_file}', expected: '{source_file}'")

print(f'Percentual of plagiated paper that are most similar to the orginal one: {count/174}')