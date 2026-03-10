from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token

api = Namespace('users', description='User operations')

login_model = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return {"access_token": access_token}, 200
