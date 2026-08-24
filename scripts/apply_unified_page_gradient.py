# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

unified_page_gradient_css = """
    /* ==========================================================================
       [메인페이지 전체 단일 수직 융합 그라데이션 (Single Unified Canvas Gradient)]
       상단: 가장 밝고 맑은 밀크티 아이보리 (#FCFBF8)
       ➔ 아래로 스크롤할수록 끊김 없이 점진적으로 따뜻해지는 어반 웜 그레이지 (#D8CBB9)
       ========================================================================== */

    body {
      background-color: #FCFBF8 !important;
      color: var(--color-text-primary) !important;
    }

    #page-main {
      background: linear-gradient(
        180deg,
        #FCFBF8 0%,       /* [0% 최상단] 가장 밝고 맑은 클린 밀크티 아이보리 */
        #FAF7F2 10%,      /* [10% 히어로] 부드럽고 따뜻한 웜 아이보리 */
        #F6F0E6 25%,      /* [25% 지표/서사] 은은한 온기가 스며드는 소프트 샌드 */
        #EFE7DA 45%,      /* [45% 3대 대표작] 포근한 오트밀 린넨 */
        #E8DEC F 65%,      /* [65% 임상 증명/카탈로그] 차분하고 고급스러운 어반 웜 그레이지 */
        #DFD4C4 85%,      /* [85% HUD/센터] 깊고 따뜻한 웜 토프 */
        #D6C8B5 100%      /* [100% FAQ/하단] 가장 따뜻하고 안정감 있는 딥 웜 그레이지 */
      ) !important;
      background-size: 100% 100% !important;
      min-height: 100vh !important;
    }

    /* 모든 섹션의 개별 배경 제거 ➔ 메인페이지 단일 그라데이션이 자연스럽게 전체를 관통 */
    #page-main .hero-section,
    #page-main .journey-section,
    #page-main #sec-featured,
    #page-main .proof-section,
    #page-main .faq-container,
    #page-main section {
      background: transparent !important;
      background-color: transparent !important;
      background-image: none !important;
    }

    /* 상단 GNB: 최상단의 맑은 밀크티 아이보리와 자연스러운 일체감 */
    .header-gnb {
      background: rgba(252, 251, 248, 0.95) !important;
      backdrop-filter: blur(12px) !important;
      border-bottom: 1px solid rgba(226, 218, 208, 0.5) !important;
    }

    /* 콘텐츠 카드 서피스: 맑은 순백 바탕으로 그라데이션 위에서 부드러운 입체 부양 */
    .pride-metrics-bar {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E2D5 !important;
      box-shadow: 0 8px 24px rgba(90, 75, 60, 0.05) !important;
    }
    .journey-chapter,
    .featured-card,
    .proof-stat-card,
    .review-card,
    .explore-catalog-banner,
    .fit-finder-banner,
    .hud-card,
    .center-card,
    .faq-item {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(216, 204, 188, 0.75) !important;
      box-shadow: 0 6px 20px rgba(80, 65, 50, 0.04) !important;
    }
    .faq-item.open {
      background: #FAF8F5 !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 기존 개별 섹션 그라데이션 CSS를 단일 페이지 그라데이션 CSS로 교체
    if "/* ==========================================================================\n       [스밈 시그니처 융합 그라데이션:" in content:
        content = re.sub(
            r'/\* ==========================================================================\s*\[스밈 시그니처 융합 그라데이션:.*?</style>',
            unified_page_gradient_css + "\n  </style>",
            content,
            flags=re.DOTALL
        )
    elif "/* ==========================================================================\n       [메인페이지 전체 단일 수직 융합 그라데이션" not in content:
        content = content.replace("</style>", unified_page_gradient_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied unified single-canvas vertical gradient to {path}")
