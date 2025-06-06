# Salt River Shop

Starter code for a simple Flask + Firebase demo application. The project
includes a minimal backend API and static frontend pages.

## Requirements

- Python 3.8+
- Node.js optional (only plain JavaScript used)

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running

1. Place your Firebase credentials in `firebase_credentials.json` and update
   `backend/firebase_config.py` with your project settings.
2. Start the Flask development server:

```bash
python backend/app.py
```

The app serves the pages in `frontend/pages`. Visit `http://localhost:5000` to
see the landing page.
