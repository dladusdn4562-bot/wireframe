# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 3가지 둥글기 시스템 CSS 정의
radius_switcher_css = """
    /* ==========================================================================
       [3대 상자 모서리 둥글기 (Border Radius) 실시간 비교 시스템]
       ========================================================================== */

    /* 1. 🌿 옵션 1: 유기적 조약돌 & 감성 웰니스 (크기별 비례 라운드 16px ~ 36px) */
    body.radius-theme-pebble .pride-metrics-bar { border-radius: 36px !important; }
    body.radius-theme-pebble .featured-card { border-radius: 26px !important; }
    body.radius-theme-pebble .journey-chapter,
    body.radius-theme-pebble .journey-visual-card { border-radius: 30px !important; }
    body.radius-theme-pebble .explore-catalog-banner,
    body.radius-theme-pebble .fit-finder-banner { border-radius: 32px !important; }
    body.radius-theme-pebble .one-view-card { border-radius: 16px !important; }
    body.radius-theme-pebble .hud-card,
    body.radius-theme-pebble .center-card,
    body.radius-theme-pebble .proof-stat-card,
    body.radius-theme-pebble .review-card,
    body.radius-theme-pebble .faq-item { border-radius: 20px !important; }

    /* 2. 🏛️ 옵션 2: 비대칭 유기적 아치 & 현대 갤러리 (꽃잎 및 돔 아치형 비대칭 곡선) */
    body.radius-theme-asymm .pride-metrics-bar { border-radius: 28px !important; }
    body.radius-theme-asymm .featured-card { border-radius: 36px 36px 14px 14px !important; }
    body.radius-theme-asymm .journey-chapter,
    body.radius-theme-asymm .journey-visual-card { border-radius: 36px 10px 36px 10px !important; }
    body.radius-theme-asymm .explore-catalog-banner,
    body.radius-theme-asymm .fit-finder-banner { border-radius: 36px 12px 36px 12px !important; }
    body.radius-theme-asymm .one-view-card { border-radius: 24px 8px 24px 8px !important; }
    body.radius-theme-asymm .hud-card,
    body.radius-theme-asymm .center-card,
    body.radius-theme-asymm .proof-stat-card,
    body.radius-theme-asymm .review-card { border-radius: 24px 8px 24px 8px !important; }
    body.radius-theme-asymm .faq-item { border-radius: 18px 6px 18px 6px !important; }

    /* 3. ☕ 옵션 3: 킨포크 에디토리얼 & 기능별 릴렉스 (서사 12px vs 배너 38px 명확한 대비) */
    body.radius-theme-editorial .pride-metrics-bar { border-radius: 38px !important; }
    body.radius-theme-editorial .featured-card { border-radius: 22px !important; }
    body.radius-theme-editorial .journey-chapter,
    body.radius-theme-editorial .journey-visual-card { border-radius: 12px !important; }
    body.radius-theme-editorial .explore-catalog-banner,
    body.radius-theme-editorial .fit-finder-banner { border-radius: 38px !important; }
    body.radius-theme-editorial .one-view-card { border-radius: 14px !important; }
    body.radius-theme-editorial .hud-card,
    body.radius-theme-editorial .center-card,
    body.radius-theme-editorial .proof-stat-card,
    body.radius-theme-editorial .review-card,
    body.radius-theme-editorial .faq-item { border-radius: 14px !important; }
"""

# 상단 알림바 바로 위에 배치될 실시간 둥글기 스위처 툴바
radius_toolbar_html = """
    <!-- 3대 상자 둥글기 실시간 비교 선택 툴바 -->
    <div style="background:#36302B; color:#FDFBF7; padding:9px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.15); flex-wrap:wrap; gap:10px; font-size:12.5px; z-index:1200; position:relative;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="color:#E5A99B; font-weight:800; font-size:13.5px;">🔘 3대 상자 둥글기 실시간 체험:</span>
        <span style="color:#D8CEC4;">원하는 스타일 버튼을 클릭하여 웹사이트 내 카드와 상자들의 둥글기 변화를 바로 확인하세요!</span>
      </div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <button class="btn-radius-selector active" data-radius="radius-theme-pebble" onclick="applyRadiusThemeDirect('radius-theme-pebble')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:2px solid #E5A99B; background:#FDFBF7; color:#4A433E; cursor:pointer; font-weight:800; font-family:'Gowun Batang', serif;">
          🌿 1. 유기적 조약돌 (비례 16~36px)
        </button>
        <button class="btn-radius-selector" data-radius="radius-theme-asymm" onclick="applyRadiusThemeDirect('radius-theme-asymm')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.3); background:rgba(255,255,255,0.1); color:#FDFBF7; cursor:pointer; font-weight:700; font-family:'Gowun Batang', serif;">
          🏛️ 2. 비대칭 아치 (꽃잎/아치 곡선)
        </button>
        <button class="btn-radius-selector" data-radius="radius-theme-editorial" onclick="applyRadiusThemeDirect('radius-theme-editorial')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.3); background:rgba(255,255,255,0.1); color:#FDFBF7; cursor:pointer; font-weight:700; font-family:'Gowun Batang', serif;">
          ☕ 3. 킨포크 에디토리얼 (서사 12px vs 배너 38px)
        </button>
      </div>
    </div>
"""

# 전역 JS 함수
radius_js = """
    function applyRadiusThemeDirect(radiusClass) {
      console.log('Applying Radius Theme:', radiusClass);
      document.body.className = document.body.className.replace(/\\bradius-theme-\\S+/g, '').trim();
      document.body.classList.add(radiusClass);
      
      document.querySelectorAll('.btn-radius-selector').forEach(function(b) {
        if (b.getAttribute('data-radius') === radiusClass) {
          b.style.borderColor = '#E5A99B';
          b.style.borderWidth = '2px';
          b.style.background = '#FDFBF7';
          b.style.color = '#4A433E';
          b.style.fontWeight = '800';
          b.classList.add('active');
        } else {
          b.style.borderColor = 'rgba(255,255,255,0.3)';
          b.style.borderWidth = '1px';
          b.style.background = 'rgba(255,255,255,0.1)';
          b.style.color = '#FDFBF7';
          b.style.fontWeight = '700';
          b.classList.remove('active');
        }
      });
    }
    window.applyRadiusThemeDirect = applyRadiusThemeDirect;
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 주입
    if "/* ==========================================================================\n       [3대 상자 모서리 둥글기" not in content:
        content = content.replace("</style>", radius_switcher_css + "\n  </style>")

    # 2. JS 함수 주입
    if "window.applyRadiusThemeDirect" not in content:
        content = content.replace("</head>", "  <script>\n" + radius_js + "  </script>\n</head>")

    # 3. 툴바 주입
    if "<!-- 3대 상자 둥글기 실시간 비교 선택 툴바 -->" not in content:
        content = content.replace(
            '<div id="site-header-fixed"',
            radius_toolbar_html.strip() + '\n    <div id="site-header-fixed"'
        )

    # 4. body 기본 클래스에 radius-theme-pebble 추가
    if 'class="' in content and '<body' in content:
        content = re.sub(r'<body class="([^"]*)"', r'<body class="\1 radius-theme-pebble"', content)
    else:
        content = content.replace("<body>", '<body class="radius-theme-pebble">')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied real-time radius switcher to {path}")
