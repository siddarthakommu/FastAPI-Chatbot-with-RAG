from fastapi import FastAPI
from app.auth import router as auth_router
from app.chat import router as chat_router
import uvicorn

app = FastAPI(title="RAG Chatbot with FastAPI")

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
