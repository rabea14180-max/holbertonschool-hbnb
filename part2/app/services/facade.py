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

   # ------------------- Places -------------------
    def create_place(self, data):
        place = Place(**data)
        self.place_repo.add(place.id, place)
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        owner = self.user_repo.get(place.owner_id)
        amenities = [self.amenity_repo.get(aid) for aid in place.amenities]
        reviews = [self.review_repo.get(rid) for rid in place.reviews]
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": owner,
            "amenities": [{"id": a.id, "name": a.name} for a in amenities if a],
            "reviews": [{"id": r.id, "text": r.text, "rating": r.rating, "user_id": r.user_id} for r in reviews if r]
        }

    def get_all_places(self):
        return [{"id": p.id, "title": p.title, "latitude": p.latitude, "longitude": p.longitude}
                for p in self.place_repo.list_all()]

    def update_place(self, place_id, data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        place.update(data)
        place.validate()
        return place


    # ------------------- Reviews -------------------
    def create_review(self, data):
        review = Review(**data)
        self.review_repo.add(review.id, review)
        # attach review to place
        place = self.place_repo.get(review.place_id)
        if place:
            place.add_review(review.id)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.list_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        return [self.review_repo.get(rid) for rid in place.reviews]

    def update_review(self, review_id, data):
        review = self.review_repo.get(review_id)
        if review:
            review.update(data)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
