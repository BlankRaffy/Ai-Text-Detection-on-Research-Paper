import csv
import json

# Initialize dictionaries to store total support, total confidence, and counts for each section
sections = {
    'abstract': {'total_support': 0, 'total_confidence': 0, 'count': 0},
    'intro': {'total_support': 0, 'total_confidence': 0, 'count': 0},
    'conclusion': {'total_support': 0, 'total_confidence': 0, 'count': 0}
}

# Function to convert single quotes to double quotes in JSON strings
def fix_json_string(json_str):
    return json_str.replace("'", '"')

# Read the CSV file
with open('AI_Detection/support_and_confidence/support_and_confidence_plagiated_semantic_filter.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for section in sections:
            result = json.loads(fix_json_string(row[f'{section}_result']))
            support = result['support']
            confidence = result['confidence']
            if support != 0:  # Only consider non-zero support values
                sections[section]['total_support'] += support
                sections[section]['total_confidence'] += confidence
                sections[section]['count'] += 1

# Calculate average values for each section
averages = {}
for section, values in sections.items():
    if values['count'] > 0:  # Ensure there are entries before calculating averages
        avg_support = values['total_support'] / values['count']
        avg_confidence = values['total_confidence'] / values['count']
        averages[section] = {'average_support': avg_support, 'average_confidence': avg_confidence}
    else:
        averages[section] = {'average_support': 0, 'average_confidence': 0}  # Handle case where count is 0

# Print the results
for section, avg in averages.items():
    print(f"{section.capitalize()} - Average Support: {avg['average_support']}, Average Confidence: {avg['average_confidence']}")
