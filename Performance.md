#  Performance Analysis

## Retrieval

- Vector Store: We used ChromaDB as the vector database to store and retrieve document embeddings. It provides persistent local storage, making it fast and lightweight for development use-cases.

- Embedding Model: Hugging Face's all-MiniLM-L6-v2 model is used for creating semantic embeddings. It balances speed and accuracy well.

- Retrieval Strategy: Top-k similarity search (k=2) retrieves the two most relevant documents per query based on cosine similarity in embedding space.


## Improvements for Future:
- Replace Chroma with FAISS or Weaviate for scalable production setups.

- Integrate feedback loop for continuous improvement (like relevance scoring).

- Add batch processing for multi-query performance benchmarks.
