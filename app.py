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

# function to summarize text with GroqCloud using the Llama-3.1-8b-instant model
def summarize_text(text):
    try:
        summary_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text: {text}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return summary_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

