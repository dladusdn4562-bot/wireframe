# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 5대 테마 CSS 정의
theme_css = """
    /* ==========================================================================
       [5대 감성 강조 스타일 테마 시스템]
       사용자가 상단 툴바에서 1번~5번을 클릭하여 실시간으로 비교 체험할 수 있는 시스템
       ========================================================================== */

    /* 기본 공통 */
    body {
      transition: all 0.3s ease;
    }

    /* --------------------------------------------------------------------------
       [스타일 1: 이솝 · 사담재] 1px 미세 연장선 (Editorial Hairline Accent)
       -------------------------------------------------------------------------- */
    body.theme-style-1 .section-tag,
    body.theme-style-1 .hero-eyebrow,
    body.theme-style-1 .catalog-tag,
    body.theme-style-1 .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      color: var(--color-terracotta) !important;
      letter-spacing: -0.01em !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 12px !important;
      margin-bottom: 14px !important;
      padding: 0 !important;
      box-shadow: none !important;
    }
    body.theme-style-1 .section-tag::before,
    body.theme-style-1 .hero-eyebrow::before,
    body.theme-style-1 .catalog-tag::before,
    body.theme-style-1 .journey-tag::before {
      content: '' !important;
      display: inline-block !important;
      width: 36px !important;
      height: 1px !important;
      background: var(--color-terracotta) !important;
      opacity: 0.7 !important;
    }
    body.theme-style-1 .section-tag::after,
    body.theme-style-1 .hero-eyebrow::after {
      content: '' !important;
      display: inline-block !important;
      width: 36px !important;
      height: 1px !important;
      background: var(--color-terracotta) !important;
      opacity: 0.7 !important;
    }

    /* --------------------------------------------------------------------------
       [스타일 2: 킨포크 · 시리얼] 오버사이즈 반투명 워터마크 넘버 (Watermark Number)
       -------------------------------------------------------------------------- */
    body.theme-style-2 .section-tag,
    body.theme-style-2 .hero-eyebrow,
    body.theme-style-2 .catalog-tag,
    body.theme-style-2 .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      color: var(--color-forest) !important;
      letter-spacing: -0.01em !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      gap: 4px !important;
      margin-bottom: 16px !important;
      padding: 0 !important;
      box-shadow: none !important;
    }
    body.theme-style-2 .section-tag::before,
    body.theme-style-2 .hero-eyebrow::before,
    body.theme-style-2 .catalog-tag::before,
    body.theme-style-2 .journey-tag::before {
      content: 'SEUMIM' !important;
      font-family: var(--font-gowun), serif !important;
      font-size: 28px !important;
      font-weight: 900 !important;
      color: rgba(217, 83, 30, 0.22) !important;
      letter-spacing: 0.15em !important;
      line-height: 1 !important;
      margin-bottom: 2px !important;
    }
    body.theme-style-2 .section-title-wrap {
      text-align: center !important;
    }

    /* --------------------------------------------------------------------------
       [스타일 3: 모두의매트 · 프라마] 좌측 웜 테라코타 버티컬 바 & 2단 인덴트
       -------------------------------------------------------------------------- */
    body.theme-style-3 .section-title-wrap {
      border-left: 4px solid var(--color-terracotta) !important;
      padding-left: 20px !important;
      text-align: left !important;
      margin-bottom: 36px !important;
    }
    body.theme-style-3 .section-tag,
    body.theme-style-3 .hero-eyebrow,
    body.theme-style-3 .catalog-tag,
    body.theme-style-3 .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 13.5px !important;
      font-weight: 800 !important;
      color: var(--color-terracotta) !important;
      letter-spacing: -0.01em !important;
      display: inline-block !important;
      margin-bottom: 6px !important;
      padding: 0 !important;
      box-shadow: none !important;
    }
    body.theme-style-3 .section-tag::before,
    body.theme-style-3 .hero-eyebrow::before {
      content: none !important;
    }

    /* --------------------------------------------------------------------------
       [스타일 4: 동양적 젠(Zen)] 단아한 한글 낙관 인장 심볼 (Zen Stamp Accent)
       -------------------------------------------------------------------------- */
    body.theme-style-4 .section-tag,
    body.theme-style-4 .hero-eyebrow,
    body.theme-style-4 .catalog-tag,
    body.theme-style-4 .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 14.5px !important;
      font-weight: 700 !important;
      color: var(--color-text-primary) !important;
      letter-spacing: -0.02em !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 10px !important;
      margin-bottom: 14px !important;
      padding: 0 !important;
      box-shadow: none !important;
    }
    body.theme-style-4 .section-tag::before,
    body.theme-style-4 .hero-eyebrow::before,
    body.theme-style-4 .catalog-tag::before,
    body.theme-style-4 .journey-tag::before {
      content: '結' !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      width: 22px !important;
      height: 22px !important;
      background: var(--color-terracotta) !important;
      color: #ffffff !important;
      font-size: 12px !important;
      font-weight: 900 !important;
      border-radius: 4px !important;
      box-shadow: 0 2px 6px rgba(217, 83, 30, 0.3) !important;
    }

    /* --------------------------------------------------------------------------
       [스타일 5: 수채화 · 패브릭] 내추럴 브러시 웨이브 언더라인 (Organic Brush)
       -------------------------------------------------------------------------- */
    body.theme-style-5 .section-tag,
    body.theme-style-5 .hero-eyebrow,
    body.theme-style-5 .catalog-tag,
    body.theme-style-5 .journey-tag {
      background: linear-gradient(180deg, transparent 50%, rgba(217, 83, 30, 0.18) 50%, rgba(217, 83, 30, 0.18) 92%, transparent 92%) !important;
      border: none !important;
      border-radius: 2px !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 14.5px !important;
      font-weight: 800 !important;
      color: var(--color-text-primary) !important;
      letter-spacing: -0.01em !important;
      display: inline-block !important;
      margin-bottom: 14px !important;
      padding: 0 6px !important;
      box-shadow: none !important;
    }
    body.theme-style-5 .section-tag::before,
    body.theme-style-5 .hero-eyebrow::before {
      content: '🌿 ' !important;
      font-size: 13px !important;
    }
"""

