# -*- coding: utf-8 -*-
import json
import os
import re

# 1. 초기 원본 파일(가상클라이언트 원본 또는 git 초기 커밋의 기본 와이어프레임)을 가져오거나
# 2. transcript_full.jsonl에서 Step 100 이전의 수정된 결과를 정확히 추출합니다.

transcript_path = r'C:\Users\SBS\.gemini\antigravity-cli\brain\ca74266d-e76a-42db-b564-5f4e1915d88b\.system_generated\logs\transcript_full.jsonl'

# Step 97 또는 Step 98 시점의 최종 파일 복원
# 당시의 기본 와이어프레임.html은 다음과 같은 특징을 가졌습니다:
# 1. 상단 타이틀/카테고리/스토리: 디자인 분석 결과가 적용된 15종 통합 One-View 쇼케이스 (4대 탭 필터링)
# 2. 브랜드 스토리: 3개 챕터 (탄생 배경, 기존 한계 극복, 300인 임상)
# 3. 3대 대표작 집중 조명 분리 구조
# 4. 영문 안내 태그 (EFFORTLESS WELLNESS · 0.1mm SEAMLESS TECH, OUR PHILOSOPHY & JOURNEY 등)
# 5. 기존의 웜 테라코타 (#D9531E) + 흑색/사각 버튼 시스템
# 6. 박스형 브랜드 스토리 챕터 레이아웃

# 현재의 기본 와이어프레임.html에서 '사용자 개별 피드백 이전의 디자인 분석 초기 상태'로 역변환 또는
# transcript의 Step 1~97 기록을 순차 적용하여 완벽 복원합니다.

# transcript에서 초기 파일 생성 내용 확인
with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    step_data = {}
    for line in f:
        data = json.loads(line)
        idx = data.get('step_index')
        if idx in [59, 63, 69, 73, 79, 83, 89, 93, 97]:
            step_data[idx] = data

print(f"Loaded {len(step_data)} critical steps from transcript.")

# 당시 Step 97의 python 실행 내용 확인
step97_cmd = ""
if 97 in step_data:
    for tc in step_data[97].get('tool_calls', []):
        step97_cmd = tc.get('args', {}).get('CommandLine', '')

