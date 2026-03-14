# tests/test_models_full.py
import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

# ------------------ User Tests ------------------
def test_create_user_valid():
    user = User(first_name="John", last_name="Doe", email="john@example.com", password="pass")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@example.com"
    assert hasattr(user, "id")

def test_create_user_invalid_email():
    with pytest.raises(ValueError):
        User(first_name="Jane", last_name="Doe", email="", password="pass")

def test_create_user_missing_password():
    with pytest.raises(ValueError):
        User(first_name="Jane", last_name="Doe", email="jane@example.com", password=None)

# ------------------ Place Tests ------------------
def test_create_place_valid():
    user = User(first_name="Owner", last_name="One", email="owner@example.com", password="pass")
    place = Place(title="Hotel", description="Nice", price=100, latitude=10, longitude=20, owner_id=user.id)
    assert place.title == "Hotel"
    assert place.price == 100
    assert place.owner_id == user.id

def test_create_place_invalid_price():
    with pytest.raises(ValueError):
        Place(title="Hotel", description="Nice", price=-50, latitude=10, longitude=20, owner_id="user1")

def test_create_place_invalid_lat_lon():
    user = User(first_name="Owner", last_name="Two", email="owner2@example.com", password="pass")
    with pytest.raises(ValueError):
        Place(title="Inn", description="Desc", price=50, latitude=-100, longitude=200, owner_id=user.id)

# ------------------ Amenity Tests ------------------
def test_create_amenity_valid():
    amenity = Amenity(name="Pool", description="Outdoor")
    assert amenity.name == "Pool"

def test_create_amenity_invalid_name():
    with pytest.raises(ValueError):
        Amenity(name="", description="Desc")

# ------------------ Review Tests ------------------
def test_create_review_valid():
    user = User(first_name="User", last_name="A", email="usera@example.com", password="pass")
    place = Place(title="Hotel", description="Nice", price=100, latitude=10, longitude=20, owner_id=user.id)
    review = Review(rating=5, comment="Great", user_id=user.id, place_id=place.id)
    assert review.rating == 5
    assert review.comment == "Great"

def test_create_review_invalid_rating():
    user = User(first_name="User", last_name="B", email="userb@example.com", password="pass")
    place = Place(title="Inn", description="Cozy", price=80, latitude=15, longitude=25, owner_id=user.id)
    with pytest.raises(ValueError):
        Review(rating=10, comment="Bad", user_id=user.id, place_id=place.id)

def test_create_review_missing_user_or_place():
    user = User(first_name="User", last_name="C", email="userc@example.com", password="pass")
    place = Place(title="Villa", description="Lux", price=200, latitude=20, longitude=30, owner_id=user.id)
    with pytest.raises(ValueError):
        Review(rating=4, comment="Good", user_id=None, place_id=place.id)
    with pytest.raises(ValueError):
        Review(rating=4, comment="Good", user_id=user.id, place_id=None)
