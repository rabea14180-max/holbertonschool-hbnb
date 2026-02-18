#part2/app/services/facade.py
from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass


    # =================== AMENITIES ===================
    def create_amenity(self, amenity_data):
        """Create a new Amenity"""
        name = amenity_data.get("name") if amenity_data else None
        if not name:
            raise ValueError("Amenity name is required")
        amenity = Amenity(name=name)
        self.amenity_repo.add(amenity.id, amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Get Amenity by ID"""
        return self.amenity_repo.get(amenity_id)

    def list_amenities(self):
        """Return all amenities"""
        return self.amenity_repo.list_all()

    def update_amenity(self, amenity_id, data):
        """Update existing Amenity"""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        amenity.update(data)
        return amenity
