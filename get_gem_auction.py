"""
{
    "ItemLevelMin": 0,
    "ItemLevelMax": 1800,
    "ItemGradeQuality": null,
    "ItemUpgradeLevel": null,
    "ItemTradeAllowCount": null,
    "SkillOptions": [
        {
            "FirstOption": null,
            "SecondOption": null,
            "MinValue": null,
            "MaxValue": null
        }
    ],
    "EtcOptions": [
        {
            "FirstOption": null,
            "SecondOption": null,
            "MinValue": null,
            "MaxValue": null
        }
    ],
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": null,
    "ItemTier": null,
    "ItemGrade": null,
    "ItemName": "10레벨 작열",
    "PageNo": 1,
    "SortCondition": "ASC"
}
"""

import requests
import json
import os

# .env 파일에서 토큰 로드
from dotenv import load_dotenv
load_dotenv()
Token = os.environ.get('token')

# API URL 및 헤더 설정
url = 'https://developer-lostark.game.onstove.com/auctions/items'
headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {Token}',
    'Content-Type': 'application/json'
}

# 요청에 필요한 JSON 데이터
payload = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 1800,
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
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": None,
    "ItemTier": None,
    "ItemGrade": None,
    "ItemName": "10레벨 작열",
    "PageNo": 1,
    "SortCondition": "ASC"
}

# API 요청
response = requests.post(url, headers=headers, json=payload)

# 응답 처리
if response.status_code == 200:
    try:
        # JSON 데이터 파싱
        response_data = response.json()

        # example 폴더에 gem_result.json 저장
        output_folder = "example"
        os.makedirs(output_folder, exist_ok=True)  # example 폴더가 없으면 생성
        output_file = os.path.join(output_folder, "gem_result.json")

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(response_data, file, indent=4, ensure_ascii=False)

        print(f"Data saved successfully to {output_file}")
    except json.JSONDecodeError:
        print("Error: Failed to parse response JSON.")
else:
    print(f"Error: Received status code {response.status_code}")
    print("Response Text:", response.text)
