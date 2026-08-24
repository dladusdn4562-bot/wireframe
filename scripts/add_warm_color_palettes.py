# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

palette_css = """
    /* ==========================================================================
       [5대 부드럽고 따뜻한 감성 컬러 팔레트 테마 시스템]
       ========================================================================== */

    /* 1. 세이지 힐링 그린 (Healing Sage & Olive Green) - 자연의 편안한 쉼 */
    body.palette-sage {
      --color-terracotta: #3B7A57 !important;
      --color-forest: #204E38 !important;
    }
    body.palette-sage .btn-primary,
    body.palette-sage .btn-accent,
    body.palette-sage .btn-primary.btn-accent {
      background: #3B7A57 !important;
      border-color: #3B7A57 !important;
      box-shadow: 0 4px 14px rgba(59, 122, 87, 0.25) !important;
    }
    body.palette-sage .btn-primary:hover,
    body.palette-sage .btn-accent:hover {
      background: #2D6345 !important;
      border-color: #2D6345 !important;
    }
    body.palette-sage .btn-secondary {
      color: #3B7A57 !important;
      border-color: #3B7A57 !important;
    }
    body.palette-sage .btn-secondary:hover {
      background: #F0F7F3 !important;
      color: #2D6345 !important;
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
      background: linear-gradient(180deg, transparent 70%, rgba(59, 122, 87, 0.18) 70%) !important;
    }
    body.palette-sage .gnb-text-btn .btn-badge,
    body.palette-sage .floating-bottom-bar .btn-accent {
      background: #3B7A57 !important;
    }

    /* 2. 소프트 카라멜 브라운 (Soft Warm Caramel & Pecan) - 포근하고 깊은 온기 */
    body.palette-caramel {
      --color-terracotta: #A76336 !important;
      --color-forest: #4A2B18 !important;
    }
    body.palette-caramel .btn-primary,
    body.palette-caramel .btn-accent,
    body.palette-caramel .btn-primary.btn-accent {
      background: #A76336 !important;
      border-color: #A76336 !important;
      box-shadow: 0 4px 14px rgba(167, 99, 54, 0.25) !important;
    }
    body.palette-caramel .btn-primary:hover,
    body.palette-caramel .btn-accent:hover {
      background: #8F522A !important;
      border-color: #8F522A !important;
    }
    body.palette-caramel .btn-secondary {
      color: #A76336 !important;
      border-color: #A76336 !important;
    }
    body.palette-caramel .btn-secondary:hover {
      background: #FDF7F2 !important;
      color: #8F522A !important;
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
      background: linear-gradient(180deg, transparent 70%, rgba(167, 99, 54, 0.18) 70%) !important;
    }
    body.palette-caramel .gnb-text-btn .btn-badge,
    body.palette-caramel .floating-bottom-bar .btn-accent {
      background: #A76336 !important;
    }

    /* 3. 더스티 웜 로즈 (Dusty Rose & Muted Terracotta) - 체온 같은 포근한 온기 */
    body.palette-dustyrose {
      --color-terracotta: #B55B65 !important;
      --color-forest: #4A1E24 !important;
    }
    body.palette-dustyrose .btn-primary,
    body.palette-dustyrose .btn-accent,
    body.palette-dustyrose .btn-primary.btn-accent {
      background: #B55B65 !important;
      border-color: #B55B65 !important;
      box-shadow: 0 4px 14px rgba(181, 91, 101, 0.25) !important;
    }
    body.palette-dustyrose .btn-primary:hover,
    body.palette-dustyrose .btn-accent:hover {
      background: #9D4952 !important;
      border-color: #9D4952 !important;
    }
    body.palette-dustyrose .btn-secondary {
      color: #B55B65 !important;
      border-color: #B55B65 !important;
    }
    body.palette-dustyrose .btn-secondary:hover {
      background: #FDF5F6 !important;
      color: #9D4952 !important;
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
      background: linear-gradient(180deg, transparent 70%, rgba(181, 91, 101, 0.18) 70%) !important;
    }
    body.palette-dustyrose .gnb-text-btn .btn-badge,
    body.palette-dustyrose .floating-bottom-bar .btn-accent {
      background: #B55B65 !important;
    }

    /* 4. 웜 허니 오커 (Warm Honey & Golden Ochre) - 나른한 오후의 햇살 */
    body.palette-honey {
      --color-terracotta: #B87B28 !important;
      --color-forest: #4A3310 !important;
    }
    body.palette-honey .btn-primary,
    body.palette-honey .btn-accent,
    body.palette-honey .btn-primary.btn-accent {
      background: #B87B28 !important;
      border-color: #B87B28 !important;
      box-shadow: 0 4px 14px rgba(184, 123, 40, 0.25) !important;
    }
    body.palette-honey .btn-primary:hover,
    body.palette-honey .btn-accent:hover {
      background: #9E671D !important;
      border-color: #9E671D !important;
    }
    body.palette-honey .btn-secondary {
      color: #B87B28 !important;
      border-color: #B87B28 !important;
    }
    body.palette-honey .btn-secondary:hover {
      background: #FDF9F2 !important;
      color: #9E671D !important;
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
      background: linear-gradient(180deg, transparent 70%, rgba(184, 123, 40, 0.18) 70%) !important;
    }
    body.palette-honey .gnb-text-btn .btn-badge,
    body.palette-honey .floating-bottom-bar .btn-accent {
      background: #B87B28 !important;
    }

    /* 5. 웜 라벤더 토프 (Warm Lavender Taupe & Oatmeal) - 차분한 릴렉스 */
    body.palette-taupe {
      --color-terracotta: #7B627D !important;
      --color-forest: #332036 !important;
    }
    body.palette-taupe .btn-primary,
    body.palette-taupe .btn-accent,
    body.palette-taupe .btn-primary.btn-accent {
      background: #7B627D !important;
      border-color: #7B627D !important;
      box-shadow: 0 4px 14px rgba(123, 98, 125, 0.25) !important;
    }
    body.palette-taupe .btn-primary:hover,
    body.palette-taupe .btn-accent:hover {
      background: #664E68 !important;
      border-color: #664E68 !important;
    }
    body.palette-taupe .btn-secondary {
      color: #7B627D !important;
      border-color: #7B627D !important;
    }
    body.palette-taupe .btn-secondary:hover {
      background: #FAF6FB !important;
      color: #664E68 !important;
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
      background: linear-gradient(180deg, transparent 70%, rgba(123, 98, 125, 0.18) 70%) !important;
    }
    body.palette-taupe .gnb-text-btn .btn-badge,
    body.palette-taupe .floating-bottom-bar .btn-accent {
      background: #7B627D !important;
    }
"""

