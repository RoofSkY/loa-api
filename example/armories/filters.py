import requests
from urllib.parse import quote

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

# name과 filters 변수 설정
name = ""  # 여기에 캐릭터 이름을 입력하세요.
# 여기에 필터 조건을 입력하세요 (profiles, equipment, avatars, combat-skills, engravings, cards, gems, colosseums, collectibles, arkpassive / 다중선택: 필터1+필터2+...). 공백이면 필터 추가 안 함.
filters = ""

# API URL 및 헤더 설정
base_url = f"https://developer-lostark.game.onstove.com/armories/characters/{
    name}"
headers = {
    "accept": "application/json",
    "authorization": f"bearer {Token}"  # 여기에 실제 Token 값을 입력하세요.
}

if filters.strip():  # filters 값이 비어있지 않으면 쿼리 파라미터 추가
    base_url = f"{base_url}?filters={quote(filters)}"

# GET 요청 보내기
response = requests.get(base_url, headers=headers)

# 응답 확인 및 출력
if response.status_code == 200:
    print("응답 데이터:")
    print(response.json())
else:
    print(f"요청 실패: 상태 코드 {response.status_code}")
    print("응답 내용:", response.text)
