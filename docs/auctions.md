# Auctions

## Example Value (Full Size)

```
{
  "ItemLevelMin": 0,
  "ItemLevelMax": 0,
  "ItemGradeQuality": null,
  "ItemUpgradeLevel": null,
  "ItemTradeAllowCount": null,
  "SkillOptions": [
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    },
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    },
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
    },
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    },
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    },
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    },
    {
      "FirstOption": null,
      "SecondOption": null,
      "MinValue": null,
      "MaxValue": null
    }
  ],
  "Sort": "BIDSTART_PRICE",
  "CategoryCode": 0,
  "CharacterClass": null,
  "ItemTier": null,
  "ItemGrade": null,
  "ItemName": null,
  "PageNo": 0,
  "SortCondition": "ASC"
}
```

## Parameters

### ItemLevelMin

-   integer($int32)
-   범위: 0 ~ 1800

---

### ItemLevelMax

-   integer($int32)
-   범위: 0 ~ 1800

---

### ItemGradeQuality

-   integer($int32)
    | 값 | 설명 |
    |-------|------------|
    | NULL | 전체 품질 |
    | 10 | 10 이상 |
    | 20 | 20 이상 |
    | 30 | 30 이상 |
    | 40 | 40 이상 |
    | 50 | 50 이상 |
    | 60 | 60 이상 |
    | 70 | 70 이상 |
    | 80 | 80 이상 |
    | 90 | 90 이상 |

---

### ItemUpgradeLevel

-   integer($int32)
    | 값 | 설명 |
    |------|------------|
    | NULL | 전체 |
    | 0 | 연마 전 |
    | 1 | 1단계 |
    | 2 | 2단계 |
    | 3 | 3단계 |

---

### ItemTradeAllowCount

-   integer($int32)
    | 값 | 설명 |
    |------|------------------------|
    | NULL | 전체 |
    | 0 | 구매 시 거래 불가 |
    | 1 | 구매 시 거래 1회 가능 |
    | 2 | 구매 시 거래 2회 가능 |

---

### SkillOptions

#### FirstOption

-   integer($int32)

#### SecondOption

-   integer($int32)

#### MinValue

-   integer($int32)

#### MaxValue

-   integer($int32)

---

### EtcOptions

#### FirstOption

-   integer($int32)
    | 값 | 설명 |
    |------|--------------------|
    | NULL | 전체 |
    | 2 | 전투 특성 |
    | 3 | 각인 효과 |
    | 6 | 감소 효과 |
    | 1 | 팔찌 기본 효과 |
    | 5 | 팔찌 특수 효과 |
    | 4 | 팔찌 옵션 수량 |
    | 7 | 연마 효과 |
    | 8 | 아크 패시브 |

#### SecondOption

-   integer($int32)

##### 전투 특성

| 값   | 설명   |
| ---- | ------ |
| NULL | 미선택 |
| 15   | 치명   |
| 16   | 특화   |
| 17   | 제압   |
| 18   | 신속   |
| 19   | 인내   |
| 20   | 숙련   |

##### 각인 효과

