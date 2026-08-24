# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

# 1번 유기적 조약돌 둥글기 확정 및 스토리 섹션 완전 탈박스화 CSS
unboxed_journey_and_pebble_css = """
    /* ==========================================================================
       [1번 유기적 조약돌 둥글기 확정 & 스토리 섹션 완전 탈박스화 (Unboxed Open Layout)]
       ========================================================================== */

    /* 1. 1번 유기적 조약돌 둥글기 영구 확정 */
    .pride-metrics-bar { border-radius: 36px !important; }
    .featured-card { border-radius: 26px !important; }
    .explore-catalog-banner, .fit-finder-banner { border-radius: 32px !important; }
    .one-view-card { border-radius: 16px !important; }
    .hud-card, .center-card, .proof-stat-card, .review-card, .faq-item { border-radius: 20px !important; }

    /* 2. '스밈의 철학 · 우리가 걸어온 길' 완전 탈박스화 (배경에 바로 노출되는 오픈 에디토리얼 레이아웃) */
    .journey-section {
      background: transparent !important;
      padding: 80px 0 !important;
    }
    .journey-grid {
      display: flex !important;
      flex-direction: column !important;
      gap: 70px !important;
      max-width: 1080px !important;
      margin: 0 auto !important;
    }
    .journey-chapter,
    .journey-visual-card {
      background: transparent !important;
      background-color: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
    }
    
    /* 각 챕터별 오픈 에디토리얼 2열 그리드 */
    .journey-chapter-row {
      display: grid !important;
      grid-template-columns: 1fr 1.2fr !important;
      gap: 48px !important;
      align-items: center !important;
      padding-bottom: 56px !important;
      border-bottom: 1px solid rgba(232, 225, 211, 0.7) !important;
    }
    .journey-chapter-row:last-child {
      border-bottom: none !important;
      padding-bottom: 0 !important;
    }
    
    /* 이미지/비주얼 영역: 단정한 크림 서피스 미니멀 프레임 */
    .journey-visual-open {
      background: #F7F3EB !important;
      border: 1px solid #E8E1D3 !important;
      border-radius: 22px !important;
      padding: 36px 28px !important;
      text-align: center !important;
      box-shadow: 0 4px 16px rgba(74, 67, 62, 0.03) !important;
    }

    /* 텍스트 서사 영역: 박스 없이 배경 위에 직접 자연스럽게 배치 */
    .journey-text-open {
      padding: 0 10px !important;
    }
    .journey-text-open .journey-tag {
      display: inline-block !important;
      font-size: 13.5px !important;
      color: #E5A99B !important;
      font-family: var(--font-gowun), serif !important;
      font-weight: 700 !important;
      margin-bottom: 12px !important;
    }
    .journey-text-open h3 {
      font-family: var(--font-gowun), serif !important;
      font-size: 26px !important;
      font-weight: 800 !important;
      color: #4A433E !important;
      line-height: 1.45 !important;
      margin-bottom: 18px !important;
      letter-spacing: -0.02em !important;
    }
    .journey-text-open p {
      font-size: 15.5px !important;
      color: #7A7067 !important;
      line-height: 1.8 !important;
      margin-bottom: 16px !important;
    }
    .journey-text-open .journey-quote-box {
      background: #F7F3EB !important;
      border-left: 3px solid #E5A99B !important;
      border-radius: 0 12px 12px 0 !important;
      padding: 16px 20px !important;
      margin-top: 18px !important;
    }
    .journey-text-open .journey-quote-box p {
      margin: 0 !important;
      font-size: 14.5px !important;
      color: #4A433E !important;
      font-weight: 600 !important;
      line-height: 1.6 !important;
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 임시 둥글기 툴바 제거
    content = re.sub(
        r'<!-- 3대 상자 둥글기 실시간 비교 선택 툴바 -->.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. padding-top 원복 (상단 헤더 117px)
    content = re.sub(r'padding-top:\s*\d+px;', 'padding-top: 117px;', content, count=1)

    # 3. CSS 주입
    if "/* ==========================================================================\n       [1번 유기적 조약돌 둥글기 확정" not in content:
        content = content.replace("</style>", unboxed_journey_and_pebble_css + "\n  </style>")

    # 4. 스밈의 철학 · 우리가 걸어온 길 HTML 마크업을 완전 탈박스화 오픈 에디토리얼 구조로 개편
    old_journey_regex = r'<section class="journey-section"[^>]*>.*?</section>'
    
    new_journey_html = """<section class="journey-section" id="sec-philosophy">
      <div class="container">
        
        <!-- 섹션 헤더 (이솝 1px 미세선 스타일) -->
        <div style="text-align:center; margin-bottom:56px;">
          <div class="section-tag">스밈의 철학 · 우리가 걸어온 길</div>
          <h2 style="font-family:var(--font-gowun), serif; font-size:32px; font-weight:800; color:#4A433E; margin-top:12px; letter-spacing:-0.02em;">
            억지로 조이지 않고, 일상 속에 바른 균형이 스며들도록
          </h2>
          <p style="font-size:16px; color:#7A7067; max-width:640px; margin:12px auto 0; line-height:1.7;">
            스밈(SEUMIM)이 탄생한 이유와 3년간의 인체공학 연구 및 300인 전문가 실착 검증 여정을 들려드립니다.
          </p>
        </div>

        <!-- 탈박스화 오픈 에디토리얼 서사 리스트 -->
        <div class="journey-grid">
          
          <!-- 챕터 01: 탄생의 배경 -->
          <div class="journey-chapter-row">
            <div class="journey-visual-open">
              <div style="font-size:36px; margin-bottom:12px;">🧵</div>
              <div style="font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">[3년 450번의 원사 배합 실험]</div>
              <p style="font-size:14px; color:#7A7067; line-height:1.6; margin:0;">
                머리카락보다 얇은 나노 탄성 섬유를 무봉제로 직조하여 이물감 제로와 100회 물세탁 내구성을 완성했습니다.
              </p>
              <div style="margin-top:14px; display:inline-block; padding:4px 12px; background:#FFFFFF; border-radius:9999px; border:1px solid #E8E1D3; font-size:12px; color:#E5A99B; font-weight:700;">
                실사 화보 01 · 일상의 편안함
              </div>
            </div>
            <div class="journey-text-open">
              <span class="journey-tag">── 첫 번째 이야기 · 탄생의 배경 ──</span>
              <h3>"왜 체형 교정은 늘 아프고 불편해야만 할까요?"</h3>
              <p>
                우리는 본래 첨단 스마트 섬유 부품을 개발하던 엔지니어 팀이었습니다. 하루 14시간씩 모니터를 보며 일하던 개발자들은 하나같이 심각한 거북목과 허리 통증을 겪고 있었습니다. 시중의 딱딱한 강제 압박 밴드는 옷 밖으로 튀어나왔고 강한 조임은 숨을 턱턱 막히게 했습니다.
              </p>
              <div class="journey-quote-box">
                <p>"몸을 억지로 조이지 않으면서도, 마치 아무것도 입지 않은 것처럼 가볍게 바른 자세를 유도할 수는 없을까?" 이 질문 하나에서 스밈의 여정이 시작되었습니다.</p>
              </div>
            </div>
          </div>

          <!-- 챕터 02: 기존 시장의 한계 극복 -->
          <div class="journey-chapter-row">
            <div class="journey-text-open">
              <span class="journey-tag">── 두 번째 이야기 · 기존 시장의 한계 극복 ──</span>
              <h3>고통스러운 강제 조임과 시끄러운 오알람의 종말</h3>
              <p>
                기존의 고무줄 강제 압박기는 착용할수록 주변 근육을 퇴화시키고 소화불량을 유발합니다. 또한 기존의 부착형 센서는 물을 마시는 일상 동작조차 '불량 자세'로 오진하여 시도 때도 없이 진동을 울려 극심한 스트레스를 주었습니다.
              </p>
              <p>
                스밈은 <strong>0.01초 자연 신체 필터링 알고리즘</strong>으로 일시적 움직임과 고착된 나쁜 자세를 완벽히 구분하고, <strong>0.1mm 초슬림 텐션 밴딩</strong>을 통해 스스로 바른 척추 정렬을 유지하도록 돕습니다.
              </p>
            </div>
            <div class="journey-visual-open">
              <div style="font-size:36px; margin-bottom:12px;">⚖️</div>
              <div style="font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">[기존 강제 교정기 vs 스밈 0.1mm 코어웨어]</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:12px; text-align:left;">
                <div style="background:#FFFFFF; padding:10px 12px; border-radius:12px; border:1px solid #E8E1D3; font-size:12.5px;">
                  <span style="color:#C25442; font-weight:800;">기존 교정기 ✕</span><br>
                  • 250g 무거운 쇠 와이어<br>
                  • 숨 막히는 강제 늑골 압박
                </div>
                <div style="background:#FFFFFF; padding:10px 12px; border-radius:12px; border:1px solid #B4C4B1; font-size:12.5px;">
                  <span style="color:#4C6649; font-weight:800;">스밈 0.1mm ◯</span><br>
                  • 38g 깃털 같은 초경량<br>
                  • 99.8% 옷 속 완벽 은폐
                </div>
              </div>
            </div>
          </div>

          <!-- 챕터 03: 스밈의 철학과 약속 -->
          <div class="journey-chapter-row">
            <div class="journey-visual-open">
              <div style="font-size:36px; margin-bottom:12px;">🩺</div>
              <div style="font-size:16px; font-weight:800; color:#4A433E; margin-bottom:8px;">[300+ 현업 전문가 실착 임상 검증]</div>
              <p style="font-size:14px; color:#7A7067; line-height:1.6; margin:0;">
                정형외과 의사, 물리치료사, IT 개발자들이 3주간 일상에서 착용하고 통증 87% 감소 효과를 직접 검증했습니다.
              </p>
              <div style="margin-top:14px; display:inline-block; padding:4px 12px; background:#EFF4EE; border-radius:9999px; border:1px solid #B4C4B1; font-size:12px; color:#4C6649; font-weight:700;">
                실착 임상 만족도 99.4%
              </div>
            </div>
            <div class="journey-text-open">
              <span class="journey-tag">── 세 번째 이야기 · 스밈의 철학과 약속 ──</span>
              <h3>"일상에 바른 균형이 자연스럽게 스며들도록"</h3>
              <p>
                스밈(SEUMIM)은 '스며들다'에서 비롯된 이름입니다. 퇴근 후 지친 몸을 이끌고 억지로 운동을 강요하지 않습니다. 모니터 앞, 조타실, 수술실, 분장실 등 여러분이 치열하게 일하는 그 자리에서 바른 습관이 옷처럼 편안하게 스며듭니다.
              </p>
              <div class="journey-quote-box">
                <p>하드웨어 28종 + AI 10초 미니멀 케어 구독 + 전국 웰니스 센터의 3중 선순환 플랫폼으로 지속 가능한 건강한 변화를 약속합니다.</p>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>"""

    content = re.sub(old_journey_regex, new_journey_html, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied Unboxed Flat Editorial Story & Confirmed Pebble Radius in {path}")
