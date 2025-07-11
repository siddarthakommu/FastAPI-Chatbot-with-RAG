
---

## **Design Decisions & Trade-offs **

```
# Design Decisions

## Authentication
- Chose OAuth2PasswordBearer with JWT token system for simplicity and statelessness.
- SQLite DB used to store hashed user credentials securely.

## Vector Store & Embedding
- Used HuggingFace model `all-MiniLM-L6-v2` for faster and lighter embedding generation.
- ChromaDB chosen for its lightweight local persistence and fast similarity search.

## RAG Flow
- `load_docs.py` loads support files, chunks them using LangChain’s `RecursiveCharacterTextSplitter`, and stores embeddings.
- `/chat/` endpoint performs similarity search → forms prompt → sends to LLM for response.

## Ultrasafe
- Used UltraSafe which allows OpenAI-compatible APIs for broader compatibility.

## Testing
- Used FastAPI’s `TestClient` to simulate login and chat queries with token authentication.

## Architecture
- Modular app design with folders for `models`, `utils`, and `auth/chat` endpoints.
