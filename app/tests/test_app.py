import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_hello_endpoint(client):
    """Test the hello endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert "message" in response.json
    assert "status" in response.json
    assert response.json["status"] == "running" 