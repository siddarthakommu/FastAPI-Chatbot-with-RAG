from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_and_chat():
    res = client.post("/auth/token", data={"username": "siddartha", "password": "password123"})
    assert res.status_code == 200
    token = res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    chat = client.post("/chat/", json={"message": "How do I reset my password?"}, headers=headers)
    assert chat.status_code == 200
    assert "response" in chat.json()
