# Bryan's PDF Question Answering App

## Overview
This Streamlit-based application allows users to upload PDF files, summarize their content, and ask questions about the extracted text using AI.

## Features
- Extracts text from PDF files.
- Summarizes extracted text using the Groq API.
- Answers user queries based on the PDF content.
- Interactive and user-friendly interface.

## Technologies Used
- **Streamlit**: front-end For the web User interface.
- **PyMuPDF (fitz)**: used in the backend, For extracting text from PDF files.
- **Groq API**: AI source For summarization and question answering.
- **Python**: Primary programming language for the backend and front-end

## Prerequisites
1. Python 3.7 or higher installed on your system.
2. A Groq API key (store this in a `.env` file). you can get it here https://console.groq.com/keys

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-question-answering-app.git
   cd pdf-question-answering-app
    ```
2. Install dependences:
    ```bash
    pip install -r requirements.txt
    ```
3. Add Your GroqCloud key here
    ```bash
    # Initialize the Groq client
    client = Groq(api_key='key') # change 'key' and add your API key 
    ```
4. Run the application and enjoy :)
    ```bash
    streamlit run app.py
    ```
## How to use
- Upload a PDF file via the provided file uploader.
- View extracted text and summarize it using the Summarize Text button.
- Ask questions about the PDF content in the input box.

## Example
- Upload a sample PDF file.
- Extracted text will appear in the app interface.
- Click Summarize Text to get a concise summary.
- Ask a question like, "What is the main topic?" and receive an answer.

## Troubleshooting
If PDF text isn't extracted:
- Ensure the file is a valid PDF.
- Check dependencies are correctly installed.
- If summarization or question answering fails:
- Verify the Groq API key in .env.
