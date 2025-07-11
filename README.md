# RAG Chatbot with FastAPI

A secure and lightweight Retrieval-Augmented Generation chatbot using FastAPI, JWT auth, HuggingFace embeddings, and Chroma vector database.

## Setup Instructions

```bash
# Create virtual environment
python -m venv V
source V/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Load environment variables
cp .env.example .env
# Add your credentials in `.env`

# Load documents into vector store
python load_docs.py

# Run FastAPI app
uvicorn app.main:app --reload
