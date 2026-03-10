from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Namespace('users', description='User operations')

login_model = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String,
    'last_name': fields.String
})


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate and receive a JWT token"""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(
            identity=user.id,
            additional_claims={"is_admin": user.is_admin}
        )
        return {"access_token": access_token}, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.expect(user_update_model)
    def put(self, user_id):
        """Modify user details (self only, no email/password changes)"""
        current_user_id = get_jwt_identity()

        # Only allow users to modify their own data
        if current_user_id != user_id:
            return {"error": "Unauthorized action"}, 403

        data = request.get_json()
        if not data:
            return {"error": "No data provided"}, 400

        # Prevent email or password modification
        if 'email' in data or 'password' in data:
            return {"error": "You cannot modify email or password"}, 400

        user = User.query.filter_by(id=user_id).first()
        if not user:
            return {"error": "User not found"}, 404

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        db.session.commit()
        return user.to_dict(), 200
