
import os

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    patent_name = os.path.basename(pdf_path)

    for doc in documents:
        doc.metadata["patent_name"] = patent_name

    return documents
