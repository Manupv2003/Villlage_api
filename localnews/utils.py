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
    # Remove empty or None tokens
    tokens = [t for t in tokens if t]
    if not tokens:
        return
    from .models import Device
    batch_size = 500
    for i in range(0, len(tokens), batch_size):
        batch = tokens[i:i+batch_size]
        if not batch:
            continue
        print("Sending notification to:", batch)
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            tokens=batch,
        )
        try:
            response = messaging.send_multicast(message)
            print(f"FCM response: {response}")
            # Remove invalid tokens
            for idx, resp in enumerate(response.responses):
                if not resp.success:
                    error = resp.exception
                    if isinstance(error, messaging.UnregisteredError):
                        Device.objects.filter(token=batch[idx]).delete()
                        print(f"Removed invalid FCM token: {batch[idx]}")
        except Exception as e:
            print(f"FCM send error: {e}")
    return