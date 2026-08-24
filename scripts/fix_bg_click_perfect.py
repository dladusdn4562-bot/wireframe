# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 극명한 시각적 차이를 주는 6대 배경 테마 CSS
distinct_bg_css = """
    /* ==========================================================================
       [6대 감성 메인 전체 배경색 테마 시스템 - 극명하고 부드러운 시각적 변화]
       ========================================================================== */

    /* 1. 🥛 웜 밀크티 아이보리 (Warm Milk Tea Ivory) */
    body.bg-theme-ivory,
    body.bg-theme-ivory .hero-section,
    body.bg-theme-ivory .journey-section,
    body.bg-theme-ivory .proof-section,
    body.bg-theme-ivory #page-shop,
    body.bg-theme-ivory #page-story {
      background-color: #FAF7F2 !important;
    }
    body.bg-theme-ivory .header-gnb,
    body.bg-theme-ivory .pride-metrics-bar,
    body.bg-theme-ivory .one-view-card,
    body.bg-theme-ivory .featured-card,
    body.bg-theme-ivory .fit-finder-banner {
      background-color: #FFFFFF !important;
      border-color: #E8E2D5 !important;
    }

    /* 2. 🌾 웜 린넨 & 오트밀 (Warm Linen & Oatmeal) - 포근한 린넨 패브릭 */
    body.bg-theme-linen,
    body.bg-theme-linen .hero-section,
    body.bg-theme-linen .journey-section,
    body.bg-theme-linen .proof-section,
    body.bg-theme-linen #page-shop,
    body.bg-theme-linen #page-story {
      background-color: #EFE8DA !important;
    }
    body.bg-theme-linen .header-gnb,
    body.bg-theme-linen .pride-metrics-bar,
    body.bg-theme-linen .one-view-card,
    body.bg-theme-linen .featured-card,
    body.bg-theme-linen .fit-finder-banner {
      background-color: #F8F4EC !important;
      border-color: #D8CEBC !important;
    }

    /* 3. 🧈 버터밀크 & 바닐라 (Cozy Buttermilk & Warm Vanilla) - 화사하고 달콤한 아침 햇살 */
    body.bg-theme-butter,
    body.bg-theme-butter .hero-section,
    body.bg-theme-butter .journey-section,
    body.bg-theme-butter .proof-section,
    body.bg-theme-butter #page-shop,
    body.bg-theme-butter #page-story {
      background-color: #F9F3DC !important;
    }
    body.bg-theme-butter .header-gnb,
    body.bg-theme-butter .pride-metrics-bar,
    body.bg-theme-butter .one-view-card,
    body.bg-theme-butter .featured-card,
    body.bg-theme-butter .fit-finder-banner {
      background-color: #FFFFFF !important;
      border-color: #E4D9B8 !important;
    }

    /* 4. 🍵 세이지 틴트 린넨 (Calm Sage-Tinted Linen) - 따뜻한 찻잔과 숲속 휴식 */
    body.bg-theme-sage-tint,
    body.bg-theme-sage-tint .hero-section,
    body.bg-theme-sage-tint .journey-section,
    body.bg-theme-sage-tint .proof-section,
    body.bg-theme-sage-tint #page-shop,
    body.bg-theme-sage-tint #page-story {
      background-color: #E7EFE3 !important;
    }
    body.bg-theme-sage-tint .header-gnb,
    body.bg-theme-sage-tint .pride-metrics-bar,
    body.bg-theme-sage-tint .one-view-card,
    body.bg-theme-sage-tint .featured-card,
    body.bg-theme-sage-tint .fit-finder-banner {
      background-color: #F4F8F1 !important;
      border-color: #C8D8C2 !important;
    }

    /* 5. 🍑 피치 파우더 베이지 (Soft Peach & Dusty Clay) - 살결 같은 다정한 온기 */
    body.bg-theme-peach,
    body.bg-theme-peach .hero-section,
    body.bg-theme-peach .journey-section,
    body.bg-theme-peach .proof-section,
    body.bg-theme-peach #page-shop,
    body.bg-theme-peach #page-story {
      background-color: #F7EBE1 !important;
    }
    body.bg-theme-peach .header-gnb,
    body.bg-theme-peach .pride-metrics-bar,
    body.bg-theme-peach .one-view-card,
    body.bg-theme-peach .featured-card,
    body.bg-theme-peach .fit-finder-banner {
      background-color: #FDF7F2 !important;
      border-color: #E8D2C2 !important;
    }

    /* 6. 🏛️ 어반 웜 그레이지 (Warm Urban Taupe & Greige) - 이솝 플래그십 스파 감성 */
    body.bg-theme-greige,
    body.bg-theme-greige .hero-section,
    body.bg-theme-greige .journey-section,
    body.bg-theme-greige .proof-section,
    body.bg-theme-greige #page-shop,
    body.bg-theme-greige #page-story {
      background-color: #E8E3DC !important;
    }
    body.bg-theme-greige .header-gnb,
    body.bg-theme-greige .pride-metrics-bar,
    body.bg-theme-greige .one-view-card,
    body.bg-theme-greige .featured-card,
    body.bg-theme-greige .fit-finder-banner {
      background-color: #F4F0EB !important;
      border-color: #CBC4B8 !important;
    }
"""

