# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

# 5대 요소(4, 6, 7, 9, 10번) 전용 스타일링 CSS
five_elements_css = """
    /* ==========================================================================
       [5대 엄선 UX 디자인 요소 (4, 6, 7, 9, 10번) 고도화 시스템]
       ========================================================================== */

    /* 4번: 피치 코랄 틴트 하이라이트 띠 */
    .highlight-peach {
      background: linear-gradient(180deg, transparent 60%, rgba(229, 169, 155, 0.34) 60%) !important;
      display: inline !important;
      padding: 0 4px !important;
      font-weight: inherit !important;
    }

    /* 6번: 가로 스냅 슬라이더 시스템 */
    .horizontal-slider-wrapper {
      position: relative;
      margin: 24px 0;
    }
    .horizontal-snap-track {
      display: flex !important;
      gap: 20px !important;
      overflow-x: auto !important;
      scroll-snap-type: x mandatory !important;
      scroll-behavior: smooth !important;
      padding: 16px 4px 28px !important;
      -webkit-overflow-scrolling: touch !important;
    }
    .horizontal-snap-track::-webkit-scrollbar {
      height: 6px;
    }
    .horizontal-snap-track::-webkit-scrollbar-track {
      background: #F0ECE1;
      border-radius: 9999px;
    }
    .horizontal-snap-track::-webkit-scrollbar-thumb {
      background: #E5A99B;
      border-radius: 9999px;
    }
    .horizontal-snap-track > * {
      scroll-snap-align: start !important;
      flex: 0 0 280px !important;
      max-width: 280px !important;
    }
    .slider-nav-btn {
      position: absolute;
      top: 45%;
      transform: translateY(-50%);
      width: 40px;
      height: 40px;
      border-radius: 9999px;
      background: #FFFFFF;
      border: 1.5px solid #E8E1D3;
      color: #4A433E;
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(74, 67, 62, 0.1);
      z-index: 10;
      transition: all 0.2s ease;
    }
    .slider-nav-btn:hover {
      background: #E5A99B;
      color: #FFFFFF;
      border-color: #E5A99B;
    }
    .slider-nav-prev { left: -16px; }
    .slider-nav-next { right: -16px; }

    /* 7번: 3초 체형 밸런스 자가진단 위젯 */
    .balance-checker-container {
      background: #F7F3EB !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 32px !important;
      padding: 36px 32px !important;
      margin: 48px auto !important;
      max-width: 980px !important;
      box-shadow: 0 8px 24px rgba(74, 67, 62, 0.04) !important;
      text-align: center !important;
    }
    .checker-chip-grid {
      display: flex !important;
      justify-content: center !important;
      flex-wrap: wrap !important;
      gap: 12px !important;
      margin: 22px 0 26px !important;
    }
    .checker-chip {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 9999px !important;
      padding: 10px 20px !important;
      font-size: 14px !important;
      font-weight: 700 !important;
      color: #4A433E !important;
      cursor: pointer !important;
      transition: all 0.2s ease !important;
      font-family: var(--font-gowun), serif !important;
    }
    .checker-chip:hover {
      border-color: #E5A99B !important;
      background: #FDFBF7 !important;
      transform: translateY(-2px) !important;
    }
    .checker-chip.active {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      border-color: #E5A99B !important;
      box-shadow: 0 4px 12px rgba(229, 169, 155, 0.35) !important;
    }
    .checker-result-card {
      background: #FFFFFF !important;
      border: 1.5px solid #B4C4B1 !important;
      border-radius: 20px !important;
      padding: 20px 24px !important;
      margin-top: 16px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 16px !important;
      text-align: left !important;
    }

    /* 9번: 300인 전문가 임상 갤러리 */
    .clinical-proof-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 20px !important;
      margin: 28px 0 !important;
    }
    .clinical-card {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 20px !important;
      padding: 24px !important;
      text-align: left !important;
      box-shadow: 0 4px 16px rgba(74, 67, 62, 0.03) !important;
    }
    .clinical-rating {
      color: #E5A99B !important;
      font-size: 14px !important;
      font-weight: 800 !important;
      margin-bottom: 8px !important;
    }

    /* 10번: 조약돌 아코디언 FAQ 인터랙션 */
    .faq-item {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 20px !important;
      padding: 20px 24px !important;
      margin-bottom: 14px !important;
      cursor: pointer !important;
      transition: all 0.3s ease !important;
    }
    .faq-item:hover {
      border-color: #E5A99B !important;
      box-shadow: 0 4px 16px rgba(74, 67, 62, 0.04) !important;
    }
    .faq-item.open {
      background: #FDFBF7 !important;
      border-color: #B4C4B1 !important;
    }
    .faq-question {
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      font-family: var(--font-gowun), serif !important;
      font-size: 16.5px !important;
      font-weight: 800 !important;
      color: #4A433E !important;
    }
    .faq-answer {
      margin-top: 14px !important;
      padding-top: 14px !important;
      border-top: 1px dashed #E8E1D3 !important;
      font-size: 14.5px !important;
      color: #7A7067 !important;
      line-height: 1.7 !important;
    }
"""

