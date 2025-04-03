import os
import sys
import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the app and db
from app import app, db

# This fixture will be available to all tests
@pytest.fixture(scope="session")
def app():
    """Create and configure a Flask app for testing."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    yield app
    
    # Clean up
    with app.app_context():
        db.session.remove()
        db.drop_all()

# This file helps pytest find and import the app module
# It's automatically loaded by pytest before running tests 