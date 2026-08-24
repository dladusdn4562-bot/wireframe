# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

palette_override_css = """
    /* ==========================================================================
       [5대 감성 웜 컬러 팔레트 완전 우선순위 오버라이드]
       ========================================================================== */

    /* 2. 세이지 힐링 그린 (Healing Sage & Forest Green) - 숲속의 고요한 쉼 */
    body.palette-sage, body.palette-sage * {
      --color-terracotta: #3B7A57 !important;
    }
    body.palette-sage .btn-primary,
    body.palette-sage .btn-accent,
    body.palette-sage .btn-primary.btn-accent,
    body.palette-sage .hero-cta-group .btn-primary,
    body.palette-sage .floating-bottom-bar .btn-accent,
    body.palette-sage .gnb-actions .btn-primary,
    body.palette-sage .gnb-text-btn .btn-badge {
      background: #3B7A57 !important;
      border-color: #3B7A57 !important;
      box-shadow: 0 4px 14px rgba(59, 122, 87, 0.28) !important;
      color: #ffffff !important;
    }
    body.palette-sage .btn-primary:hover,
    body.palette-sage .hero-cta-group .btn-primary:hover {
      background: #2D6345 !important;
      border-color: #2D6345 !important;
    }
    body.palette-sage .btn-secondary,
    body.palette-sage .hero-cta-group .btn-secondary {
      color: #3B7A57 !important;
      border-color: #3B7A57 !important;
      background: #ffffff !important;
    }
    body.palette-sage .btn-secondary:hover {
      background: #F0F7F3 !important;
      color: #2D6345 !important;
      border-color: #2D6345 !important;
    }
    body.palette-sage .section-tag,
    body.palette-sage .hero-eyebrow,
    body.palette-sage .catalog-tag,
    body.palette-sage .journey-tag {
      color: #3B7A57 !important;
    }
    body.palette-sage .section-tag::before,
    body.palette-sage .section-tag::after,
    body.palette-sage .hero-eyebrow::before,
    body.palette-sage .hero-eyebrow::after,
    body.palette-sage .catalog-tag::before,
    body.palette-sage .catalog-tag::after,
    body.palette-sage .journey-tag::before,
    body.palette-sage .journey-tag::after {
      background: #3B7A57 !important;
    }
    body.palette-sage .hero-manifesto-title span {
      color: #3B7A57 !important;
      background: linear-gradient(180deg, transparent 65%, rgba(59, 122, 87, 0.18) 65%) !important;
    }
    body.palette-sage .btn-page-tab.active {
      background: #3B7A57 !important;
    }

    /* 3. 소프트 카라멜 브라운 (Warm Caramel & Roasted Pecan) - 포근한 온기 */
    body.palette-caramel, body.palette-caramel * {
      --color-terracotta: #A76336 !important;
    }
    body.palette-caramel .btn-primary,
    body.palette-caramel .btn-accent,
    body.palette-caramel .btn-primary.btn-accent,
    body.palette-caramel .hero-cta-group .btn-primary,
    body.palette-caramel .floating-bottom-bar .btn-accent,
    body.palette-caramel .gnb-actions .btn-primary,
    body.palette-caramel .gnb-text-btn .btn-badge {
      background: #A76336 !important;
      border-color: #A76336 !important;
      box-shadow: 0 4px 14px rgba(167, 99, 54, 0.28) !important;
      color: #ffffff !important;
    }
    body.palette-caramel .btn-primary:hover,
    body.palette-caramel .hero-cta-group .btn-primary:hover {
      background: #8F522A !important;
      border-color: #8F522A !important;
    }
    body.palette-caramel .btn-secondary,
    body.palette-caramel .hero-cta-group .btn-secondary {
      color: #A76336 !important;
      border-color: #A76336 !important;
      background: #ffffff !important;
    }
    body.palette-caramel .btn-secondary:hover {
      background: #FDF7F2 !important;
      color: #8F522A !important;
      border-color: #8F522A !important;
    }
    body.palette-caramel .section-tag,
    body.palette-caramel .hero-eyebrow,
    body.palette-caramel .catalog-tag,
    body.palette-caramel .journey-tag {
      color: #A76336 !important;
    }
    body.palette-caramel .section-tag::before,
    body.palette-caramel .section-tag::after,
    body.palette-caramel .hero-eyebrow::before,
    body.palette-caramel .hero-eyebrow::after,
    body.palette-caramel .catalog-tag::before,
    body.palette-caramel .catalog-tag::after,
    body.palette-caramel .journey-tag::before,
    body.palette-caramel .journey-tag::after {
      background: #A76336 !important;
    }
    body.palette-caramel .hero-manifesto-title span {
      color: #A76336 !important;
      background: linear-gradient(180deg, transparent 65%, rgba(167, 99, 54, 0.18) 65%) !important;
    }
    body.palette-caramel .btn-page-tab.active {
      background: #A76336 !important;
    }

    /* 4. 더스티 웜 로즈 (Dusty Warm Rose) - 체온 같은 우아한 포근함 */
    body.palette-dustyrose, body.palette-dustyrose * {
      --color-terracotta: #B55B65 !important;
    }
    body.palette-dustyrose .btn-primary,
    body.palette-dustyrose .btn-accent,
    body.palette-dustyrose .btn-primary.btn-accent,
    body.palette-dustyrose .hero-cta-group .btn-primary,
    body.palette-dustyrose .floating-bottom-bar .btn-accent,
    body.palette-dustyrose .gnb-actions .btn-primary,
    body.palette-dustyrose .gnb-text-btn .btn-badge {
      background: #B55B65 !important;
      border-color: #B55B65 !important;
      box-shadow: 0 4px 14px rgba(181, 91, 101, 0.28) !important;
      color: #ffffff !important;
    }
    body.palette-dustyrose .btn-primary:hover,
    body.palette-dustyrose .hero-cta-group .btn-primary:hover {
      background: #9D4952 !important;
      border-color: #9D4952 !important;
    }
    body.palette-dustyrose .btn-secondary,
    body.palette-dustyrose .hero-cta-group .btn-secondary {
      color: #B55B65 !important;
      border-color: #B55B65 !important;
      background: #ffffff !important;
    }
    body.palette-dustyrose .btn-secondary:hover {
      background: #FDF5F6 !important;
      color: #9D4952 !important;
      border-color: #9D4952 !important;
    }
    body.palette-dustyrose .section-tag,
    body.palette-dustyrose .hero-eyebrow,
    body.palette-dustyrose .catalog-tag,
    body.palette-dustyrose .journey-tag {
      color: #B55B65 !important;
    }
    body.palette-dustyrose .section-tag::before,
    body.palette-dustyrose .section-tag::after,
    body.palette-dustyrose .hero-eyebrow::before,
    body.palette-dustyrose .hero-eyebrow::after,
    body.palette-dustyrose .catalog-tag::before,
    body.palette-dustyrose .catalog-tag::after,
    body.palette-dustyrose .journey-tag::before,
    body.palette-dustyrose .journey-tag::after {
      background: #B55B65 !important;
    }
    body.palette-dustyrose .hero-manifesto-title span {
      color: #B55B65 !important;
      background: linear-gradient(180deg, transparent 65%, rgba(181, 91, 101, 0.18) 65%) !important;
    }
    body.palette-dustyrose .btn-page-tab.active {
      background: #B55B65 !important;
    }

    /* 5. 웜 허니 골드 (Warm Honey & Ochre) - 나른한 오후의 햇살 */
    body.palette-honey, body.palette-honey * {
      --color-terracotta: #B87B28 !important;
    }
    body.palette-honey .btn-primary,
    body.palette-honey .btn-accent,
    body.palette-honey .btn-primary.btn-accent,
    body.palette-honey .hero-cta-group .btn-primary,
    body.palette-honey .floating-bottom-bar .btn-accent,
    body.palette-honey .gnb-actions .btn-primary,
    body.palette-honey .gnb-text-btn .btn-badge {
      background: #B87B28 !important;
      border-color: #B87B28 !important;
      box-shadow: 0 4px 14px rgba(184, 123, 40, 0.28) !important;
      color: #ffffff !important;
    }
    body.palette-honey .btn-primary:hover,
    body.palette-honey .hero-cta-group .btn-primary:hover {
      background: #9E671D !important;
      border-color: #9E671D !important;
    }
    body.palette-honey .btn-secondary,
    body.palette-honey .hero-cta-group .btn-secondary {
      color: #B87B28 !important;
      border-color: #B87B28 !important;
      background: #ffffff !important;
    }
    body.palette-honey .btn-secondary:hover {
      background: #FDF9F2 !important;
      color: #9E671D !important;
      border-color: #9E671D !important;
    }
    body.palette-honey .section-tag,
    body.palette-honey .hero-eyebrow,
    body.palette-honey .catalog-tag,
    body.palette-honey .journey-tag {
      color: #B87B28 !important;
    }
    body.palette-honey .section-tag::before,
    body.palette-honey .section-tag::after,
    body.palette-honey .hero-eyebrow::before,
    body.palette-honey .hero-eyebrow::after,
    body.palette-honey .catalog-tag::before,
    body.palette-honey .catalog-tag::after,
    body.palette-honey .journey-tag::before,
    body.palette-honey .journey-tag::after {
      background: #B87B28 !important;
    }
    body.palette-honey .hero-manifesto-title span {
      color: #B87B28 !important;
      background: linear-gradient(180deg, transparent 65%, rgba(184, 123, 40, 0.18) 65%) !important;
    }
    body.palette-honey .btn-page-tab.active {
      background: #B87B28 !important;
    }

    /* 6. 웜 라벤더 토프 (Warm Lavender Taupe) - 깊은 숙면과 차분한 릴렉스 */
    body.palette-taupe, body.palette-taupe * {
      --color-terracotta: #7B627D !important;
    }
    body.palette-taupe .btn-primary,
    body.palette-taupe .btn-accent,
    body.palette-taupe .btn-primary.btn-accent,
    body.palette-taupe .hero-cta-group .btn-primary,
    body.palette-taupe .floating-bottom-bar .btn-accent,
    body.palette-taupe .gnb-actions .btn-primary,
    body.palette-taupe .gnb-text-btn .btn-badge {
      background: #7B627D !important;
      border-color: #7B627D !important;
      box-shadow: 0 4px 14px rgba(123, 98, 125, 0.28) !important;
      color: #ffffff !important;
    }
    body.palette-taupe .btn-primary:hover,
    body.palette-taupe .hero-cta-group .btn-primary:hover {
      background: #664E68 !important;
      border-color: #664E68 !important;
    }
    body.palette-taupe .btn-secondary,
    body.palette-taupe .hero-cta-group .btn-secondary {
      color: #7B627D !important;
      border-color: #7B627D !important;
      background: #ffffff !important;
    }
    body.palette-taupe .btn-secondary:hover {
      background: #FAF6FB !important;
      color: #664E68 !important;
      border-color: #664E68 !important;
    }
    body.palette-taupe .section-tag,
    body.palette-taupe .hero-eyebrow,
    body.palette-taupe .catalog-tag,
    body.palette-taupe .journey-tag {
      color: #7B627D !important;
    }
    body.palette-taupe .section-tag::before,
    body.palette-taupe .section-tag::after,
    body.palette-taupe .hero-eyebrow::before,
    body.palette-taupe .hero-eyebrow::after,
    body.palette-taupe .catalog-tag::before,
    body.palette-taupe .catalog-tag::after,
    body.palette-taupe .journey-tag::before,
    body.palette-taupe .journey-tag::after {
      background: #7B627D !important;
    }
    body.palette-taupe .hero-manifesto-title span {
      color: #7B627D !important;
      background: linear-gradient(180deg, transparent 65%, rgba(123, 98, 125, 0.18) 65%) !important;
    }
    body.palette-taupe .btn-page-tab.active {
      background: #7B627D !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 끝부분에 palette_override_css 주입
    if "/* [5대 감성 웜 컬러 팔레트 완전 우선순위 오버라이드] */" not in content:
        content = content.replace("</style>", palette_override_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated palette priority in {path}")
