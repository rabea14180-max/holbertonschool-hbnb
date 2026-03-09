import pytest
from models.user import User

def test_create_valid_user():
    user = User(name="Ali", email="ali@test.com")
    assert user.name == "Ali"

def test_invalid_email():
    with pytest.raises(ValueError):
        User(name="Ali", email="invalid-email")
