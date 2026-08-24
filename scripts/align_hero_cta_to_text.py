# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

hero_align_css = """
    /* [히어로 텍스트 수직 시작선 완벽 일치 정렬 (Left-align Axis)] */
    .hero-content-left {
      text-align: left !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: flex-start !important;
    }
    .hero-content-left .hero-eyebrow {
      justify-content: flex-start !important;
      margin: 0 0 16px 0 !important;
      padding: 0 !important;
      text-align: left !important;
    }
    .hero-manifesto-title {
      text-align: left !important;
      margin: 0 0 18px 0 !important;
      padding: 0 !important;
    }
    .hero-subcopy {
      text-align: left !important;
      margin: 0 0 32px 0 !important;
      padding: 0 !important;
    }
    .hero-cta-group {
      display: flex !important;
      justify-content: flex-start !important;
      align-items: center !important;
      gap: 14px !important;
      margin: 0 !important;
      padding: 0 !important;
      width: 100% !important;
    }
    .hero-cta-group .btn-primary {
      margin-left: 0 !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 추가
    if "/* [히어로 텍스트 수직 시작선 완벽 일치 정렬" not in content:
        content = content.replace("</style>", hero_align_css + "\n  </style>")
    else:
        content = re.sub(r'/\* \[히어로 텍스트 수직 시작선 완벽 일치 정렬.*?\*/.*?}\n', hero_align_css, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated Hero Alignment in {path}")
