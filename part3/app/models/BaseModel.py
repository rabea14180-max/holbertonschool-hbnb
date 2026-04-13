#part3/app/models/BaseModel.py
from app import db
import uuid
from datetime import datetime, timezone


class BaseModel(db.Model):
    """
    Abstract SQLAlchemy base model providing common columns: id, created_at, updated_at.
    __abstract__ = True tells SQLAlchemy NOT to create a separate table for this class.
    """
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not getattr(self, "id", None):
            self.id = str(uuid.uuid4())
        if not getattr(self, "created_at", None):
            self.created_at = datetime.now(timezone.utc)
        if not getattr(self, "updated_at", None):
            self.updated_at = datetime.now(timezone.utc)

    def save(self):
        """Update the updated_at timestamp and flush to session."""
        self.updated_at = datetime.now(timezone.utc)
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Apply a dict of updates and save."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
