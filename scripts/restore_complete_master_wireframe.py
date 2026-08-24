# -*- coding: utf-8 -*-
import re

# 원본의 풍부한 모든 섹션(SEC-01~16) 마크업과 컴포넌트 CSS가 들어있는 소스를 기반으로 완벽 재구성
src_path = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\디자인 분석 와이어프레임.html'
with open(src_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 2030 웜 뉴트럴 확정 마스터 CSS (기존 모든 컴포넌트 스타일을 온전히 유지하면서 4색 시스템 & 조약돌 둥글기 & 5대 요소 융합)
master_warm_neutral_css = """
    /* ==========================================================================
       [SEUMIM 확정 마스터 2030 웜 뉴트럴 디자인 시스템]
       1. Base Background: 단일 크림 오트밀 (#FDFBF7)
       2. Typography: 웜 브라운 차콜 (#4A433E)
       3. Primary (메인 CTA / 강조): 소프트 피치 코랄 (#E5A99B)
       4. Secondary (상태 알림 / 보조): 뮤티드 세이지 (#B4C4B1)
       5. 1번 유기적 조약돌 둥글기 시스템 (16px ~ 36px, 9999px)
       ========================================================================== */

    :root {
      --bg-base: #FDFBF7;
      --bg-surface: #F7F3EB;
      --bg-surface-elevated: #EFE8DC;
      --bg-card: #FFFFFF;
      --bg-card-alt: #FDFBF7;
      --bg-warm-glow: rgba(229, 169, 155, 0.08);

      --color-text-primary: #4A433E;
      --color-text-secondary: #7A7067;
      --color-text-muted: #9E9388;
      --color-text-inverse: #FFFFFF;

      --color-primary: #E5A99B;
      --color-primary-hover: #D49586;
      --color-primary-light: #FDF5F3;
      --color-secondary: #B4C4B1;
      --color-secondary-hover: #9FB39B;
      --color-secondary-light: #EFF4EE;
      --color-secondary-text: #4C6649;

      --color-terracotta: #E5A99B;
      --color-forest: #4A433E;
      --color-sage: #B4C4B1;
      --color-wood: #7A7067;

      --color-border: #E8E1D3;
      --color-border-light: #F2ECE1;
      --color-border-soft: rgba(74, 67, 62, 0.08);

      --font-gowun: 'Gowun Batang', 'Noto Serif KR', serif;
      --font-serif: 'Gowun Batang', 'Noto Serif KR', serif;
      --font-maruburi: 'Gowun Batang', 'Noto Serif KR', serif;
      --font-sans: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 26px;
      --radius-xl: 36px;
      --radius-full: 9999px;

      --shadow-sm: 0 2px 8px rgba(74, 67, 62, 0.04);
      --shadow-md: 0 6px 20px rgba(74, 67, 62, 0.05);
      --shadow-lg: 0 12px 36px rgba(74, 67, 62, 0.07);

      --container-max: 1240px;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    body, #page-main, #page-shop, #page-story {
      background-color: #FDFBF7 !important;
      color: #4A433E !important;
      font-family: var(--font-sans);
    }

    /* 1px 미세 연장선 (이솝 스타일) */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 14px !important;
      color: #E5A99B !important;
      font-family: var(--font-gowun), serif !important;
      font-size: 13.5px !important;
      font-weight: 700 !important;
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
    }
    .section-tag::before, .section-tag::after,
    .hero-eyebrow::before, .hero-eyebrow::after,
    .catalog-tag::before, .catalog-tag::after,
    .journey-tag::before, .journey-tag::after {
      content: '' !important;
      display: inline-block !important;
      width: 28px !important;
      height: 1px !important;
      background: #E5A99B !important;
      opacity: 0.85 !important;
    }

    /* 4번: 피치 코랄 틴트 하이라이트 띠 */
    .highlight-peach {
      background: linear-gradient(180deg, transparent 60%, rgba(229, 169, 155, 0.34) 60%) !important;
      display: inline !important;
      padding: 0 4px !important;
    }

    /* 버튼: 조약돌 둥근 듀얼 CTA */
    .btn-primary, .btn-accent, .floating-bottom-bar .btn-accent {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      border: 1.5px solid #E5A99B !important;
      border-radius: 9999px !important;
      box-shadow: 0 4px 14px rgba(229, 169, 155, 0.35) !important;
      font-weight: 700 !important;
      padding: 12px 24px !important;
      transition: var(--transition) !important;
    }
    .btn-primary:hover, .btn-accent:hover {
      background: #D49586 !important;
      border-color: #D49586 !important;
      transform: translateY(-1px) !important;
    }
    .btn-secondary {
      background: #FFFFFF !important;
      color: #4A433E !important;
      border: 1.5px solid #E5A99B !important;
      border-radius: 9999px !important;
      font-weight: 700 !important;
      padding: 12px 24px !important;
      transition: var(--transition) !important;
    }
    .btn-secondary:hover {
      background: #FDF5F3 !important;
      color: #D49586 !important;
      border-color: #D49586 !important;
    }

    /* 1번 유기적 조약돌 둥글기 시스템 */
    .pride-metrics-bar { border-radius: 36px !important; background: #FFFFFF !important; border: 1.5px solid #E8E1D3 !important; }
    .featured-card { border-radius: 26px !important; border: 1.5px solid #E8E1D3 !important; }
    .explore-catalog-banner, .fit-finder-banner { border-radius: 32px !important; }
    .one-view-card { border-radius: 16px !important; border: 1.5px solid #E8E1D3 !important; }
    .hud-card, .center-card, .proof-stat-card, .review-card, .faq-item { border-radius: 20px !important; border: 1.5px solid #E8E1D3 !important; }

    /* 히어로 2열 스플릿 앰비언트 비주얼 앵커 */
    .hero-split-grid {
      display: grid !important;
      grid-template-columns: 1.15fr 0.85fr !important;
      gap: 44px !important;
      align-items: center !important;
      margin-bottom: 48px !important;
    }
    .hero-content-left { text-align: left !important; }
    .hero-content-left .hero-eyebrow { justify-content: flex-start !important; margin-bottom: 14px !important; }
    .hero-manifesto-title {
      font-family: var(--font-gowun), serif !important;
      font-size: 40px !important;
      font-weight: 800 !important;
      line-height: 1.35 !important;
      color: #4A433E !important;
      letter-spacing: -0.02em !important;
      margin-bottom: 18px !important;
    }
    .hero-subcopy {
      font-size: 16px !important;
      color: #7A7067 !important;
      line-height: 1.75 !important;
      margin-bottom: 28px !important;
      max-width: 520px !important;
    }
    .hero-cta-group { display: flex !important; gap: 14px !important; align-items: center !important; flex-wrap: wrap !important; }

    .hero-visual-anchor {
      background: #F7F3EB !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 32px !important;
      padding: 24px !important;
      box-shadow: 0 6px 20px rgba(74, 67, 62, 0.05) !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      height: 380px !important;
    }
    .hero-visual-inner {
      background: #FFFFFF !important;
      border: 1px dashed #E8E1D3 !important;
      border-radius: 22px !important;
      height: 240px !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
      text-align: center !important;
      padding: 20px !important;
      position: relative !important;
    }
    .hero-visual-badge-top {
      position: absolute !important;
      top: 14px !important;
      left: 14px !important;
      background: #EFF4EE !important;
      color: #4C6649 !important;
      border: 1px solid #B4C4B1 !important;
      padding: 4px 10px !important;
      border-radius: 9999px !important;
      font-size: 11px !important;
      font-weight: 800 !important;
    }
    .hero-visual-caption {
      margin-top: 14px !important;
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
    }
    .hero-caption-title {
      font-family: var(--font-gowun), serif !important;
      font-size: 15px !important;
      font-weight: 800 !important;
      color: #4A433E !important;
    }
    .hero-caption-desc { font-size: 12.5px !important; color: #7A7067 !important; }

    /* 탈박스화 브랜드 스토리 섹션 */
    .journey-section { background: transparent !important; padding: 80px 0 !important; }
    .journey-grid { display: flex !important; flex-direction: column !important; gap: 64px !important; max-width: 1080px !important; margin: 0 auto !important; }
    .journey-chapter, .journey-chapter-card, .journey-visual-card {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
    }
    .journey-chapter-row {
      display: grid !important;
      grid-template-columns: 1fr 1.2fr !important;
      gap: 48px !important;
      align-items: center !important;
      padding-bottom: 56px !important;
      border-bottom: 1px solid #E8E1D3 !important;
    }
    .journey-chapter-row:last-child { border-bottom: none !important; padding-bottom: 0 !important; }
    .journey-visual-open {
      background: #F7F3EB !important;
      border: 1px solid #E8E1D3 !important;
      border-radius: 22px !important;
      padding: 32px 24px !important;
      text-align: center !important;
      box-shadow: 0 4px 16px rgba(74, 67, 62, 0.03) !important;
    }
    .journey-text-open .journey-tag { justify-content: flex-start !important; margin-bottom: 10px !important; }
    .journey-text-open h3 {
      font-family: var(--font-gowun), serif !important;
      font-size: 25px !important;
      font-weight: 800 !important;
      color: #4A433E !important;
      line-height: 1.45 !important;
      margin-bottom: 16px !important;
    }
    .journey-text-open p { font-size: 15px !important; color: #7A7067 !important; line-height: 1.8 !important; margin-bottom: 14px !important; }
    .journey-quote-box {
      background: #F7F3EB !important;
      border-left: 3px solid #E5A99B !important;
      border-radius: 0 12px 12px 0 !important;
      padding: 14px 18px !important;
      margin-top: 16px !important;
    }
    .journey-quote-box p { margin: 0 !important; font-size: 14px !important; color: #4A433E !important; font-weight: 600 !important; }

    /* 7번: 3초 자가진단 위젯 */
    .balance-checker-container {
      background: #F7F3EB !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 32px !important;
      padding: 36px 32px !important;
      margin: 48px auto !important;
      max-width: 980px !important;
      box-shadow: 0 6px 20px rgba(74, 67, 62, 0.04) !important;
      text-align: center !important;
    }
    .checker-chip-grid { display: flex !important; justify-content: center !important; flex-wrap: wrap !important; gap: 10px !important; margin: 20px 0 24px !important; }
    .checker-chip {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 9999px !important;
      padding: 10px 18px !important;
      font-size: 13.5px !important;
      font-weight: 700 !important;
      color: #4A433E !important;
      cursor: pointer !important;
      transition: var(--transition) !important;
      font-family: var(--font-gowun), serif !important;
    }
    .checker-chip:hover { border-color: #E5A99B !important; transform: translateY(-2px) !important; }
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
      padding: 18px 22px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 16px !important;
      text-align: left !important;
    }

    /* 6번: 가로 스냅 슬라이더 */
    .horizontal-slider-wrapper { position: relative !important; margin: 24px 0 !important; }
    .horizontal-snap-track {
      display: flex !important;
      gap: 20px !important;
      overflow-x: auto !important;
      scroll-snap-type: x mandatory !important;
      scroll-behavior: smooth !important;
      padding: 12px 4px 24px !important;
      -webkit-overflow-scrolling: touch !important;
    }
    .horizontal-snap-track::-webkit-scrollbar { height: 6px !important; }
    .horizontal-snap-track::-webkit-scrollbar-track { background: #F7F3EB !important; border-radius: 9999px !important; }
    .horizontal-snap-track::-webkit-scrollbar-thumb { background: #E5A99B !important; border-radius: 9999px !important; }
    .horizontal-snap-track > * { scroll-snap-align: start !important; flex: 0 0 280px !important; max-width: 280px !important; }
    .slider-nav-btn {
      position: absolute !important;
      top: 45% !important;
      transform: translateY(-50%) !important;
      width: 40px !important;
      height: 40px !important;
      border-radius: 9999px !important;
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      color: #4A433E !important;
      font-size: 18px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      cursor: pointer !important;
      box-shadow: 0 4px 12px rgba(74, 67, 62, 0.08) !important;
      z-index: 10 !important;
      transition: var(--transition) !important;
    }
    .slider-nav-btn:hover { background: #E5A99B !important; color: #FFFFFF !important; border-color: #E5A99B !important; }
    .slider-nav-prev { left: -16px !important; }
    .slider-nav-next { right: -16px !important; }

    /* 9번: 300인 전문가 임상 갤러리 */
    .clinical-proof-grid { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 20px !important; margin: 28px 0 !important; }
    .clinical-card {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 20px !important;
      padding: 24px !important;
      text-align: left !important;
      box-shadow: 0 4px 16px rgba(74, 67, 62, 0.03) !important;
    }
    .clinical-rating { color: #E5A99B !important; font-size: 14px !important; font-weight: 800 !important; margin-bottom: 8px !important; }

    /* 10번: 조약돌 아코디언 FAQ */
    .faq-item {
      background: #FFFFFF !important;
      border: 1.5px solid #E8E1D3 !important;
      border-radius: 20px !important;
      padding: 20px 24px !important;
      margin-bottom: 14px !important;
      cursor: pointer !important;
      transition: var(--transition) !important;
    }
    .faq-item:hover { border-color: #E5A99B !important; box-shadow: 0 4px 16px rgba(74, 67, 62, 0.04) !important; }
    .faq-item.open { background: #FDFBF7 !important; border-color: #B4C4B1 !important; }
    .faq-question {
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      font-family: var(--font-gowun), serif !important;
      font-size: 16px !important;
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

    /* 플로팅 바 */
    .floating-bottom-bar {
      position: fixed !important;
      bottom: 0 !important;
      left: 0 !important;
      right: 0 !important;
      background: #4A433E !important;
      color: #FDFBF7 !important;
      padding: 12px 24px !important;
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      z-index: 1000 !important;
      border-top: 1px solid rgba(255,255,255,0.12) !important;
      box-shadow: 0 -4px 20px rgba(74, 67, 62, 0.12) !important;
    }
    .floating-bottom-bar .badge-price {
      background: #E5A99B !important;
      color: #FFFFFF !important;
      font-size: 11px !important;
      font-weight: 800 !important;
      padding: 3px 8px !important;
      border-radius: 9999px !important;
      margin-right: 8px !important;
    }

    /* 반응형 */
    @media (max-width: 992px) {
      .hero-split-grid { grid-template-columns: 1fr !important; gap: 32px !important; }
      .hero-content-left { text-align: center !important; }
      .hero-content-left .hero-eyebrow { justify-content: center !important; }
      .hero-cta-group { justify-content: center !important; }
      .pride-metrics-bar { grid-template-columns: repeat(2, 1fr) !important; }
      .featured-card { grid-template-columns: 1fr !important; }
      .clinical-proof-grid { grid-template-columns: 1fr !important; }
    }
"""

# 기존 CSS를 보존하면서 최상위 우선순위 마스터 CSS를 </style> 직전에 안전하게 결합
content = content.replace("</style>", master_warm_neutral_css + "\n  </style>")

# 2. 2열 스플릿 히어로 마크업
hero_markup = """<section class="hero-section" id="sec-manifesto">
      <div class="container">
        
        <!-- [1번: 2열 스플릿 히어로 - 헤드라인 + 감성 앰비언트 비주얼 앵커] -->
        <div class="hero-split-grid">
          
          <!-- 좌측: 매니페스토 & CTA -->
          <div class="hero-content-left">
            <div class="hero-eyebrow">일상에 자연스럽게 스며드는 0.1MM 바른 균형</div>
            <h1 class="hero-manifesto-title">
              바쁜 하루 속에서도,<br>
              나를 먼저 아끼는 <span class="highlight-peach">다정한 균형</span>
            </h1>
            <p class="hero-subcopy">
              억지스러운 압박 대신 기분 좋은 편안함으로,<br>
              당신의 일상에 건강한 쉼을 채워드릴게요.
            </p>
            <div class="hero-cta-group">
              <a href="#sec-philosophy" class="btn-primary">스밈의 시작 알아보기 ➔</a>
              <a href="#sec-featured" class="btn-secondary">스밈 3대 대표작 알아보기 ➔</a>
            </div>
          </div>

          <!-- 우측: 0.1mm 일상 실착 앰비언트 비주얼 앵커 -->
          <div class="hero-visual-anchor">
            <div class="hero-visual-inner">
              <span class="hero-visual-badge-top">🌿 99.8% 출근복 속 완벽 은폐</span>
              <div style="font-size:42px; margin-bottom:8px;">☕ 👕</div>
              <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:#4A433E; margin-bottom:4px;">
                [일상 실착 앰비언트 무드컷]
              </div>
              <div style="font-size:12.5px; color:#7A7067; line-height:1.5;">
                셔츠 속에 0.1mm 초슬림 넥&숄더 밴드를 착용하고<br>편안하게 데스크 업무를 보는 자연스러운 일상 실루엣
              </div>
            </div>
            <div class="hero-visual-caption">
              <div>
                <div class="hero-caption-title">0.1mm 초박형 센서 섬유 직조</div>
                <div class="hero-caption-desc">38g 깃털 같은 무게로 피로도 제로</div>
              </div>
              <div style="font-size:11.5px; font-weight:800; color:#E5A99B; background:#FDF5F3; padding:4px 10px; border-radius:9999px;">
                실사 화보 슬롯
              </div>
            </div>
          </div>

        </div>

        <!-- 4대 자부심 지표 바 -->
        <div class="pride-metrics-bar">
          <div class="metric-item">
            <div class="metric-num">38g</div>
            <div class="metric-label">깃털 같은 초경량</div>
            <div class="metric-sub">0.1mm 초박형 센서 섬유</div>
          </div>
          <div class="metric-item">
            <div class="metric-num">99.8%</div>
            <div class="metric-label">무봉제 은폐율</div>
            <div class="metric-sub">출근복 속에 쏙 숨는 핏</div>
          </div>
          <div class="metric-item">
            <div class="metric-num">300+</div>
            <div class="metric-label"><span class="highlight-peach">전문가 실착 검증</span></div>
            <div class="metric-sub">정형외과 의사·개발자 추천</div>
          </div>
          <div class="metric-item">
            <div class="metric-num">100%</div>
            <div class="metric-label"><span class="highlight-peach">30일 안심 무료 반품</span></div>
            <div class="metric-sub">결제금액 0원 무료 맞교환</div>
          </div>
        </div>

      </div>
    </section>"""

content = re.sub(r'<section class="hero-section"[^>]*>.*?</section>', hero_markup, content, flags=re.DOTALL)

# 3. 탈박스화 오픈 스토리 섹션 마크업
unboxed_story_markup = """<section class="journey-section" id="sec-philosophy">
      <div class="container">
        
        <div style="text-align:center; margin-bottom:56px;">
          <div class="journey-tag">스밈의 철학 · 우리가 걸어온 길</div>
          <h2 style="font-family:var(--font-gowun), serif; font-size:32px; font-weight:800; color:#4A433E; margin-top:12px; letter-spacing:-0.02em;">
            억지로 조이지 않고, 일상 속에 바른 균형이 스며들도록
          </h2>
          <p style="font-size:16px; color:#7A7067; max-width:640px; margin:12px auto 0; line-height:1.7;">
            스밈(SEUMIM)이 탄생한 이유와 3년간의 인체공학 연구 및 300인 전문가 실착 검증 여정을 들려드립니다.
          </p>
        </div>

        <div class="journey-grid">
          
          <!-- 챕터 01 -->
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

          <!-- 챕터 02 -->
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

          <!-- 챕터 03 -->
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

content = re.sub(r'<section class="journey-section"[^>]*>.*?</section>', unboxed_story_markup, content, flags=re.DOTALL)

# 4. 7번 자가진단 위젯 주입
checker_markup = """
      <!-- [7번: 3초 체형 밸런스 파인더 자가진단 위젯] -->
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
          <button class="btn-primary" onclick="filterCatalogByTag('neck')" style="padding:10px 18px; font-size:13px; border-radius:9999px; white-space:nowrap;">
            처방 상품 보러가기 ➔
          </button>
        </div>
      </div>
"""

if 'id="self-checker-sec"' not in content and '</section>\n\n    <!-- ==========================================================================\n         [SEC-06' in content:
    content = content.replace(
        '</section>\n\n    <!-- ==========================================================================\n         [SEC-06',
        '</section>\n\n    ' + checker_markup + '\n\n    <!-- ==========================================================================\n         [SEC-06'
    )

# 5. 필요한 인터랙션 JS 주입
checker_js = """
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
            <div style="font-size:32px; background:#EFF4EE; width:54px; height:54px; border-radius:9999px; display:flex; align-items:center; justify-content:center;">
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

if "function selectCheckerJob" not in content:
    content = content.replace("</head>", "  <script>\n" + checker_js + "  </script>\n</head>")

# 6. 타이틀 업데이트
content = content.replace("<title>SEUMIM (스밈) - 디자인 분석 와이어프레임 (Design Analysis Wireframe)</title>", "<title>SEUMIM (스밈) - 수정 와이어프레임 (Refined Master Wireframe)</title>")

# 저장 대상 파일들
output_files = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

for out_path in output_files:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Perfect Restored and Upgraded: {out_path}")
