# part2/app/models/user.py

from app.models.BaseModel import BaseModel


class User(BaseModel):
    def __init__(self, first_name="", last_name="", email="", password="", is_admin=False):
        super().__init__()

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

        self.validate()

    def validate(self):
        """Validate user attributes."""
        if not isinstance(self.first_name, str) or self.first_name.strip() == "":
            raise ValueError("first_name must be a non-empty string")

        if not isinstance(self.last_name, str) or self.last_name.strip() == "":
            raise ValueError("last_name must be a non-empty string")

        if not isinstance(self.email, str) or self.email.strip() == "":
            raise ValueError("email must be a non-empty string")

        if "@" not in self.email or "." not in self.email:
            raise ValueError("email must be a valid email address")

        if not isinstance(self.password, str) or self.password.strip() == "":
            raise ValueError("password must be a non-empty string")

        if not isinstance(self.is_admin, bool):
            raise ValueError("is_admin must be a boolean")

    def register(self):
        """Simulate user registration."""
        self.validate()
        return True

    def updateProfile(self, data):
        """Update user profile information."""
        self.update(data)
        self.validate()

    def delete(self):
        """Simulate deleting the user."""
        return True
