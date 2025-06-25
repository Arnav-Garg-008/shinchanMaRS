# shinchanMaRS
This project aims to develop an automated metadata generation system. This system will enhance document discoverability, classification, and subsequent analysis by producing scalable, consistent, and semantically rich metadata.

# AutoMetalysis – Intelligent Document Metadata Generator

AutoMetalysis is a web-based tool built with Flask that allows you to upload any document — PDF, DOCX, TXT, PPTX, or even images — and get back a complete semantic analysis. It uses natural language processing (NLP) and OCR to extract key insights like summaries, keywords, named entities, topics, sentiment, readability, and even word clouds.

---

## 🔍 What This Tool Does

- ✅ Works with PDFs, Word files, slides, plain text, and scanned documents
- 🧠 Extracts **semantic metadata** from your files:
  - Short summary
  - Key topics and keywords
  - Named entities (people, places, etc.)
  - Readability scores (Flesch Reading Ease)
  - Sentiment (positive/negative)
- 📊 Includes word clouds and keyword graphs
- 📄 Analyzes each page separately (for PDFs)
- 🔁 Offers a REST API for backend integration

---

## 🧱 Behind the Scenes

The system is made up of four main components:

- **ContentExtractor** – Extracts text using OCR or direct parsing
- **SemanticProcessor** – Runs NLP models like spaCy, LDA, KeyBERT, and more
- **MetadataGenerator** – Organizes results into structured output
- **Flask App** – Provides a web interface + API

---

## 🛠️ Technologies Used

- Python + Flask
- spaCy, TextBlob, KeyBERT, textstat
- scikit-learn, matplotlib, wordcloud
- pytesseract (for OCR)
- LDA (topic modeling)

---

## 📸 Demo Screenshots

Here’s what the app looks like in action:

![Upload Screen](https://github.com/user-attachments/assets/5f0e7a46-a337-4a66-9549-1ff58c80f04f)  
![Results Page](https://github.com/user-attachments/assets/40718d2d-1230-4ff0-bf4d-ae0f0c3c8518)  
![Results Page](https://github.com/user-attachments/assets/e1c700ac-9d07-4ec3-937a-0eeeace46509)  

---

## ▶️ How to Run Locally

> Works on Windows, Mac, or Linux. Follow these steps:

### 1. Clone the Repo

Open your terminal or command prompt and run on bash:(replace the file name to what you have)
git clone https://github.com/Arnav-Garg-008/shinchanMaRS
cd AutoMetalysis


2.Set Up Python Virtual Environment
Create and activate a virtual environment to manage dependencies:

bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows


3.Install Required Dependencies
Install all necessary Python packages:

bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

4. Run the Flask Application
Start the web server:

bash
python app.py
(now it would run at your local host)