# 스타일 선택기 HTML 툴바
selector_html = """
    <!-- 5대 감성 강조 스타일 실시간 비교 선택 툴바 -->
    <div style="background:#1B201D; color:#f0ece4; padding:8px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.12); flex-wrap:wrap; gap:10px; font-size:12.5px; z-index:1200; position:relative;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="color:#D9531E; font-weight:800; font-size:13.5px;">🎨 5대 강조 스타일 실시간 비교:</span>
        <span style="color:#c5beb3;">원하는 스타일 버튼을 클릭하여 와이어프레임의 시각적 변화를 바로 확인하세요!</span>
      </div>
      <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <button class="btn-theme-selector active" onclick="switchThemeStyle('theme-style-1', this)" style="padding:4px 11px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(217,83,30,0.85); color:#fff; cursor:pointer; font-family:'Gowun Batang', serif; font-weight:700;">
          1. 이솝 1px 미세선
        </button>
        <button class="btn-theme-selector" onclick="switchThemeStyle('theme-style-2', this)" style="padding:4px 11px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); color:#dedede; cursor:pointer; font-family:'Gowun Batang', serif; font-weight:700;">
          2. 킨포크 워터마크
        </button>
        <button class="btn-theme-selector" onclick="switchThemeStyle('theme-style-3', this)" style="padding:4px 11px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); color:#dedede; cursor:pointer; font-family:'Gowun Batang', serif; font-weight:700;">
          3. 프라마 버티컬바
        </button>
        <button class="btn-theme-selector" onclick="switchThemeStyle('theme-style-4', this)" style="padding:4px 11px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); color:#dedede; cursor:pointer; font-family:'Gowun Batang', serif; font-weight:700;">
          4. 젠(Zen) 한글낙관
        </button>
        <button class="btn-theme-selector" onclick="switchThemeStyle('theme-style-5', this)" style="padding:4px 11px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); color:#dedede; cursor:pointer; font-family:'Gowun Batang', serif; font-weight:700;">
          5. 수채화 브러시
        </button>
      </div>
    </div>
"""

# 스타일 전환 자바스크립트
selector_js = """
    function switchThemeStyle(styleClass, btn) {
      // 1. body의 모든 theme-style 클래스 제거
      document.body.classList.remove('theme-style-1', 'theme-style-2', 'theme-style-3', 'theme-style-4', 'theme-style-5');
      // 2. 선택된 스타일 클래스 추가
      document.body.classList.add(styleClass);
      
      // 3. 버튼 active 스타일 업데이트
      document.querySelectorAll('.btn-theme-selector').forEach(b => {
        b.style.background = 'rgba(255,255,255,0.1)';
        b.style.color = '#dedede';
        b.classList.remove('active');
      });
      if (btn) {
        btn.style.background = 'rgba(217,83,30,0.85)';
        btn.style.color = '#fff';
        btn.classList.add('active');
      }
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 추가
    if "</style>" in content and "/* 5대 감성 강조 스타일 테마 시스템 */" not in content:
        content = content.replace("</style>", theme_css + "\n  </style>")

    # 2. Body 기본 클래스에 theme-style-1 추가
    content = content.replace("<body>", '<body class="theme-style-1">')

    # 3. 상단 fixed header에 selector_html 추가
    if 'id="site-header-fixed">' in content and "5대 감성 강조 스타일 실시간 비교" not in content:
        content = content.replace(
            '<header class="site-header-fixed" id="site-header-fixed">',
            '<header class="site-header-fixed" id="site-header-fixed">\n' + selector_html
        )

    # 4. JS 스크립트에 switchThemeStyle 추가
    if "</script>" in content and "function switchThemeStyle" not in content:
        content = content.replace("</script>", selector_js + "\n  </script>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied 5-theme live switcher to {path}")
