# tests/test_api_full.py
import pytest
from run import app
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

from flask import Blueprint

amenity_bp = Blueprint('amenities', __name__, url_prefix='/amenities')

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# ------------------ User Endpoints ------------------
def test_get_users(client):
    response = client.get("/api/v1/users/")
    assert response.status_code == 200

def test_create_user_valid(client):
    response = client.post("/api/v1/users/", json={
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@example.com",
        "password": "pass"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["first_name"] == "Alice"

def test_create_user_invalid(client):
    response = client.post("/api/v1/users/", json={
        "first_name": "",
        "last_name": "",
        "email": "invalid-email"
    })
    assert response.status_code == 400

# ------------------ Place Endpoints ------------------
def test_get_places(client):
    response = client.get("/api/v1/places/")
    assert response.status_code == 200

def test_create_place_valid(client):
    user = User(first_name="Owner", last_name="One", email="owner1@example.com", password="pass")
    response = client.post("/api/v1/places/", json={
        "title": "Hotel",
        "description": "Nice place",
        "price": 150,
        "latitude": 10.0,
        "longitude": 20.0,
        "owner_id": user.id,
        "amenities": []
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Hotel"

def test_create_place_invalid(client):
    response = client.post("/api/v1/places/", json={
        "title": "",
        "price": -10,
        "latitude": 100,
        "longitude": 200,
        "owner_id": "fake_id"
    })
    assert response.status_code == 400

# ------------------ Review Endpoints ------------------
def test_get_reviews(client):
    response = client.get("/api/v1/reviews/")
    assert response.status_code == 200

def test_create_review_valid(client):
    user = User(first_name="User", last_name="A", email="usera@example.com", password="pass")
    place = Place(title="Inn", description="Cozy", price=80, latitude=15, longitude=25, owner_id=user.id)
    response = client.post("/api/v1/reviews/", json={
        "rating": 5,
        "comment": "Excellent",
        "user_id": user.id,
        "place_id": place.id
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["rating"] == 5

def test_create_review_invalid(client):
    response = client.post("/api/v1/reviews/", json={
        "rating": 10,
        "comment": "",
        "user_id": "fake_user",
        "place_id": "fake_place"
    })
    assert response.status_code == 400

# ------------------ Amenity Endpoints ------------------
def test_get_amenities(client):
    response = client.get("/api/v1/amenities/")
    assert response.status_code == 200

def test_create_amenity_valid(client):
    response = client.post("/api/v1/amenities/", json={
        "name": "Gym",
        "description": "Fitness center"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Gym"

def test_create_amenity_invalid(client):
    response = client.post("/api/v1/amenities/", json={
        "name": ""
    })
    assert response.status_code == 400
