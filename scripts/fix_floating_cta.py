# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

btn_fix_css = """
    /* 플로팅 바 & 모든 CTA 완전 동기화 */
    .floating-bottom-bar .btn-accent,
    .floating-bottom-bar button,
    .gnb-actions .btn-primary,
    .hero-cta-group .btn-primary,
    .one-view-btn-primary {
      background: #E5A99B !important;
      border-color: #E5A99B !important;
      color: #FFFFFF !important;
    }
    .floating-bottom-bar .btn-accent:hover,
    .gnb-actions .btn-primary:hover,
    .hero-cta-group .btn-primary:hover {
      background: #D49586 !important;
      border-color: #D49586 !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "/* 플로팅 바 & 모든 CTA 완전 동기화 */" not in content:
        content = content.replace("</style>", btn_fix_css + "\n  </style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed floating CTA button color in {path}")
