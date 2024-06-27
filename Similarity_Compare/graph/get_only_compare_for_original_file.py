import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Similarity_Compare/topic_with_final_score.csv')

# Create an empty DataFrame with the same columns as the original
df_results = pd.DataFrame(columns=df.columns)

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Check if the input file, after replacing '_plagiated.xml' with '.xml', matches the compare file
    if row['input_file'].replace('_plagiated.xml', '.xml') == row['compare_file']:
        df_results = pd.concat([df_results, pd.DataFrame([row])], ignore_index=True)


df_results.to_csv('Similarity_Compare/graph/dataframe_for_graphic.csv', index=False)
print(df_results.shape)
