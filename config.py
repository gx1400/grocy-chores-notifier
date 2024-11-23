import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access environment variables
GROCY_BASEURL = os.getenv("GROCY_BASEURL")
GROCY_APIKEY = os.getenv("GROCY_APIKEY")
PUSHOVER_USERKEY = os.getenv("PUSHOVER_USERKEY")
PUSHOVER_APPKEY = os.getenv("PUSHOVER_APPKEY")
