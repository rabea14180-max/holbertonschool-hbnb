# app/api/v1/amenities.py
from flask import Blueprint, request, jsonify
from app.services import HBnBFacade

amenity_bp = Blueprint("amenities", __name__)
facade = HBnBFacade()

@amenity_bp.route("/amenities", methods=["GET"])
def get_amenities():
    amenities = facade.list_amenities()
    return jsonify([a.to_dict() for a in amenities]), 200

@amenity_bp.route("/amenities/<amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    amenity = facade.get_amenity(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route("/amenities", methods=["POST"])
def create_amenity():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    try:
        amenity = facade.create_amenity(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(amenity.to_dict()), 201

@amenity_bp.route("/amenities/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    amenity = facade.update_amenity(amenity_id, data)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200
