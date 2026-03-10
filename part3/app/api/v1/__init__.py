from flask_restx import Api
from .users import api as users_ns
from .amenities import api as amenities_ns

api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB Application API"
)

# Add namespaces so they appear in Swagger
api.add_namespace(users_ns)
api.add_namespace(amenities_ns)
