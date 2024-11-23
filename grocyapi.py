import requests
from datetime import datetime, timedelta
import sys
from pushover import send_pushover_notification
from config import GROCY_BASEURL, GROCY_APIKEY

def validate_grocy_env_vars():
    """Validate required environment variables for Grocy API."""
    if not GROCY_BASEURL or not GROCY_APIKEY:
        print("Error: GROCY_BASEURL and GROCY_APIKEY must be provided in the .env file.")
        sys.exit(1)

def verify_grocy_api():
    """Verify the Grocy API by checking the /api/objects/products endpoint."""
    validate_grocy_env_vars()
    
    headers = {
        "GROCY-API-KEY": GROCY_APIKEY,
        "Accept": "application/json"
    }
    try:
        # Make the GET request
        response = requests.get(f"{GROCY_BASEURL}/api/objects/products", headers=headers)

        if response.status_code == 200:
            print("Grocy API is accessible and processing requests.")
            return True
        else:
            print(f"Grocy API returned an unexpected status code: {response.status_code}")
            send_pushover_notification(
                title="Grocery Chore Notifier",
                message=f"Grocy API request failed with status code {response.status_code}.",
                priority=1
            )
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to connect to the Grocy API: {e}")
        send_pushover_notification(
            title="Grocery Chore Notifier",
            message="Grocy API request failed due to a connection error.",
            priority=1
        )
        return False

def get_chores_due_next_7_days():
    """Fetch chores due in the next 7 days and send a Pushover notification."""
    validate_grocy_env_vars()
    
    headers = {
        "GROCY-API-KEY": GROCY_APIKEY,
        "Accept": "application/json"
    }

    try:
        # Make the GET request to fetch all chores
        response = requests.get(f"{GROCY_BASEURL}/api/chores", headers=headers)
        response.raise_for_status()

        chores = response.json()

        # Calculate the date range for the next 7 days
        today = datetime.now()
        next_7_days = today + timedelta(days=7)

        print("Chores Due in the Next 7 Days:")
        chores_due = []

        for chore in chores:
            # Parse due date
            due_date_str = chore.get("next_estimated_execution_time")
            if not due_date_str:
                continue

            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S")

            # Check if due date is within the next 7 days
            if today <= due_date <= next_7_days:
                chores_due.append({
                    "name": chore["chore_name"],
                    "due_date": due_date.strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"Chore Name: {chore['chore_name']}")
                print(f"Next Execution Due: {due_date.strftime('%Y-%m-%d %H:%M:%S')}")
                print("-" * 30)

        if not chores_due:
            # Send a priority 0 notification if no chores are due
            print("No chores due in the next 7 days.")
            send_pushover_notification(
                title="Grocery Chore Notifier",
                message="No chores due in the next 7 days.",
                priority=0
            )
        else:
            # Create a nicely formatted message
            message = "Chores Due in the Next 7 Days:\n\n"
            for chore in chores_due:
                message += f"- {chore['name']} (Due: {chore['due_date']})\n"

            # Send a priority 0 notification with the list of chores
            send_pushover_notification(
                title="Grocery Chore Notifier",
                message=message,
                priority=0
            )

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch chores: {e}")
        send_pushover_notification(
            title="Grocery Chore Notifier",
            message="Failed to fetch chores due in the next 7 days.",
            priority=1
        )
