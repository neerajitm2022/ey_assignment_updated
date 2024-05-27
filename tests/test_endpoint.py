from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_addition_endpoint():
    payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["status"] == "complete"
    assert isinstance(data["response"], list)
    assert len(data["response"]) == 2