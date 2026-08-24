# -*- coding: utf-8 -*-
import os
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

head_script = """  <script>
    // 전역 즉시 실행 테마 전환 함수
    window.switchThemeStyle = function(styleClass, btn) {
      console.log('Switching to theme:', styleClass);
      // 1. body의 모든 theme-style 클래스 제거
      document.body.classList.remove('theme-style-1', 'theme-style-2', 'theme-style-3', 'theme-style-4', 'theme-style-5');
      // 2. 선택된 스타일 클래스 추가
      document.body.classList.add(styleClass);
      
      // 3. 모든 테마 선택 버튼 활성화 상태 업데이트
      document.querySelectorAll('.btn-theme-selector, .btn-hero-theme').forEach(function(b) {
        if (b.getAttribute('data-theme') === styleClass) {
          b.style.background = '#D9531E';
          b.style.color = '#ffffff';
          b.style.borderColor = '#D9531E';
          b.classList.add('active');
        } else {
          b.style.background = 'rgba(255,255,255,0.1)';
          b.style.color = '#dedede';
          b.style.borderColor = 'rgba(255,255,255,0.25)';
          b.classList.remove('active');
        }
      });
    };
  </script>
"""

# 본문 상단 인터랙티브 체험 바
hero_interactive_bar = """
        <!-- [실시간 5대 감성 강조 스타일 체험 배너] -->
        <div style="background:var(--bg-surface); border:1.5px solid var(--color-border); border-radius:var(--radius-lg); padding:20px 24px; margin:0 auto 36px; max-width:960px; box-shadow:var(--shadow-md); text-align:center;">
          <div style="display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:12px;">
            <span style="font-size:18px;">🎨</span>
            <span style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary);">어떤 강조 방식이 가장 마음에 드시나요? 아래 버튼을 눌러 실시간으로 확인해보세요!</span>
          </div>
          <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
            <button class="btn-hero-theme active" data-theme="theme-style-1" onclick="window.switchThemeStyle('theme-style-1', this)" style="padding:8px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1px solid #D9531E; background:#D9531E; color:#fff; cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              1. 이솝 1px 미세선
            </button>
            <button class="btn-hero-theme" data-theme="theme-style-2" onclick="window.switchThemeStyle('theme-style-2', this)" style="padding:8px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1px solid var(--color-border); background:var(--bg-card); color:var(--color-text-secondary); cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              2. 킨포크 워터마크
            </button>
            <button class="btn-hero-theme" data-theme="theme-style-3" onclick="window.switchThemeStyle('theme-style-3', this)" style="padding:8px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1px solid var(--color-border); background:var(--bg-card); color:var(--color-text-secondary); cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              3. 프라마 버티컬바
            </button>
            <button class="btn-hero-theme" data-theme="theme-style-4" onclick="window.switchThemeStyle('theme-style-4', this)" style="padding:8px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1px solid var(--color-border); background:var(--bg-card); color:var(--color-text-secondary); cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              4. 젠(Zen) 한글낙관
            </button>
            <button class="btn-hero-theme" data-theme="theme-style-5" onclick="window.switchThemeStyle('theme-style-5', this)" style="padding:8px 16px; font-size:13.5px; font-weight:700; border-radius:9999px; border:1px solid var(--color-border); background:var(--bg-card); color:var(--color-text-secondary); cursor:pointer; font-family:'Gowun Batang', serif; transition:all 0.2s ease;">
              5. 수채화 브러시
            </button>
          </div>
        </div>
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. <head> 안에 즉시 실행 스크립트 주입
    if "</head>" in content and "window.switchThemeStyle" not in content:
        content = content.replace("</head>", head_script + "\n</head>")

    # 2. padding-top 조정 (고정 헤더 높이 반영)
    content = re.sub(r'padding-top:\s*\d+px;', 'padding-top: 165px;', content, count=1)

    # 3. 버튼에 data-theme 속성 추가
    content = content.replace(
        'onclick="switchThemeStyle(\'theme-style-1\', this)"',
        'data-theme="theme-style-1" onclick="window.switchThemeStyle(\'theme-style-1\', this)"'
    )
    content = content.replace(
        'onclick="switchThemeStyle(\'theme-style-2\', this)"',
        'data-theme="theme-style-2" onclick="window.switchThemeStyle(\'theme-style-2\', this)"'
    )
    content = content.replace(
        'onclick="switchThemeStyle(\'theme-style-3\', this)"',
        'data-theme="theme-style-3" onclick="window.switchThemeStyle(\'theme-style-3\', this)"'
    )
    content = content.replace(
        'onclick="switchThemeStyle(\'theme-style-4\', this)"',
        'data-theme="theme-style-4" onclick="window.switchThemeStyle(\'theme-style-4\', this)"'
    )
    content = content.replace(
        'onclick="switchThemeStyle(\'theme-style-5\', this)"',
        'data-theme="theme-style-5" onclick="window.switchThemeStyle(\'theme-style-5\', this)"'
    )

    # 4. 메인 히어로 섹션 상단에 인터랙티브 배너 주입
    if '<section class="hero-section">' in content and "어떤 강조 방식이 가장 마음에 드시나요?" not in content:
        content = content.replace(
            '<section class="hero-section">\n      <div class="container">',
            '<section class="hero-section">\n      <div class="container">\n' + hero_interactive_bar
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed click handling and added hero interactive bar in {path}")
