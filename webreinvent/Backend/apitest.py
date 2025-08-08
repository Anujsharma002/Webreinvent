import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPER_API_KEY")
response = requests.post(
    "https://google.serper.dev/search",
    headers={
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    },
    json={"q": "webreinvent agency ranking"}
)

print(response.status_code)
print(response.text)
