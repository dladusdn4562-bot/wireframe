# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 개선: 딱딱한 박스 제거, 부드러운 서정적 한글 라벨 및 포인트 색상 강화
    css_old_tags = """.section-tag, .hero-eyebrow, .story92-pillar-badge, .catalog-tag, .journey-tag {
      background: #f1f3f5 !important;
      color: #495057 !important;
      border: 1px solid #ced4da !important;
      border-radius: 4px !important;
    }"""
    
    css_new_tags = """/* [섹션 안내 문구 - 답답한 사각 박스를 걷어내고 부드러운 한글 감성 라벨 & 포인트 색상 적용] */
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
    }
    .section-title {
      font-family: var(--font-serif) !important;
      font-size: clamp(28px, 3.5vw, 38px) !important;
      font-weight: 800 !important;
      line-height: 1.35 !important;
      color: var(--color-text-primary) !important;
      letter-spacing: -0.03em !important;
      margin-bottom: 12px !important;
    }
    .section-desc {
      font-family: var(--font-sans) !important;
      font-size: 16px !important;
      color: var(--color-text-secondary) !important;
      line-height: 1.8 !important;
      word-break: keep-all !important;
    }
    .journey-highlight {
      background: rgba(217, 83, 30, 0.05) !important;
      border-left: 3px solid var(--color-terracotta) !important;
      border-top: none !important;
      border-right: none !important;
      border-bottom: none !important;
      padding: 16px 22px !important;
      border-radius: 0 14px 14px 0 !important;
      font-family: var(--font-serif) !important;
      font-size: 14.5px !important;
      color: var(--color-text-primary) !important;
      line-height: 1.8 !important;
    }"""
    
    if css_old_tags in content:
        content = content.replace(css_old_tags, css_new_tags)

    # 2. Section Tag 영문 문구 -> 친절하고 감성적인 한글로 전면 수정
    replacements = [
        # 메인 히어로
        ("EFFORTLESS WELLNESS · 0.1mm SEAMLESS TECH", "일상에 자연스럽게 스며드는 0.1mm 바른 균형"),
        ("OUR PHILOSOPHY &amp; JOURNEY", "스밈의 철학 · 우리가 걸어온 길"),
        ("OUR PHILOSOPHY & JOURNEY", "스밈의 철학 · 우리가 걸어온 길"),
        ("FEATURED MASTERPIECES TOP 3", "스밈 대표 시그니처 3선"),
        ("CLINICAL &amp; SOCIAL PROOF", "300인의 전문가 실착 검증 &amp; 임상 데이터"),
        ("CLINICAL & SOCIAL PROOF", "300인의 전문가 실착 검증 & 임상 데이터"),
        ("FULL COLLECTION (15 PRODUCTS)", "15종 부위별 맞춤 전 컬렉션"),
        ("SMART FIT FINDER", "1초 체형 맞춤 사이즈 파인더"),
        ("AI REALTIME HUD", "실시간 스마트 자세 케어"),
        ("O2O WELLNESS CENTER", "전국 오프라인 웰니스 센터"),
        ("FREQUENTLY ASKED QUESTIONS", "자주 묻는 질문 &amp; 안심 케어"),
        ("SHOP ALL / 15 PRODUCTS CATALOG", "스밈 15종 전 상품 맞춤 컬렉션"),
        ("[BRAND MANIFESTO] 0.1mm Seamless · 스며드는 다정한 균형", "[브랜드 선언] 일상에 자연스럽게 스며드는 바른 균형"),
        ("WHY SEUMIM &amp; BRAND ORIGIN", "스밈의 어원과 탄생 이야기"),
        ("WHY SEUMIM & BRAND ORIGIN", "스밈의 어원과 탄생 이야기"),
        ("3D TECHNICAL BLUEPRINT", "3D 인체공학 입체 설계도"),
        ("FILTERABLE USE CASES", "일상 속 착용 전·후 실루엣 변화"),
        ("COLLECTION SHOWCASE", "3대 부위별 맞춤 쇼케이스"),
        ("CHAPTER 01 · 탄생의 배경", "첫 번째 이야기 · 탄생의 배경"),
        ("CHAPTER 02 · 기존 시장의 한계 극복", "두 번째 이야기 · 기존 시장의 한계 극복"),
        ("CHAPTER 03 · 브랜드 철학과 가치", "세 번째 이야기 · 스밈의 철학과 약속"),
        ("PHOTO PLACEHOLDER 01", "실사 화보 01 · 일상의 편안함"),
        ("PHOTO PLACEHOLDER 02", "실사 화보 02 · 0.1mm의 혁신"),
        ("PHOTO PLACEHOLDER 03", "실사 화보 03 · 300인의 검증"),
    ]

    for old_str, new_str in replacements:
        content = content.replace(old_str, new_str)

    # 3. 박스 최소화: 무거운 테두리와 배경 박스를 걷어내고 여백과 포인트 라인으로 전환
    # hero-manifesto-title 스타일 강화
    content = re.sub(
        r'(\.hero-manifesto-title\s*\{[^}]*?\})',
        r'''.hero-manifesto-title {
      font-family: var(--font-serif);
      font-size: clamp(34px, 4.5vw, 50px);
      font-weight: 800;
      line-height: 1.32;
      color: var(--color-text-primary);
      max-width: 880px;
      margin: 0 auto 20px;
      letter-spacing: -0.03em;
    }
    .hero-manifesto-title span {
      color: var(--color-terracotta);
      font-weight: 900;
      background: linear-gradient(180deg, transparent 70%, rgba(217, 83, 30, 0.15) 70%);
      padding: 0 4px;
      text-decoration: none !important;
    }''',
        content,
        count=1
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully refined {path}")
