from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # USER METHODS

    def create_user(self, user_data):

        users = self.user_repo.get_all()

        for user in users:
            if user.email == user_data["email"]:
                raise ValueError("Email already exists")

        user = User(**user_data)

        self.user_repo.add(user)

        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    # AMENITY METHODS

    def create_amenity(self, amenity_data):

        amenity = Amenity(**amenity_data)

        self.amenity_repo.add(amenity)

        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data):

        amenity = self.amenity_repo.get(amenity_id)

        if not amenity:
            return None

        amenity.update(data)

        return amenity
    # PLACE METHODS

    def create_place(self, place_data):

        place = Place(**place_data)

        self.place_repo.add(place)

        return place


    def get_place(self, place_id):

        return self.place_repo.get(place_id)


    def get_all_places(self):

        return self.place_repo.get_all()

    # REVIEW METHODS

    def create_review(self, review_data):

        review = Review(**review_data)

        self.review_repo.add(review)

        return review


    def get_review(self, review_id):

        return self.review_repo.get(review_id)


    def get_all_reviews(self):

        return self.review_repo.get_all()
