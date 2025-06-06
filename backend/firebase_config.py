import pyrebase

config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "databaseURL": "https://YOUR_PROJECT.firebaseio.com",
    "projectId": "YOUR_PROJECT",
    "storageBucket": "YOUR_PROJECT.appspot.com",
    "messagingSenderId": "YOUR_MSG_SENDER_ID",
    "appId": "YOUR_APP_ID",
    "serviceAccount": "firebase_credentials.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
