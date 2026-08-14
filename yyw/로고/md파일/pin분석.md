# [Pipeline 2] 레퍼런스 분석 및 Flow 프롬프트 작성 가이드 (pin분석.md)

---

## 1. 개요 및 실행 트리거 (Trigger Protocol)

### 1) 일반 실행 ("레퍼런스 분석 시작해" 또는 파이프라인 자동 연계)
* `output/` 폴더에 수집된 **최신 로고 레퍼런스 이미지(`.jpg`)를 정밀 분석**합니다.
* 스마트 체형 교정 웰니스 브랜드 **'스밈(SEUMIM)'**의 핵심 가치가 온전히 담긴 **Flow AI 이미지 생성 전용 완성형 영문 프롬프트**를 작성합니다.
* **상단 누적 기록 규칙 (Prepend to Top)**: 기존 `output/flow.md`의 이전 기록을 100% 보존하면서, 새 프롬프트를 **파일 맨 위(최상단)에 추가**하여 최신 결과가 항상 최상단에 위치하도록 저장합니다.

### 2) 재실행 ("재실행")
* `output/` 내의 모든 레퍼런스 이미지를 처음부터 다시 분석하여 `output/flow.md`를 최신순으로 전면 재작성합니다.

---

## 2. '스밈(SEUMIM)' 레퍼런스 정밀 분석 4대 핵심 기준

`output/` 내의 레퍼런스 이미지를 분석할 때 다음 4가지 핵심 요소를 도출하여 프롬프트에 융합합니다.

1. **조형 구조 & 스마트 직조 (Form & Smart Weaving Structure)**
   - 기하학적 원형 가이드라인 기반의 대칭 구조(Radial / Bilateral / Rotational symmetry)
   - 전도성 센서 섬유가 엮인 듯한 유연하고 매끄러운 모노라인 및 면의 연결(Woven continuous ribbons / fluid contours)
   - 닫힌 답답함이 아닌 호흡이 통하는 내부 네거티브 스페이스(Open negative-space channels)

2. **시각적 모티프 (Visual Motif)**
   - **스밈과 순환 (Seeping & Circulation)**: 일상에 자연스럽게 스며드는 유기적 곡선(Organic seamless flow)
   - **척추/체형 정렬 (Spinal Posture Alignment)**: 곧게 뻗은 중심축, 바른 자세를 유도하는 부드러운 S-커브(S-curve spine curvature), 인체 코어 노드
   - **자세 개방 및 활력 (Chest Opening & Uplifting Vitality)**: 날개/새싹/꽃잎 형태의 상방 전개

3. **브랜드 컨셉 연계성 (SEUMIM Brand Context)**
   - 억지 강제 압박이 아닌 자연스럽게 스며드는 바른 자세
   - 전도성 센서 섬유 기술의 첨단성과 직장인의 일상에 녹아드는 따뜻하고 편안한 웰니스 무드
   - 몸과 마음의 완벽한 균형(Equilibrium between body and mind)

4. **스타일 규격 (Style & Contrast)**
   - 2D 플랫 벡터(Flat vector), 단색(Solid Monochrome Black / Pure White)
   - 화면 중앙 정면 배치(Front-facing isolated center), 넉넉하고 균일한 여백(Generous even whitespace)

---

## 3. '스밈(SEUMIM)' 전용 Flow 영문 프롬프트 작성 표준 템플릿

Flow 이미지 생성 엔진에서 최고 품질의 미니멀 스마트 웰니스 로고를 생성할 수 있도록 아래의 5단 레이어 표준 영문 구조를 준수합니다.

```text
Create an original minimalist geometric vector logo for 'SEUMIM', an integrated smart posture-care and wellness lifestyle brand. Design a centered {형태/대칭 구조} built from {세부 모듈 및 스마트 섬유/곡선 조형 특징}, evoking seamless permeation of healthy habits, spinal posture alignment, continuous breathing flow, and mindful equilibrium between body and mind. {세부 조형미, 네거티브 스페이스 및 선/면 연결 규칙}. Render the symbol in {단색 색상 및 배경 대비}, front-facing and isolated with generous even whitespace. Keep the composition completely flat, crisp, mathematically balanced, and highly scalable. No text, letters, numbers, border, frame, mockup, product scene, photography, 3D effects, gradients, drop shadows, textures, watermark, or signature.
```

---

## 4. 저장 위치 및 마크다운 작성 양식 (`output/flow.md`)

* **저장 파일 경로**: `output/flow.md`
* **마크다운 작성 형식 (최신순 상단 누적)**:
  - 파일 최상단에 **대제목(`# similar_logo_{번호}.jpg`)**과 완성형 영문 프롬프트를 추가

```markdown
# similar_logo_{번호}.jpg

Create an original minimalist geometric vector logo for 'SEUMIM' ... (완성형 영문 프롬프트)

(아래쪽에는 기존에 작성된 이전 프롬프트들이 그대로 유지됨)
```

---

## 5. 실행 체크리스트
- [ ] '스밈(SEUMIM)'의 브랜드 가치(스며드는 바른 자세, 스마트 섬유, 척추 정렬)가 프롬프트에 충실히 반영되었는가?
- [ ] 프롬프트가 100% 영문(English) 완성형 단일 문단으로 작성되었는가?
- [ ] 기존 `flow.md`의 이전 이력이 손실 없이 유지되었는가?
- [ ] 신규 프롬프트가 `flow.md` 최상단(Prepend)에 올바르게 배치되었는가?
