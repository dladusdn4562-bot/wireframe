# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

mobile_drawer_fix_css = """
    /* Mobile Menu Drawer 기본 닫힘 및 토글 */
    .mobile-menu-drawer {
      display: none !important;
      background: var(--bg-surface);
      border-top: 1px solid var(--color-border);
      padding: 18px 24px;
    }
    .mobile-menu-drawer.open {
      display: block !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS 추가
    if ".mobile-menu-drawer {" not in content:
        content = content.replace("</style>", mobile_drawer_fix_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed mobile menu drawer in {path}")
