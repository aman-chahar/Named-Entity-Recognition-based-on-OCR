## Image Text Extraction and Named Entity Recognition (NER) using Tesseract OCR and spaCy

This repository contains a Python script that demonstrates how to extract text from images using Tesseract OCR, process the extracted text, and perform Named Entity Recognition (NER) using spaCy.

### Requirements

- Python 3.x
- Tesseract OCR
- OpenCV (cv2)
- pytesseract
- docx (python-docx)
- spaCy

### Installation

1. **Tesseract OCR**: Install Tesseract OCR and set the path accordingly:

   ```bash
   pip install pytesseract
   ```

   Ensure that Tesseract OCR is installed on your system and the path is correctly set.

2. **OpenCV (cv2)**: Install OpenCV for image processing:

   ```bash
   pip install opencv-python
   ```

3. **docx (python-docx)**: Install python-docx for working with Word documents:

   ```bash
   pip install python-docx
   ```

4. **pdf2image**: Install pdf2image for extracting pages from PDFs:

   ```bash
   pip install pdf2image
   ```

5. **spaCy**: Install spaCy and the English language model:

   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

### Usage

1. **Image Text Extraction**:
   - Replace `news1.jpg` with the path to your image file.
   - The script uses OpenCV to read the image and Tesseract OCR to extract text.

   ```python
   import cv2
   import pytesseract

   # Read the image
   img = cv2.imread("news1.jpg")

   # Extract text from image
   text = pytesseract.image_to_string(img)
   print(text)
   ```

2. **Saving Extracted Text to Document**:
   - The extracted text can be saved to a Word document using python-docx.

   ```python
   from docx import Document

   # Create a new Word document
   doc = Document()
   doc.add_paragraph(text)

   # Save the Word document
   doc.save("output.docx")
   ```

3. **Named Entity Recognition (NER) using spaCy**:
   - Perform Named Entity Recognition (NER) on the extracted text using spaCy.

   ```python
   import spacy

   # Load spaCy English language model
   nlp = spacy.load('en_core_web_sm')

   # Define a function to display basic entity information
   def show_ents(doc):
       if doc.ents:
           for ent in doc.ents:
               print(ent.text, '-', ent.start_char, '-', ent.end_char, '-', ent.label_, '-', spacy.explain(ent.label_))
       else:
           print("No named entities found.")

   # Example usage
   doc = nlp(text)
   show_ents(doc)
   ```

### Additional Notes

- Ensure all required dependencies are installed before running the script.
- Adjust paths and filenames as per your system configuration.

---
