# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

# 타입 2번: 부드러운 수채화 손그림 물결 곡선 (컬러 1번: 소프트 세이지 그린)
wave_sage_css = """
    /* ==========================================================================
       [타입 2번 + 컬러 1번: 부드러운 소프트 세이지 그린 손그림 물결 밑줄]
       ========================================================================== */
    .highlight-wave-sage, .highlight-peach {
      position: relative !important;
      display: inline-block !important;
      color: #4A433E !important;
      font-weight: 800 !important;
      background: none !important;
      padding: 0 4px !important;
      z-index: 2 !important;
    }
    .highlight-wave-sage::after, .highlight-peach::after {
      content: '' !important;
      position: absolute !important;
      left: -2px !important;
      right: -2px !important;
      bottom: -6px !important;
      height: 11px !important;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 18' preserveAspectRatio='none'%3E%3Cpath d='M2,9 C22,3 42,15 62,9 C82,3 102,15 118,9' fill='none' stroke='%23B4C4B1' stroke-width='5' stroke-linecap='round' opacity='0.75'/%3E%3C/svg%3E") !important;
      background-repeat: no-repeat !important;
      background-size: 100% 100% !important;
      z-index: -1 !important;
      pointer-events: none !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 추가
    if "/* [타입 2번 + 컬러 1번: 부드러운 소프트 세이지 그린" not in content:
        content = content.replace("</style>", wave_sage_css + "\n  </style>")
    else:
        content = re.sub(r'/\* =+ \n\s*\[타입 2번 \+ 컬러 1번:.*?\}\n', wave_sage_css, content, flags=re.DOTALL)

    # 마크업 클래스도 명시적으로 변경
    content = content.replace(
        '<span class="highlight-peach">다정한 균형</span>',
        '<span class="highlight-wave-sage">다정한 균형</span>'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied Wave Sage Underline in {path}")
