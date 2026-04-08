# part3/tests/test_api.py
import json


def _register(client, email, is_admin=False):
    return client.post(
        "/api/v1/users/register",
        data=json.dumps(
            {
                "first_name": "Test",
                "last_name": "User",
                "email": email,
                "password": "Secret123!",
                "is_admin": is_admin,
            }
        ),
        content_type="application/json",
    )


def _login(client, email, password="Secret123!"):
    return client.post(
        "/api/v1/users/login",
        data=json.dumps({"email": email, "password": password}),
        content_type="application/json",
    )


def test_users_collection_get_not_allowed(client):
    response = client.get("/api/v1/users/")
    assert response.status_code == 405


def test_get_places_empty(client):
    response = client.get("/api/v1/places/")
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_reviews_empty(client):
    response = client.get("/api/v1/reviews/")
    assert response.status_code == 200
    assert response.get_json() == []


def test_guest_cannot_create_place(client):
    email = "guest@example.com"
    assert _register(client, email, is_admin=False).status_code == 201
    login = _login(client, email)
    assert login.status_code == 200
    token = login.get_json()["access_token"]
    response = client.post(
        "/api/v1/places/",
        data=json.dumps(
            {
                "title": "Villa",
                "description": "Nice",
                "price": 99.0,
                "latitude": 40.0,
                "longitude": -74.0,
                "amenities": [],
            }
        ),
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
    assert "Admin" in response.get_json().get("error", "")


def test_admin_can_create_place(client):
    email = "admin@example.com"
    assert _register(client, email, is_admin=True).status_code == 201
    login = _login(client, email)
    assert login.status_code == 200
    token = login.get_json()["access_token"]
    response = client.post(
        "/api/v1/places/",
        data=json.dumps(
            {
                "title": "Admin Villa",
                "description": "OK",
                "price": 120.0,
                "latitude": 48.85,
                "longitude": 2.35,
                "amenities": [],
            }
        ),
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Admin Villa"
    assert "id" in data

    listed = client.get("/api/v1/places/").get_json()
    assert len(listed) == 1
    assert listed[0]["title"] == "Admin Villa"


def test_guest_can_review_admin_place(client):
    """End-to-end: admin creates a listing; guest user posts a review."""
    assert _register(client, "owner@example.com", is_admin=True).status_code == 201
    owner_login = _login(client, "owner@example.com")
    owner_token = owner_login.get_json()["access_token"]
    place_resp = client.post(
        "/api/v1/places/",
        data=json.dumps(
            {
                "title": "Beach House",
                "description": "Sandy",
                "price": 200.0,
                "latitude": 25.0,
                "longitude": -80.0,
                "amenities": [],
            }
        ),
        content_type="application/json",
        headers={"Authorization": f"Bearer {owner_token}"},
    )
    assert place_resp.status_code == 201
    place_id = place_resp.get_json()["id"]

    assert _register(client, "reviewer@example.com", is_admin=False).status_code == 201
    rev_login = _login(client, "reviewer@example.com")
    rev_token = rev_login.get_json()["access_token"]
    review_resp = client.post(
        "/api/v1/reviews/",
        data=json.dumps(
            {"place_id": place_id, "text": "Lovely stay", "rating": 5}
        ),
        content_type="application/json",
        headers={"Authorization": f"Bearer {rev_token}"},
    )
    assert review_resp.status_code == 201
    assert review_resp.get_json()["rating"] == 5

    detail = client.get(f"/api/v1/places/{place_id}").get_json()
    assert len(detail["reviews"]) == 1
    assert detail["reviews"][0]["text"] == "Lovely stay"


def test_login_invalid_credentials(client):
    assert _register(client, "u1@example.com", is_admin=False).status_code == 201
    bad = _login(client, "u1@example.com", password="WrongPassword!")
    assert bad.status_code == 401


def test_create_place_without_token(client):
    response = client.post(
        "/api/v1/places/",
        data=json.dumps(
            {
                "title": "X",
                "description": "y",
                "price": 1.0,
                "latitude": 0.0,
                "longitude": 0.0,
                "amenities": [],
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 401


def test_get_unknown_place(client):
    r = client.get("/api/v1/places/00000000-0000-0000-0000-000000000001")
    assert r.status_code == 404
    assert "error" in r.get_json()


def test_duplicate_review_rejected(client):
    assert _register(client, "o2@example.com", is_admin=True).status_code == 201
    ot = _login(client, "o2@example.com").get_json()["access_token"]
    pid = client.post(
        "/api/v1/places/",
        data=json.dumps(
            {
                "title": "Dup",
                "description": "d",
                "price": 10.0,
                "latitude": 1.0,
                "longitude": 1.0,
                "amenities": [],
            }
        ),
        content_type="application/json",
        headers={"Authorization": f"Bearer {ot}"},
    ).get_json()["id"]
    assert _register(client, "r2@example.com", is_admin=False).status_code == 201
    rt = _login(client, "r2@example.com").get_json()["access_token"]
    body = {"place_id": pid, "text": "First", "rating": 5}
    h = {"Authorization": f"Bearer {rt}", "Content-Type": "application/json"}
    assert client.post("/api/v1/reviews/", data=json.dumps(body), headers=h).status_code == 201
    second = client.post("/api/v1/reviews/", data=json.dumps(body), headers=h)
    assert second.status_code == 400
