import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def verify_api_key(api_key, permission):
    """
    Verify the API key using the Unkey API.
    :param api_key: The API key to verify.
    :param permission: The permission to verify.
    :return: The response from the Unkey API.
    """
    url = "https://api.unkey.dev/v1/keys.verifyKey"

    payload = {
        "apiId": os.getenv("UNKEY_API_ID"),
        "key": api_key,
        "authorization": {
            "permissions": permission
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request(
        "POST", url, json=payload, headers=headers).json()
    print(response)
    if response['valid']:
        return True
    else:
        return False
