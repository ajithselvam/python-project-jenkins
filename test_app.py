import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    rv = client.get('/')
    assert b'Hello World!' in rv.data
    assert rv.status_code == 200
