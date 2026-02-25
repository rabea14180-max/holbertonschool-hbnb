# part2/app/models/user.py
from app.models.BaseModel import BaseModel
from typing import List


class User(BaseModel):
    def __init__(self, email: str = "", password: str = "", first_name: str = "",
                 last_name: str = "", is_admin=False, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.places: List['Place'] = []
        self.reviews: List['Review'] = []

    def add_place(self, place: 'Place'):
        if place not in self.places:
            self.places.append(place)
            place.user_id = self.id

    def add_review(self, review: 'Review'):
        if review not in self.reviews:
            self.reviews.append(review)
            review.user_id = self.id

    def update_info(self, **kwargs):
        allowed_fields = ['email', 'password', 'first_name', 'last_name', 'is_admin']
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
        self.save()

    def __str__(self):
        return f"[User] ({self.id}) {self.first_name} {self.last_name} <{self.email}>"

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": getattr(self, "is_admin", None)
        })
        return base
