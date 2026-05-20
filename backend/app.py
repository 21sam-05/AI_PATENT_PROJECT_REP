from fastapi import FastAPI, UploadFile, File
import shutil
import os

from utils.pdf_loader import load_pdf
from utils.chunker import split_documents
from utils.embeddings import get_embedding_model
from utils.vector import create_vector_store
from utils.patent_search import search_similar_patents
from utils.llm import get_llm
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure folders exist
os.makedirs("data", exist_ok=True)


# ---------------------------
# HOME ROUTE
# ---------------------------
@app.get("/")
def home():
    return {
        "message": "AI Patent Search Assistant is running"
    }


# ---------------------------
# UPLOAD PATENT PDF
# ---------------------------
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"data/{file.filename}"

    # Save file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load PDF
    documents = load_pdf(file_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Load embedding model
    embedding_model = get_embedding_model()

    # Store in FAISS vector DB
    create_vector_store(chunks, embedding_model)

    return {
        "message": "Patent uploaded and indexed successfully",
        "filename": file.filename,
        "chunks_created": len(chunks)
    }


# ---------------------------
# SIMILAR PATENT SEARCH
# ---------------------------
@app.get("/similar_patents")
def similar_patents(query: str, k: int = 3):

    # Retrieve similar patent chunks
    results = search_similar_patents(query, k)

    formatted_results = []

    combined_context = ""

    # --------------------------------------------
    # HANDLE RESULTS SAFELY
    # --------------------------------------------
    for result in results:

        # unpack safely
        doc = result[0]
        score = result[1]

        # Convert FAISS distance to similarity %
        similarity = 1 / (1 + float(score))

        similarity_percent = round(
            similarity * 100,
            2
        )

        # GET PATENT NAME CORRECTLY
        patent_name = doc.metadata.get(
            "patent_name",
            "Unknown Patent"
        )

        formatted_results.append({

            "patent": patent_name,

            "similarity_percent":
                similarity_percent,

            "raw_score":
                float(score),

            "content":
                doc.page_content[:500]

        })

        combined_context += f"""

PATENT NAME:
{patent_name}

PATENT CONTENT:
{doc.page_content}

"""

    # --------------------------------------------
    # GEMINI ANALYSIS
    # --------------------------------------------
    llm = get_llm()

    prompt = f"""
You are an AI Patent Analysis Expert.

Analyze the USER QUERY against the retrieved patent documents.

USER QUERY:
{query}

RETRIEVED PATENT CONTEXT:
{combined_context}

Tasks:
1. Find overlapping technical concepts
2. Identify which patent is most relevant
3. Estimate prior-art risk:
   LOW / MEDIUM / HIGH
4. Summarize innovation overlap

Return concise analysis.
"""

    response = llm.generate_content(prompt)

    # --------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------
    return {

        "query": query,

        # IMPORTANT:
        # frontend expects "results"
        "results": formatted_results,

        "ai_analysis": response.text

    }




