# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 새로운 2030 라이프스타일 웰니스 웜 뉴트럴 컬러 시스템 CSS
global_warm_neutral_css = """
    /* ==========================================================================
       [2030 라이프스타일 웰니스 전역 웜 뉴트럴 (Warm Neutral) 컬러 시스템]
       1. Base Background: 크림 오트밀 (#FDFBF7)
       2. Typography: 웜 브라운 차콜 (#4A433E)
       3. Primary (메인 CTA / 강조): 소프트 피치 코랄 (#E5A99B)
       4. Secondary (상태 알림 / 보조 태그 / 아이콘): 뮤티드 세이지 (#B4C4B1)
       ========================================================================== */

    :root {
      /* 1. Base & Surface Background */
      --bg-base: #FDFBF7;              /* 크림 오트밀 (전체 배경 및 카드 배경) */
      --bg-surface: #F7F3EB;           /* 소프트 오트밀 서피스 */
      --bg-surface-elevated: #EFE8DC;  /* 웜 샌드 서피스 */
      --bg-card: #FDFBF7;              /* 카드 배경 (크림 오트밀) */
      --bg-card-alt: #F4EFE6;

      /* 2. Typography */
      --color-text-primary: #4A433E;   /* 웜 브라운 차콜 (본문 및 H1~H6) */
      --color-text-secondary: #7A7067; /* 웜 미디엄 브라운 */
      --color-text-muted: #9E9388;     /* 소프트 웜 그레이 */

      /* 3. Primary */
      --color-primary: #E5A99B;        /* 소프트 피치 코랄 (메인 CTA & 강조) */
      --color-primary-hover: #D49586;  /* 호버 피치 코랄 */
      --color-primary-light: #FDF5F3;  /* 연한 피치 코랄 틴트 */
      --color-terracotta: #E5A99B;     /* 레거시 호환 */

      /* 4. Secondary */
      --color-secondary: #B4C4B1;      /* 뮤티드 세이지 (상태 알림, 보조 태그, 아이콘) */
      --color-secondary-hover: #9FB39B;
      --color-secondary-light: #EFF4EE;/* 소프트 세이지 틴트 */
      --color-secondary-text: #4C6649; /* 세이지 텍스트 가독성 */

      /* Borders & Shadows */
      --color-border: #E8E1D3;         /* 부드러운 오트밀 보더 */
      --color-border-light: #F2ECE1;
      --shadow-sm: 0 2px 8px rgba(74, 67, 62, 0.04);
      --shadow-md: 0 6px 20px rgba(74, 67, 62, 0.06);
      --shadow-lg: 0 12px 36px rgba(74, 67, 62, 0.08);

      /* Typography fonts */
      --font-gowun: 'Gowun Batang', 'MaruBuri', serif;
      --font-sans: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
    }

    body {
      background-color: #FDFBF7 !important;
      color: #4A433E !important;
      font-family: var(--font-sans);
    }

    #page-main, #page-shop, #page-story {
      background-color: #FDFBF7 !important;
      color: #4A433E !important;
    }

    /* 모든 텍스트 및 헤딩: 웜 브라운 차콜 (#4A433E) */
    h1, h2, h3, h4, h5, h6, p, span, div, li, td, th {
      color: #4A433E;
    }
    .text-secondary, .hero-subcopy, .journey-lead {
      color: #7A7067 !important;
    }
    .text-muted {
      color: #9E9388 !important;
    }

    /* 상단 GNB: 크림 오트밀 (#FDFBF7) & 웜 보더 */
    .header-gnb {
      background: rgba(253, 251, 247, 0.96) !important;
      backdrop-filter: blur(12px) !important;
      border-bottom: 1px solid #E8E1D3 !important;
    }
    .logo-brand {
      color: #4A433E !important;
    }
    .gnb-tag {
      color: #E5A99B !important;
    }
    .gnb-link {
      color: #4A433E !important;
    }
    .gnb-link:hover, .gnb-link.active {
      color: #E5A99B !important;
      border-bottom-color: #E5A99B !important;
    }

    /* 상단 고정 최상단 알림바 */
    #site-header-fixed {
      background: #4A433E !important;
      color: #FDFBF7 !important;
      border-bottom: 1px solid rgba(255,255,255,0.12) !important;
    }
    .btn-page-tab {
      background: rgba(255,255,255,0.12) !important;
      color: #FDFBF7 !important;
      border-color: rgba(255,255,255,0.2) !important;
    }
    .btn-page-tab.active {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      border-color: #E5A99B !important;
    }

    /* 1px 미세 연장선 안내 텍스트: 소프트 피치 코랄 (#E5A99B) */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      color: #E5A99B !important;
      font-family: var(--font-gowun), serif !important;
    }
    .section-tag::before, .section-tag::after,
    .hero-eyebrow::before, .hero-eyebrow::after,
    .catalog-tag::before, .catalog-tag::after,
    .journey-tag::before, .journey-tag::after {
      background: #E5A99B !important;
    }

    /* 매니페스토 헤드라인 & 하이라이트 */
    .hero-manifesto-title {
      color: #4A433E !important;
      font-family: var(--font-gowun), serif !important;
    }
    .hero-manifesto-title span {
      color: #4A433E !important;
      background: linear-gradient(180deg, transparent 65%, rgba(229, 169, 155, 0.28) 65%) !important;
    }

    /* Primary: 메인 CTA 버튼 (소프트 피치 코랄 #E5A99B) */
    .btn-primary,
    .btn-accent,
    .hero-cta-group .btn-primary,
    .floating-bottom-bar .btn-accent,
    .gnb-actions .btn-primary {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      border-color: #E5A99B !important;
      border-radius: 9999px !important;
      box-shadow: 0 4px 14px rgba(229, 169, 155, 0.35) !important;
      font-weight: 700 !important;
    }
    .btn-primary:hover,
    .btn-accent:hover,
    .hero-cta-group .btn-primary:hover {
      background: #D49586 !important;
      border-color: #D49586 !important;
      transform: translateY(-1px) !important;
    }

    /* Secondary CTA 버튼: 둥근 화이트/크림 + 피치 코랄 아웃라인 */
    .btn-secondary,
    .hero-cta-group .btn-secondary {
      background: #FDFBF7 !important;
      color: #4A433E !important;
      border: 1.5px solid #E5A99B !important;
      border-radius: 9999px !important;
      font-weight: 700 !important;
    }
    .btn-secondary:hover,
    .hero-cta-group .btn-secondary:hover {
      background: #FDF5F3 !important;
      color: #D49586 !important;
      border-color: #D49586 !important;
    }

    /* Secondary: 뮤티드 세이지 (#B4C4B1) 상태 알림, 보조 태그, 아이콘, 뱃지 */
    .badge-secondary,
    .status-badge,
    .filter-tag.active,
    .badge-accent {
      background: #EFF4EE !important;
      color: #4C6649 !important;
      border: 1px solid #B4C4B1 !important;
    }
    .proof-check-icon,
    .tech-icon,
    .icon-sage {
      color: #7A9B76 !important;
    }

    /* 카드 및 서피스: 크림 오트밀 (#FDFBF7) & 웜 보더 (#E8E1D3) */
    .pride-metrics-bar {
      background: #FDFBF7 !important;
      border: 1.5px solid #E8E1D3 !important;
      box-shadow: 0 8px 24px rgba(74, 67, 62, 0.05) !important;
    }
    .journey-chapter,
    .featured-card,
    .proof-stat-card,
    .review-card,
    .explore-catalog-banner,
    .fit-finder-banner,
    .hud-card,
    .center-card,
    .faq-item,
    .one-view-card {
      background: #FDFBF7 !important;
      border: 1.5px solid #E8E1D3 !important;
      box-shadow: 0 6px 20px rgba(74, 67, 62, 0.04) !important;
    }
    .faq-item.open {
      background: #F7F3EB !important;
    }

    /* 하단 플로팅 고정 바 */
    .floating-bottom-bar {
      background: #4A433E !important;
      color: #FDFBF7 !important;
      border-top: 1px solid rgba(255,255,255,0.12) !important;
    }
    .floating-bottom-bar span {
      color: #FDFBF7 !important;
    }
    .floating-bottom-bar .badge-price {
      background: #E5A99B !important;
      color: #FFFFFF !important;
    }

    /* GNB 뱃지 */
    .gnb-text-btn .btn-badge {
      background: #E5A99B !important;
      color: #FFFFFF !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 기존 그라데이션 및 이전 팔레트 CSS 제거/대체
    if "/* ==========================================================================\n       [2030 라이프스타일 웰니스 전역 웜 뉴트럴" not in content:
        content = content.replace("</style>", global_warm_neutral_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied 2030 Lifestyle Warm Neutral color system to {path}")
