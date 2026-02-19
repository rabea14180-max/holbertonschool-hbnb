#part2/app/api/__init__.py
#!/usr/bin/python3
"""
API initialization module

Creates the main API object and registers namespaces.
"""

from flask_restx import Api
from app.api.v1.users import api as users_ns


def create_api(app):
    """
    Create and configure the API
    """

    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Evolution REST API",
        doc="/api/v1/docs"  # Swagger documentation endpoint
    )

    # Register namespaces
    api.add_namespace(users_ns, path="/api/v1/users")

    return api
