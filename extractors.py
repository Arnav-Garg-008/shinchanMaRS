import PyPDF2
import docx
import pytesseract
from pdf2image import convert_from_path
import os
from tempfile import TemporaryDirectory

class ContentExtractor:
    def extract_text(self, file_path, file_type):
        file_type = file_type.lower()
        try:
            if file_type == 'pdf':
                return self._extract_pdf(file_path)
            elif file_type == 'docx':
                return self._extract_docx(file_path)
            elif file_type == 'txt':
                return self._extract_txt(file_path)
            else:
                return self._ocr_extraction(file_path)
        except Exception as e:
            raise ValueError(f"Extraction failed: {str(e)}")

    def _extract_pdf(self, path):
        text = ""
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    def _extract_docx(self, path):
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])

    def _extract_txt(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    def _ocr_extraction(self, path):
        images = convert_from_path(path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
        return text

    def extract_page_wise_text(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                if not reader.pages:
                    raise ValueError("PDF has no readable pages.")
                
                page_texts = []
                for i, page in enumerate(reader.pages):
                    text = page.extract_text() or ""
                    page_texts.append({
                        'page_number': i + 1,
                        'text': text,
                        'char_count': len(text),
                        'word_count': len(text.split())
                    })
                return page_texts
        except Exception as e:
            # Fallback to OCR if PDF parsing fails
            return self._ocr_page_wise(pdf_path)

    def _ocr_page_wise(self, pdf_path):
        text_data = []
        with TemporaryDirectory() as temp_dir:
            images = convert_from_path(pdf_path, dpi=300, output_folder=temp_dir)
            for i, img in enumerate(images):
                text = pytesseract.image_to_string(img)
                text_data.append({
                    'page_number': i + 1,
                    'text': text,
                    'char_count': len(text),
                    'word_count': len(text.split())
                })
        return text_data