| 값  | 설명              | 값  | 설명              | 값  | 설명          | 값  | 설명           |
| --- | ----------------- | --- | ----------------- | --- | ------------- | --- | -------------- |
| 255 | 각성              | 286 | 갈증              | 243 | 강령술        | 129 | 강화 무기      |
| 242 | 강화 방패         | 288 | 결투의 대가       | 225 | 고독한 기사   | 800 | 공격력 감소    |
| 802 | 공격속도 감소     | 125 | 광기              | 188 | 광전사의 비기 | 134 | 구슬동자       |
| 123 | 굳은 의지         | 314 | 권왕파천무        | 312 | 그믐의 경계   | 190 | 극의: 체술     |
| 142 | 급소 타격         | 249 | 기습의 대가       | 302 | 긴급구조      | 199 | 넘치는 교감    |
| 287 | 달의 소리         | 238 | 달인의 저력       | 254 | 돌격대장      | 258 | 두 번째 동료   |
| 168 | 마나 효율 증가    | 251 | 마나의 흐름       | 306 | 만개          | 311 | 만월의 집행자  |
| 281 | 멈출 수 없는 충동 | 253 | 바리케이드        | 801 | 방어력 감소   | 279 | 버스트         |
| 246 | 번개의 분노       | 245 | 부러진 뼈         | 196 | 분노의 망치   | 236 | 분쇄의 주먹    |
| 235 | 불굴              | 290 | 사냥의 시간       | 198 | 상급 소환사   | 244 | 선수필승       |
| 256 | 세맥타통          | 300 | 속전속결          | 315 | 수라의 길     | 121 | 슈퍼 차지      |
| 248 | 승부사            | 298 | 시선 집중         | 237 | 실드관통      | 282 | 심판자         |
| 299 | 아드레날린        | 284 | 아르데타인의 기술 | 111 | 안정된 상태   | 107 | 약자 무시      |
| 110 | 에테르 포식자     | 239 | 여신의 가호       | 257 | 역천지체      | 141 | 예리한 둔기    |
| 127 | 오의 강화         | 292 | 오의난무          | 280 | 완벽한 억제   | 118 | 원한           |
| 140 | 위기 모면         | 803 | 이동속도 감소     | 308 | 이슬비        | 291 | 일격필살       |
| 278 | 잔재된 기운       | 247 | 저주받은 인형     | 301 | 전문의        | 224 | 전투 태세      |
| 194 | 절실한 구원       | 276 | 절정              | 277 | 절제          | 293 | 점화           |
| 109 | 정기 흡수         | 303 | 정밀 단도         | 259 | 죽음의 습격   | 240 | 중갑 착용      |
| 197 | 중력 수련         | 195 | 진실된 용맹       | 285 | 진화의 유산   | 295 | 질량 증가      |
| 307 | 질풍노도          | 310 | 처단자            | 189 | 초심          | 167 | 최대 마나 증가 |
| 296 | 추진력            | 283 | 축복의 오라       | 191 | 충격 단련     | 297 | 타격의 대가    |
| 202 | 탈출의 명수       | 193 | 포격 강화         | 309 | 포식자        | 241 | 폭발물 전문가  |
| 289 | 피스메이커        | 192 | 핸드거너          | 130 | 화력 강화     | 294 | 환류           |
| 201 | 황제의 칙령       | 200 | 황후의 은총       | 305 | 회귀          |     |                |

##### 감소 효과

| 값  | 설명          |
| --- | ------------- |
| 800 | 공격력 감소   |
| 802 | 공격속도 감소 |
| 801 | 방어력 감소   |
| 803 | 이동속도 감소 |

##### 팔찌 기본 효과

| 값  | 설명 |
| --- | ---- |
| 3   | 힘   |
| 4   | 민첩 |
| 5   | 지능 |
| 6   | 체력 |

##### 팔찌 특수 효과

| 값  | 설명                                  |
| --- | ------------------------------------- |
| 39  | 강타                                  |
| 60  | 공격 및 이동 속도 증가                |
| 33  | 긴급 수혈                             |
| 38  | 돌진                                  |
| 36  | 마나회수                              |
| 2   | 마법 방어력                           |
| 29  | 멸시                                  |
| 30  | 무시                                  |
| 1   | 물리 방어력                           |
| 28  | 반격                                  |
| 31  | 반전                                  |
| 26  | 속공                                  |
| 62  | 시드 이하 받는 피해 감소              |
| 61  | 시드 이하 주는 피해 증가              |
| 35  | 앵콜                                  |
| 37  | 오뚝이                                |
| 34  | 응급 처치                             |
| 63  | 이동기 및 기상기 재사용 대기시간 감소 |
| 59  | 전투 자원 회복량                      |
| 6   | 전투 중 생명력 회복량                 |
| 4   | 최대 마나                             |
| 3   | 최대 생명력                           |
| 40  | 타격                                  |
| 27  | 투자                                  |
| 64  | 피격 이상 면역 효과                   |
| 32  | 회생                                  |

