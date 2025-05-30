from flask import Blueprint, request, jsonify
from firebase_config import auth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return jsonify({"message": "Account created", "uid": user['localId']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
