import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

@pytest.fixture(autouse=True)
def reset_activities():
    # Resetuje stan activities przed każdym testem
    for activity in activities.values():
        activity['participants'].clear()

@pytest.fixture
def client():
    return TestClient(app)
