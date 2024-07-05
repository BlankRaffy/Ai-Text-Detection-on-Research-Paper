import matplotlib.pyplot as plt

# Data
top_k = [3, 5, 7, 10, 15, 20, 25, 30, 50, 70, 100]
accuracy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
number_of_paper = [155, 159, 161, 164, 166, 167, 168, 169, 169, 171, 174]

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plot accuracy
ax1.set_xlabel('Top K')
ax1.set_ylabel('Accuracy', color='tab:blue')
ax1.plot(top_k, accuracy, color='tab:blue', marker='o', label='Accuracy')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Set x-ticks to be the top_k values
ax1.set_xticks(top_k)

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Papers', color='tab:red')
ax2.plot(top_k[:len(number_of_paper)], number_of_paper, color='tab:red', marker='x', label='Number of Papers')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Format the y-axis of the number of papers to display integers
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# Add titles and legends
plt.title('Accuracy and Number of Papers vs. Top K')
fig.tight_layout()
plt.show()
