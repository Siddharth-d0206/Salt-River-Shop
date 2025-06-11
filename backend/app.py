from flask import Flask
from firebase_admin import credentials, initialize_app

from .config import Config
from .models import db
from .routes import bp

cred = credentials.Certificate('firebase_credentials.json')
initialize_app(cred)


def create_app():
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
