# part2/app/api/v1/users.py
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

user_input_model = api.model('UserInput', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'is_admin': fields.Boolean
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'password': fields.String,
    'is_admin': fields.Boolean
})

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
        try:
            user = facade.create_user(api.payload)
            return user.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.marshal_list_with(user_output_model)
    def get(self):
        return [u.to_dict() for u in facade.get_all_users()], 200

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_output_model)
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200

    @api.expect(user_update_model, validate=True)
    @api.marshal_with(user_output_model)
    def put(self, user_id):
        try:
            user = facade.update_user(user_id, api.payload)
            if not user:
                api.abort(404, "User not found")
            return user.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))
