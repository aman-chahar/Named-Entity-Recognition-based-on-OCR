import streamlit as st
import pytesseract
from PIL import Image
import spacy
from spacy import displacy

# Set the path to Tesseract executable (Update this path based on your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load SpaCy NER model
nlp = spacy.load('en_core_web_sm')

# Define function to perform NER on text
def perform_ner(text):
    doc = nlp(text)
    return doc

# Streamlit App
def main():
    st.title("Named Entity Recognition (NER) from Image")

    # Upload Image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        # Display uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Extract text from the uploaded image using Tesseract OCR
        image = Image.open(uploaded_image)
        extracted_text = pytesseract.image_to_string(image)

        st.header("Extracted Text:")
        st.text(extracted_text)

        # Perform Named Entity Recognition (NER) on the extracted text
        st.header("Named Entity Recognition (NER) Results:")
        ner_doc = perform_ner(extracted_text)

        # Display NER results using SpaCy's displacy
        displacy_result = displacy.render(ner_doc, style="ent", page=True)
        st.write(displacy_result, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
