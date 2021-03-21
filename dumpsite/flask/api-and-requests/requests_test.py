import os
import requests

from dotenv import load_dotenv
load_dotenv()

headers = {
    'user-agent': os.getenv('USER_AGENT'),
}

params = {
    'q' : 'hello'
}

URL = "https://www.google.com/search"

r = requests.get(URL, headers=headers, params=params)
print(r.status_code)
print(r.url)