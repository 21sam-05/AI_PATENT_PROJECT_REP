


import os
import shutil
from pathlib import Path

import pymupdf as fitz
import pytesseract

from langchain_core.documents import Document


# Locate the Tesseract executable.
TESSERACT_PATH = shutil.which("tesseract")

if not TESSERACT_PATH:
    default_path = Path(
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    if default_path.exists():
        TESSERACT_PATH = str(default_path)
    else:
        raise RuntimeError(
            "Tesseract OCR executable not found. "
            "Please install Tesseract or add it to PATH."
        )

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


# Minimum extracted characters before triggering OCR.
MIN_TEXT_LENGTH = 250

# Render scanned pages at 300 DPI for better OCR accuracy.
OCR_DPI = 300



def extract_page_text(page):

    text = page.get_text("text").strip()

    if len(text) >= MIN_TEXT_LENGTH:
        return text, "text", None

    pix = page.get_pixmap(
        dpi=OCR_DPI,
        colorspace=fitz.csRGB,
        alpha=False
    )

    image = pix.pil_image()

    ocr_data = pytesseract.image_to_data(
        image,
        lang="eng",
        output_type=pytesseract.Output.DICT
    )

    valid_words = []
    confidence_scores = []

    for word, confidence in zip(
        ocr_data["text"],
        ocr_data["conf"]
    ):

        word = word.strip()

        try:
            confidence = float(confidence)
        except (ValueError, TypeError):
            continue

        if word and confidence >= 0:
            valid_words.append(word)
            confidence_scores.append(confidence)

    ocr_text = " ".join(valid_words)

    average_confidence = (
        round(sum(confidence_scores) / len(confidence_scores), 2)
        if confidence_scores else None
    )

    return ocr_text, "ocr", average_confidence


def load_pdf(pdf_path):

    pdf_path = Path(pdf_path).resolve()
    patent_name = os.path.basename(pdf_path)

    documents = []

    with fitz.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf):

            text, extraction_method, ocr_confidence = extract_page_text(page)

            if not text:
                continue

            document = Document(
                page_content=text,
                metadata={
                    "source": str(pdf_path),
                    "patent_name": patent_name,
                    "page": page_number,
                    "extraction_method": extraction_method,
                    "ocr_confidence": ocr_confidence
                }
            )

            documents.append(document)

    if not documents:
        raise ValueError(
            f"No extractable text found in PDF: {patent_name}"
        )

    return documents
