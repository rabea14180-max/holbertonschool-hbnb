from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

facade = HBnBFacade()

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})


@api.route('/')
class AmenityList(Resource):

    def get(self):
        """List all amenities"""
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200

    @api.expect(amenity_model)
    def post(self):
        """Create a new amenity"""
        data = api.payload

        amenity = facade.create_amenity(data)

        return amenity.to_dict(), 201


@api.route('/<amenity_id>')
class AmenityResource(Resource):

    def get(self, amenity_id):
        """Get amenity by ID"""
        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {"error": "Amenity not found"}, 404

        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    def put(self, amenity_id):
        """Update an amenity"""

        data = api.payload

        amenity = facade.update_amenity(amenity_id, data)

        if not amenity:
            return {"error": "Amenity not found"}, 404

        return amenity.to_dict(), 200
