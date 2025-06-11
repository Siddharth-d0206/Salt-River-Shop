from flask import request, jsonify

from . import bp
from ..models import db, Listing


@bp.route('/listings', methods=['POST'])
def create_listing():
    data = request.get_json()
    listing = Listing(
        title=data.get('title'),
        description=data.get('description'),
        posted_by=data.get('user_id')
    )
    db.session.add(listing)
    db.session.commit()
    return jsonify({'id': listing.id})


@bp.route('/listings', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    return jsonify([
        {
            'id': l.id,
            'title': l.title,
            'description': l.description,
            'posted_by': l.posted_by
        } for l in listings
    ])