color_switcher_bar = """
    <!-- 5대 웜 컬러 팔레트 실시간 비교 선택 툴바 -->
    <div style="background:#1B201D; color:#f0ece4; padding:8px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.12); flex-wrap:wrap; gap:10px; font-size:12.5px; z-index:1200; position:relative;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="color:#FAF7F2; font-weight:800; font-size:13.5px;">🎨 5대 감성 웜 컬러 팔레트 실시간 체험:</span>
        <span style="color:#c5beb3;">원하는 색상 버튼을 클릭하여 웹사이트의 전체 분위기 변화를 바로 확인하세요!</span>
      </div>
      <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <button class="btn-palette-selector active" data-palette="palette-terracotta" onclick="window.switchColorPalette('palette-terracotta', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1.5px solid #D9531E; background:#D9531E; color:#fff; cursor:pointer; font-weight:700;">
          ● 1. 테라코타 오렌지 (현재)
        </button>
        <button class="btn-palette-selector" data-palette="palette-sage" onclick="window.switchColorPalette('palette-sage', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(59,122,87,0.3); color:#fff; cursor:pointer; font-weight:700;">
          🌿 2. 세이지 힐링 그린
        </button>
        <button class="btn-palette-selector" data-palette="palette-caramel" onclick="window.switchColorPalette('palette-caramel', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(167,99,54,0.3); color:#fff; cursor:pointer; font-weight:700;">
          ☕ 3. 소프트 카라멜 브라운
        </button>
        <button class="btn-palette-selector" data-palette="palette-dustyrose" onclick="window.switchColorPalette('palette-dustyrose', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(181,91,101,0.3); color:#fff; cursor:pointer; font-weight:700;">
          🌸 4. 더스티 웜 로즈
        </button>
        <button class="btn-palette-selector" data-palette="palette-honey" onclick="window.switchColorPalette('palette-honey', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(184,123,40,0.3); color:#fff; cursor:pointer; font-weight:700;">
          🍯 5. 웜 허니 골드
        </button>
        <button class="btn-palette-selector" data-palette="palette-taupe" onclick="window.switchColorPalette('palette-taupe', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(123,98,125,0.3); color:#fff; cursor:pointer; font-weight:700;">
          ☁️ 6. 웜 라벤더 토프
        </button>
      </div>
    </div>
"""

color_switcher_js = """
    window.switchColorPalette = function(paletteClass, btn) {
      document.body.classList.remove('palette-terracotta', 'palette-sage', 'palette-caramel', 'palette-dustyrose', 'palette-honey', 'palette-taupe');
      if (paletteClass !== 'palette-terracotta') {
        document.body.classList.add(paletteClass);
      }
      document.querySelectorAll('.btn-palette-selector').forEach(function(b) {
        if (b.getAttribute('data-palette') === paletteClass) {
          b.style.borderColor = '#ffffff';
          b.style.transform = 'scale(1.05)';
        } else {
          b.style.borderColor = 'rgba(255,255,255,0.25)';
          b.style.transform = 'scale(1)';
        }
      });
    };
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 추가
    if "/* 5대 부드럽고 따뜻한 감성 컬러 팔레트 테마 시스템 */" not in content:
        content = content.replace("</style>", palette_css + "\n  </style>")

    # 2. 헤더 상단에 컬러 스위처 바 삽입
    if "5대 웜 컬러 팔레트 실시간 비교 선택 툴바" not in content:
        content = content.replace(
            '<header class="site-header-fixed" id="site-header-fixed">',
            '<header class="site-header-fixed" id="site-header-fixed">\n' + color_switcher_bar
        )
        content = re.sub(r'padding-top:\s*\d+px;', 'padding-top: 165px;', content, count=1)

    # 3. JS 스크립트 추가
    if "window.switchColorPalette" not in content:
        content = content.replace("</script>", color_switcher_js + "\n  </script>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Added warm color palettes switcher to {path}")