# 본문 상단 인터랙티브 큰 카드 배너
hero_bg_card = """
        <!-- [본문 상단: 6대 메인 전체 배경색 실시간 선택 배너] -->
        <div style="background:var(--bg-surface); border:2px solid var(--color-border); border-radius:var(--radius-lg); padding:22px 26px; margin:0 auto 36px; max-width:980px; box-shadow:var(--shadow-md); text-align:center;">
          <div style="display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:14px;">
            <span style="font-size:20px;">🏡</span>
            <span style="font-family:var(--font-gowun), serif; font-size:16.5px; font-weight:800; color:var(--color-text-primary);">웹사이트의 전체 배경색을 골라보세요! 아래 버튼을 누르면 전체 공간이 즉시 변합니다.</span>
          </div>
          <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">
            <button class="btn-hero-bg active" data-bg="bg-theme-ivory" onclick="applyBgThemeDirect('bg-theme-ivory')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:2px solid #D9531E; background:#FAF7F2; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🥛 1. 밀크티 아이보리 (기본)
            </button>
            <button class="btn-hero-bg" data-bg="bg-theme-linen" onclick="applyBgThemeDirect('bg-theme-linen')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1.5px solid var(--color-border); background:#EFE8DA; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🌾 2. 웜 린넨 & 오트밀
            </button>
            <button class="btn-hero-bg" data-bg="bg-theme-butter" onclick="applyBgThemeDirect('bg-theme-butter')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1.5px solid var(--color-border); background:#F9F3DC; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🧈 3. 버터밀크 & 바닐라
            </button>
            <button class="btn-hero-bg" data-bg="bg-theme-sage-tint" onclick="applyBgThemeDirect('bg-theme-sage-tint')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1.5px solid var(--color-border); background:#E7EFE3; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🍵 4. 세이지 틴트 린넨
            </button>
            <button class="btn-hero-bg" data-bg="bg-theme-peach" onclick="applyBgThemeDirect('bg-theme-peach')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1.5px solid var(--color-border); background:#F7EBE1; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🍑 5. 피치 파우더 베이지
            </button>
            <button class="btn-hero-bg" data-bg="bg-theme-greige" onclick="applyBgThemeDirect('bg-theme-greige')" style="padding:10px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1.5px solid var(--color-border); background:#E8E3DC; color:#1F1D1A; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              🏛️ 6. 어반 웜 그레이지
            </button>
          </div>
        </div>
"""

# 완전 안전한 전역 JS 함수
reliable_js = """  <script>
    function applyBgThemeDirect(bgClass) {
      console.log('Applying Background Theme:', bgClass);
      document.body.className = document.body.className.replace(/\\bbg-theme-\\S+/g, '').trim();
      document.body.classList.add(bgClass);
      
      // 상단 및 본문 버튼 스타일 업데이트
      document.querySelectorAll('.btn-bg-selector, .btn-hero-bg').forEach(function(b) {
        if (b.getAttribute('data-bg') === bgClass) {
          b.style.borderColor = '#D9531E';
          b.style.borderWidth = '2px';
          b.style.fontWeight = '900';
          b.classList.add('active');
        } else {
          b.style.borderColor = 'rgba(0,0,0,0.15)';
          b.style.borderWidth = '1.5px';
          b.style.fontWeight = '700';
          b.classList.remove('active');
        }
      });
    }
    window.switchBgTheme = applyBgThemeDirect;
    window.applyBgThemeDirect = applyBgThemeDirect;
  </script>
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. <head> 안에 완전 안전한 JS 함수 주입
    content = re.sub(r'<script>\s*window\.switchBgTheme\s*=.*?</script>', '', content, flags=re.DOTALL)
    content = content.replace("</head>", reliable_js + "\n</head>")

    # 2. CSS 주입
    if "/* [6대 감성 메인 전체 배경색 테마 시스템" not in content:
        content = content.replace("</style>", distinct_bg_css + "\n  </style>")

    # 3. 본문 상단 히어로에 큰 선택 배너 주입
    if '<section class="hero-section">\n      <div class="container">' in content and "웹사이트의 전체 배경색을 골라보세요!" not in content:
        content = content.replace(
            '<section class="hero-section">\n      <div class="container">',
            '<section class="hero-section">\n      <div class="container">\n' + hero_bg_card
        )

    # 4. 상단 툴바의 onclick을 applyBgThemeDirect로 확실하게 교체
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-ivory', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-ivory')\""
    )
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-linen', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-linen')\""
    )
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-butter', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-butter')\""
    )
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-sage-tint', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-sage-tint')\""
    )
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-peach', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-peach')\""
    )
    content = content.replace(
        "onclick=\"window.switchBgTheme('bg-theme-greige', this)\"",
        "onclick=\"applyBgThemeDirect('bg-theme-greige')\""
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed click & enhanced background theme switcher in {path}")
