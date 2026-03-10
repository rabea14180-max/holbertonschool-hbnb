from app.models.BaseModel import BaseModel


class Review(BaseModel):

    def __init__(self, text="", rating=0, user_id="", place_id=""):
        super().__init__()

        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

        self.validate()

    def validate(self):

        if not isinstance(self.text, str) or self.text.strip() == "":
            raise ValueError("Review text cannot be empty")

        if not isinstance(self.rating, int):
            raise ValueError("Rating must be an integer")

        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5")
