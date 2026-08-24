# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

# 4개 버튼 감성 지그재그(Zigzag Staggered) 레이아웃 CSS
zigzag_checker_css = """
    /* [7번 자가진단 위젯: 4개 버튼 감성 조약돌 지그재그 나열 시스템] */
    .checker-chip-grid {
      display: grid !important;
      grid-template-columns: repeat(2, minmax(280px, 1fr)) !important;
      gap: 18px 32px !important;
      max-width: 780px !important;
      margin: 28px auto 42px !important;
      padding: 10px 16px 20px !important;
    }
    .checker-chip {
      width: 100% !important;
      text-align: center !important;
      padding: 13px 22px !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 9999px !important;
      color: #4A433E !important;
      cursor: pointer !important;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
      font-family: var(--font-gowun), serif !important;
      box-shadow: 0 2px 8px rgba(74, 67, 62, 0.03) !important;
    }
    /* 지그재그 오프셋 효과 */
    .checker-chip:nth-child(1) { transform: translateY(0px); }
    .checker-chip:nth-child(2) { transform: translateY(16px); }
    .checker-chip:nth-child(3) { transform: translateY(4px); }
    .checker-chip:nth-child(4) { transform: translateY(20px); }

    .checker-chip:hover {
      border-color: #E5A99B !important;
      background: #FDFBF7 !important;
      box-shadow: 0 6px 16px rgba(229, 169, 155, 0.25) !important;
    }
    .checker-chip:nth-child(1):hover { transform: translateY(-3px) scale(1.02); }
    .checker-chip:nth-child(2):hover { transform: translateY(13px) scale(1.02); }
    .checker-chip:nth-child(3):hover { transform: translateY(1px) scale(1.02); }
    .checker-chip:nth-child(4):hover { transform: translateY(17px) scale(1.02); }

    .checker-chip.active {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      border-color: #E5A99B !important;
      box-shadow: 0 6px 18px rgba(229, 169, 155, 0.4) !important;
    }

    @media (max-width: 640px) {
      .checker-chip-grid {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }
      .checker-chip:nth-child(odd),
      .checker-chip:nth-child(even) {
        transform: translateY(0) !important;
      }
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 주입
    if "/* [7번 자가진단 위젯: 4개 버튼 감성 조약돌 지그재그" not in content:
        content = content.replace("</style>", zigzag_checker_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied Zigzag Checker Chips in {path}")
