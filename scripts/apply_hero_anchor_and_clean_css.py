# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

# 1. 완벽하게 정돈된 통합 단일 Clean CSS (레거시 오버라이드 100% 제거)
clean_unified_css = """
    /* ==========================================================================
       [SEUMIM Clean Master CSS - 2030 Lifestyle Warm Neutral System]
       1. Base Background: 크림 오트밀 (#FDFBF7)
       2. Typography: 웜 브라운 차콜 (#4A433E)
       3. Primary (메인 CTA / 강조): 소프트 피치 코랄 (#E5A99B)
       4. Secondary (상태 알림 / 보조): 뮤티드 세이지 (#B4C4B1)
       5. 1번 유기적 조약돌 둥글기 시스템 (16px ~ 36px, 9999px)
       ========================================================================== */

    :root {
      /* Base & Surfaces */
      --bg-base: #FDFBF7;
      --bg-surface: #F7F3EB;
      --bg-surface-elevated: #EFE8DC;
      --bg-card: #FFFFFF;
      --bg-card-alt: #FDFBF7;

      /* Typography */
      --color-text-primary: #4A433E;
      --color-text-secondary: #7A7067;
      --color-text-muted: #9E9388;
      --color-text-inverse: #FFFFFF;

      /* Primary & Secondary */
      --color-primary: #E5A99B;
      --color-primary-hover: #D49586;
      --color-primary-light: #FDF5F3;
      --color-secondary: #B4C4B1;
      --color-secondary-hover: #9FB39B;
      --color-secondary-light: #EFF4EE;
      --color-secondary-text: #4C6649;

      /* Borders & Shadows */
      --color-border: #E8E1D3;
      --color-border-light: #F2ECE1;
      --shadow-sm: 0 2px 8px rgba(74, 67, 62, 0.04);
      --shadow-md: 0 6px 20px rgba(74, 67, 62, 0.05);
      --shadow-lg: 0 12px 36px rgba(74, 67, 62, 0.07);

      /* Typography fonts */
      --font-gowun: 'Gowun Batang', 'MaruBuri', serif;
      --font-sans: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

      /* Pebble Radiuses */
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 26px;
      --radius-xl: 36px;
      --radius-full: 9999px;

      --container-max: 1240px;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Reset & Base */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; font-family: var(--font-sans); word-break: keep-all; }
    html { scroll-behavior: smooth; font-size: 16px; }
    body {
      background-color: var(--bg-base);
      color: var(--color-text-primary);
      line-height: 1.75;
      letter-spacing: -0.02em;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      padding-top: 117px;
    }
    section, [id^="sec-"], main { scroll-margin-top: 130px; }
    a { text-decoration: none; color: inherit; }
    button { cursor: pointer; border: none; background: none; font-family: inherit; }
    ul { list-style: none; }
    .container { width: 100%; max-width: var(--container-max); margin: 0 auto; padding: 0 clamp(16px, 3.5vw, 28px); }

    /* Top Fixed Switcher Bar */
    .site-header-fixed {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      width: 100%;
      z-index: 1100;
      background: transparent;
      box-shadow: 0 4px 20px rgba(74, 67, 62, 0.06);
    }
    .page-switch-bar {
      background: var(--color-text-primary);
      color: #FFFFFF;
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      border-bottom: 1px solid rgba(255,255,255,0.12);
    }
    .page-switch-tabs { display: flex; gap: 8px; }
    .btn-page-tab {
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: rgba(255,255,255,0.12);
      color: #dedede;
      font-weight: 700;
      font-size: 12.5px;
      transition: var(--transition);
      border: 1px solid rgba(255,255,255,0.18);
    }
    .btn-page-tab:hover, .btn-page-tab.active {
      background: var(--color-primary);
      color: #FFFFFF;
      border-color: var(--color-primary);
    }

    /* GNB */
    .header-gnb {
      background: rgba(253, 251, 247, 0.98);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--color-border);
    }
    .gnb-inner { display: flex; justify-content: space-between; align-items: center; height: 72px; }
    .logo {
      font-family: var(--font-gowun), serif;
      font-size: 24px;
      font-weight: 800;
      color: var(--color-text-primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .logo-badge { font-size: 11px; font-weight: 700; color: var(--color-primary); }
    .gnb-nav { display: flex; gap: 28px; align-items: center; }
    .gnb-link { font-size: 14.5px; font-weight: 700; color: var(--color-text-secondary); transition: var(--transition); position: relative; }
    .gnb-link:hover, .gnb-link.active { color: var(--color-primary); }
    .gnb-link.active::after {
      content: ''; position: absolute; bottom: -8px; left: 0; width: 100%; height: 2px; background: var(--color-primary);
    }
    .gnb-actions { display: flex; gap: 10px; align-items: center; }
    .gnb-text-btn {
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: var(--bg-surface);
      border: 1px solid var(--color-border);
      font-size: 12.5px;
      font-weight: 700;
      color: var(--color-text-primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .gnb-text-btn .btn-badge {
      background: var(--color-primary);
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: var(--radius-full);
    }

    /* 1px 미세 연장선 안내 텍스트 (이솝 에디토리얼 스타일) */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      color: var(--color-primary);
      font-family: var(--font-gowun), serif;
      font-size: 13.5px;
      font-weight: 700;
      letter-spacing: 0.04em;
    }
    .section-tag::before, .section-tag::after,
    .hero-eyebrow::before, .hero-eyebrow::after,
    .catalog-tag::before, .catalog-tag::after,
    .journey-tag::before, .journey-tag::after {
      content: '';
      display: inline-block;
      width: 28px;
      height: 1px;
      background: var(--color-primary);
      opacity: 0.85;
    }

    /* 4번: 피치 코랄 하이라이트 띠 */
    .highlight-peach {
      background: linear-gradient(180deg, transparent 60%, rgba(229, 169, 155, 0.34) 60%);
      display: inline;
      padding: 0 4px;
      font-weight: inherit;
    }

    /* 버튼 시스템: 조약돌 둥근 듀얼 CTA */
    .btn-primary, .btn-accent {
      background: var(--color-primary);
      color: #FFFFFF;
      border: 1.5px solid var(--color-primary);
      border-radius: var(--radius-full);
      box-shadow: 0 4px 14px rgba(229, 169, 155, 0.35);
      font-weight: 700;
      padding: 12px 26px;
      font-size: 14px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: var(--transition);
    }
    .btn-primary:hover, .btn-accent:hover {
      background: var(--color-primary-hover);
      border-color: var(--color-primary-hover);
      transform: translateY(-1px);
    }
    .btn-secondary {
      background: #FFFFFF;
      color: var(--color-text-primary);
      border: 1.5px solid var(--color-primary);
      border-radius: var(--radius-full);
      font-weight: 700;
      padding: 12px 26px;
      font-size: 14px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: var(--transition);
    }
    .btn-secondary:hover {
      background: var(--color-primary-light);
      color: var(--color-primary-hover);
      border-color: var(--color-primary-hover);
    }

    /* ==========================================================================
       [1번: 히어로 2열 스플릿 앰비언트 비주얼 앵커 시스템]
       ========================================================================== */
    .hero-section {
      padding: 60px 0 40px;
      background: var(--bg-base);
    }
    .hero-split-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 44px;
      align-items: center;
      margin-bottom: 48px;
    }
    .hero-content-left {
      text-align: left;
    }
    .hero-content-left .hero-eyebrow {
      justify-content: flex-start;
      margin-bottom: 14px;
    }
    .hero-manifesto-title {
      font-family: var(--font-gowun), serif;
      font-size: 40px;
      font-weight: 800;
      line-height: 1.35;
      color: var(--color-text-primary);
      letter-spacing: -0.02em;
      margin-bottom: 18px;
    }
    .hero-subcopy {
      font-size: 16px;
      color: var(--color-text-secondary);
      line-height: 1.75;
      margin-bottom: 28px;
      max-width: 520px;
    }
    .hero-cta-group {
      display: flex;
      gap: 14px;
      align-items: center;
      flex-wrap: wrap;
    }

    /* 우측 앰비언트 실착 비주얼 프레임 */
    .hero-visual-anchor {
      background: var(--bg-surface);
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-xl);
      padding: 24px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 380px;
    }
    .hero-visual-inner {
      background: #FFFFFF;
      border: 1px dashed var(--color-border);
      border-radius: var(--radius-lg);
      height: 240px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 20px;
      position: relative;
    }
    .hero-visual-badge-top {
      position: absolute;
      top: 14px;
      left: 14px;
      background: #EFF4EE;
      color: #4C6649;
      border: 1px solid #B4C4B1;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 800;
    }
    .hero-visual-caption {
      margin-top: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .hero-caption-title {
      font-family: var(--font-gowun), serif;
      font-size: 15px;
      font-weight: 800;
      color: var(--color-text-primary);
    }
    .hero-caption-desc {
      font-size: 12.5px;
      color: var(--color-text-secondary);
    }

    /* 4대 자부심 지표 바 */
    .pride-metrics-bar {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-xl);
      padding: 28px 36px;
      box-shadow: var(--shadow-sm);
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      text-align: center;
    }
    .metric-item { position: relative; }
    .metric-item:not(:last-child)::after {
      content: '';
      position: absolute;
      right: 0;
      top: 15%;
      height: 70%;
      width: 1px;
      background: var(--color-border);
    }
    .metric-num {
      font-family: var(--font-sans);
      font-size: 34px;
      font-weight: 900;
      color: var(--color-text-primary);
      line-height: 1.1;
      margin-bottom: 6px;
    }
    .metric-label { font-size: 13.5px; font-weight: 800; color: var(--color-text-primary); }
    .metric-sub { font-size: 11.5px; color: var(--color-text-muted); margin-top: 3px; }

    /* 탈박스화 브랜드 스토리 섹션 */
    .journey-section { padding: 80px 0; background: var(--bg-base); }
    .journey-grid { display: flex; flex-direction: column; gap: 64px; max-width: 1080px; margin: 0 auto; }
    .journey-chapter-row {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 48px;
      align-items: center;
      padding-bottom: 56px;
      border-bottom: 1px solid var(--color-border);
    }
    .journey-chapter-row:last-child { border-bottom: none; padding-bottom: 0; }
    .journey-visual-open {
      background: var(--bg-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 32px 24px;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }
    .journey-text-open .journey-tag { justify-content: flex-start; margin-bottom: 10px; }
    .journey-text-open h3 {
      font-family: var(--font-gowun), serif;
      font-size: 25px;
      font-weight: 800;
      color: var(--color-text-primary);
      line-height: 1.45;
      margin-bottom: 16px;
    }
    .journey-text-open p { font-size: 15px; color: var(--color-text-secondary); line-height: 1.8; margin-bottom: 14px; }
    .journey-quote-box {
      background: var(--bg-surface);
      border-left: 3px solid var(--color-primary);
      border-radius: 0 12px 12px 0;
      padding: 14px 18px;
      margin-top: 16px;
    }
    .journey-quote-box p { margin: 0; font-size: 14px; color: var(--color-text-primary); font-weight: 600; }

    /* 3대 대표작 집중 조명 카드 */
    .featured-grid { display: flex; flex-direction: column; gap: 36px; margin: 40px 0; }
    .featured-card {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: 36px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
      align-items: center;
      box-shadow: var(--shadow-md);
    }

    /* 7번: 3초 자가진단 위젯 */
    .balance-checker-container {
      background: var(--bg-surface);
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-xl);
      padding: 36px 32px;
      margin: 48px auto;
      max-width: 980px;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }
    .checker-chip-grid { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 20px 0 24px; }
    .checker-chip {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-full);
      padding: 10px 18px;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--color-text-primary);
      transition: var(--transition);
      font-family: var(--font-gowun), serif;
    }
    .checker-chip:hover { border-color: var(--color-primary); transform: translateY(-2px); }
    .checker-chip.active {
      background: var(--color-primary);
      color: #FFFFFF;
      border-color: var(--color-primary);
      box-shadow: 0 4px 12px rgba(229, 169, 155, 0.35);
    }
    .checker-result-card {
      background: #FFFFFF;
      border: 1.5px solid var(--color-secondary);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      text-align: left;
    }

    /* 6번: 가로 스냅 슬라이더 */
    .horizontal-slider-wrapper { position: relative; margin: 24px 0; }
    .horizontal-snap-track {
      display: flex;
      gap: 20px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scroll-behavior: smooth;
      padding: 12px 4px 24px;
      -webkit-overflow-scrolling: touch;
    }
    .horizontal-snap-track::-webkit-scrollbar { height: 6px; }
    .horizontal-snap-track::-webkit-scrollbar-track { background: var(--bg-surface); border-radius: var(--radius-full); }
    .horizontal-snap-track::-webkit-scrollbar-thumb { background: var(--color-primary); border-radius: var(--radius-full); }
    .horizontal-snap-track > * { scroll-snap-align: start; flex: 0 0 280px; max-width: 280px; }
    .slider-nav-btn {
      position: absolute;
      top: 45%;
      transform: translateY(-50%);
      width: 40px;
      height: 40px;
      border-radius: var(--radius-full);
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      color: var(--color-text-primary);
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
      z-index: 10;
      transition: var(--transition);
    }
    .slider-nav-btn:hover { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); }
    .slider-nav-prev { left: -16px; }
    .slider-nav-next { right: -16px; }

    /* 15종 One-View 카드 */
    .one-view-card {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      transition: var(--transition);
    }
    .one-view-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); border-color: var(--color-primary); }

    /* 9번: 300인 전문가 임상 갤러리 */
    .clinical-proof-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 28px 0; }
    .clinical-card {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-md);
      padding: 24px;
      text-align: left;
      box-shadow: var(--shadow-sm);
    }
    .clinical-rating { color: var(--color-primary); font-size: 14px; font-weight: 800; margin-bottom: 8px; }

    /* 10번: 조약돌 아코디언 FAQ */
    .faq-item {
      background: #FFFFFF;
      border: 1.5px solid var(--color-border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin-bottom: 14px;
      cursor: pointer;
      transition: var(--transition);
    }
    .faq-item:hover { border-color: var(--color-primary); box-shadow: var(--shadow-sm); }
    .faq-item.open { background: var(--bg-card-alt); border-color: var(--color-secondary); }
    .faq-question {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-gowun), serif;
      font-size: 16px;
      font-weight: 800;
      color: var(--color-text-primary);
    }
    .faq-answer {
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px dashed var(--color-border);
      font-size: 14.5px;
      color: var(--color-text-secondary);
      line-height: 1.7;
    }

    /* 하단 플로팅 고정 바 */
    .floating-bottom-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--color-text-primary);
      color: var(--bg-base);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
      border-top: 1px solid rgba(255,255,255,0.12);
      box-shadow: 0 -4px 20px rgba(74, 67, 62, 0.12);
    }
    .floating-bottom-bar .badge-price {
      background: var(--color-primary);
      color: #FFFFFF;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      margin-right: 8px;
    }

    /* Responsive */
    @media (max-width: 992px) {
      .hero-split-grid { grid-template-columns: 1fr; gap: 32px; }
      .hero-content-left { text-align: center; }
      .hero-content-left .hero-eyebrow { justify-content: center; }
      .hero-cta-group { justify-content: center; }
      .pride-metrics-bar { grid-template-columns: repeat(2, 1fr); }
      .metric-item:nth-child(2)::after { display: none; }
      .featured-card { grid-template-columns: 1fr; }
      .clinical-proof-grid { grid-template-columns: 1fr; }
    }
"""

