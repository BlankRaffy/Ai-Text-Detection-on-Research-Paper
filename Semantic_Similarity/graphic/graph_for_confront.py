import matplotlib.pyplot as plt

def create_circular_progress_chart(percentage, size=0.3):
    # Create a figure and axis for plotting
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

    # Data for plotting
    data = [percentage, 100 - percentage]
    wedges, texts = ax.pie(data, startangle=90, colors=['#1E6091', '#f0f0f0'],
                           wedgeprops=dict(width=size, edgecolor='w'))

    # Add text label in the 1E6091
    ax.text(0, 0, f"{percentage}%", ha='center', va='center', fontsize=50, color='#1E6091')

    # Set axis to be equal to ensure the pie chart is circular
    ax.set(aspect="equal")

    # Remove axis lines and labels
    plt.axis('off')

    # Show the plot
    plt.show()

# Customize the percentage value here
percentage_value = 74 # Change this value to customize the chart
create_circular_progress_chart(percentage_value)
