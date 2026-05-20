# 🧠 AI Patent Intelligence System (RAG-Based Search Engine)

A Retrieval-Augmented Generation (RAG) system that allows users to upload patent PDFs and search for similar innovations using semantic search + AI analysis.

---

## 🚀 Features

- 📄 Upload patent PDFs
- 🔍 Semantic patent search using embeddings
- 📊 Similarity scoring (FAISS vector search)
- 🤖 AI-powered innovation overlap analysis (Gemini)
- 🧩 Chunk-based document processing
- ⚡ FastAPI backend for fast API handling
- 🌐 Simple HTML/CSS/JS frontend

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- LangChain
- FAISS
- Google Gemini API

### Frontend
- HTML
- CSS
- JavaScript

---

## ⚙️ How It Works

1. Upload a patent PDF
2. Extract text using LangChain
3. Split into chunks
4. Convert chunks into embeddings
5. Store embeddings in FAISS
6. User enters a query
7. Retrieve similar patent chunks
8. Gemini generates analysis
9. Results shown in frontend

---
