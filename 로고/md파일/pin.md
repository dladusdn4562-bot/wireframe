# [Pipeline 1] 핀터레스트 레퍼런스 수집 가이드 (pin.md)

---

## 1. 개요 및 실행 트리거 (Trigger Protocol)
사용자가 **"1번 실행해"**, **"2번 3개 찾아줘"**, **"실행 시작"** 과 같이 명령하면, 지정된 초안 번호의 이미지를 분석하여 Pinterest에서 스마트 웰니스 브랜드 **'스밈(SEUMIM)'**의 컨셉과 조형미에 부합하는 최적의 로고 레퍼런스를 수집하고 `output/similar_logo_{번호}.jpg`로 저장합니다.

### 초안 번호 매핑 및 조형 모티프
* `1번` ➔ `input/로고 초안1.jpeg` *(5개 전도성 섬유 노드의 방사형 회전 순환 모티프)*
* `2번` ➔ `input/로고 초안2.jpg` *(기하학적 4방향 신체 균형 및 교차 개화 잎사귀 모티프)*
* `3번` ➔ `input/로고 초안3.jpg` *(원형 노드와 대각선 관통 축 기반의 8자 무한대 척추 정렬 모티프)*
* `4번` ➔ `input/로고 초안4.jpg` *(원형 그리드 속 자연스러운 척추 S-커브 및 호흡의 스밈 모티프)*
* `5번` ➔ `input/로고 초안5.jpg` *(교차 원형 기하학 기반의 상승 아치 날개 및 자세 개방 모티프)*

---

## 2. 브랜드 정체성 및 디자인 조건 ('스밈 SEUMIM')
* **브랜드 네임**: **스밈 (SEUMIM)**
* **브랜드 의미**: '스며들다(permeate, seep into)'에서 유래. 강제 압박식 교정이 아닌, 독자적인 전도성 센서 섬유 기술과 인체공학적 설계를 통해 바른 자세와 건강한 습관이 일상 속에 자연스럽게 스며들어 몸과 마음의 균형을 완성하는 통합형 스마트 웰니스 플랫폼.
* **브랜드 슬로건**: "일상에 바른 균형이 스며들게, 당신의 일상 균형 '스밈(SEUMIM)'"
* **핵심 비주얼 키워드**:
  1. **스마트 직조 & 스밈 (Smart Weaving & Permeation)**: 유연한 센서 섬유의 부드러운 연결, 이음새 없는 흐름(Seamless flow)
  2. **척추/자세 정렬 (Spine & Posture Alignment)**: 신체 중심축, 자연스러운 S자 곡선, 코어 안정감
  3. **호흡과 순환 (Breathing Rhythm & Circulation)**: 연속 루프, 유기적 개화, 활력의 도약
* **색상 규격**: 단색 미니멀 (Monochrome Solid Black / Pure White)
* **형태 규격**: 2D 플랫 벡터 심볼 마크 (Flat Vector Symbol Mark)
* **배경 규격**: 순수 흰색 (#FFFFFF) 또는 순수 검정 (#000000)

---

## 3. Pinterest 최적화 검색 쿼리 매트릭스 (Search Matrix)
초안의 특징에 맞춰 아래 영문 쿼리를 조합하여 검색합니다:
* `"seumim smart fabric logo symbol minimalist black"`
* `"organic spine posture alignment logo mark minimal black white"`
* `"continuous woven line wellness logo symbol vector"`
* `"geometric figure 8 spine posture logo black flat"`
* `"radial swirl circle logo mark minimal black white"`
* `"minimalist s curve wave spine logo symbol flat vector"`
* `"uplifting curved wing crest logo minimal black white"`

---

## 4. 엄격한 금지 및 배제 조건 (Drop Rules)
아래 조건 중 **하나라도 해당되는 핀은 즉시 수집 대상에서 제외(Drop)**합니다.

1. **유채색 및 그라데이션 (Color Drop)**: 컬러, 무지개색, 그라데이션, 메탈릭 광택
2. **목업 및 3D 입체 효과 (Mockup & 3D Drop)**: 명함, 의류 합성, 간판, 종이 엠보싱, 3D 렌더링, 입체 그림자, 질감/노이즈
3. **텍스트 및 복잡한 세밀화 (Typography & Detail Drop)**: 브랜드 텍스트만 나열된 워드마크, 지나치게 복잡한 삽화 일러스트, 프레임/테두리 박스

---

## 5. 수집 및 저장 표준 프로세스
1. **지정 초안 로드**: 사용자가 지정한 초안(`input/로고 초안{번호}`)의 기하학적 형태, 대칭 축, 곡선 모티프 분석
2. **Pinterest 탐색 & Drop Rules 필터링**: 최적 쿼리 및 Visual Search를 통해 순수 단색 플랫 심볼 후보 선별
3. **고해상도 무손실 원본 다운로드**: CDN 원본 URL을 확보하여 `output/similar_logo_{번호}.jpg`로 자동 증분 저장
4. **저장 검증**: 다운로드된 이미지를 실제로 열어 잘림, 워터마크, UI 침범 여부 육안 검증 후 Phase 2로 연계
