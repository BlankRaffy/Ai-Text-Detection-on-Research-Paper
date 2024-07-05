import pandas as pd

df=pd.read_csv('Semantic_Similarity\semantic_rank\semantic_rank_all.csv')

# Group the DataFrame by 'input_file'
grouped = df.groupby('input_file')

# Initialize a list to hold the filtered groups
filtered_groups = []

# Iterate through each group
for name, group in grouped:
    # Check if any row in the group has the same 'compare_file' as 'input_file'
    if any(group['compare_file'] == name.replace('_plagiated.xml','.xml')):
        filtered_groups.append(group)

# Concatenate the filtered groups into a new DataFrame
new_df = pd.concat(filtered_groups)

# Output the new DataFrame
#print(new_df)
print(f'the number of detected file is {len(new_df)/5}')
precision =[]
grouped_df=new_df.groupby('input_file')

for ele in new_df.groupby('input_file'):
    i=0
    for item in ele[1]['compare_file']:
        if ele[0].replace('_plagiated.xml','.xml')==item:
            #print(f'1/{i+1}')
            precision.append(1/(i+1))
        i+=1
    


# Output the new DataFrame and the mean precision
print(sum(precision)/len(precision))
