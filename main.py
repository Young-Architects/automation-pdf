
from pdf2docx import Converter

from pdf2image import convert_from_path
import pytesseract
from docx import Document

# Path to your PDF file
pdf_file = r"./Tang.pdf"
poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Output path for the Word document
docx_file = "./Tang_Word.docx"
output_docx = docx_file
'''
# Create a PDF to Word converter object
cv = Converter(pdf_file)

# Perform the conversion
cv.convert(docx_file)

# Close the converter
cv.close()

print(f"Conversion complete. Word document saved at {docx_file}")
'''



# Convert PDF pages to images
pages = convert_from_path(pdf_file,poppler_path=poppler_path)

# Create a Word document
doc = Document()

# Perform OCR on each page
for page in pages:
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(page)

    # Add extracted text to Word document
    doc.add_paragraph(text)

# Save the document
doc.save(output_docx)

print(f"Conversion complete. Editable Word document saved at {output_docx}")
