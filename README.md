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
2. Place your Firebase service account credentials in `firebase_credentials.json`.
3. Start the development server:
   ```bash
   python -m backend.app
   ```
