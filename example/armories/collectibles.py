import requests
from urllib.parse import quote

from dotenv import load_dotenv
import os
load_dotenv()
Token = os.environ.get('token')

# name 변수 설정
name = ""  # 여기에 캐릭터 이름을 입력하세요.

# API URL과 헤더 설정
base_url = f"https://developer-lostark.game.onstove.com/armories/characters/{
    name}/collectibles"
headers = {
    "accept": "application/json",
    "authorization": f"bearer {Token}"  # .env에 실제 API 키를 입력하세요.
}

# GET 요청 보내기
response = requests.get(base_url, headers=headers)

# 응답 확인 및 출력
if response.status_code == 200:
    print("응답 데이터:")
    print(response.json())
else:
    print(f"요청 실패: 상태 코드 {response.status_code}")
    print("응답 내용:", response.text)
