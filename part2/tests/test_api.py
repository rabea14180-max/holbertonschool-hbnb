import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_get_users(client):
    response = client.get("/api/v1/users")
    assert response.status_code == 200


def test_create_user(client):
    data = {
        "name": "Ali",
        "email": "ali@test.com"
    }

    response = client.post("/api/v1/users", json=data)
    assert response.status_code in [200, 201]


def test_create_invalid_user(client):
    data = {
        "name": "",
        "email": "invalid"
    }

    response = client.post("/api/v1/users", json=data)
    assert response.status_code == 400


def test_get_places(client):
    response = client.get("/api/v1/places")
    assert response.status_code == 200


def test_get_reviews(client):
    response = client.get("/api/v1/reviews")
    assert response.status_code == 200