# 7번 자가진단 위젯 HTML 컴포넌트
checker_html = """
      <!-- [7번 인터랙티브 체형 밸런스 3초 간이 자가진단 위젯] -->
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
            <div style="font-size:32px; background:#F0F5EF; width:54px; height:54px; border-radius:9999px; display:flex; align-items:center; justify-content:center;">
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
          <button class="btn-primary" onclick="filterCatalogByTag('neck')" style="padding:10px 18px; font-size:13px; border-radius:9999px; white-space:nowrap;">
            처방 상품 보러가기 ➔
          </button>
        </div>
      </div>
"""

# JS 인터랙션 함수 (자가진단 및 가로 슬라이더 제어)
five_elements_js = """
    const checkerPrescriptions = [
      {
        icon: '🌿',
        tag: '모니터 근무 직장인 최적 처방',
        title: '0.1mm 심리스 넥&숄더 밴드 + 척추 정렬 조끼',
        desc: '키보드 타건 시 발생하는 전방 두부 쏠림 4.2kg 하중을 승모근 뒤쪽으로 0.1초 분산',
        filter: 'neck'
      },
      {
        icon: '🧍',
        tag: '기립·보행 직업군 최적 처방',
        title: '골반 수평 에어셀 벨트 + 기립 체압 분산 힐 컵',
        desc: '짝다리 짚기 및 골반 회전을 실시간 차단하고 발뒤꿈치 충격을 40% 흡수',
        filter: 'pelvis'
      },
      {
        icon: '🚗',
        tag: '운전·출장 직업군 최적 처방',
        title: '출장용 에어 럼버 앵커 + 스마트 체형 센서웨어',
        desc: '시트 착석 시 무너지는 요추 C자 커브를 공기압으로 지지하고 졸음 운전 방지 진동',
        filter: 'waist'
      },
      {
        icon: '🎨',
        tag: '정밀 수작업 직업군 최적 처방',
        title: '타블렛 암레스트 서포터 + 손목 텐션 밴드',
        desc: '반복 마우스/펜 조작 시 손목 터널 증후군 및 회전근개 긴장을 0.1mm 텐션으로 보조',
        filter: 'acc'
      }
    ];

    function selectCheckerJob(index, btn) {
      document.querySelectorAll('.checker-chip').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      
      const p = checkerPrescriptions[index];
      const box = document.getElementById('checker-result-box');
      if (box) {
        box.innerHTML = `
          <div style="display:flex; align-items:center; gap:16px;">
            <div style="font-size:32px; background:#F0F5EF; width:54px; height:54px; border-radius:9999px; display:flex; align-items:center; justify-content:center;">
              ${p.icon}
            </div>
            <div>
              <div style="font-size:12.5px; color:#4C6649; font-weight:800;">[${p.tag}]</div>
              <div style="font-family:var(--font-gowun), serif; font-size:17px; font-weight:800; color:#4A433E; margin:3px 0;">
                ${p.title}
              </div>
              <div style="font-size:13px; color:#7A7067;">
                ${p.desc}
              </div>
            </div>
          </div>
          <button class="btn-primary" onclick="filterCatalogByTag('${p.filter}')" style="padding:10px 18px; font-size:13px; border-radius:9999px; white-space:nowrap;">
            처방 상품 보러가기 ➔
          </button>
        `;
      }
    }

    function scrollSlider(trackId, offset) {
      const track = document.getElementById(trackId);
      if (track) {
        track.scrollBy({ left: offset, behavior: 'smooth' });
      }
    }

    function toggleFaqItem(el) {
      const isOpen = el.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function(item) { item.classList.remove('open'); });
      if (!isOpen) {
        el.classList.add('open');
      }
    }
"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 주입
    if "/* [5대 엄선 UX 디자인 요소 (4, 6, 7, 9, 10번) 고도화 시스템]" not in content:
        content = content.replace("</style>", five_elements_css + "\n  </style>")

    # 2. JS 함수 주입
    if "function selectCheckerJob" not in content:
        content = content.replace("</head>", "  <script>\n" + five_elements_js + "  </script>\n</head>")

    # 3. 7번 자가진단 위젯 주입 (3대 대표작 바로 아래)
    if 'id="self-checker-sec"' not in content and '</section>\n\n    <!-- ==========================================================================\n         [SEC-06' in content:
        content = content.replace(
            '</section>\n\n    <!-- ==========================================================================\n         [SEC-06',
            '</section>\n\n    ' + checker_html + '\n\n    <!-- ==========================================================================\n         [SEC-06'
        )

    # 4. 4번 피치 코랄 틴트 하이라이트 적용 (헤드라인 및 주요 키워드)
    content = content.replace("나를 먼저 아끼는 다정한 균형", '나를 먼저 아끼는 <span class="highlight-peach">다정한 균형</span>')
    content = content.replace("30일 안심 무료 반품", '<span class="highlight-peach">30일 안심 무료 반품</span>')
    content = content.replace("300+ 전문가 실착 검증", '<span class="highlight-peach">300+ 전문가 실착 검증</span>')
    content = content.replace("통증 87% 감소", '<span class="highlight-peach">통증 87% 감소</span>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied 5 Selected Design Elements (4, 6, 7, 9, 10) to {path}")
