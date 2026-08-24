# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 1번 [이솝 · 사담재 1px 미세선] 확정 CSS
fixed_style_1_css = """
    /* ==========================================================================
       [확정 디자인 시스템: 이솝 · 사담재 1px 미세선 (Editorial Hairline Accent)]
       1. 박스 제로(Zero-Box)의 극도로 정갈하고 차분한 갤러리/에디토리얼 무드
       2. 고운바탕(Gowun Batang) 한글 감성 서체 + 1px 웜 테라코타 미세 가로 확장선
       3. 눈의 피로를 덜어주는 웜 어스톤(아이보리/샌드) 베이스 & 은은한 앰버 하이라이트
       ========================================================================== */
    .section-tag,
    .hero-eyebrow,
    .catalog-tag,
    .journey-tag {
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      font-family: 'Gowun Batang', 'Noto Serif KR', serif !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      color: var(--color-terracotta) !important;
      letter-spacing: -0.01em !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 12px !important;
      margin-bottom: 16px !important;
      padding: 0 !important;
      box-shadow: none !important;
    }
    .section-tag::before,
    .hero-eyebrow::before,
    .catalog-tag::before,
    .journey-tag::before {
      content: '' !important;
      display: inline-block !important;
      width: 36px !important;
      height: 1px !important;
      background: var(--color-terracotta) !important;
      opacity: 0.65 !important;
    }
    .section-tag::after,
    .hero-eyebrow::after {
      content: '' !important;
      display: inline-block !important;
      width: 36px !important;
      height: 1px !important;
      background: var(--color-terracotta) !important;
      opacity: 0.65 !important;
    }
    .hero-eyebrow {
      font-size: 15px !important;
      margin-bottom: 20px !important;
    }
    .section-title {
      font-family: 'Gowun Batang', 'Noto Serif KR', serif !important;
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
    .text-highlight {
      background: linear-gradient(180deg, transparent 65%, rgba(217, 83, 30, 0.16) 65%) !important;
      padding: 0 4px !important;
      border-radius: 3px !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 임시 배너 및 툴바 제거 (깨끗한 원본 완성형 룩)
    # 5대 테마 선택 툴바 제거
    content = re.sub(
        r'<!-- 5대 감성 강조 스타일 실시간 비교 선택 툴바 -->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    # 본문 상단 임시 체험 배너 제거
    content = re.sub(
        r'<!-- \[실시간 5대 감성 강조 스타일 체험 배너\] -->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. padding-top을 원래 깔끔한 높이(117px)로 복원
    content = re.sub(r'padding-top:\s*\d+px;', 'padding-top: 117px;', content, count=1)

    # 3. body 태그 기본형 복원
    content = content.replace('<body class="theme-style-1">', '<body>')

    # 4. 확정 스타일 CSS 주입
    if "/* ==========================================================================\n       [확정 디자인 시스템: 이솝 · 사담재 1px 미세선" not in content:
        # 기존 테마 CSS 교체
        content = re.sub(
            r'/\* ==========================================================================\s*\[5대 감성 강조 스타일 테마 시스템\].*?</style>',
            fixed_style_1_css + "\n  </style>",
            content,
            flags=re.DOTALL
        )

    # 5. 불필요해진 임시 switchThemeStyle 함수 제거
    content = re.sub(r'function switchThemeStyle\(.*?\n    \}', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// 전역 즉시 실행 테마 전환 함수.*?</script>', '', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Finalized Style 1 (Aesop Hairline) in {path}")
