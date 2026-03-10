# part2/tests/test_models.py
import pytest
from app.models.place import Place
from app.models.review import Review

# ----- Place Tests -----
def test_create_place():
    place = Place(
        title="Hotel",
        description="Nice place",
        price=100.0,
        latitude=21.5,
        longitude=39.2,
        owner_id="user_1"
    )
    assert place.title == "Hotel"
    assert place.price == 100.0
    assert place.owner_id == "user_1"

def test_invalid_place_title():
    with pytest.raises(ValueError):
        Place(title="", description="Desc", price=50.0, owner_id="user_1")

def test_invalid_place_price():
    with pytest.raises(ValueError):
        Place(title="Test", description="Desc", price=-10, owner_id="user_1")

# ----- Review Tests -----
def test_create_review():
    review = Review(
        rating=5,
        comment="Great place",
        user_id="user_1",
        place_id="place_1"
    )
    assert review.rating == 5
    assert review.comment == "Great place"

def test_invalid_rating():
    with pytest.raises(ValueError):
        Review(rating=10, comment="Bad", user_id="user_1", place_id="place_1")

def test_missing_user_id():
    with pytest.raises(ValueError):
        Review(rating=4, comment="Good", user_id=None, place_id="place_1")

def test_missing_place_id():
    with pytest.raises(ValueError):
        Review(rating=4, comment="Good", user_id="user_1", place_id=None)
