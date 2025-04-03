import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from app import app, db
except ImportError as e:
    print(f"Error importing app: {e}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    raise

@pytest.fixture
def client():
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Initialize the database
    with app.app_context():
        db.create_all()
    
    # Create a test client
    with app.test_client() as client:
        yield client
    
    # Clean up after tests
    with app.app_context():
        db.session.remove()
        db.drop_all()

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