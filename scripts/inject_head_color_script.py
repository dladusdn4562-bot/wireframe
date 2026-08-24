# -*- coding: utf-8 -*-

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

head_color_script = """  <script>
    window.switchColorPalette = function(paletteClass, btn) {
      console.log('Palette selected:', paletteClass);
      document.body.classList.remove('palette-terracotta', 'palette-sage', 'palette-caramel', 'palette-dustyrose', 'palette-honey', 'palette-taupe');
      if (paletteClass && paletteClass !== 'palette-terracotta') {
        document.body.classList.add(paletteClass);
      }
      document.querySelectorAll('.btn-palette-selector').forEach(function(b) {
        if (b.getAttribute('data-palette') === paletteClass) {
          b.style.borderColor = '#ffffff';
          b.style.transform = 'scale(1.05)';
        } else {
          b.style.borderColor = 'rgba(255,255,255,0.25)';
          b.style.transform = 'scale(1)';
        }
      });
    };
  </script>
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # <head> 안에 주입
    if "</head>" in content and "window.switchColorPalette" not in content[:content.find("</head>")]:
        content = content.replace("</head>", head_color_script + "\n</head>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Added head_color_script to {path}")
