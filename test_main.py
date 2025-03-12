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

@pytest.fixture
def env_setup():
    """Fixture to set up and tear down environment variables"""
    old_pod_number = os.environ.get('POD_NUMBER')
    os.environ['POD_NUMBER'] = 'TEST-POD-1'
    yield
    if old_pod_number:
        os.environ['POD_NUMBER'] = old_pod_number
    else:
        del os.environ['POD_NUMBER']

def test_pod_number_environment_variable(env_setup, client):
    """Test POD_NUMBER environment variable handling"""
    response = client.get('/pod1')
    assert 'TEST-POD-1' in response.get_data(as_text=True) 
    