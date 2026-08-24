# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

new_btn_css = """    /* ==========================================================================
       [버튼 시스템 고도화 - 칙칙한 검정 & 각진 사각 테두리 배제]
       밝고 따뜻한 웜 테라코타 오렌지 / 소프트 아이보리 & 조약돌 둥근 버튼(Pill Radius)
       ========================================================================== */
    .btn-primary {
      background: #D9531E !important;
      color: #ffffff !important;
      border: 1.5px solid #D9531E !important;
      border-radius: var(--radius-full) !important;
      padding: 13px 26px !important;
      font-size: 14.5px !important;
      font-weight: 700 !important;
      letter-spacing: -0.01em !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 8px !important;
      cursor: pointer !important;
      box-shadow: 0 4px 14px rgba(217, 83, 30, 0.22) !important;
      transition: all 0.25s ease !important;
      text-decoration: none !important;
    }
    .btn-primary:hover {
      background: #E05A24 !important;
      border-color: #E05A24 !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 6px 18px rgba(217, 83, 30, 0.32) !important;
      color: #ffffff !important;
    }

    .btn-secondary {
      background: #ffffff !important;
      color: #D9531E !important;
      border: 1.5px solid #D9531E !important;
      border-radius: var(--radius-full) !important;
      padding: 13px 26px !important;
      font-size: 14.5px !important;
      font-weight: 700 !important;
      letter-spacing: -0.01em !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 8px !important;
      cursor: pointer !important;
      box-shadow: 0 2px 10px rgba(217, 83, 30, 0.08) !important;
      transition: all 0.25s ease !important;
      text-decoration: none !important;
    }
    .btn-secondary:hover {
      background: #FFF5F0 !important;
      color: #E05A24 !important;
      border-color: #E05A24 !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 4px 14px rgba(217, 83, 30, 0.18) !important;
    }

    .btn-accent, .btn-primary.btn-accent {
      background: #D9531E !important;
      color: #ffffff !important;
      border: 1.5px solid #D9531E !important;
      border-radius: var(--radius-full) !important;
      box-shadow: 0 4px 14px rgba(217, 83, 30, 0.25) !important;
    }
    .btn-accent:hover, .btn-primary.btn-accent:hover {
      background: #E05A24 !important;
      border-color: #E05A24 !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 6px 20px rgba(217, 83, 30, 0.35) !important;
    }

    .btn-sm-ghost {
      background: #ffffff !important;
      color: var(--color-text-primary) !important;
      border: 1px solid var(--color-border) !important;
      border-radius: var(--radius-full) !important;
      padding: 8px 18px !important;
      font-size: 13px !important;
      font-weight: 600 !important;
      transition: all 0.2s ease !important;
    }
    .btn-sm-ghost:hover {
      background: var(--bg-surface) !important;
      border-color: #D9531E !important;
      color: #D9531E !important;
    }

    .gnb-text-btn {
      padding: 7px 14px !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      color: var(--color-text-primary) !important;
      background: #ffffff !important;
      border: 1px solid var(--color-border) !important;
      border-radius: var(--radius-full) !important;
      cursor: pointer !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      transition: all 0.2s ease !important;
    }
    .gnb-text-btn:hover {
      background: #FFF5F0 !important;
      border-color: #D9531E !important;
      color: #D9531E !important;
    }
    .gnb-text-btn .btn-badge {
      background: #D9531E !important;
      color: #ffffff !important;
      font-size: 11px !important;
      padding: 1px 7px !important;
      border-radius: 9999px !important;
      font-weight: 800 !important;
    }

    .btn-card-wish-text {
      padding: 4px 10px !important;
      font-size: 11.5px !important;
      font-weight: 700 !important;
      background: #ffffff !important;
      border: 1px solid var(--color-border) !important;
      border-radius: var(--radius-full) !important;
      color: var(--color-text-secondary) !important;
      cursor: pointer !important;
      transition: all 0.2s ease !important;
    }
    .btn-card-wish-text.active {
      background: #FFF5F0 !important;
      color: #D9531E !important;
      border-color: #D9531E !important;
    }"""

# 히어로 CTA 마크업 개선
hero_cta_old = """        <div class="hero-cta-group">
          <button class="btn-primary" onclick="scrollToSection('sec-journey')">스밈의 시작 알아보기 [바로가기]</button>
          <button class="btn-secondary" onclick="scrollToSection('sec-featured')">스밈 3대 대표작 알아보기 </button>
        </div>"""

hero_cta_new = """        <div class="hero-cta-group" style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap; margin:28px 0 36px;">
          <button class="btn-primary" onclick="scrollToSection('sec-journey')">
            스밈의 시작 알아보기 ➔
          </button>
          <button class="btn-secondary" onclick="scrollToSection('sec-featured')">
            스밈 3대 대표작 알아보기 ➔
          </button>
        </div>"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 칙칙한 검정 사각 버튼 CSS 교체
    old_btn_block_pattern = r'\.btn-primary\s*\{[^}]*?background:\s*#212529[^}]*?\}.*?\.btn-sm-ghost\s*\{[^}]*?\}'
    if re.search(old_btn_block_pattern, content, flags=re.DOTALL):
        content = re.sub(old_btn_block_pattern, new_btn_css, content, flags=re.DOTALL)
    else:
        # 안전한 교체
        content = content.replace(
            ".btn-primary {\n      background: #212529 !important;",
            new_btn_css + "\n    /* old replaced */\n    .btn-primary-old {"
        )

    # 2. 히어로 CTA 마크업 갱신
    if "스밈의 시작 알아보기 [바로가기]" in content:
        content = content.replace(hero_cta_old, hero_cta_new)
        content = content.replace(
            '<button class="btn-secondary" onclick="scrollToSection(\'sec-featured\')">스밈 3대 대표작 알아보기 </button>',
            '<button class="btn-secondary" onclick="scrollToSection(\'sec-featured\')">스밈 3대 대표작 알아보기 ➔</button>'
        )

    # 3. 3대 대표작 섹션 및 기타 섹션의 버튼 스타일도 조약돌 둥근 버튼으로 점검
    content = content.replace(
        '<button class="btn-primary" onclick="openQuickView(1)">3D 단면 분해도 보기</button>',
        '<button class="btn-secondary" style="padding:10px 18px; font-size:13px;" onclick="openQuickView(1)">🔍 3D 단면 분해도 보기</button>'
    )
    content = content.replace(
        '<button class="btn-primary" onclick="openQuickView(2)">3D 단면 분해도 보기</button>',
        '<button class="btn-secondary" style="padding:10px 18px; font-size:13px;" onclick="openQuickView(2)">🔍 3D 단면 분해도 보기</button>'
    )
    content = content.replace(
        '<button class="btn-primary" onclick="openQuickView(3)">3D 단면 분해도 보기</button>',
        '<button class="btn-secondary" style="padding:10px 18px; font-size:13px;" onclick="openQuickView(3)">🔍 3D 단면 분해도 보기</button>'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Refined button colors and shapes in {path}")
