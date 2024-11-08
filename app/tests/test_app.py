import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_menu_page(client):
    response = client.get('/menu')
    assert response.status_code == 200

def test_add_to_cart(client):
    # Add a product to the database
    with create_app().app_context():
        product = Product(name='Test Cake', price=10.00, description='Test Description')
        db.session.add(product)
        db.session.commit()
        
        response = client.get(f'/add_to_cart/{product.id}')
        assert response.status_code == 302  # Redirect status code