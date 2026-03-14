# tests/test_models.py

import pytest
from app.models.place import Place
from app.models.review import Review
from app.models.user import User
from app.models.amenity import Amenity

# -------------------- PLACE TESTS -------------------- #
def test_place_creation():
    place = Place(title="Cozy Apartment", description="Nice place", price=100.0,
                  latitude=25.0, longitude=45.0, owner_id="owner123")
    assert place.title == "Cozy Apartment"
    assert place.price == 100.0
    assert place.reviews == []
    assert place.amenities == []

def test_place_validation_error():
    with pytest.raises(ValueError):
        Place(title="", description="desc", price=50.0, latitude=0, longitude=0, owner_id="id1")

# -------------------- REVIEW TESTS -------------------- #
def test_review_creation():
    review = Review(comment="Great place!", rating=5, user_id="user123", place_id="place123")
    assert review.comment == "Great place!"
    assert review.rating == 5

def test_review_rating_validation():
    with pytest.raises(ValueError):
        Review(comment="Bad review", rating=10, user_id="user1", place_id="place1")

# -------------------- USER TESTS -------------------- #
def test_user_creation():
    user = User(first_name="Solaf", last_name="Aziz", email="Sol@test.com", password="pass123")
    assert user.first_name == "Solaf"
    assert user.email == "Sol@test.com"

def test_user_email_validation():
    with pytest.raises(ValueError):
        User(first_name="Bob", last_name="Jones", email="bob-at-test.com", password="pass123")

# -------------------- AMENITY TESTS -------------------- #
def test_amenity_creation():
    amenity = Amenity(name="Pool")
    assert amenity.name == "Pool"

def test_amenity_name_validation():
    with pytest.raises(ValueError):
        Amenity(name="")
