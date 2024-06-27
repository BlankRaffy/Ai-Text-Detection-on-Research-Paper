import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'Similarity_Compare/graph/dataframe_for_graphic.csv'
data = pd.read_csv(file_path)

# Select the first 10 elements (1st to 10th)
data = data.iloc[1:25] #with 25 we got 7, 20 we got and with 15 we got 12

# Calculate the heights for each section of the bar
data['abstract_section'] = data['abstract_score'] * 0.4
data['intro_section'] = data['intro_score'] * 0.2
data['conclusion_section'] = data['conclusion_score'] * 0.4

# Define colors for each section
colors = ['#E76F51', '#F4A261', '#E9C46A']  

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
bars = range(len(data))

# Stacking the bars with specified colors
ax.bar(bars, data['abstract_section'], bar_width, label='Abstract', color=colors[0])
ax.bar(bars, data['intro_section'], bar_width, bottom=data['abstract_section'], label='Introduction', color=colors[1])
ax.bar(bars, data['conclusion_section'], bar_width, 
       bottom=data['abstract_section'] + data['intro_section'], label='Conclusion', color=colors[2])

# Adding labels and title
ax.set_xlabel('Files')
ax.set_ylabel('Scores')
ax.set_title('Scores by Section for Each File')
ax.set_xticks(bars)
ax.set_xticklabels(data['input_file'], rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
