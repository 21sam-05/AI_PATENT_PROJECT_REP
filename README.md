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

## 🏗️ Architecture

- Python
- LangChain
- FAISS (Vector Database)
Google Gemini API
Frontend
HTML
CSS
JavaScript

# ⚙️ How It Works
User uploads a patent PDF
PDF is converted into text using LangChain
Text is split into chunks
Each chunk is converted into embeddings
Embeddings are stored in FAISS vector database
User enters a query
System retrieves most similar patent chunks
Gemini AI generates analysis of overlap and innovation similarity
Results are displayed in frontend UI

