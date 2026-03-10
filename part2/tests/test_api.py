#part2/tests/test_api.py
import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

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
    # اضف owner_id ليوافق validate
    place = Place(title="Hotel", city="Jeddah", owner_id=1)
    assert place.title == "Hotel"
    assert place.owner_id == 1

def test_invalid_place_name():
    with pytest.raises(ValueError):
        Place(title="", city="Jeddah", owner_id=1)

def test_create_review():
    # اضف user_id و place_id لتجنب ValueError
    review = Review(rating=5, comment="Great place", user_id=1, place_id=1)
    assert review.rating == 5
    assert review.user_id == 1
    assert review.place_id == 1

def test_invalid_rating():
    with pytest.raises(ValueError):
        Review(rating=10, comment="Bad", user_id=1, place_id=1)