##### 팔찌 옵션 수량

| 값  | 설명           |
| --- | -------------- |
| 1   | 고정 효과 수량 |
| 2   | 부여 효과 수량 |

##### 연마 효과

아래는 제공하신 JSON 데이터를 마크다운 형식으로 깔끔하게 정리한 예입니다:

### 연마 효과

-   **Value**: 7
-   **Text**: 연마 효과
-   **Tiers**: [4]

#### 상세 효과 항목

| Value | Text                                    | Categories | Tiers | EtcValues                         |
| ----- | --------------------------------------- | ---------- | ----- | --------------------------------- |
| 45    | 공격력 %                                | [200020]   |       | 0.40%, 0.95%, 1.55% (Percentage)  |
| 53    | 공격력 +                                |            |       | 80, 195, 390 (Non-Percentage)     |
| 44    | 낙인력                                  | [200010]   |       | 2.15%, 4.80%, 8.00% (Percentage)  |
| 46    | 무기 공격력 %                           | [200020]   |       | 0.80%, 1.80%, 3.00% (Percentage)  |
| 54    | 무기 공격력 +                           |            |       | 195, 480, 960 (Non-Percentage)    |
| 57    | 상태이상 공격 지속시간                  |            |       | 0.20%, 0.50%, 1.00% (Percentage)  |
| 43    | 세레나데, 신성, 조화 게이지 획득량 증가 | [200010]   |       | 1.60%, 3.60%, 6.00% (Percentage)  |
| 51    | 아군 공격력 강화 효과                   | [200030]   |       | 1.35%, 3.00%, 5.00% (Percentage)  |
| 52    | 아군 피해량 강화 효과                   | [200030]   |       | 2.00%, 4.50%, 7.50% (Percentage)  |
| 42    | 적에게 주는 피해 증가                   | [200010]   |       | 0.55%, 1.20%, 2.00% (Percentage)  |
| 58    | 전투 중 생명력 회복량                   |            |       | 10, 25, 50 (Non-Percentage)       |
| 56    | 최대 마나                               |            |       | 6, 15, 30 (Non-Percentage)        |
| 55    | 최대 생명력                             |            |       | 1300, 3250, 6500 (Non-Percentage) |
| 41    | 추가 피해                               | [200010]   |       | 0.70%, 1.60%, 2.60% (Percentage)  |
| 49    | 치명타 적중률                           | [200030]   |       | 0.40%, 0.95%, 1.55% (Percentage)  |
| 50    | 치명타 피해                             | [200030]   |       | 1.10%, 2.40%, 4.00% (Percentage)  |
| 48    | 파티원 보호막 효과                      | [200020]   |       | 0.95%, 2.10%, 3.50% (Percentage)  |
| 47    | 파티원 회복 효과                        | [200020]   |       | 0.95%, 2.10%, 3.50% (Percentage)  |

EtcValues 열의 value는 순서대로 1, 2, 3

##### 아크패시브

| 값  | 설명   |
| --- | ------ |
| 1   | 깨달음 |
| 2   | 도약   |

#### MinValue

-   integer($int32)

#### MaxValue

-   integer($int32)

---

### Sort

-   string
    | 값 | 설명 |
    |-----------------|--------------|
    | ITEM_GRADE | 등급 |
    | ITEM_LEVEL | 아이템레벨 |
    | ITEM_QUALITY | 품질 |
    | EXPIREDATE | 남은 시간 |
    | BIDSTART_PRICE | 최소 입찰가 |
    | BUY_PRICE | 즉시 구매가 |

---

### CategoryCode

-   integer($int32)
    | 값 | 설명 | 값 | 설명 | 값 | 설명 |  
    |----------|--------------|-----------|------------|----------|------------|  
    | 10000 | 장비 | 190010 | 투구 | 200010 | 목걸이 |  
    | 30000 | 어빌리티 스톤 | 190020 | 상의 | 200020 | 귀걸이 |  
    | 200000 | 장신구 | 190030 | 하의 | 200030 | 반지 |  
    | 210000 | 보석 | 190040 | 장갑 | 200040 | 팔찌 |  
    | 180000 | 무기 | 190050 | 어깨 | | |  
    | 170300 | 아뮬렛 | | | | |

