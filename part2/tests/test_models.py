import pytest
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place, Review

# ---------- USER TESTS ----------
def test_user_creation():
    user = User(first_name="Alice", last_name="Smith", email="alice@test.com", password="1234")
    assert user.first_name == "Alice"
    assert user.email == "alice@test.com"
    assert user.is_admin is False

def test_user_validation_error():
    with pytest.raises(ValueError):
        User(first_name="", last_name="Smith", email="alice@test.com", password="1234")

# ---------- AMENITY TESTS ----------
def test_amenity_creation():
    amenity = Amenity(name="WiFi")
    assert amenity.name == "WiFi"

def test_amenity_validation_error():
    with pytest.raises(ValueError):
        Amenity(name="")  # empty name not allowed

# ---------- PLACE TESTS ----------
def test_place_creation():
    place = Place(title="My House", description="Nice place", price=100.0,
                  latitude=10.0, longitude=20.0, owner_id="user123")
    assert place.title == "My House"
    assert place.price == 100.0

def test_place_validation_error():
    with pytest.raises(ValueError):
        Place(title="", description="desc", price=-10, latitude=0, longitude=0, owner_id="123")

# ---------- REVIEW TESTS ----------
def test_review_creation():
    review = Review(text="Great place", rating=5, user_id="u1", place_id="p1")
    assert review.text == "Great place"
    assert review.rating == 5

def test_review_validation_error():
    with pytest.raises(ValueError):
        Review(text="", rating=10, user_id="u1", place_id="p1")  # invalid text & rating
