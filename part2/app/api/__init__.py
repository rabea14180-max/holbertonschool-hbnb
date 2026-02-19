#part2/app/api/__init__.py
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns

def create_api(app):
    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Evolution REST API',
              doc='/api/v1/docs')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    return api
