import streamlit as st
from PIL import Image
import pytesseract
import spacy

# Load the spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Image Text Extraction and Named Entity Recognition")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text from the image
    st.write("Extracting text from the image...")
    extracted_text = pytesseract.image_to_string(image)
    st.write("Extracted Text:")
    st.write(extracted_text)
    
    # Perform Named Entity Recognition (NER)
    st.write("Performing Named Entity Recognition (NER)...")
    doc = nlp(extracted_text)
    
    # Display the entities
    st.write("Entities found:")
    for ent in doc.ents:
        st.write(f"{ent.text} ({ent.label_})")
