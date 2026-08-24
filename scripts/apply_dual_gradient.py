# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

gradient_css = """
    /* ==========================================================================
       [스밈 시그니처 융합 그라데이션: 밀크티 아이보리 ➔ 어반 웜 그레이지]
       '일상에 부드럽게 스며드는' 브랜드 철학을 시각화한 수직 & 앰비언트 그라데이션
       - 상단: 맑고 따뜻한 밀크티 아이보리 (#FAF7F2 / #FCFAF7)
       - 중하단: 차분하고 고급스러운 어반 웜 그레이지 (#EFEAE2 / #E6DFD6)
       ========================================================================== */

    body {
      background: linear-gradient(180deg, #FAF7F2 0%, #F4EFE7 35%, #EBE4D8 70%, #E2DAD0 100%) !important;
      background-attachment: fixed !important;
      color: var(--color-text-primary) !important;
    }

    /* 1. 상단 GNB: 맑은 밀크티 아이보리 바탕 */
    .header-gnb {
      background: rgba(250, 247, 242, 0.95) !important;
      backdrop-filter: blur(10px) !important;
      border-bottom: 1px solid rgba(226, 218, 208, 0.8) !important;
    }

    /* 2. Hero & Manifesto: 상단 아이보리 ➔ 중앙 웜 그레이지 은은한 스밈 효과 */
    .hero-section {
      background: linear-gradient(180deg, #FAF7F2 0%, #F5EFE6 60%, #EDE6DC 100%) !important;
      position: relative !important;
      overflow: hidden !important;
    }
    .hero-section::before {
      content: '' !important;
      position: absolute !important;
      top: -20% !important;
      left: 50% !important;
      transform: translateX(-50%) !important;
      width: 1000px !important;
      height: 600px !important;
      background: radial-gradient(ellipse at center, rgba(255, 255, 255, 0.8) 0%, rgba(250, 247, 242, 0) 70%) !important;
      pointer-events: none !important;
      z-index: 0 !important;
    }
    .hero-section .container {
      position: relative !important;
      z-index: 1 !important;
    }

    /* 3. 4대 자부심 지표 바: 어반 웜 그레이지 베이스 & 소프트 섀도우 */
    .pride-metrics-bar {
      background: linear-gradient(135deg, #FFFFFF 0%, #F9F6F0 100%) !important;
      border: 1.5px solid #E2D7C5 !important;
      box-shadow: 0 10px 30px rgba(100, 85, 70, 0.06) !important;
    }

    /* 4. Journey & Story: 웜 그레이지 ➔ 밀크티 서사 그라데이션 */
    .journey-section {
      background: linear-gradient(180deg, #EDE6DC 0%, #F4EEE4 50%, #FAF7F2 100%) !important;
    }
    .journey-visual-card, .journey-chapter {
      background: #FFFFFF !important;
      border-color: #E2D7C5 !important;
    }

    /* 5. 3대 대표작 & 임상 증명: 입체적 웜 그레이지 존 */
    #sec-featured {
      background: transparent !important;
    }
    .featured-card {
      background: linear-gradient(145deg, #FFFFFF 0%, #FAF7F2 100%) !important;
      border: 1.5px solid #E2D8C8 !important;
      box-shadow: 0 8px 24px rgba(90, 75, 60, 0.05) !important;
    }

    .proof-section {
      background: linear-gradient(180deg, #FAF7F2 0%, #EDE6DB 60%, #E5DDD1 100%) !important;
    }
    .proof-stat-card, .review-card {
      background: #FFFFFF !important;
      border: 1.5px solid #E0D5C3 !important;
    }

    /* 6. 탐색 배너 & 사이즈 파인더 */
    .explore-catalog-banner, .fit-finder-banner {
      background: linear-gradient(135deg, #FFFFFF 0%, #F8F4EC 100%) !important;
      border: 1.5px solid #E0D5C3 !important;
      box-shadow: 0 8px 25px rgba(90, 75, 60, 0.05) !important;
    }

    /* 7. Shop All & Our Story 서브페이지 그라데이션 */
    #page-shop {
      background: transparent !important;
    }
    #page-story {
      background: transparent !important;
    }
    .one-view-card {
      background: #FFFFFF !important;
      border: 1.5px solid #E2D7C5 !important;
      box-shadow: 0 4px 16px rgba(90, 75, 60, 0.04) !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 임시 배경 툴바 및 본문 상단 임시 배너 정리
    content = re.sub(
        r'<!-- 5대 감성 메인 배경색 실시간 비교 선택 툴바 -->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- \[본문 상단: 6대 메인 전체 배경색 실시간 선택 배너\] -->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. padding-top 복원 (117px)
    content = re.sub(r'padding-top:\s*\d+px;', 'padding-top: 117px;', content, count=1)

    # 3. body 태그 기본형 복원
    content = re.sub(r'<body[^>]*>', '<body>', content, count=1)

    # 4. 그라데이션 CSS 주입
    if "/* ==========================================================================\n       [스밈 시그니처 융합 그라데이션:" not in content:
        content = content.replace("</style>", gradient_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied signature dual gradient to {path}")
