from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from xml.etree import ElementTree as ET
import get_text 

def create_pdf(file_path,output_path):
    # Create a canvas object
    c = canvas.Canvas(output_path, pagesize=letter)

    # Set the font size
    font_size = 12

    # Set the maximum width for text
    max_width = 400

    # Parse XML and extract text
    tree = ET.parse(file_path)
    abstract_text = get_text.extract_abstract(tree)
    intro_text = get_text.extract_intro(tree)
    conclusion_text = get_text.extract_conclusion(tree)
    title_text = get_text.get_title(tree)

    # Construct the complete text
    text = title_text +'\n\n\n' + 'ABSTRACT \n'+ abstract_text + '\n\n\n'+'INTRODUCTION \n'+ intro_text + '\n\n\n'+ 'CONCLUSION \n'+ conclusion_text 

    # Split the text into multiple lines
    lines = []
    for paragraph in text.split('\n'):
        words = paragraph.split()
        line = ""
        for word in words:
            if c.stringWidth(line + " " + word, "Helvetica", font_size) < max_width:
                line += " " + word
            else:
                lines.append(line.strip())
                line = word
        lines.append(line.strip())

    # Calculate the starting position to center the text vertically
    start_y = letter[1] - 50

    # Draw text on the canvas
    c.setFont("Helvetica", font_size)
    for line in lines:
        if start_y < 50:
            # If the remaining space on the page is not enough for the next line, add a new page
            c.showPage()
            c.setFont("Helvetica", font_size)
            start_y = letter[1] - 50
        c.drawString(100, start_y, line)
        start_y -= font_size

    # Save the canvas to a PDF file
    c.save()

