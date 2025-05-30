from flask import Flask, send_from_directory
from flask_cors import CORS
from controllers.auth import auth_bp
from controllers.listings import listings_bp
from controllers.requests import requests_bp

app = Flask(__name__, static_folder='../frontend/pages', static_url_path='')
CORS(app)

# Register route blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(listings_bp, url_prefix='/listings')
app.register_blueprint(requests_bp, url_prefix='/requests')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
