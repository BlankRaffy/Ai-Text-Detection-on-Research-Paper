from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
  text=''
  reader = PdfReader(pdf_path) 
  print(len(reader.pages)) 
  for i in range(len(reader.pages)):
    text = text + reader.pages[i].extract_text() 
  return text

def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

# Example usage
pdf_path = r"Adaptive RL with LLM-augmented reward functions.pdf"
output_file = "output_test/extracted_text.txt"

pdf_text = extract_text_from_pdf(pdf_path)
save_text_to_file(pdf_text, output_file)
print("Text extracted from PDF and saved to:", output_file)
