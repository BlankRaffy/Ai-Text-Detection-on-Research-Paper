import string

def clean_text(text):
    printable = set(string.printable)
    cleaned_text = ''.join(filter(lambda x: x in printable, text))
    return cleaned_text

def clean_text_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        extracted_text = file.read()
    
    cleaned_text = clean_text(extracted_text)
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

# Example usage
input_file = "output_test/extracted_text.txt"
output_file = "output_test/cleaned_text.txt"

clean_text_file(input_file, output_file)
print("Text cleaned and saved to:", output_file)
