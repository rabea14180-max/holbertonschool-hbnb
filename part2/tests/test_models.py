# tests/test_models.py
import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

def test_create_valid_user():
    user = User(first_name="Ali", last_name="Ahmed", email="ali@test.com")
    assert user.first_name == "Ali"
    assert user.last_name == "Ahmed"
    assert user.email == "ali@test.com"

def test_invalid_email():
    with pytest.raises(ValueError):
        User(first_name="Ali", last_name="Ahmed", email="invalid-email")

def test_empty_first_name():
    with pytest.raises(ValueError):
        User(first_name="", last_name="Ahmed", email="ali@test.com")

def test_create_place():
    place = Place(name="Hotel", city="Jeddah")
    assert place.name == "Hotel"

def test_invalid_place_name():
    with pytest.raises(ValueError):
        Place(name="", city="Jeddah")

def test_create_review():
    review = Review(text="Great place", rating=5)
    assert review.rating == 5

def test_invalid_rating():
    with pytest.raises(ValueError):
        Review(text="Bad", rating=10)
