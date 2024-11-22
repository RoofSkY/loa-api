import requests
import json
# from lostark_api_token import Token

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

headers = {
    'accept': 'application/json',
    'authorization': Token
}

url = 'https://developer-lostark.game.onstove.com/example/api'
response = requests.get(url, headers=headers)

print(response)  # response 200