---

### CharacterClass

-   string
    | 값 | 직업 |
    |--------|--------------|
    | NULL | 전체 |
    | 102 | 버서커 |
    | 103 | 디스트로이어 |
    | 104 | 워로드 |
    | 105 | 홀리나이트 |
    | 112 | 슬레이어 |
    | 202 | 아르카나 |
    | 203 | 서머너 |
    | 204 | 바드 |
    | 205 | 소서리스 |
    | 302 | 배틀마스터 |
    | 303 | 인파이터 |
    | 304 | 기공사 |
    | 305 | 창술사 |
    | 312 | 스트라이커 |
    | 313 | 브레이커 |
    | 402 | 블레이드 |
    | 403 | 데모닉 |
    | 404 | 리퍼 |
    | 405 | 소울이터 |
    | 502 | 호크아이 |
    | 503 | 데빌헌터 |
    | 504 | 블래스터 |
    | 505 | 스카우터 |
    | 512 | 건슬링어 |
    | 602 | 도화가 |
    | 603 | 기상술사 |

---

### ItemTier

-   integer($int32)
    | 값 | 설명 |
    |------|--------|
    | 2 | 티어2 |
    | 3 | 티어3 |
    | 4 | 티어4 |

---

### ItemGrade

-   string
    | 값 | 설명 |
    |-------|--------|
    | NULL | 전체 |
    | 0 | 일반 |
    | 1 | 고급 |
    | 2 | 희귀 |
    | 3 | 영웅 |
    | 4 | 전설 |
    | 5 | 유물 |
    | 6 | 고대 |
    | 7 | 에스더 |

---

### ItemName

-   string

---

### PageNo

-   integer($int32)

---

### SortCondition

-   string
    | 값 | 설명 |
    |------|----------|
    | ARC | 오름차순 |
    | DISC | 내림차순 |

---

## params (참고용)

### firstCategory: 대분류

-   0: 전체
-   10000: 장비
-   30000: 어빌리티 스톤
-   200000: 장신구
-   210000: 보석

---

### secondCategory: 소분류

-   0: 전체

#### 장비

-   180000: 무기
-   190010: 투구
-   190020: 상의
-   190030: 하의
-   190040: 장갑
-   190050: 어깨
-   170300: 아뮬렛

#### 장신구

-   200010: 목걸이
-   200020: 귀걸이
-   200030: 반지
-   200040: 팔찌

---

### classNo: 클래스

-   NULL: 전체
-   102: 버서커
-   103: 디트
-   104: 워황
-   105: 홀나
-   112: 슬레
-   202: 알카
-   203: 서머너
-   204: 바드
-   205: 소서
-   302: 배마
-   303: 인파
-   304: 기공사
-   305: 창술사
-   312: 스커
-   313: 브커
-   402: 블레이드
-   403: 데모닉
-   404: 리퍼
-   405: 소울이터
-   502: 호크아이
-   503: 데헌
-   504: 블래스터
-   505: 스카우터
-   512: 건슬링어
-   602: 도화가
-   603: 기상술사

---

### itemTier: 아이템 티어

-   2: 티어2
-   3: 티어3
-   4: 티어4

---

### itemGrade: 아이템 등급

-   NULL: 전체
-   0: 일반
-   1: 고급
-   2: 희귀
-   3: 영웅
-   4: 전설
-   5: 유물
-   6: 고대
-   7: 에스더

---

### itemLevelMin: 아이템 최소 레벨

-   int

---

### itemLevelMax: 아이템 최대 레벨

-   int

---

### itemName: 아이템 명

-   string

---

### pageNo: 페이지 번호

-   int

---

### sortOption[Sort]: 정렬 기준

