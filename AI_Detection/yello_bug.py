import fitz  # PyMuPDF

def highlight_sentences(input_pdf, output_pdf, sentences_to_highlight, color=(2, 0, 0)):
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf)
    
    # Create an RGB color object
    highlight_color = fitz.utils.getColor(color)

    # Iterate through each page in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        # Search for sentences to highlight
        for sentence in sentences_to_highlight:
            # Get a list of rectangles where the text is found
            rects = page.search_for(sentence)
            # Highlight each occurrence of the sentence on the page with the specified color
            for rect in rects:
                highlight = page.add_highlight_annot(rect)
                highlight.set_colors(colors=(1,0,0),fill=highlight_color)
    
    # Save the modified PDF to a new file
    pdf_document.save(output_pdf)
    pdf_document.close()

# Example usage:
input_pdf = "example.pdf"
output_pdf = "output_highlighted.pdf"
sentences_to_highlight = ["Introduction The BRCA1 and BRCA2 BRCA1 and BRCA2 genes are expressed in the ovaries."," A mutation in BRCA1 or BRCA2 leads to the severe defects of ovarian cancer"]  # Add the sentences you want to highlight
highlight_color = (1, 0, 0)  # Red color
highlight_sentences(input_pdf, output_pdf, sentences_to_highlight, color=highlight_color)
