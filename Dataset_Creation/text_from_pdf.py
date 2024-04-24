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


pdf_path = r"C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Dataset_Collection\original_paper\0704.0858v1.Lessons_Learned_from_the_deployment_of_a_high_interaction_honeypot.pdf"

output_file = "output_test/extracted_text.txt"

pdf_text = extract_text_from_pdf(pdf_path)
save_text_to_file(pdf_text, output_file)
print("Text extracted from PDF and saved to:", output_file)
