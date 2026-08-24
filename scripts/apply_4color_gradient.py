# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

user_4color_gradient_css = """
    /* ==========================================================================
       [사용자 확정 4색 시그니처 단일 수직 그라데이션 배경]
       상단 ➔ 하단으로 물 흐르듯 이어지는 4대 감성 웜 팔레트:
       1. #FAF7F3 (최상단: 맑고 밝은 웜 린넨 아이보리)
       2. #F0E4D3 (상중단: 은은한 살구빛 웜 바닐라 베이지)
       3. #DCC5B2 (중하단: 포근한 어반 웜 클레이/오트밀 토프)
       4. #D9A299 (최하단: 깊고 따뜻한 소프트 더스티 로즈 블러쉬)
       ========================================================================== */

    body {
      background-color: #FAF7F3 !important;
      color: var(--color-text-primary) !important;
    }

    #page-main {
      background: linear-gradient(
        180deg,
        #FAF7F3 0%,       /* [0% 최상단 히어로] #FAF7F3 맑고 밝은 웜 아이보리 */
        #FAF7F3 12%,      /* [12% 히어로 콘텐츠 유지] */
        #F0E4D3 32%,      /* [32% 4대 지표 & 서사 챕터] #F0E4D3 은은한 웜 바닐라 베이지 */
        #E6D5C2 52%,      /* [52% 3대 대표작 시작] 부드러운 중간 전이 */
        #DCC5B2 72%,      /* [72% 3대 대표작 & 임상 증명] #DCC5B2 포근한 웜 클레이 토프 */
        #DBB2A5 88%,      /* [88% HUD / 센터] 더스티 블러쉬 전이 */
        #D9A299 100%      /* [100% 최하단 FAQ & 피니시] #D9A299 따뜻한 더스티 로즈 블러쉬 */
      ) !important;
      background-size: 100% 100% !important;
      min-height: 100vh !important;
    }

    /* 모든 섹션의 개별 배경 제거 ➔ 4색 그라데이션이 자연스럽게 전체를 관통 */
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

    /* 상단 GNB: 최상단의 맑은 #FAF7F3과 자연스러운 일체감 */
    .header-gnb {
      background: rgba(250, 247, 243, 0.96) !important;
      backdrop-filter: blur(12px) !important;
      border-bottom: 1px solid rgba(220, 197, 178, 0.55) !important;
    }

    /* 콘텐츠 카드 서피스: 맑은 순백 바탕으로 그라데이션 위에서 부드러운 입체 부양 */
    .pride-metrics-bar {
      background: #FFFFFF !important;
      border: 1.5px solid #E8DECF !important;
      box-shadow: 0 8px 24px rgba(120, 85, 70, 0.05) !important;
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
      border: 1.5px solid rgba(220, 197, 178, 0.75) !important;
      box-shadow: 0 6px 20px rgba(120, 85, 70, 0.04) !important;
    }
    .faq-item.open {
      background: #FCFAF7 !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 기존 단일 그라데이션 CSS를 사용자 4색 그라데이션 CSS로 교체
    if "/* ==========================================================================\n       [메인페이지 전체 단일 수직 융합 그라데이션" in content:
        content = re.sub(
            r'/\* ==========================================================================\s*\[메인페이지 전체 단일 수직 융합 그라데이션.*?</style>',
            user_4color_gradient_css + "\n  </style>",
            content,
            flags=re.DOTALL
        )
    elif "/* ==========================================================================\n       [사용자 확정 4색 시그니처 단일 수직 그라데이션" not in content:
        content = content.replace("</style>", user_4color_gradient_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied 4-color custom gradient to {path}")
