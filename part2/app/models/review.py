# part2/app/models/review.py

from app.models.BaseModel import BaseModel
from app.services import facade


class Review(BaseModel):
    def __init__(self, **kwargs):
        super().__init__()

        self.rating = kwargs.get("rating", 0)
        self.comment = kwargs.get("text", kwargs.get("comment", ""))
        self.user_id = kwargs.get("user_id", None)
        self.place_id = kwargs.get("place_id", None)

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
