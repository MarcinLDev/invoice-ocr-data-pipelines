from .s3_utils import ocr_exists, get_pdf_bytes, save_ocr
from .ocr import run_ocr

def process_single_pdf(s3_client, bucket,prefix_ocr, pdf_key):
    file_name = pdf_key.split("/")[-1].replace('.pdf','.txt')
    file_name_fully = prefix_ocr+file_name
    if ocr_exists(s3_client, bucket, file_name_fully):
        return f"SKIPPED: {file_name}"
    
    pdf_bytes = get_pdf_bytes(s3_client, bucket, pdf_key)
    text_pdf = run_ocr(pdf_bytes)
    save_ocr(s3_client, bucket,ocr_key=file_name_fully,text=text_pdf )
    return f"OK: {file_name}"