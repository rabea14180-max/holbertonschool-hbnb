# part2/app/models/user.py
from app.models.BaseModel import BaseModel
from app.services import facade

class User(BaseModel):
    
 def __init__(self, email="", password="", first_name="",
                 last_name="", is_admin=False, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.places = []
        self.reviews = []
        self.validate()

def validate(self):
        if not isinstance(self.first_name, str) or not self.first_name.strip():
            raise ValueError("first_name is required")
        if len(self.first_name.strip()) > 50:
            raise ValueError("first_name must be at most 50 characters")

        if not isinstance(self.last_name, str) or not self.last_name.strip():
            raise ValueError("last_name is required")
        if len(self.last_name.strip()) > 50:
            raise ValueError("last_name must be at most 50 characters")

        if not isinstance(self.email, str) or not self.email.strip():
            raise ValueError("email is required")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", self.email.strip()):
            raise ValueError("Invalid email format")

        if not isinstance(self.is_admin, bool):
            raise ValueError("is_admin must be a boolean")

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)

    def update_info(self, **kwargs):
        allowed_fields = ["email", "password", "first_name", "last_name", "is_admin"]
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
        self.validate()
        self.save()

    def __str__(self):
        return f"[User] ({self.id}) {self.first_name} {self.last_name} <{self.email}>"

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        })
        return base
