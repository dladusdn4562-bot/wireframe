# [Pipeline 2] 레퍼런스 분석 및 Flow 프롬프트 작성 가이드 (pin분석.md)

---

## 1. 개요 및 실행 트리거 (Trigger Protocol)

### 1) 일반 실행 ("레퍼런스 분석 시작해" 또는 "Flow 프롬프트 작성해")
* `로고/output/` 폴더에 방금 수집된 **최신 로고 레퍼런스 이미지(`.jpg`)를 정밀 분석**합니다.
* AI 이미지 생성 툴(Flow 등)에서 고품질 로고 심볼을 생성할 수 있는 **완성형 영문 프롬프트**를 작성합니다.
* **상단 누적 기록 규칙 (Prepend to Top)**: 기존 `로고/output/flow.md`의 프롬프트 내용을 **모두 보존**한 상태에서, 새롭게 생성된 프롬프트를 **파일 맨 위(최상단)에 추가**하여 최신 프롬프트가 항상 위에 쌓이도록 저장합니다.

### 2) 재실행 ("재실행")
* 사용자가 **"재실행"** 명령을 입력하면 `로고/output/` 내의 모든 레퍼런스 이미지를 처음부터 다시 분석하여 `로고/output/flow.md`를 최신순으로 전면 재작성 및 갱신합니다.

---

## 2. 레퍼런스 분석 핵심 기준
`로고/output/` 내의 레퍼런스 이미지를 분석할 때 다음 4가지 핵심 요소를 도출합니다.

1. **조형 구조 (Form & Structure)**
   - 방사형 대칭(Radial symmetry), 단일 루프, 연속 곡선, 유기적 꽃잎/노드 등
   - 선의 굵기 변화(Stroke modulation), 내부 네거티브 스페이스(Negative space), 대칭/비대칭 균형
2. **시각적 모티프 (Visual Motif)**
   - 호흡 및 순환(Breathing rhythm, cyclical expansion)
   - 척추/자세 정렬 라인(Spinal posture alignment)
   - 유기적 식물/새싹/씨앗(Petals, sprout, leaf, seed)
3. **브랜드 컨셉 연계성 (Brand Context)**
   - 바쁜 일상 속 바른 자세와 건강한 습관
   - 몸과 마음의 균형(Balance of body and mind)
   - 친근하고 따뜻한 라이프 웰니스 무드
4. **스타일 규격 (Style & Contrast)**
   - 2D 플랫 벡터, 단색(Black/White), 단일 중심 배치, 넉넉한 여백

---

## 3. Flow 이미지 생성 영문 프롬프트 작성 표준

모든 생성 프롬프트는 Flow AI 엔진의 해석력을 극대화하기 위해 **영문(English)**으로 작성하며, 아래의 완성형 프롬프트 구조를 준수합니다.

```text
Create an original minimalist/geometric vector logo for a warm, approachable wellness brand. Design a centered {형태/대칭 구조} built from {세부 모듈 및 곡선 특징}, suggesting continuous breathing, healthy movement, connection, and balance between body and mind. {세부 조형미 및 선/면 규칙}. Render the symbol in {단색 색상 및 배경 대비}, front-facing and isolated with generous even whitespace. Keep the composition flat, crisp, scalable, and highly legible at small sizes. No text, letters, numbers, border, mockup, product scene, photography, 3D effects, gradients, shadows, textures, watermark, or signature.
```

---

## 4. 저장 위치 및 마크다운 작성 양식 (`로고/output/flow.md`)

* **저장 파일 경로**: `로고/output/flow.md`
* **마크다운 작성 형식 (최신순 상단 누적)**:
  - 파일 최상단에 **대제목(`# similar_logo_{번호}.jpg`)**과 영문 프롬프트를 추가

```markdown
# similar_logo_{번호}.jpg

Create an original ... (완성형 영문 프롬프트)

(아래쪽에는 기존에 작성된 이전 프롬프트들이 그대로 유지됨)
```

---

## 5. 실행 체크리스트
- [ ] 프롬프트가 100% 영문(English)으로 완성형으로 작성되었는가?
- [ ] 기존 `flow.md`에 있던 이전 프롬프트들이 삭제되지 않고 보존되었는가?
- [ ] 신규 프롬프트가 `flow.md`의 최상단(위쪽)에 올바르게 추가(Prepend)되었는가?
