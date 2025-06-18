import firebase_admin
from firebase_admin import credentials, messaging
import os
import json

# Only initialize once
if not firebase_admin._apps:
    firebase_json = os.environ.get('FIREBASE_SERVICE_ACCOUNT_JSON')
    if firebase_json:
        cred = credentials.Certificate(json.loads(firebase_json))
    else:
        cred = credentials.Certificate(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'village-app-97c3a-firebase-adminsdk-fbsvc-deba4452d4.json')
        )
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