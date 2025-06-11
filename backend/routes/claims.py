from flask import request, jsonify

from . import bp
from ..models import db, Claim


@bp.route('/claims', methods=['POST'])
def create_claim():
    data = request.get_json()
    claim = Claim(
        listing_id=data.get('listing_id'),
        nonprofit_id=data.get('nonprofit_id')
    )
    db.session.add(claim)
    db.session.commit()
    return jsonify({'id': claim.id})


@bp.route('/claims', methods=['GET'])
def get_claims():
    claims = Claim.query.all()
    return jsonify([
        {
            'id': c.id,
            'listing_id': c.listing_id,
            'nonprofit_id': c.nonprofit_id,
            'status': c.status
        } for c in claims
    ])
