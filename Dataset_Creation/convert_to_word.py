from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    # Initialize converter
    cv = Converter(pdf_file)

    # Convert the PDF to DOCX format
    cv.convert(docx_file, start=0, end=None)

    # Close the converter
    cv.close()

# Example usage
pdf_file = r"Dataset_Collection\original_paper\0704.0004v1.A_determinant_of_Stirling_cycle_numbers_counts_unlabeled_acyclic_single_source_automata.pdf"  # Replace with the path to your PDF file
docx_file = "output_test\output_document.docx"  # Specify the output DOCX file path
convert_pdf_to_docx(pdf_file,docx_file)
