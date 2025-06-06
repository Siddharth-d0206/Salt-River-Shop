"""Authentication endpoints."""

from flask import Blueprint, request, jsonify

from firebase_config import auth

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    """Create a new user account."""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return (
            jsonify({"message": "Account created", "uid": user["localId"]}),
            200,
        )
    except Exception as e:  # pragma: no cover - external service error text
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    """Sign in an existing user."""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return (
            jsonify(
                {
                    "message": "Login successful",
                    "idToken": user.get("idToken"),
                    "uid": user.get("localId"),
                }
            ),
            200,
        )
    except Exception as e:  # pragma: no cover - external service error text
        return jsonify({"error": str(e)}), 400
