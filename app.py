import streamlit as st
import fitz  # PyMuPDF
from groq import Groq

# Initialize the Groq client
client = Groq(api_key='') # Add Your groq key you can get it here (https://console.groq.com/keys)

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.
    Handles file-like objects (uploaded via Streamlit).
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text