import re
import PyPDF2

def clean_text(text):
    # Remove non-printable characters and extra whitespaces
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def save_text_to_file(text, output_file):
    with open(output_file, "w") as file:
        file.write(text)

# Example usage
pdf_path = r"Dataset_Collection\original_paper\0704.0004v1.A_determinant_of_Stirling_cycle_numbers_counts_unlabeled_acyclic_single_source_automata.pdf"
output_file = "output_test\extracted_text.txt"

extracted_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(extracted_text)
save_text_to_file(cleaned_text, output_file)

print("Text extracted and saved to", output_file)
