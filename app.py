import streamlit as st
import fitz  # PyMuPDF
from groq import Groq

# Back-End

# Initialize the Groq client
client = Groq(api_key='') # Add Your groq key you can get it here (https://console.groq.com/keys)

# Function to extract text from the pdf using fitz
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

# Function to ask a question to the model
def ask_question(context, question):
    try:
        answer_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {context} Question: {question}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return answer_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Front-End
# Streamlit UI
st.title("PDF Question Answering App")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("Text Extracted from PDF:")
    st.write(pdf_text[:500])  # Display a snippet of the text for review

    summary_button = st.button("Summarize Text")
    if summary_button:
        summary = summarize_text(pdf_text)
        st.subheader("Summary:")
        st.write(summary)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = ask_question(pdf_text, question)
        st.subheader("Answer:")
        st.write(answer)
