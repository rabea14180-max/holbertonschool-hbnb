#part2/app/services/facade.py
from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.services import facade

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # =================== USERS ===================
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update_info(**data)
        return user

    # =================== AMENITIES ===================
    def create_amenity(self, amenity_data):
        if not amenity_data or not amenity_data.get("name"):
            raise ValueError("Amenity name is required")
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def list_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        amenity.updateAmenity(data)
        return amenity

    # =================== PLACES ===================
    def create_place(self, place_data):
        owner = self.user_repo.get(place_data.get("owner_id"))
        if not owner:
            raise ValueError("Owner not found")

        amenities = []
        for aid in place_data.get("amenities", []):
            amenity = self.amenity_repo.get(aid)
            if not amenity:
                raise ValueError(f"Amenity ID {aid} not found")
            amenities.append(amenity)

        place = Place(**place_data)
        for amenity in amenities:
            place.add_amenity(amenity.id)

        self.place_repo.add(place)
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
            "reviews": [{"id": r.id, "text": r.comment, "rating": r.rating, "user_id": r.user_id} for r in reviews if r]
        }

    def get_all_places(self):
        return [self.get_place(p.id) for p in self.place_repo.get_all()]

    def update_place(self, place_id, data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for field in ["title", "description", "price", "latitude", "longitude"]:
            if field in data:
                setattr(place, field, data[field])
        if "amenities" in data:
            new_amenities = []
            for aid in data["amenities"]:
                amenity = self.amenity_repo.get(aid)
                if not amenity:
                    raise ValueError(f"Amenity ID {aid} not found")
                new_amenities.append(aid)
            place.amenities = new_amenities
        return self.get_place(place_id)

    # =================== REVIEWS ===================
    def create_review(self, review_data):
        user = self.user_repo.get(review_data.get("user_id"))
        if not user:
            raise ValueError("User not found")
        place = self.place_repo.get(review_data.get("place_id"))
        if not place:
            raise ValueError("Place not found")
        rating = review_data.get("rating")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be integer 1-5")
        text = review_data.get("text") or review_data.get("comment")
        review_data["comment"] = text
        review = Review(**review_data)
        self.review_repo.add(review)
        place.add_review(review.id)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def update_review(self, review_id, data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        review.updateReview(data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        return [self.review_repo.get(rid) for rid in place.reviews if self.review_repo.get(rid)]
