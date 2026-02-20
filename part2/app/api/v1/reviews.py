#part2/app/api/v1/reviews.py
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')
facade = HBnBFacade()

review_model = api.model('Review', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True),
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    def post(self):
        try:
            review = facade.create_review(api.payload)
            return {
                "id": review.id,
                "text": review.comment,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id
            }, 201
        except Exception as e:
            return {"error": str(e)}, 400

    def get(self):
        return [
            {
                "id": r.id,
                "text": r.comment,
                "rating": r.rating,
                "user_id": r.user_id,
                "place_id": r.place_id
            } for r in facade.get_all_reviews()
        ], 200

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.comment,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }, 200

    @api.expect(review_model)
    def put(self, review_id):
        review = facade.update_review(review_id, api.payload)
        if not review:
            return {"error": "Review not found"}, 404
        return {"message": "Review updated successfully"}, 200

    def delete(self, review_id):
        deleted = facade.delete_review(review_id)
        if not deleted:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted successfully"}, 200
