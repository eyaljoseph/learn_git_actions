import pytest
from main import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pod1(client):
    """Test pod1 endpoint"""
    response = client.get('/pod1')
    assert response.status_code == 200
    assert "Hello, World! from pod" in response.get_data(as_text=True)

def test_pod2(client):
    """Test pod2 endpoint"""
    response = client.get('/pod2')
    assert response.status_code == 200
    assert "Hello, World! from pod" in response.get_data(as_text=True)

def test_pod3(client):
    """Test pod3 endpoint"""
    response = client.get('/pod3')
    assert response.status_code == 200
    assert "Hello, World! from pod" in response.get_data(as_text=True)

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {
        'status': 'healthy',
        'version': '1.0.0'
    }

def test_pod_number_environment_variable():
    """Test POD_NUMBER environment variable handling"""
    test_pod_number = "TEST-POD-1"
    os.environ["POD_NUMBER"] = test_pod_number
    with app.test_client() as client:
        response = client.get('/pod1')
        assert test_pod_number in response.get_data(as_text=True) 