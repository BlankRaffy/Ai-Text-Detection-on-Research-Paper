import csv

# Define the path to your input CSV file
input_csv_file_path = 'Ai_detection_using_mean/ai_detection_mean_for_part_multiplagiated.csv'

# Define the path to your output CSV file
output_csv_file_path = 'Ai_detection_using_mean/result_aggregation.csv'

# Initialize a list to store the results
results = []
count_above_0_5 = 0

# Read the input CSV file
with open(input_csv_file_path, mode='r') as input_file:
    csv_reader = csv.DictReader(input_file)
    for row in csv_reader:
        # Extract values and calculate the average probability
        input_file_name = row['input_file']
        abstract_probability = float(row['abstract_probability'])
        intro_probability = float(row['intro_probability'])
        conclusion_probability = float(row['conclusion_probability'])
        average_probability = (abstract_probability+ intro_probability + conclusion_probability) / 3
        
        # Append the result to the list
        results.append((input_file_name, average_probability))
        
        # Count if the average probability is greater than 0.5
        if average_probability > 0.35:
            count_above_0_5 += 1

# Write the results to the output CSV file
with open(output_csv_file_path, mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    # Write the header
    csv_writer.writerow(['input_file', 'average_probability'])
    # Write the data
    for input_file_name, average_probability in results:
        csv_writer.writerow([input_file_name, average_probability])

# Print the count of files with an average probability greater than 0.5
print(f"Number of files with an average probability greater than 0.5: {count_above_0_5}")
