# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

bg_palette_css = """
    /* ==========================================================================
       [5대 부드럽고 따뜻한 '전체 메인 배경색' 테마 시스템 (Background Palettes)]
       웹사이트 전체의 Base 배경, Surface 배경, 카드 톤, 지표 바 톤이 일괄 변환됩니다.
       ========================================================================== */

    /* 1. 기본값: 웜 밀크티 아이보리 (Warm Milk Tea Ivory) */
    body.bg-theme-ivory {
      --bg-base: #FAF7F2 !important;
      --bg-surface: #F3EFE6 !important;
      --bg-card: #FFFFFF !important;
      --bg-surface-elevated: #ECE5D8 !important;
      background-color: #FAF7F2 !important;
    }

    /* 2. 소프트 웜 린넨 & 오트밀 (Warm Linen & Oatmeal) - 햇살에 말린 린넨 패브릭 */
    body.bg-theme-linen {
      --bg-base: #F5F0E6 !important;
      --bg-surface: #EAE2D2 !important;
      --bg-card: #FAF7F0 !important;
      --bg-surface-elevated: #DFD5C2 !important;
      background-color: #F5F0E6 !important;
    }
    body.bg-theme-linen .header-gnb,
    body.bg-theme-linen .pride-metrics-bar,
    body.bg-theme-linen .one-view-card,
    body.bg-theme-linen .journey-chapter,
    body.bg-theme-linen .featured-card {
      background-color: #FAF7F0 !important;
      border-color: #E2D7C3 !important;
    }
    body.bg-theme-linen .hero-section,
    body.bg-theme-linen .journey-section,
    body.bg-theme-linen .proof-section {
      background-color: #F5F0E6 !important;
    }

    /* 3. 포근한 버터 밀크 & 바닐라 (Cozy Buttermilk & Warm Vanilla) - 화사하고 달콤한 온기 */
    body.bg-theme-butter {
      --bg-base: #FAF6EB !important;
      --bg-surface: #F2EBD7 !important;
      --bg-card: #FFFFFF !important;
      --bg-surface-elevated: #E8DECA !important;
      background-color: #FAF6EB !important;
    }
    body.bg-theme-butter .header-gnb,
    body.bg-theme-butter .pride-metrics-bar,
    body.bg-theme-butter .one-view-card,
    body.bg-theme-butter .journey-chapter,
    body.bg-theme-butter .featured-card {
      background-color: #FFFFFF !important;
      border-color: #EADEBE !important;
    }
    body.bg-theme-butter .hero-section,
    body.bg-theme-butter .journey-section,
    body.bg-theme-butter .proof-section {
      background-color: #FAF6EB !important;
    }

    /* 4. 차분한 세이지 틴트 린넨 (Calm Sage-Tinted Linen) - 따뜻한 찻잔과 숲속 휴식 */
    body.bg-theme-sage-tint {
      --bg-base: #F2F5F0 !important;
      --bg-surface: #E5ECE1 !important;
      --bg-card: #FAFBF9 !important;
      --bg-surface-elevated: #D7E2D1 !important;
      background-color: #F2F5F0 !important;
    }
    body.bg-theme-sage-tint .header-gnb,
    body.bg-theme-sage-tint .pride-metrics-bar,
    body.bg-theme-sage-tint .one-view-card,
    body.bg-theme-sage-tint .journey-chapter,
    body.bg-theme-sage-tint .featured-card {
      background-color: #FAFBF9 !important;
      border-color: #D6E0D0 !important;
    }
    body.bg-theme-sage-tint .hero-section,
    body.bg-theme-sage-tint .journey-section,
    body.bg-theme-sage-tint .proof-section {
      background-color: #F2F5F0 !important;
    }

    /* 5. 소프트 피치 파우더 베이지 (Soft Peach & Dusty Clay Cream) - 살결 같은 다정한 온기 */
    body.bg-theme-peach {
      --bg-base: #F8F3EE !important;
      --bg-surface: #EFE6DD !important;
      --bg-card: #FCFAF7 !important;
      --bg-surface-elevated: #E5D7CA !important;
      background-color: #F8F3EE !important;
    }
    body.bg-theme-peach .header-gnb,
    body.bg-theme-peach .pride-metrics-bar,
    body.bg-theme-peach .one-view-card,
    body.bg-theme-peach .journey-chapter,
    body.bg-theme-peach .featured-card {
      background-color: #FCFAF7 !important;
      border-color: #E2D3C4 !important;
    }
    body.bg-theme-peach .hero-section,
    body.bg-theme-peach .journey-section,
    body.bg-theme-peach .proof-section {
      background-color: #F8F3EE !important;
    }

    /* 6. 어반 웜 토프 & 오트 그레이지 (Warm Urban Taupe & Greige) - 이솝 플래그십 스파 감성 */
    body.bg-theme-greige {
      --bg-base: #F0EDE8 !important;
      --bg-surface: #E3DED7 !important;
      --bg-card: #F8F6F3 !important;
      --bg-surface-elevated: #D5CFC6 !important;
      background-color: #F0EDE8 !important;
    }
    body.bg-theme-greige .header-gnb,
    body.bg-theme-greige .pride-metrics-bar,
    body.bg-theme-greige .one-view-card,
    body.bg-theme-greige .journey-chapter,
    body.bg-theme-greige .featured-card {
      background-color: #F8F6F3 !important;
      border-color: #D2CBC1 !important;
    }
    body.bg-theme-greige .hero-section,
    body.bg-theme-greige .journey-section,
    body.bg-theme-greige .proof-section {
      background-color: #F0EDE8 !important;
    }
"""