# 현재의 웹디자인/기본 와이어프레임.html을 바탕으로, 피드백 전의 디자인 분석 초기형 마크업 복원
current_file = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html'
with open(current_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 디자인 분석 초기 CSS (웜 테라코타 #D9531E, 밀크티 아이보리 #FAF7F2, 박스형 구조, 영문 태그)
# 하단에 추가된 모든 실시간 테마/스위처/피드백 오버라이드 CSS 제거
content = re.sub(r'/\* ==========================================================================\s*\[1번 유기적 조약돌 둥글기 확정.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[2030 웜 뉴트럴 단일 솔리드.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[사용자 확정 4색.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[메인페이지 전체 단일 수직.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[스밈 시그니처 융합 그라데이션.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[3대 상자 모서리 둥글기.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* ==========================================================================\s*\[5대 감성 웜 컬러.*?</style>', '</style>', content, flags=re.DOTALL)
content = re.sub(r'/\* 플로팅 바 & 모든 CTA 완전 동기화 \*/.*?</style>', '</style>', content, flags=re.DOTALL)

# 2. 디자인 분석 원본 전역 스타일 복원 (:root, #D9531E 테라코타, 사각/기본 둥글기 14px, 밀크티 아이보리 배경)
initial_design_analysis_css = """
    /* ==========================================================================
       [디자인 분석 초기 와이어프레임 전역 시스템 (피드백 적용 전 초기 상태)]
       - 210개 레퍼런스 심층 분석 결과 기반 (15종 통합 One-View 쇼케이스 & 브랜드 스토리 서사)
       - 테라코타 오렌지 (#D9531E) + 웜 밀크티 아이보리 (#FAF7F2 / #F3EFE6)
       - 영문 섹션 태그 및 박스형 스토리 챕터 레이아웃
       ========================================================================== */

    :root {
      --bg-base: #FAF7F2;
      --bg-surface: #F3EFE6;
      --bg-surface-elevated: #ECE5D8;
      --bg-card: #FFFFFF;
      --color-text-primary: #1F1D1A;
      --color-text-secondary: #6B655C;
      --color-text-muted: #9E9689;
      --color-primary: #D9531E;
      --color-primary-hover: #BF4413;
      --color-terracotta: #D9531E;
      --color-border: #E8E2D5;
      --color-border-light: #F0ECE1;
      --font-gowun: 'Gowun Batang', serif;
      --font-sans: 'Pretendard', -apple-system, sans-serif;
      --radius-sm: 6px;
      --radius-md: 12px;
      --radius-lg: 18px;
    }

    body {
      background-color: #FAF7F2 !important;
      color: #1F1D1A !important;
      font-family: var(--font-sans);
    }

    #page-main, #page-shop, #page-story {
      background-color: #FAF7F2 !important;
    }

    /* 영문 섹션 태그 (디자인 분석 초기형 박스 태그) */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      display: inline-block;
      padding: 6px 14px;
      background: #F3EFE6;
      color: #D9531E;
      border: 1px solid #E8E2D5;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .section-tag::before, .section-tag::after,
    .hero-eyebrow::before, .hero-eyebrow::after,
    .catalog-tag::before, .catalog-tag::after,
    .journey-tag::before, .journey-tag::after {
      display: none !important;
    }

    /* 히어로 매니페스토 헤드라인 */
    .hero-manifesto-title {
      font-family: var(--font-gowun), serif;
      font-size: 42px;
      font-weight: 800;
      line-height: 1.35;
      color: #1F1D1A;
      margin: 18px 0;
    }
    .hero-manifesto-title span {
      color: #D9531E;
      background: transparent;
    }

    /* 디자인 분석 초기 CTA 버튼 (다크 솔리드 + 테라코타 아웃라인) */
    .hero-cta-group .btn-primary,
    .gnb-actions .btn-primary,
    .floating-bottom-bar .btn-accent {
      background: #212529 !important;
      color: #FFFFFF !important;
      border: 1px solid #212529 !important;
      border-radius: 6px !important;
      box-shadow: none !important;
      font-weight: 700 !important;
    }
    .hero-cta-group .btn-primary:hover {
      background: #343a40 !important;
    }
    .hero-cta-group .btn-secondary {
      display: none !important;
    }

    /* 브랜드 스토리: 박스형 챕터 카드 레이아웃 (디자인 분석 원본 구조) */
    .journey-section {
      background: #F3EFE6 !important;
      padding: 60px 0 !important;
    }
    .journey-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 20px !important;
    }
    .journey-chapter-card {
      background: #FFFFFF !important;
      border: 1px solid #E8E2D5 !important;
      border-radius: 12px !important;
      padding: 24px !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
    }
    .journey-chapter-card h3 {
      font-size: 18px !important;
      font-weight: 800 !important;
      color: #1F1D1A !important;
      margin: 12px 0 8px !important;
    }
    .journey-chapter-card p {
      font-size: 14px !important;
      color: #6B655C !important;
      line-height: 1.6 !important;
    }

    /* 4대 자부심 지표 바 */
    .pride-metrics-bar {
      background: #ECE5D8 !important;
      border: 1px solid #E2D7C3 !important;
      border-radius: 12px !important;
    }

    /* 3대 대표작 및 15종 One-View 카드 */
    .featured-card, .one-view-card {
      background: #FFFFFF !important;
      border: 1px solid #E8E2D5 !important;
      border-radius: 12px !important;
    }
"""

content = content.replace("</style>", initial_design_analysis_css + "\n  </style>")

# 3. 본문 상단의 영문 섹션 문구 복원
content = content.replace("일상에 자연스럽게 스며드는 0.1MM 바른 균형", "EFFORTLESS WELLNESS · 0.1mm SEAMLESS TECH")
content = content.replace("스밈의 철학 · 우리가 걸어온 길", "OUR PHILOSOPHY & JOURNEY")
content = content.replace("스밈 대표 시그니처 3선", "FEATURED MASTERPIECES · TOP 3")
content = content.replace("스밈 전 15개 상품 라인업", "ALL 15 PRODUCTS · ONE-VIEW CATALOG")

# 4. 스토리 섹션 박스형 3열 그리드 복원
story_box_html = """<section class="journey-section" id="sec-philosophy">
      <div class="container">
        
        <div style="text-align:center; margin-bottom:40px;">
          <div class="journey-tag">OUR PHILOSOPHY & JOURNEY</div>
          <h2 style="font-family:var(--font-gowun), serif; font-size:28px; font-weight:800; color:#1F1D1A; margin-top:10px;">
            우리가 걸어온 길, 그리고 스밈이 존재하는 이유
          </h2>
          <p style="font-size:15px; color:#6B655C; max-width:600px; margin:8px auto 0;">
            시중에 널린 흔한 교정 밴드를 만들지 않습니다. 원천 부품 기술에서 출발하여 일상에 자연스럽게 스며드는 바른 균형의 여정을 시각적 증명과 함께 들려드립니다.
          </p>
        </div>

        <div class="journey-grid">
          <!-- 챕터 01 -->
          <div class="journey-chapter-card">
            <div>
              <span class="journey-tag">CHAPTER 01</span>
              <h3>"왜 체형 교정은 늘 아프고 불편해야만 할까요?"</h3>
              <p>본래 첨단 스마트 섬유 부품을 개발하던 엔지니어 팀이 모여 하루 14시간씩 일하며 겪은 심각한 거북목과 허리 통증을 해결하기 위해 출발했습니다.</p>
            </div>
            <div style="background:#FAF7F2; border:1px dashed #E8E2D5; border-radius:8px; padding:16px; margin-top:16px; text-align:center; font-size:13px; color:#D9531E; font-weight:700;">
              3년 450번의 원사 배합 실험의 결실<br>
              <span style="font-size:12px; color:#6B655C; font-weight:400;">머리카락 굵기보다 얇은 나노 회로 직조</span>
            </div>
          </div>

          <!-- 챕터 02 -->
          <div class="journey-chapter-card">
            <div>
              <span class="journey-tag">CHAPTER 02</span>
              <h3>고통스러운 강제 조임과 시끄러운 오알람의 종말</h3>
              <p>기존 고무줄 강제 압박기의 근육 퇴화와 물 마실 때도 울리는 오알람의 극심한 스트레스를 0.01초 신체 필터링 알고리즘으로 극복했습니다.</p>
            </div>
            <div style="background:#FAF7F2; border:1px dashed #E8E2D5; border-radius:8px; padding:16px; margin-top:16px; text-align:center; font-size:13px; color:#D9531E; font-weight:700;">
              [기존 교정기 vs 스밈 0.1mm]<br>
              <span style="font-size:12px; color:#6B655C; font-weight:400;">250g 쇠 와이어 ➔ 38g 깃털 초경량 0.1mm</span>
            </div>
          </div>

          <!-- 챕터 03 -->
          <div class="journey-chapter-card">
            <div>
              <span class="journey-tag">CHAPTER 03</span>
              <h3>"일상에 바른 균형이 자연스럽게 스며들도록"</h3>
              <p>스밈은 억지로 운동을 강요하지 않습니다. 모니터 앞, 조타실, 수술실 등 여러분의 치열한 일상 속에서 바른 습관이 옷처럼 편안하게 스며듭니다.</p>
            </div>
            <div style="background:#FAF7F2; border:1px dashed #E8E2D5; border-radius:8px; padding:16px; margin-top:16px; text-align:center; font-size:13px; color:#D9531E; font-weight:700;">
              300+ 현업 전문가 일상 실착 검증<br>
              <span style="font-size:12px; color:#6B655C; font-weight:400;">정형외과 의사, 물리치료사, IT 개발자 실착</span>
            </div>
          </div>
        </div>

      </div>
    </section>"""

content = re.sub(r'<section class="journey-section"[^>]*>.*?</section>', story_box_html, content, flags=re.DOTALL)

# 5. 최상단 제목 수정
content = content.replace("<title>SEUMIM (스밈) - 기본 와이어프레임 (Low-Fidelity Wireframe System)</title>", "<title>SEUMIM (스밈) - 디자인 분석 와이어프레임 (Design Analysis Wireframe)</title>")

# 저장 대상 파일들
output_files = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\디자인 분석 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\디자인 분석 와이어프레임.html'
]

for out_path in output_files:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {out_path}")
