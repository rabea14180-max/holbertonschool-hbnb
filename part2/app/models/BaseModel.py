#part2/app/models/BaseModel.py
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel defines common attributes/methods
    for all models in the application.
    """

    def __init__(self, **kwargs):
        """
        Initialize a new model instance
        """

        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.utcnow())
        self.updated_at = kwargs.get("updated_at", datetime.utcnow())

    def save(self):
        """
        Updates the updated_at timestamp
        """
        self.updated_at = datetime.utcnow()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save()

   def to_dict(self):
       base = super().to_dict()
       base.update({
           "first_name": self.first_name,
           "last_name": self.last_name,
           "email": self.email,
           "is_admin": getattr(self, "is_admin", None)
       })
       return base
