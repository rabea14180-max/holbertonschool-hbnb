# part2/app/models/review.py

from app.models.BaseModel import BaseModel
from app.services import facade


class Review(BaseModel):
   def __init__(self, title="", description="", price=0.0, latitude=0.0, longitude=0.0, owner_id=None): 
       super().__init__()
       
       self.title = title 
       self.description = description 
       self.price = price
       self.latitude = latitude 
       self.longitude = longitude
       
       self.owner_id = owner_id # linked to User 
       self.reviews = [] # list of Review objects or IDs 
       self.amenities = [] # list of Amenity objects or IDs 
       
       self.validate()

    def validate(self):
        """Validate review attributes."""
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("rating must be an integer between 1 and 5")

        if not isinstance(self.comment, str):
            raise ValueError("comment must be a string")

        if self.user_id is None:
            raise ValueError("user_id is required")

        if self.place_id is None:
            raise ValueError("place_id is required")

    def updateReview(self, data):
        """Update review attributes."""
        self.update(data)
        self.validate()

    def deleteReview(self):
        """Simulate deleting a review."""
        return True
