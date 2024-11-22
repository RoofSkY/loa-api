import requests
import json

# from lostark_api_token import Token

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

item_code = 6861012

# API URL
url = f'https://developer-lostark.game.onstove.com/markets/items/{item_code}'

# 헤더 설정
headers = {
    'accept': 'application/json',
    'authorization': f"Bearer {Token}"
}

# API 요청
response = requests.get(url, headers=headers)

# 상태 코드 확인
if response.status_code == 200:
    try:
        json_data = response.json()  # JSON 응답 파싱

        # JSON 데이터를 보기 좋게 출력
        formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
        print("Formatted JSON Data:\n")
        print(formatted_json)

    except requests.exceptions.JSONDecodeError:
        print("Error: Failed to parse JSON response.")
else:
    print(f"Error: Unexpected status code {response.status_code}")
    print("Response Text:", response.text)
