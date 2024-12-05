import requests

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

# API URL 및 헤더 설정
url = "https://developer-lostark.game.onstove.com/news/events"
headers = {
    "accept": "application/json",
    "authorization": f"bearer {Token}"  # .env에 실제 API 키를 입력하세요.
}

# GET 요청 보내기
response = requests.get(url, headers=headers)

# 응답 확인 및 출력
if response.status_code == 200:
    print("응답 데이터:")
    print(response.json())
else:
    print(f"요청 실패: 상태 코드 {response.status_code}")
    print("응답 내용:", response.text)
