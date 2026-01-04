from pdf2image import convert_from_bytes
import pytesseract

def run_ocr(pdf_bytes):
    pages = convert_from_bytes(pdf_bytes, dpi=200)
    text_all = ""

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="pol")
        text_all += f"--- Strona {i+1} ---\n{text}\n\n"

    return text_all