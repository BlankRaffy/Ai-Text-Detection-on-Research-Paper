import fitz  # PyMuPDF

def highlight_sentences(input_pdf, output_pdf, sentences_to_highlight, color):
    """
    Highlights sentences in a PDF document and adds the text from the sentence inside the highlighted rectangles.

    Args:
        input_pdf (str): Path to the original PDF file.
        output_pdf (str): Path to save the highlighted PDF.
        sentences_to_highlight (list): List of strings containing the sentences to be highlighted.
        color (tuple): A tuple representing the RGB color for highlighting.
    """
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf)
    
    # Convert RGB values to the range [0, 1]
    highlight_color = tuple(component / 255 for component in color)
    
    # Iterate through each page in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        # Search for sentences to highlight
        for sentence in sentences_to_highlight:
            rects = page.search_for(sentence)
            # Highlight each occurrence of the sentence on the page
            for rect in rects:
                # Draw rectangle annotation for the fill color inside
                page.draw_rect(rect, fill=highlight_color, color=highlight_color)
                # Add the text from the sentence inside the rectangle
                page.insert_text((rect[0], rect[1]), sentence, fontsize=8, fontname="helv", color=(0, 0, 0))

    # Save the modified PDF to a new file
    pdf_document.save(output_pdf)
    pdf_document.close()

# Example usage:
input_pdf = "example.pdf"
output_pdf = "output_highlighted_with_text.pdf"
sentences_to_highlight = [
    "Introduction The BRCA1 and BRCA2 BRCA1 and BRCA2 genes are expressed in the ovaries.",
    "A mutation in BRCA1 or BRCA2 leads to the severe defects of ovarian cancer"
]
highlight_color = (255, 165, 0)  # Orange color in RGB format

highlight_sentences(input_pdf, output_pdf, sentences_to_highlight, color=highlight_color)
