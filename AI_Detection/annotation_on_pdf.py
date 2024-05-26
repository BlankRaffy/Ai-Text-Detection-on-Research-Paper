import fitz  # PyMuPDF

def highlight_sentences(pdf_dpcument, output_pdf, sentences_to_highlight, color):
    # Open the input PDF file
    
    
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
                highlight.set_colors(color,fill=highlight_color)
                highlight.set_colors(stroke=color) # light red color (r, g, b) the one who set the color
                highlight.update()
    

 

# Example usage:
input_pdf = "example.pdf"
output_pdf = "output_highlighted.pdf"
pdf_document = fitz.open(input_pdf)
sentences_to_highlight = ["Introduction The BRCA1 and BRCA2 BRCA1 and BRCA2 genes are expressed in the ovaries."," A mutation in BRCA1 or BRCA2 leads to the severe defects of ovarian cancer"]  # Add the sentences you want to highlight
highlight_color = (1, 0.8, 0.8)  # light red color
highlight_sentences(pdf_document, output_pdf, sentences_to_highlight, color=highlight_color)

sentences_to_highlight = ["Lastly, we demonstrate with various antibodies that both broad-spectrum BRCA1 and BRAC2 proteins"]  # Add the sentences you want to highlight
highlight_color = (1, 0.8, 0.6)  # light orange color
highlight_sentences(pdf_document, output_pdf, sentences_to_highlight, color=highlight_color)

pdf_document.save(output_pdf)
pdf_document.close()