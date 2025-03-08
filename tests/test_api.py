from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_usage_endpoint():
    """Test if the /usage endpoint responds correctly."""
    response = client.get("/usage")
    assert response.status_code == 200  # API should return 200 OK
    data = response.json()
    
    assert "usage" in data
    assert isinstance(data["usage"], list)

    for entry in data["usage"]:
        assert "id" in entry
        assert "timestamp" in entry
        assert "credits" in entry
        if "report_name" in entry:
            assert isinstance(entry["report_name"], str)  # Ensure report_name is a string if present
