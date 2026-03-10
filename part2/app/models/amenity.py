from app.models.BaseModel import BaseModel


class Amenity(BaseModel):

    def __init__(self, name=""):
        super().__init__()

        self.name = name
        self.validate()

    def validate(self):

        if not isinstance(self.name, str) or self.name.strip() == "":
            raise ValueError("Amenity name cannot be empty")

        if len(self.name) > 50:
            raise ValueError("Amenity name must be at most 50 characters")

    def update(self, data):

        if "name" in data:
            self.name = data["name"]

        self.validate()
        self.save()

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