-   ITEM_GRADE: 등급
-   ITEM_LEVEL: 아이템레벨
-   ITEM_QUALITY: 품질
-   EXPIREDATE: 남은 시간
-   BIDSTART_PRICE: 최소 입찰가
-   BUY_PRICE: 즉시 구매가

---

### sortOption[IsDesc]: 정렬 순서

-   false: 오름차순
-   true: 내림차순

---

### gradeQuality: 품질

-   NULL: 전체 품질
-   10: 10 이상
-   20: 20 이상
-   30: 30 이상
-   40: 40 이상
-   50: 50 이상
-   60: 60 이상
-   70: 70 이상
-   80: 80 이상
-   90: 90 이상

---

### upgradeLevel: 연마 단계

-   NULL: 전체
-   0: 연마 전
-   1: 1단계
-   2: 2단계
-   3: 3단계

---

### tradeAllowCount: 거래 가능 횟수

-   NULL: 전체
-   0: 구매 시 거래 불가
-   1: 구매 시 거래 1회 가능
-   2: 구매 시 거래 2회 가능

---

### skillOptionList[0][firstOption]: 스킬 상세 옵션-스킬 선택 첫 번째

-   로아 코덱스 참고

### skillOptionList[0][secondOption]: 스킬 상세 옵션-옵션 선택(트포) 첫 번째

```
1 2 3
4 5 6
 7 8
```

### skillOptionList[0][minValue]: 스킬 상세 옵션-수치설정-최소값 첫 번째

### skillOptionList[0][maxValue]: 스킬 상세 옵션-수치설정-최대값 첫 번째

### skillOptionList[1][firstOption]:

### skillOptionList[1][secondOption]:

### skillOptionList[1][minValue]:

### skillOptionList[1][maxValue]:

### skillOptionList[2][firstOption]:

### skillOptionList[2][secondOption]:

### skillOptionList[2][minValue]:

### skillOptionList[2][maxValue]:

---

### etcOptionList[0][firstOption]: 기타 상세 옵션-기타선택 첫 번째

-   NULL: 전체
-   2: 전투 특성
-   3: 각인 효과
-   6: 감소 효과
-   1: 팔찌 기본 효과
-   5: 팔찌 특수 효과
-   4: 팔찌 옵션 수량
-   7: 연마효과
-   8: 아크패시브

### etcOptionList[0][secondOption]: 기타 상세 옵션-옵션 선택 첫 번째

-   NULL: 미선택
-   15: 치명
-   16: 특화
-   17: 제압
-   18: 신속
-   19: 인내
-   20: 숙련

---

-   255: 각성
-   286: 갈증
-   243: 강령술
-   129: 강화 무기
-   242: 강화 방패
-   288: 결투의 대가
-   225: 고독한 기사
-   800: 공격력 감소
-   802: 공격속도 감소
-   125: 광기
-   188: 광전사의 비기
-   134: 구슬동자
-   123: 굳은 의지
-   314: 권왕파천무
-   312: 그믐의 경계
-   190: 극의: 체술
-   142: 급소 타격
-   249: 기습의 대가
-   302: 긴급구조
-   199: 넘치는 교감
-   287: 달의 소리
-   238: 달인의 저력
-   254: 돌격대장
-   258: 두 번째 동료
-   168: 마나 효율 증가
-   251: 마나의 흐름
-   306: 만개
-   311: 만월의 집행자
-   281: 멈출 수 없는 충동
-   253: 바리케이드
-   801: 방어력 감소
-   279: 버스트
-   246: 번개의 분노
-   245: 부러진 뼈
-   196: 분노의 망치
-   236: 분쇄의 주먹
-   235: 불굴
-   290: 사냥의 시간
-   198: 상급 소환사
-   244: 선수필승
-   256: 세맥타통
-   300: 속전속결
-   315: 수라의 길
-   121: 슈퍼 차지
-   248: 승부사
-   298: 시선 집중
-   237: 실드관통
-   282: 심판자
-   299: 아드레날린
-   284: 아르데타인의 기술
-   111: 안정된 상태
-   107: 약자 무시
-   110: 에테르 포식자
-   239: 여신의 가호
-   257: 역천지체
-   141: 예리한 둔기
-   127: 오의 강화
-   292: 오의난무
-   280: 완벽한 억제
-   118: 원한
-   140: 위기 모면
-   803: 이동속도 감소
-   308: 이슬비
-   291: 일격필살
-   278: 잔재된 기운
-   247: 저주받은 인형
-   301: 전문의
-   224: 전투 태세
-   194: 절실한 구원
-   276: 절정
-   277: 절제
-   293: 점화
-   109: 정기 흡수
-   303: 정밀 단도
-   259: 죽음의 습격
-   240: 중갑 착용
-   197: 중력 수련
-   195: 진실된 용맹
-   285: 진화의 유산
-   295: 질량 증가
-   307: 질풍노도
-   310: 처단자
-   189: 초심
-   167: 최대 마나 증가
-   296: 추진력
-   283: 축복의 오라
-   191: 충격 단련
-   297: 타격의 대가
-   202: 탈출의 명수
-   193: 포격 강화
-   309: 포식자
-   241: 폭발물 전문가
-   289: 피스메이커
-   192: 핸드거너
-   130: 화력 강화
-   294: 환류
-   201: 황제의 칙령
-   200: 황후의 은총
-   305: 회귀

