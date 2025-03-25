from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Running"}

def test_read_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"message": "Checking"}

