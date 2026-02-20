#part2/app/api/v1/ places.py
from flask_restx import Namespace, Resource, fields
from app.services import facade

facade = HBnBFacade()
api = Namespace('places', description='Place operations')

# Models
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String,
    'name': fields.String
})
user_model = api.model('PlaceUser', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})
review_model = api.model('PlaceReview', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,
    'user_id': fields.String
})
place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'owner': fields.Nested(user_model),
    'amenities': fields.List(fields.Nested(amenity_model)),
    'reviews': fields.List(fields.Nested(review_model))
})

# Routes
@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    def post(self):
        data = api.payload
        try:
            place = facade.create_place(data)
            return {"id": place.id, "title": place.title, "description": place.description,
                    "price": place.price, "latitude": place.latitude,
                    "longitude": place.longitude, "owner_id": place.owner_id}, 201
        except Exception as e:
            return {"error": str(e)}, 400

    def get(self):
        return facade.get_all_places(), 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place, 200

    @api.expect(place_model)
    def put(self, place_id):
        data = api.payload
        try:
            updated = facade.update_place(place_id, data)
        except Exception as e:
            return {"error": str(e)}, 400
        if not updated:
            return {"error": "Place not found"}, 404
        return {"message": "Place updated successfully"}, 200

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            return {"error": "Place not found"}, 404
        return [{"id": r.id, "text": r.text, "rating": r.rating, "user_id": r.user_id} for r in reviews], 200
