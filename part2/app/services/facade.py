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
    def create_place(self, place_data):
        # Validate owner
        owner = self.user_repo.get(place_data.get("owner_id"))
        if not owner:
            raise ValueError("Owner not found")

        # Validate amenities
        amenities = []
        for aid in place_data.get("amenities", []):
            amenity = self.amenity_repo.get(aid)
            if not amenity:
                raise ValueError(f"Amenity ID {aid} not found")
            amenities.append(amenity)

        # Create Place
        place = Place(**place_data)
        for amenity in amenities:
            place.add_amenity(amenity.id)

        self.place_repo.add(place.id, place)
        return self.get_place(place.id)

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
            "owner": {
                "id": owner.id,
                "first_name": owner.first_name,
                "last_name": owner.last_name,
                "email": owner.email
            } if owner else None,
            "amenities": [{"id": a.id, "name": a.name} for a in amenities if a],
            "reviews": [{"id": r.id, "text": r.text, "rating": r.rating, "user_id": r.user_id} for r in reviews if r]
        }

    def get_all_places(self):
        return [self.get_place(p.id) for p in self.place_repo.list_all()]

    def update_place(self, place_id, data):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Update allowed fields
        for field in ["title", "description", "price", "latitude", "longitude"]:
            if field in data:
                setattr(place, field, data[field])

        # Update amenities if provided
        if "amenities" in data:
            new_amenities = []
            for aid in data["amenities"]:
                amenity = self.amenity_repo.get(aid)
                if not amenity:
                    raise ValueError(f"Amenity ID {aid} not found")
                new_amenities.append(aid)
            place.amenities = new_amenities

        return self.get_place(place_id)

    # ------------------- Reviews -------------------
    def create_review(self, review_data):
        # Validate user
        user = self.user_repo.get(review_data.get("user_id"))
        if not user:
            raise ValueError("User not found")

        # Validate place
        place = self.place_repo.get(review_data.get("place_id"))
        if not place:
            raise ValueError("Place not found")

        # Validate rating
        rating = review_data.get("rating")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be integer 1-5")

        review = Review(**review_data)
        self.review_repo.add(review.id, review)
        place.add_review(review.id)
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }

    def get_all_reviews(self):
        return [self.get_review(r.id) for r in self.review_repo.list_all()]

    def update_review(self, review_id, data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        for field in ["text", "rating"]:
            if field in data:
                setattr(review, field, data[field])
        return self.get_review(review_id)

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        return [self.get_review(rid) for rid in place.reviews]
