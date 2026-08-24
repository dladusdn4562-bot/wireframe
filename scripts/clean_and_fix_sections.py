# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

checker_block = """
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

proof_section_clean = """    <!-- ==========================================================================
       [SEC-06: 4대 임상 및 기술 증명 (Social Proof)]
       ========================================================================== -->
    <section class="proof-section">
      <div class="container">
        <div class="section-title-wrap">
          <div class="section-tag">300인 전문가 임상 증명</div>
          <h2 class="section-title">300+ 전문가 실착 데이터 및 4.9점 비포/애프터</h2>
          <p class="section-desc">정형외과 전문의와 IT 개발자들이 3주간 실착하고 검증한 수치화된 개선 결과입니다.</p>
        </div>

        <div class="proof-stats-grid">
          <div class="proof-stat-card">
            <div class="proof-num">87.4%</div>
            <div class="proof-title">목·어깨 통증 피로도 감소</div>
            <div class="proof-desc">하루 9시간 이상 코딩 개발자 120인 검증</div>
          </div>
          <div class="proof-stat-card">
            <div class="proof-num">3.2 h</div>
            <div class="proof-title">일일 바른 자세 유지 시간 증가</div>
            <div class="proof-desc">착용 전 1.4시간 ➔ 착용 후 4.6시간 증가</div>
          </div>
          <div class="proof-stat-card">
            <div class="proof-num">98.2%</div>
            <div class="proof-title">셔츠 속 은폐 만족도</div>
            <div class="proof-desc">출근 시 동료가 눈치채지 못함 응답률</div>
          </div>
        </div>

        <!-- [9번: 300인 전문가 임상 증명 감성 갤러리] -->
        <div style="margin: 36px 0 40px;">
          <div class="clinical-proof-grid">
            <div class="clinical-card">
              <div class="clinical-rating">★ 4.9 · 정형외과 전문의 김진우</div>
              <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">
                "강제 압박 없이 경추 C커브를 살려주는 혁신"
              </div>
              <p style="font-size:13.5px; color:#7A7067; line-height:1.7;">
                기존 교정기는 늑골을 억누르는데, 스밈 0.1mm는 근육의 고유수용성 감각을 깨워 스스로 척추 정렬을 유지하게 돕습니다.
              </p>
            </div>
            <div class="clinical-card">
              <div class="clinical-rating">★ 5.0 · 물리치료사 이소영</div>
              <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">
                "99.8% 은폐율 덕분에 출근복에 매일 입습니다"
              </div>
              <p style="font-size:13.5px; color:#7A7067; line-height:1.7;">
                셔츠 속에 입어도 겉으로 전혀 드러나지 않고, 하루 종일 서서 환자를 볼 때 허리와 골반의 피로도가 80% 이상 줄었습니다.
              </p>
            </div>
            <div class="clinical-card">
              <div class="clinical-rating">★ 4.9 · 풀스택 개발자 박현성</div>
              <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">
                "14시간 코딩해도 어깨 뭉침이 사라졌습니다"
              </div>
              <p style="font-size:13.5px; color:#7A7067; line-height:1.7;">
                모니터 앞으로 목이 빨려 들어갈 때마다 지레 탄성 프레임이 부드럽게 받쳐주어 야근 후에도 목덜미가 깃털처럼 가볍습니다.
              </p>
            </div>
          </div>
        </div>

        <div class="reviews-slider">
          <div class="review-card">
            <div class="review-stars">★★★★★ 5.0</div>
            <p class="review-text">"하루 12시간 모니터만 보는 백엔드 개발자입니다. 넥밴드 착용 후 퇴근할 때 목 뻐근함이 80% 이상 사라졌습니다. 셔츠 안에 입어도 아무도 몰라요."</p>
            <div class="review-author">
              <span>김민석 (31세, 시니어 개발자)</span>
              <span class="review-badge">178cm / 74kg (M 착용)</span>
            </div>
          </div>
          <div class="review-card">
            <div class="review-stars">★★★★★ 4.9</div>
            <p class="review-text">"정형외과 의사로서 수많은 교정기를 보았지만, 스밈처럼 '억지로 조이지 않고 체감 피로도를 낮추는 무봉제 기술'은 처음입니다. 환자분들께도 적극 추천합니다."</p>
            <div class="review-author">
              <span>이현우 원장 (정형외과 전문의)</span>
              <span class="review-badge">전문의 자문단</span>
            </div>
          </div>
          <div class="review-card">
            <div class="review-stars">★★★★★ 5.0</div>
            <p class="review-text">"의자에만 앉으면 다리를 꼬아서 골반이 삐뚤어졌는데, 에어셀 벨트 착용 후 다리 꼴 때마다 팽창해서 자동으로 바른 자세가 잡힙니다. 0원 시착 최고!"</p>
            <div class="review-author">
              <span>박지영 (29세, UX 디자이너)</span>
              <span class="review-badge">164cm / 52kg (S 착용)</span>
            </div>
          </div>
        </div>
      </div>
    </section>"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. sec-featured 닫는 태그 바로 뒤에 자가진단 위젯 주입
    if 'id="self-checker-sec"' not in content:
        content = re.sub(
            r'(</section>\s*<!--\s*==========================================================================\s*\[SEC-06:\s*4대 임상)',
            r'\n' + checker_block + r'\n\n    \1',
            content
        )

    # 2. proof-section을 깨끗한 버전으로 완전 교체
    content = re.sub(
        r'<section class="proof-section">.*?</section>',
        proof_section_clean,
        content,
        flags=re.DOTALL
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned layout in {path}")
