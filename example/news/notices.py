import requests
from urllib.parse import urlencode

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

# 기본 URL
base_url = "https://developer-lostark.game.onstove.com/news/notices"

# type 변수 설정
# type에 원하는 값을 입력하세요 (예: "공지", "점검", "상점", "이벤트"). 빈 문자열이면 전체 검색.
type_value = ""

# URL 동적 생성
if type_value.strip():  # type 값이 비어있지 않으면 쿼리 파라미터 추가
    params = {"type": type_value}
    url = f"{base_url}?{urlencode(params)}"
else:
    url = base_url

# API 헤더 설정
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
