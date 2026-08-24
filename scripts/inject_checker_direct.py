# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

checker_html = """
    <!-- [7번: 3초 체형 밸런스 파인더 자가진단 위젯 (지그재그 버튼)] -->
    <div class="balance-checker-container" id="self-checker-sec">
      <div class="section-tag">3초 맞춤 처방 · 체형 밸런스 파인더</div>
      <h3 style="font-family:var(--font-gowun), serif; font-size:24px; font-weight:800; color:#4A433E; margin:10px 0 6px;">
        "당신의 하루 중 가장 치열한 작업 환경은 어디인가요?"
      </h3>
      <p style="font-size:14.5px; color:#7A7067; margin:0;">
        작업 환경을 선택하시면, 신체 부하를 분산시키는 <span class="highlight-peach">0.1mm 맞춤 코어웨어 조합</span>을 즉시 처방해 드립니다.
      </p>
      <div class="checker-chip-grid">
        <button class="checker-chip active" onclick="selectCheckerJob(0, this)">💻 모니터 앞 8시간 (거북목·말린어깨)</button>
        <button class="checker-chip" onclick="selectCheckerJob(1, this)">🧍 하루 6시간 기립·이동 (허리·골반 틀어짐)</button>
        <button class="checker-chip" onclick="selectCheckerJob(2, this)">🚗 장시간 운전·출장 (허리 뻐근함·다리 꼬기)</button>
        <button class="checker-chip" onclick="selectCheckerJob(3, this)">🎨 정밀 작업·수작업 (손목·승모근 결림)</button>
      </div>
      <div class="checker-result-card" id="checker-result-box">
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="font-size:32px; background:#EFF4EE; width:54px; height:54px; border-radius:9999px; display:flex; align-items:center; justify-content:center;">
            🌿
          </div>
          <div>
            <div style="font-size:12.5px; color:#4C6649; font-weight:800;">[모니터 근무 직장인 최적 처방]</div>
            <div style="font-family:var(--font-gowun), serif; font-size:17px; font-weight:800; color:#4A433E; margin:3px 0;">
              0.1mm 심리스 넥&숄더 밴드 + 척추 정렬 조끼
            </div>
            <div style="font-size:13px; color:#7A7067;">
              키보드 타건 시 발생하는 전방 두부 쏠림 4.2kg 하중을 승모근 뒤쪽으로 0.1초 분산
            </div>
          </div>
        </div>
        <button class="btn-primary" onclick="filterCatalogByTag('cat_neck')" style="padding:10px 18px; font-size:13px; border-radius:9999px; white-space:nowrap;">
          처방 상품 보러가기 ➔
        </button>
      </div>
    </div>
"""

target_str = '<section class="proof-section">'

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="self-checker-sec"' not in content and target_str in content:
        content = content.replace(target_str, checker_html + '\n\n    ' + target_str)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Injected self-checker in {path}")
