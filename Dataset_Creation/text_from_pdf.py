import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

# Example usage
pdf_path = r"Dataset_Collection\original_paper\0704.0004v1.A_determinant_of_Stirling_cycle_numbers_counts_unlabeled_acyclic_single_source_automata.pdf"
output_file = "output_test/extracted_text.txt"

pdf_text = extract_text_from_pdf(pdf_path)
save_text_to_file(pdf_text, output_file)
print("Text extracted from PDF and saved to:", output_file)
