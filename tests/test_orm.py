import sys
sys.path.append('./tests')
sys.path.append('./tests/app')

from starlette.testclient import TestClient
import pytest

@pytest.fixture(scope='module')
def test_client():
    import os
    os.environ['ENV'] = 'TEST'
    os.path.exists('./test.db') and os.unlink('./test.db')
    from main import app
    client = TestClient(app)
    res = client.post('/users', json={'id': 'joe', 'email': 'joe@test.com'})
    assert res.status_code == 200
    return client

def test_get_users(test_client):
    res = test_client.get('/users')
    assert res.status_code == 200
    users = res.json()
    assert len(users) == 1
    assert users[0]['id'] == 'joe'

