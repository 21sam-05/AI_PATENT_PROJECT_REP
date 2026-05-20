## 📌 AI Patent Intelligence System (RAG-based Search Engine)

🚀 Overview

# The AI Patent Intelligence System is a Retrieval-Augmented Generation (RAG) based application that allows users to upload patent PDFs and search for similar innovations using semantic search and AI-powered analysis.

# It helps identify prior-art overlap, similar inventions, and technical relationships between patents using vector embeddings and LLM-based reasoning.

# 🧠 Key Features
📄 Upload patent PDFs for processing
🔍 Semantic search across patent documents
🤖 AI-generated analysis of innovation overlap
📊 Similarity scoring using vector embeddings (FAISS)
🧩 Chunk-based document processing for better retrieval
⚡ FastAPI backend for high-performance API handling
🌐 Simple HTML/CSS/JS frontend interface




# 🛠️ Tech Stack

Backend
FastAPI
Python
LangChain
FAISS (Vector Database)
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

