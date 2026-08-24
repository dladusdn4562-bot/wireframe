# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Google Fonts에 Gowun Batang(고운바탕) 및 Gowun Dodum(고운돋움) 추가 (딱딱함 100% 제거)
    old_fonts = '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Noto+Serif+KR:wght@300;400;500;600;700;900&family=Pretendard:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
    new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gowun+Dodum&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Noto+Serif+KR:wght@300;400;500;600;700;900&family=Pretendard:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
    
    if old_fonts in content:
        content = content.replace(old_fonts, new_fonts)

    # 2. CSS 토큰의 기본 서체를 고운바탕(Gowun Batang)으로 업그레이드
    content = content.replace(
        "--font-serif: 'Noto Serif KR', 'Batang', serif;",
        "--font-serif: 'Gowun Batang', 'Noto Serif KR', serif;\n      --font-gowun: 'Gowun Batang', serif;\n      --font-gowun-dodum: 'Gowun Dodum', sans-serif;"
    )
    content = content.replace(
        "--font-maruburi: 'Noto Serif KR', serif;",
        "--font-maruburi: 'Gowun Batang', 'Noto Serif KR', serif;"
    )

    # 3. 섹션 태그 및 안내 라벨 CSS 전면 고도화:
    # 폰트 색상뿐만 아니라 [소프트 앰버 틴트 캡슐 + 1px 블러 보더 + 펄스 도트 + 웜 글로우]로 확실한 전경 강조
    old_tag_css = """/* [섹션 안내 문구 - 답답한 사각 박스를 걷어내고 부드러운 한글 감성 라벨 & 포인트 색상 적용] */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: var(--font-serif) !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      color: var(--color-terracotta) !important;
      letter-spacing: -0.02em !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      margin-bottom: 12px !important;
      padding: 0 !important;
    }
    .section-tag::before, .hero-eyebrow::before, .catalog-tag::before, .journey-tag::before {
      content: '●' !important;
      font-size: 7px !important;
      color: var(--color-terracotta) !important;
      vertical-align: middle !important;
    }
    .hero-eyebrow {
      font-size: 15px !important;
      color: var(--color-terracotta) !important;
      margin-bottom: 16px !important;
    }"""

    new_tag_css = """/* [섹션 안내 문구 - 고운바탕 서체 + 소프트 앰버 글로우 캡슐로 압도적 시각 강조] */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      background: rgba(217, 83, 30, 0.08) !important;
      border: 1px solid rgba(217, 83, 30, 0.25) !important;
      border-radius: var(--radius-full) !important;
      font-family: var(--font-gowun), 'Noto Serif KR', serif !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      color: #B84314 !important;
      letter-spacing: -0.02em !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      margin-bottom: 16px !important;
      padding: 5px 16px !important;
      box-shadow: 0 2px 10px rgba(217, 83, 30, 0.08) !important;
      transition: var(--transition) !important;
    }
    .section-tag:hover, .hero-eyebrow:hover {
      background: rgba(217, 83, 30, 0.14) !important;
      border-color: rgba(217, 83, 30, 0.45) !important;
      transform: translateY(-1px) !important;
    }
    .section-tag::before, .hero-eyebrow::before, .catalog-tag::before, .journey-tag::before {
      content: '' !important;
      width: 7px !important;
      height: 7px !important;
      background: #D9531E !important;
      border-radius: 50% !important;
      display: inline-block !important;
      box-shadow: 0 0 8px rgba(217, 83, 30, 0.8) !important;
    }
    .hero-eyebrow {
      font-size: 14.5px !important;
      padding: 7px 20px !important;
      margin-bottom: 22px !important;
    }
    
    /* 세이지 그린 계열 캡슐 태그 */
    .section-tag-sage {
      background: rgba(47, 133, 90, 0.09) !important;
      border-color: rgba(47, 133, 90, 0.28) !important;
      color: #236946 !important;
      box-shadow: 0 2px 10px rgba(47, 133, 90, 0.08) !important;
    }
    .section-tag-sage::before {
      background: #2F855A !important;
      box-shadow: 0 0 8px rgba(47, 133, 90, 0.8) !important;
    }

    /* 텍스트 하이라이트 & 타이포그래피 강조 */
    .text-highlight {
      background: linear-gradient(180deg, transparent 60%, rgba(217, 83, 30, 0.16) 60%) !important;
      padding: 0 6px !important;
      border-radius: 4px !important;
      color: #1F1D1A !important;
      font-weight: 800 !important;
    }
    .journey-tag {
      background: #FAF3EC !important;
      border: 1px solid rgba(217, 83, 30, 0.2) !important;
      color: #B84314 !important;
      padding: 4px 14px !important;
    }"""

    if old_tag_css in content:
        content = content.replace(old_tag_css, new_tag_css)

    # 4. 헤드라인 및 타이틀 스타일 고도화 (고운바탕 서체 적용)
    content = content.replace(
        "font-family: var(--font-serif) !important;",
        "font-family: 'Gowun Batang', 'Noto Serif KR', serif !important;"
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Refined typography and visual cues in {path}")
