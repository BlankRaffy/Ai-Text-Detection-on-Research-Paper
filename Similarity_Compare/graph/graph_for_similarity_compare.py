import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'Similarity_Compare/graph/dataframe_for_graphic.csv'
data = pd.read_csv(file_path)

# Select the first 20 elements (2nd to 21st)
data = data.iloc[0:20]

# Calculate the heights for each section of the bar
data['abstract_section'] = data['abstract_score'] * 0.4
data['intro_section'] = data['intro_score'] * 0.2
data['conclusion_section'] = data['conclusion_score'] * 0.4

# Define colors for each section
colors = ['#E76F51', '#F4A261', '#E9C46A']

# Plotting the stacked horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_height = 0.5
bars = range(len(data))

# Stacking the bars with specified colors
ax.barh(bars, data['abstract_section'], bar_height, label='Abstract', color=colors[0])
ax.barh(bars, data['intro_section'], bar_height, left=data['abstract_section'], label='Introduction', color=colors[1])
ax.barh(bars, data['conclusion_section'], bar_height, 
        left=data['abstract_section'] + data['intro_section'], label='Conclusion', color=colors[2])

# Adding labels and title
ax.set_ylabel('Files')
ax.set_xlabel('Scores')
ax.set_title('Scores by Section for Each File')
ax.set_yticks(bars)
ax.set_yticklabels(data['input_file'])
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
