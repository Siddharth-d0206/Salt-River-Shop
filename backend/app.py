from flask import Flask
import firebase_admin
from firebase_admin import credentials

from .config import Config
from .models import db
from .routes import bp

cred = credentials.Certificate('firebase_credentials.json')


def _init_firebase():
    """Initialize Firebase only if it hasn't been initialized."""
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(cred)


def create_app():
    _init_firebase()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/api')

    @app.route('/')
    def index():
        return {'message': 'Salt River API'}

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
