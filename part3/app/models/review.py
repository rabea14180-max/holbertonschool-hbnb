#part3/app/models/review.py
from app import db
from app.models.BaseModel import BaseModel


class Review(BaseModel):
    """Review entity mapped to the 'reviews' table via SQLAlchemy.
    Note: relationships (to User, Place) will be added in a later task.
    """
    __tablename__ = 'reviews'

    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # FK columns stored as plain strings until relationships are added
    user_id = db.Column(db.String(36), nullable=False)
    place_id = db.Column(db.String(36), nullable=False)

    def __init__(self, rating=0, text="", comment=None,
                 user_id=None, place_id=None, **kwargs):
        super().__init__(**kwargs)
        self.rating = rating
        # Support both 'text' (API field) and 'comment' (legacy field)
        self.text = text or comment or ""
        self.user_id = user_id
        self.place_id = place_id
        self.validate()

    # Allow legacy access via .comment for backwards compatibility
    @property
    def comment(self):
        return self.text

    @comment.setter
    def comment(self, value):
        self.text = value

    def validate(self):
        """Validate review attributes."""
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("rating must be an integer between 1 and 5")
        if not isinstance(self.text, str):
            raise ValueError("text must be a string")
        if self.user_id is None:
            raise ValueError("user_id is required")
        if self.place_id is None:
            raise ValueError("place_id is required")

    def updateReview(self, data):
        """Update review attributes."""
        if 'text' in data:
            self.text = data['text']
        if 'comment' in data:
            self.text = data['comment']
        if 'rating' in data:
            self.rating = data['rating']
        self.validate()
        db.session.commit()

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
        })
        return base
