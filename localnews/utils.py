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

def send_fcm_v1_notification(tokens, title, body):
    if not tokens:
        return
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        tokens=tokens,
    )
    response = messaging.send_multicast(message)
    # Remove invalid tokens
    from .models import Device
    for idx, resp in enumerate(response.responses):
        if not resp.success:
            error = resp.exception
            if isinstance(error, messaging.UnregisteredError):
                Device.objects.filter(token=tokens[idx]).delete()
                print(f"Removed invalid FCM token: {tokens[idx]}")
    return response