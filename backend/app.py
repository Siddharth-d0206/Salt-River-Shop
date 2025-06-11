from flask import Flask, send_from_directory
import firebase_admin
from firebase_admin import credentials, initialize_app
import os

from .config import Config
from .models import db
from .routes import bp

cred = credentials.Certificate('firebase_credentials.json')
if not firebase_admin._apps:
    initialize_app(cred)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/api')

    @app.route('/')
    def index():
        return send_from_directory('../frontend', 'index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    port = int(os.getenv("PORT", 5001))
    app.run(debug=True, port=port)
