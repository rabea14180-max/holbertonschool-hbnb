# part2/app/models/amenity.py

from app.models.BaseModel import BaseModel
from app.services import facade


class Amenity(BaseModel):
    def __init__(self, name="", description=""):
        super().__init__()

        self.name = name
        self.description = description

        self.validate()

    def validate(self):
        """Validate amenity attributes."""
        if not isinstance(self.name, str) or self.name.strip() == "":
            raise ValueError("name must be a non-empty string")

        if not isinstance(self.description, str):
            raise ValueError("description must be a string")

    def updateAmenity(self, data):
        """Update amenity attributes."""
        self.update(data)
        self.validate()

    def deleteAmenity(self):
        """Simulate deleting an amenity."""
        return True
        
    def to_dict(self):
        base = super().to_dict()
        base.update({
            "name": self.name,
            "description": self.description
        })
        return base
