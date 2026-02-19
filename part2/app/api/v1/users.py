#part2/app/api/v1/users.py
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('users', description='User operations')
facade = HBnBFacade()

# Input model (includes password)
user_input_model = api.model('UserInput', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'is_admin': fields.Boolean(required=False)
})

# Output model (NO password)
user_output_model = api.model('UserOutput', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'is_admin': fields.Boolean,
    'created_at': fields.String,
    'updated_at': fields.String
})


@api.route('/')
class UserList(Resource):

    @api.expect(user_input_model, validate=True)
    @api.marshal_with(user_output_model, code=201)
    def post(self):
        """Create a new user"""
        data = api.payload
        user = facade.create_user(data)
        return user.to_dict(), 201


    @api.marshal_list_with(user_output_model)
    def get(self):
        """Retrieve list of users"""
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200


@api.route('/<string:user_id>')
class UserResource(Resource):

    @api.marshal_with(user_output_model)
    def get(self, user_id):
        """Retrieve user by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200


    @api.expect(user_input_model, validate=False)
    @api.marshal_with(user_output_model)
    def put(self, user_id):
        """Update user information"""
        data = api.payload
        user = facade.update_user(user_id, data)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200
