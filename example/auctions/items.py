import requests
import json

from dotenv import load_dotenv
import os
load_dotenv()  # load .env
Token = os.environ.get('token')

# API URL
url = "https://developer-lostark.game.onstove.com/auctions/items"

# 헤더 설정
headers = {
    "accept": "application/json",
    "authorization": f"bearer {Token}",  # .env에 실제 API 키를 입력하세요.
    "Content-Type": "application/json"
}

# 요청 데이터
payload = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 0,
    "ItemGradeQuality": None,
    "ItemUpgradeLevel": None,
    "ItemTradeAllowCount": None,
    "SkillOptions": [
        {
            "FirstOption": None,
            "SecondOption": None,
            "MinValue": None,
            "MaxValue": None
        }
    ],
    "EtcOptions": [
        {
            "FirstOption": None,
            "SecondOption": None,
            "MinValue": None,
            "MaxValue": None
        }
    ],
    "Sort": "BIDSTART_PRICE",
    "CategoryCode": 0,
    "CharacterClass": None,
    "ItemTier": 4,
    "ItemGrade": None,
    "ItemName": None,
    "PageNo": 0,
    "SortCondition": "ASC"
}

# POST 요청 보내기
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 응답 확인 및 출력
if response.status_code == 200:
    print("응답 데이터:")
    print(response.json())
else:
    print(f"요청 실패: 상태 코드 {response.status_code}")
