import firebase_admin
from firebase_admin import credentials, messaging
import os
import json

# Only initialize once
if not firebase_admin._apps:
    firebase_json = os.environ.get('FIREBASE_SERVICE_ACCOUNT_JSON')
    cred = credentials.Certificate(json.loads(firebase_json))
    firebase_admin.initialize_app(cred)

def send_fcm_v1_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message)
    return response