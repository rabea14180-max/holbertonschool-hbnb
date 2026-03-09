import pytest
from app.models.user import User


def test_create_valid_user():
    user = User(name="Ali", email="ali@test.com")
    assert user.name == "Ali"
    assert user.email == "ali@test.com"


def test_invalid_email():
    with pytest.raises(ValueError):
        User(name="Ali", email="invalid-email")


def test_empty_name():
    with pytest.raises(ValueError):
        User(name="", email="ali@test.com")


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
