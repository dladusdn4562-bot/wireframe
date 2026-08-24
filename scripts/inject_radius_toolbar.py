# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

radius_toolbar_html = """  <!-- 3대 상자 둥글기 실시간 비교 선택 툴바 -->
  <div style="background:#36302B; color:#FDFBF7; padding:9px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.15); flex-wrap:wrap; gap:10px; font-size:12.5px; z-index:1200; position:relative;">
    <div style="display:flex; align-items:center; gap:8px;">
      <span style="color:#E5A99B; font-weight:800; font-size:13.5px;">🔘 3대 상자 둥글기 실시간 체험:</span>
      <span style="color:#D8CEC4;">원하는 스타일 버튼을 클릭하여 웹사이트 내 카드와 상자들의 둥글기 변화를 바로 확인하세요!</span>
    </div>
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <button class="btn-radius-selector active" data-radius="radius-theme-pebble" onclick="applyRadiusThemeDirect('radius-theme-pebble')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:2px solid #E5A99B; background:#FDFBF7; color:#4A433E; cursor:pointer; font-weight:800; font-family:'Gowun Batang', serif;">
        🌿 1. 유기적 조약돌 (비례 16~36px)
      </button>
      <button class="btn-radius-selector" data-radius="radius-theme-asymm" onclick="applyRadiusThemeDirect('radius-theme-asymm')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.3); background:rgba(255,255,255,0.1); color:#FDFBF7; cursor:pointer; font-weight:700; font-family:'Gowun Batang', serif;">
        🏛️ 2. 비대칭 아치 (꽃잎/아치 곡선)
      </button>
      <button class="btn-radius-selector" data-radius="radius-theme-editorial" onclick="applyRadiusThemeDirect('radius-theme-editorial')" style="padding:6px 14px; font-size:12px; border-radius:9999px; border:1px solid rgba(255,255,255,0.3); background:rgba(255,255,255,0.1); color:#FDFBF7; cursor:pointer; font-weight:700; font-family:'Gowun Batang', serif;">
        ☕ 3. 킨포크 에디토리얼 (서사 12px vs 배너 38px)
      </button>
    </div>
  </div>
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 툴바 주입
    if "<!-- 3대 상자 둥글기 실시간 비교 선택 툴바 -->" not in content:
        content = content.replace(
            '<header class="site-header-fixed"',
            radius_toolbar_html + '\n  <header class="site-header-fixed"'
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Injected toolbar successfully into {path}")
