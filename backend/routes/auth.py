from flask import request, jsonify
from firebase_admin import auth as firebase_auth

from . import bp
from ..models import db, User


@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'business')
    user_record = firebase_auth.create_user(email=email, password=password)
    user = User(id=user_record.uid, email=email, role=role)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Account created', 'uid': user_record.uid})


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    id_token = data.get('idToken')
    try:
        decoded = firebase_auth.verify_id_token(id_token)
        return jsonify({'message': 'Login verified', 'uid': decoded['uid']})
    except Exception:
        return jsonify({'error': 'Invalid token'}), 401
