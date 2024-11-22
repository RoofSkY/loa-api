import requests
import json
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()
Token = os.environ.get('token')

# API URL 및 헤더 설정
base_url = 'https://developer-lostark.game.onstove.com/markets/items/'
headers = {
    'accept': 'application/json',
    'authorization': f"Bearer {Token}"
}

# data.json 파일 읽기
with open("data.json", "r", encoding="utf-8") as data_file:
    items = json.load(data_file)

# 결과 저장 리스트
results = []

# 각 아이템 코드에 대해 API 호출
for item in items:
    item_code = item["code"]
    item_name = item["name"]
    url = f'{base_url}{item_code}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            json_data = response.json()  # JSON 응답 파싱
            results.append({
                "item_name": item_name,
                "item_code": item_code,
                "data": json_data
            })  # 결과 저장
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Failed to parse JSON for item_code {item_code}.")
    else:
        print(f"Error: Unexpected status code {
              response.status_code} for item_code {item_code}.")
        print("Response Text:", response.text)

# 결과를 보기 좋게 출력
formatted_json = json.dumps(results, indent=4, ensure_ascii=False)

# 결과 파일을 example 폴더 안에 저장
output_folder = "example"
os.makedirs(output_folder, exist_ok=True)  # example 폴더가 없으면 생성
output_file = os.path.join(output_folder, "market_results.json")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(formatted_json)

print(f"JSON data has been saved to {output_file}")
