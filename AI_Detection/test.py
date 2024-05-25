import pandas as pd
import ast  # Library to parse strings containing Python expressions

# Load the CSV into a DataFrame
df = pd.read_csv('AI_Detection/results/Ai_Detection_result.csv')

# Your string representation of a list of tuples
string_data = df['conclusion_sentence'][0]

# Convert the string to a list of tuples
data = ast.literal_eval(string_data)

print(data[0][0])