---

-   800: 공격력 감소
-   802: 공격속도 감소
-   801: 방어력 감소
-   803: 이동속도 감소

---

-   3: 힘
-   4: 민첩
-   5: 지능
-   6: 체력

---

-   39: 강타
-   60: 공격 및 이동 속도 증가
-   33: 긴급 수혈
-   38: 돌진
-   36: 마나회수
-   2: 마법 방어력
-   29: 멸시
-   30: 무시
-   1: 물리 방어력
-   28: 반격
-   31: 반전
-   26: 속공
-   62: 시드 이하 받는 피해 감소
-   61: 시드 이하 주는 피해 증가
-   35: 앵콜
-   37: 오뚝이
-   34: 응급 처치
-   63: 이동기 및 기상기 재사용 대기시간 감소
-   59: 전투 자원 회복량
-   6: 전투 중 생명력 회복량
-   4: 최대 마나
-   3: 최대 생명력
-   40: 타격
-   27: 투자
-   64: 피격 이상 면역 효과
-   32: 회생

---

-   1: 고정 효과 수량
-   2: 부여 효과 수량

---

-   45: 공격력 %
-   53: 공격력 +
-   44: 낙인력
-   46: 무기 공격력 %
-   54: 무기 공격력 +
-   57: 상태이상 공격 지속시간
-   43: 세레나데, 신성, 조화 게이지 획득량 증가
-   51: 아군 공격력 강화 효과
-   52: 아군 피해량 강화 효과
-   42: 적에게 주는 피해 증가
-   58: 전투 중 생명력 회복량
-   56: 최대 마나
-   55: 최대 생명력
-   41: 추가 피해
-   49: 치명타 적중률
-   50: 치명타 피해
-   48: 파티원 보호막 효과
-   47: 파티원 회복 효과

---

-   1: 깨달음
-   2: 도약

### etcOptionList[0][minValue]: 기타 상세 옵션-수치 최소값 첫 번째

### etcOptionList[0][maxValue]: 기타 상세 옵션-수치 최대값 첫 번째

### etcOptionList[1][firstOption]:

### etcOptionList[1][secondOption]:

### etcOptionList[1][minValue]:

### etcOptionList[1][maxValue]:

### etcOptionList[2][firstOption]:

### etcOptionList[2][secondOption]:

### etcOptionList[2][minValue]:

### etcOptionList[2][maxValue]:

### etcOptionList[3][firstOption]:

### etcOptionList[3][secondOption]:

### etcOptionList[3][minValue]:

### etcOptionList[3][maxValue]:

### etcOptionList[4][firstOption]:

### etcOptionList[4][secondOption]:

### etcOptionList[4][minValue]:

### etcOptionList[4][maxValue]:

## /auctions/options
