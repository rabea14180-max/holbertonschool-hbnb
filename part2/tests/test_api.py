import pytest
from app.api import create_api
from app.services import facade
from flask import json

@pytest.fixture
def client():
    app = create_api()
    app.config['TESTING'] = True
    return app.test_client()

# ---------- USERS API ----------
def test_create_user(client):
    payload = {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@example.com",
        "password": "1234",
        "is_admin": False
    }
    response = client.post("/api/v1/users/", json=payload)
    data = response.get_json()
    assert response.status_code == 201
    assert data["first_name"] == "Alice"

def test_get_users(client):
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# ---------- AMENITIES API ----------
def test_create_amenity(client):
    payload = {"name": "WiFi"}
    response = client.post("/api/v1/amenities/", json=payload)
    data = response.get_json()
    assert response.status_code == 201
    assert data["name"] == "WiFi"

def test_get_amenities(client):
    response = client.get("/api/v1/amenities/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# ---------- PLACES API ----------
def test_create_place(client):
    # need an existing user for owner_id
    user = facade.create_user({
        "first_name": "Bob", "last_name": "Smith",
        "email": "bob@example.com", "password": "1234"
    })
    payload = {
        "title": "My House",
        "description": "Nice place",
        "price": 100,
        "latitude": 10.0,
        "longitude": 20.0,
        "owner_id": user.id
    }
    response = client.post("/api/v1/places/", json=payload)
    data = response.get_json()
    assert response.status_code == 201
    assert data["title"] == "My House"

def test_get_places(client):
    response = client.get("/api/v1/places/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# ---------- REVIEWS API ----------
def test_create_review(client):
    # need user and place
    user = facade.create_user({
        "first_name": "Charlie", "last_name": "Brown",
        "email": "charlie@example.com", "password": "1234"
    })
    place = facade.create_place({
        "title": "House", "description": "Nice",
        "price": 50, "latitude": 10, "longitude": 20,
        "owner_id": user.id
    })
    payload = {
        "text": "Amazing place",
        "rating": 5,
        "user_id": user.id,
        "place_id": place.id
    }
    response = client.post("/api/v1/reviews/", json=payload)
    data = response.get_json()
    assert response.status_code == 201
    assert data["text"] == "Amazing place"

def test_get_reviews(client):
    response = client.get("/api/v1/reviews/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
