import requests
from config import PUSHOVER_USERKEY, PUSHOVER_APPKEY

pushover_url = "https://api.pushover.net/1/messages.json"

def send_pushover_notification(title, message, priority):
    """Send a notification via Pushover."""
    if not PUSHOVER_USERKEY or not PUSHOVER_APPKEY:
        print("Pushover keys are not provided. Skipping notification.")
        return

    payload = {
        "token": PUSHOVER_APPKEY,
        "user": PUSHOVER_USERKEY,
        "title": title,
        "message": message,
        "priority": priority,
    }
    try:
        response = requests.post(pushover_url, data=payload)
        response.raise_for_status()
        print("Pushover notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Pushover notification: {e}")
