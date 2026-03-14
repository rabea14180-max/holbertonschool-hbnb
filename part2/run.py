# part2/run.py
def create_app():
    from flask import Flask
    from flask_restx import Api
    from app.api.user import UserList
    from app.api.amenity import AmenityList
    from app.api.place import PlaceList

    app = Flask(__name__)
    api = Api(app, prefix="/api/v1")
    
    api.add_resource(UserList, '/users/')
    api.add_resource(AmenityList, '/amenities/')
    api.add_resource(PlaceList, '/places/')

    return app
