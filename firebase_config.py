import firebase_admin
from firebase_admin import credentials, firestore

# Load the Firebase service account key
cred = credentials.Certificate("firebase_config.json")

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
