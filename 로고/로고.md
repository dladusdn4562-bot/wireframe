# 스마트 웰니스 브랜드 '스밈(SEUMIM)' 로고 레퍼런스 수집 및 Flow 프롬프트 생성 가이드

---

## 0. 브랜드 핵심 개요 및 컨셉 ('스밈 SEUMIM')

* **브랜드 네임**: **스밈 (SEUMIM)**
* **브랜드 정의**: 독자적인 고정밀 전도성 센서 섬유 기술을 기반으로, 일상 속 체형 교정 하드웨어와 AI 맞춤형 코칭 서비스를 연계한 통합형 스마트 웰니스 체형 교정 플랫폼
* **브랜드 의미**: '스며들다(permeate, seep into)'에서 비롯된 이름. 억지로 몸을 조이는 강제 압박 교정이 아닌, 바른 자세와 건강한 습관이 일상 속에 자연스럽게 스며들어 몸과 마음의 균형을 완성하는 가치 지향.
* **브랜드 슬로건**: "일상에 바른 균형이 스며들게, 당신의 일상 균형 '스밈(SEUMIM)'"
* **핵심 조형 키워드**: 스마트 전도성 섬유 직조(Smart Fabric Weaving), 척추/자세 정렬(Spine Posture Alignment), 일상 속 스며듦(Seamless Flow & Permeation), 미니멀 단색 2D 플랫 벡터(Monochrome Flat Vector).

---

## 1. 명령어 실행 트리거 규칙 (Trigger Protocol)

### 1) "실행 시작" 또는 "{번호}번 실행" (수량: N개 지정 가능)
1. **초안 분석**: `input/` 폴더 내의 초안 파일(1번~5번)의 조형적 특징, 형태 구조(곡선, 나선, 척추 축, 날개 아치)를 분석합니다.
2. **스타일 기준 매칭**: `레퍼런스/` 폴더 내의 기준 이미지 스타일(순수 배경, 단색 플랫 심볼, 미니멀)을 철저히 벤치마킹합니다.
3. **Pinterest 레퍼런스 탐색**: 스밈(SEUMIM) 전용 검색 쿼리 및 Visual Search를 활용하여 조건에 완벽히 부합하는 유사 로고를 탐색합니다.
4. **고화질 저장**: 찾은 최적의 레퍼런스 이미지를 `output/` 폴더에 `.jpg` 형식(예: `output/similar_logo_{번호}.jpg`)으로 N개 저장합니다.
5. **최신순 상단 누적 Flow 프롬프트 생성**: **기존 `output/flow.md`의 내용을 온전히 보존**하면서, 방금 수집된 최신 로고의 프롬프트를 **파일 맨 위(최상단)에 추가(Prepend)**하여 저장합니다.

### 2) "재실행"
* `output/` 내 모든 레퍼런스 이미지를 처음부터 다시 분석하여 `output/flow.md`를 최신순으로 전면 재작성합니다.

---

## 2. 엄격한 금지 및 배제 조건 (Drop Rules)
아래 조건 중 **하나라도 해당되는 핀은 즉시 수집 대상에서 제외**합니다.

1. **색상이 들어간 로고**: 다채로운 색상, 그라데이션, 유채색 라인/면, 메탈릭 효과
2. **목업(Mockup) 및 3D 렌더링**: 명함, 티셔츠, 쇼핑백, 간판, 종이 엠보싱, 3D 입체, 텍스처, 그림자
3. **기타 제외 대상**: 복잡한 세밀화 일러스트, 폰트만 나열된 순수 텍스트 워드마크

---

## 3. Flow 영문 프롬프트 표준 템플릿
```text
Create an original minimalist geometric vector logo for 'SEUMIM', an integrated smart posture-care and wellness lifestyle brand. Design a centered {형태/대칭 구조} built from {세부 모듈 및 스마트 섬유/곡선 조형 특징}, evoking seamless permeation of healthy habits, spinal posture alignment, continuous breathing flow, and mindful equilibrium between body and mind. {세부 조형미, 네거티브 스페이스 및 선/면 연결 규칙}. Render the symbol in {단색 색상 및 배경 대비}, front-facing and isolated with generous even whitespace. Keep the composition completely flat, crisp, mathematically balanced, and highly scalable. No text, letters, numbers, border, frame, mockup, product scene, photography, 3D effects, gradients, drop shadows, textures, watermark, or signature.
```
