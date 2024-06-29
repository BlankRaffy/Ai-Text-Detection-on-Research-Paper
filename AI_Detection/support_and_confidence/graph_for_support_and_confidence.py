import matplotlib.pyplot as plt
import numpy as np

# Data from dictionaries
plagiated_no_filer_value = {
    'abstract': {'support': 0.779, 'confidence': 0.858},
    'intro': {'support': 0.598, 'confidence': 0.881},
    'conclusion': {'support': 0.513, 'confidence': 0.803}
}

original_value = {
    'abstract': {'support': 0.662, 'confidence': 0.765},
    'intro': {'support': 0.311, 'confidence': 0.79},
    'conclusion': {'support': 0.373, 'confidence': 0.78}
}

multiplagiated_value = {
    'abstract': {'support': 0.723, 'confidence': 0.849},
    'intro': {'support': 0.374, 'confidence': 0.834},
    'conclusion': {'support': 0.470, 'confidence': 0.825}
}

# Extract values
categories = ['abstract', 'intro', 'conclusion']
labels = ['plagiated_no_filer', 'original', 'multiplagiated']

support_values = [
    [plagiated_no_filer_value[cat]['support'] for cat in categories],
    [original_value[cat]['support'] for cat in categories],
    [multiplagiated_value[cat]['support'] for cat in categories]
]

confidence_values = [
    [plagiated_no_filer_value[cat]['confidence'] for cat in categories],
    [original_value[cat]['confidence'] for cat in categories],
    [multiplagiated_value[cat]['confidence'] for cat in categories]
]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

for i, category in enumerate(categories):
    ax = axs[i]
    ax.bar(x - width, [support_values[0][i], support_values[1][i], support_values[2][i]], width, label='Support')
    ax.bar(x, [confidence_values[0][i], confidence_values[1][i], confidence_values[2][i]], width, label='Confidence')
    ax.set_title(f'{category.capitalize()}')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

fig.suptitle('Comparison of Support and Confidence Values')
plt.show()