# 2. 새로운 2열 스플릿 히어로 HTML (시각적 앵커 슬롯 탑재)
new_hero_split_html = """<section class="hero-section" id="sec-manifesto">
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
              <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:4px;">
                [일상 실착 앰비언트 무드컷]
              </div>
              <div style="font-size:12.5px; color:var(--color-text-secondary); line-height:1.5;">
                셔츠 속에 0.1mm 초슬림 넥&숄더 밴드를 착용하고<br>편안하게 데스크 업무를 보는 자연스러운 일상 실루엣
              </div>
            </div>
            <div class="hero-visual-caption">
              <div>
                <div class="hero-caption-title">0.1mm 초박형 센서 섬유 직조</div>
                <div class="hero-caption-desc">38g 깃털 같은 무게로 피로도 제로</div>
              </div>
              <div style="font-size:11.5px; font-weight:800; color:var(--color-primary); background:var(--color-primary-light); padding:4px 10px; border-radius:var(--radius-full);">
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

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. <style>...</style> 태그 전체를 clean_unified_css로 전면 교체
    content = re.sub(r'<style>.*?</style>', '<style>' + clean_unified_css + '\n  </style>', content, flags=re.DOTALL)

    # 2. <head> 내 미사용 임시 JS 함수들 제거 (간결화)
    content = re.sub(r'<script>\s*window\.switchColorPalette\s*=.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*function applyBgThemeDirect.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*function applyRadiusThemeDirect.*?</script>', '', content, flags=re.DOTALL)

    # 3. 히어로 섹션 마크업을 new_hero_split_html로 교체
    content = re.sub(r'<section class="hero-section"[^>]*>.*?</section>', new_hero_split_html, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Refactored Clean Master CSS & Built Hero Visual Split Grid in {path}")
