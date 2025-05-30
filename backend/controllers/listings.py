from flask import Blueprint, request, jsonify
from firebase_config import db, storage

listings_bp = Blueprint('listings', __name__)

@listings_bp.route('', methods=['POST'])
def create_listing():
    title = request.form.get('title')
    description = request.form.get('description')
    user_id = request.form.get('user_id')
    file = request.files.get('image')

    if not file:
        return jsonify({"error": "Image required"}), 400

    filename = file.filename
    path = f"images/{user_id}/{filename}"
    storage.child(path).put(file)
    image_url = storage.child(path).get_url(None)

    db.child("listings").push({
        "title": title,
        "description": description,
        "image_url": image_url,
        "posted_by": user_id
    })
    return jsonify({"message": "Listing created", "image_url": image_url}), 200

@listings_bp.route('', methods=['GET'])
def get_listings():
    listings = db.child("listings").get().val()
    return jsonify(listings), 200
