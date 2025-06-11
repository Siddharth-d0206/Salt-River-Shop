# Salt River

Salt River is a platform that helps businesses donate surplus goods to verified nonprofits. This repository contains a basic Flask backend as a starting point for the system described below.

## Features
* Business and nonprofit registration via Firebase Authentication
* Listing API for businesses to post available items
* Claim API for nonprofits to request items once verified
* Minimal SQLite database using SQLAlchemy

## Running Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download a Firebase service account key (JSON) and replace the contents of
   `firebase_credentials.json` with that JSON. You can simply copy and paste the
   entire config from the Firebase console into the file.
3. Start the development server:
   ```bash
   python -m backend.app
   ```
   The API will be available at `http://localhost:5001`.
