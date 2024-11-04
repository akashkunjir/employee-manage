import pytest
from app import create_app, db
from model import Employee

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_employee(client):
    response = client.post('/api/employees/', json={'name': 'John Doe', 'department': 'Engineering'})
    assert response.status_code == 201
    assert b'John Doe' in response.data

def test_get_employees(client):
    response = client.get('/api/employees/?page=1&per_page=10')
    assert response.status_code == 200
