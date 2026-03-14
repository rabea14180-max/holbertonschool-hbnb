from flask_restx import Api
from .amenities import api as amenities_ns, amenity_bp

api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB Application API"
)

# Add namespaces so they appear in Swagger
api.add_namespace(amenities_ns)
