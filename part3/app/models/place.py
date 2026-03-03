# part2/app/models/place.py

from app.models.BaseModel import BaseModel
from app.services import facade


class Place(BaseModel):
    def __init__(self, title="", description="", price=0.0,
                 latitude=0.0, longitude=0.0, owner_id=None):
        super().__init__()

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # Relationship
        self.owner_id = owner_id  # linked to User
        self.reviews = []         # list of Review objects or IDs
        self.amenities = []       # list of Amenity objects or IDs

        self.validate()

    def validate(self):
        """Validate place attributes."""
        if not isinstance(self.title, str) or self.title.strip() == "":
            raise ValueError("title must be a non-empty string")

        if not isinstance(self.description, str):
            raise ValueError("description must be a string")

        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("price must be a positive number")

        if not isinstance(self.latitude, (int, float)) or not (-90 <= self.latitude <= 90):
            raise ValueError("latitude must be between -90 and 90")

        if not isinstance(self.longitude, (int, float)) or not (-180 <= self.longitude <= 180):
            raise ValueError("longitude must be between -180 and 180")

        if self.owner_id is None:
            raise ValueError("owner_id is required")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.save()

    def remove_amenity(self, amenity):
        """Remove an amenity from the place."""
        if amenity in self.amenities:
            self.amenities.remove(amenity)
            self.save()

    def updatePlace(self, data):
        """Update place attributes."""
        self.update(data)
        self.validate()

    def deletePlace(self):
        """Simulate deleting a place."""
        return True
