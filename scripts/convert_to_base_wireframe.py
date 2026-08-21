# -*- coding: utf-8 -*-
"""
Perfect cleanup of all SVG tags and Unicode Emojis from '기본 와이어프레임.html'
"""

import re

target_path = r"C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html"

with open(target_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace any remaining <button class="btn-card-wish...">...<svg>...</svg></button>
text = re.sub(
    r'<button\s+class="btn-card-wish(?:\s+active)?"[^>]*>.*?<svg.*?</svg>\s*</button>',
    lambda m: '<button class="btn-card-wish-text active" title="찜하기">[찜됨]</button>' if 'active' in m.group(0) else '<button class="btn-card-wish-text" title="찜하기">[찜하기]</button>',
    text,
    flags=re.DOTALL
)

# 2. Replace any SVG inside product rendering JavaScript templates
text = re.sub(
    r'<button\s+class="btn-card-wish.*?</button>',
    r'<button class="btn-card-wish-text ${p.isWished ? \'active\' : \'\'}" onclick="toggleWish(${p.id}, this)">${p.isWished ? \'[찜됨]\' : \'[찜하기]\'}</button>',
    text,
    flags=re.DOTALL
)

# 3. Replace all remaining <svg ... </svg> with descriptive text placeholders
def replace_svg(match):
    s = match.group(0)
    if 'viewBox="0 0 160 100"' in s:
        return '<div class="wf-placeholder" style="width:140px; height:80px; font-size:12px; font-weight:700;">[모션 도해 다이어그램]</div>'
    elif 'viewBox="0 0 240 120"' in s:
        return '<div class="wf-placeholder" style="width:100%; height:120px; font-size:12px; font-weight:700;">[3D CAD 분해도 다이어그램]</div>'
    elif 'nav-icon-svg' in s:
        return ''
    else:
        return '<span style="font-size:11px; font-weight:700; color:#495057;">[도해]</span>'

text = re.sub(r'<svg.*?</svg>', replace_svg, text, flags=re.DOTALL)

# 4. Remove all Unicode Emojis
text = re.sub(r'[\U00010000-\U0010ffff]', '', text)

# 5. Remove miscellaneous symbols
symbols = ['✦', '★', '☆', '🔍', '🛒', '🤍', '❤️', '⏱', '🛡', '💡', '✨', '🩺', '💻', '✈', '🏷', '⬇', '➔', '✓', '▲', '▼']
for s in symbols:
    text = text.replace(s, '')

# 6. Clean productsData icons: 'icon: ...' -> 'icon: ""'
text = re.sub(r"icon:\s*['\"][^'\"]*['\"]", "icon: ''", text)

# 7. Clean visual-3d-icon if exists
text = re.sub(r'<div class="visual-3d-icon">.*?</div>', '', text)

# Save
with open(target_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Final cleanup finished.")
