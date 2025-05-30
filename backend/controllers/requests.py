from flask import Blueprint, request, jsonify
from firebase_config import db

requests_bp = Blueprint('requests', __name__)

@requests_bp.route('', methods=['POST'])
def create_request():
    data = request.get_json()
    try:
        db.child("requests").push(data)
        return jsonify({"message": "Request submitted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