bg_switcher_toolbar = """
    <!-- 5대 감성 메인 배경색 실시간 비교 선택 툴바 -->
    <div style="background:#1B201D; color:#f0ece4; padding:8px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.12); flex-wrap:wrap; gap:10px; font-size:12.5px; z-index:1200; position:relative;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="color:#FAF7F2; font-weight:800; font-size:13.5px;">🏡 5대 메인 전체 배경색 실시간 체험:</span>
        <span style="color:#c5beb3;">원하는 배경색 버튼을 클릭하여 웹사이트 전체 공간의 무드 변화를 바로 확인하세요!</span>
      </div>
      <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <button class="btn-bg-selector active" data-bg="bg-theme-ivory" onclick="window.switchBgTheme('bg-theme-ivory', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1.5px solid #ffffff; background:#FAF7F2; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🥛 1. 밀크티 아이보리 (현재)
        </button>
        <button class="btn-bg-selector" data-bg="bg-theme-linen" onclick="window.switchBgTheme('bg-theme-linen', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:#F5F0E6; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🌾 2. 웜 린넨 & 오트밀
        </button>
        <button class="btn-bg-selector" data-bg="bg-theme-butter" onclick="window.switchBgTheme('bg-theme-butter', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:#FAF6EB; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🧈 3. 버터밀크 & 바닐라
        </button>
        <button class="btn-bg-selector" data-bg="bg-theme-sage-tint" onclick="window.switchBgTheme('bg-theme-sage-tint', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:#F2F5F0; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🍵 4. 세이지 틴트 린넨
        </button>
        <button class="btn-bg-selector" data-bg="bg-theme-peach" onclick="window.switchBgTheme('bg-theme-peach', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:#F8F3EE; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🍑 5. 피치 파우더 베이지
        </button>
        <button class="btn-bg-selector" data-bg="bg-theme-greige" onclick="window.switchBgTheme('bg-theme-greige', this)" style="padding:5px 12px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:#F0EDE8; color:#1F1D1A; cursor:pointer; font-weight:700;">
          🏛️ 6. 어반 웜 그레이지
        </button>
      </div>
    </div>
"""

bg_switcher_js = """
    window.switchBgTheme = function(bgClass, btn) {
      console.log('Background theme selected:', bgClass);
      document.body.classList.remove('bg-theme-ivory', 'bg-theme-linen', 'bg-theme-butter', 'bg-theme-sage-tint', 'bg-theme-peach', 'bg-theme-greige');
      document.body.classList.add(bgClass);
      
      document.querySelectorAll('.btn-bg-selector').forEach(function(b) {
        if (b.getAttribute('data-bg') === bgClass) {
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

    # 1. 기존 버튼 팔레트 관련 툴바 제거 후 배경 툴바로 교체
    content = re.sub(
        r'<!-- 5대 웜 컬러 팔레트 실시간 비교 선택 툴바 -->.*?</div>\s*</div>',
        bg_switcher_toolbar.strip(),
        content,
        flags=re.DOTALL
    )

    # 2. CSS 주입
    if "/* [5대 부드럽고 따뜻한 '전체 메인 배경색' 테마 시스템" not in content:
        content = content.replace("</style>", bg_palette_css + "\n  </style>")

    # 3. Head JS 함수 주입
    if "window.switchBgTheme" not in content:
        content = content.replace("</head>", "  <script>\n" + bg_switcher_js + "  </script>\n</head>")

    # 4. Body 기본 클래스에 bg-theme-ivory 추가
    content = content.replace("<body>", '<body class="bg-theme-ivory">')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied background palette system to {path}")
