# AI Patent Intelligence System

An AI-powered patent analysis and semantic search application that uses **Retrieval-Augmented Generation (RAG)** to help users explore patent documents, retrieve technically relevant information, and analyze relationships between inventions.

Built using **FastAPI, LangChain, FAISS, Hugging Face embeddings, Google Gemini, and Tesseract OCR**.

---

## Overview

Patent documents contain large amounts of technical information, making it difficult to manually identify relevant inventions, understand technical specifications, and compare related patent documents.

The AI Patent Intelligence System addresses this challenge by combining document processing, semantic search, and Large Language Models into a unified application.

Users can upload patent PDFs, extract their contents using digital text extraction and OCR, generate vector embeddings, and retrieve relevant patent information through natural-language queries.

The retrieved context is then used by Google Gemini to generate contextual responses and support technical patent comparison.

## Key Features

### 1. Patent PDF Processing
- Upload and process patent PDF documents.
- Extract text from digitally generated PDFs using PyMuPDF.
- Preserve page-level document metadata.
- Process multiple patent documents through a unified pipeline.

### 2. OCR-Based Text Extraction
- Detect pages with insufficient digitally extractable text.
- Apply Tesseract OCR as a fallback for scanned pages.
- Extract text from patent drawings and scanned document pages.
- Record the extraction method and OCR confidence metadata for each page.

### 3. Intelligent Document Chunking
- Split extracted patent content into smaller, manageable chunks.
- Use LangChain's `RecursiveCharacterTextSplitter`.
- Preserve document metadata across chunks.

Current configuration:
- Chunk size: 1000 characters
- Chunk overlap: 150 characters

### 4. Semantic Search
- Generate vector embeddings using `all-MiniLM-L6-v2`.
- Store and retrieve document embeddings using FAISS.
- Use normalized embeddings with inner-product similarity.
- Retrieve technically relevant patent passages using natural-language queries.

### 5. Retrieval-Augmented Generation (RAG)
- Retrieve relevant patent passages before generating responses.
- Use Google Gemini 2.5 Flash to generate contextual answers.
- Ground responses in retrieved patent content.

### 6. Patent Comparison and Analysis
- Support technical comparison of patent documents.
- Identify potentially overlapping technical concepts.
- Use semantic retrieval and LLM-based analysis to assist patent exploration.

*AI-generated comparisons are intended as technical research assistance, not legal opinions or determinations of patent infringement, novelty, or validity.*

### 7. Retrieval Evaluation
- Maintain a manually labelled retrieval evaluation dataset.
- Measure Precision@K and Recall@K.
- Calculate mean retrieval metrics across evaluation queries.
- Inspect retrieved patent pages and similarity scores to identify retrieval weaknesses.

---

## System Architecture

```text
             USER
               |
               v
        PATENT PDF UPLOAD
               |
               v
         FASTAPI BACKEND
               |
               v
        PDF TEXT EXTRACTION
               |
        +------+------+
        |             |
        v             v
   DIGITAL TEXT      OCR
   EXTRACTION     (TESSERACT)
        |             |
        +------+------+
               |
               v
        DOCUMENT CHUNKING
               |
               v
        TEXT EMBEDDINGS
               |
               v
          FAISS INDEX
               |
               v
        SEMANTIC RETRIEVAL
               |
               v
          GEMINI LLM
               |
               v
       CONTEXTUAL RESPONSE
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI |
| API Server | Uvicorn |
| LLM | Google Gemini 2.5 Flash |
| RAG Framework | LangChain |
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Library | Hugging Face |
| Vector Database | FAISS |
| PDF Processing | PyMuPDF |
| OCR Engine | Tesseract OCR |
| OCR Integration | Pytesseract |
| Image Processing | Pillow |
| Text Splitting | RecursiveCharacterTextSplitter |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git and GitHub |

---

## Project Structure

```text
AI_PATENT_PROJECT_REP/
│
├── backend/
│   ├── app.py
│   │
│   ├── evaluation/
│   │   └── retrieval_eval.py
│   │
│   ├── utils/
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── llm.py
│   │   ├── patent_comparison.py
│   │   ├── patent_embeddings.py
│   │   ├── patent_search.py
│   │   ├── pdf_loader.py
│   │   ├── rag_pipeline.py
│   │   ├── retriever.py
│   │   └── vector.py
│   │
│   ├── data/
│   └── vectordb/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*The frontend files and additional project files are maintained in the repository. Local patent PDFs, virtual environments, and generated vector database files are excluded from version control.*

---

## Getting Started

Follow these instructions to run the project locally.

### Prerequisites

Install the following:

- Python 3.12
- Git
- Tesseract OCR
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/21sam-05/AI_PATENT_PROJECT_REP.git
```

Navigate into the project:

```bash
cd AI_PATENT_PROJECT_REP
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows CMD:

```cmd
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

Install the Tesseract OCR engine on your operating system.

For Windows, the default installation path used by the current PDF loader is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Ensure Tesseract is installed and accessible to the application.

Verify the installation:

```cmd
tesseract --version
```

### 5. Configure Environment Variables

Create a `.env` file in the project root.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your actual `.env` file or expose your API key in source code.

### 6. Run the Backend

Navigate to the backend directory:

```cmd
cd backend
```

Start the FastAPI development server:

```cmd
uvicorn app:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

### 7. Access API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

http://127.0.0.1:8000/docs

Use the available endpoints to interact