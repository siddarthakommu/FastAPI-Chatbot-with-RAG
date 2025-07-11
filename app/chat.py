from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.auth import decode_token
from app.models.schemas import ChatRequest, ChatResponse
from app.rag_pipeline import query_rag_pipeline
from app.utils.history import save_conversation

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    answer = query_rag_pipeline(request.message)
    save_conversation(user, request.message, answer)
    return ChatResponse(user=user, response=answer)
