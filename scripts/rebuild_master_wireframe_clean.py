# -*- coding: utf-8 -*-
import re

# 디자인 분석 와이어프레임에서 순수 HTML 뼈대(body 내부 전체)를 추출하고,
# 단 하나의 최상위 무결 2030 웜 뉴트럴 Master CSS와 스크립트를 결합합니다.

src_path = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\디자인 분석 와이어프레임.html'
with open(src_path, 'r', encoding='utf-8') as f:
    full_text = f.read()

# 1. <body> 태그 내부 전체 추출
body_match = re.search(r'<body[^>]*>(.*?)</body>', full_text, flags=re.DOTALL)
if body_match:
    body_inner = body_match.group(1)
else:
    print("Error: Could not extract body")
    exit(1)

# 2. 마스터 클린 CSS 정의 (모든 컴포넌트의 완벽한 웜 뉴트럴 4색 & 조약돌 둥글기 & 5대 요소)
master_css = """
    /* ==========================================================================
       [SEUMIM Masterpiece 2030 Warm Neutral CSS]
       Base: #FDFBF7 (크림 오트밀) | Text: #4A433E (웜 브라운 차콜)
       Primary: #E5A99B (소프트 피치 코랄) | Secondary: #B4C4B1 (뮤티드 세이지)
       ========================================================================== */
    :root {
      --bg-base: #FDFBF7;
      --bg-surface: #F7F3EB;
      --bg-surface-elevated: #EFE8DC;
      --bg-card: #FFFFFF;
      --bg-card-hover: #FAF6EE;
      --color-text-primary: #4A433E;
      --color-text-secondary: #7A7067;
      --color-text-muted: #9E9388;
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
      --font-gowun: 'Gowun Batang', serif;
      --font-serif: 'Gowun Batang', serif;
      --font-maruburi: 'Gowun Batang', serif;
      --font-sans: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 26px;
      --radius-xl: 36px;
      --radius-full: 9999px;
      --shadow-sm: 0 2px 8px rgba(74, 67, 62, 0.04);
      --shadow-md: 0 6px 20px rgba(74, 67, 62, 0.05);
      --shadow-lg: 0 14px 36px rgba(74, 67, 62, 0.07);
      --container-max: 1240px;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; font-family: var(--font-sans); word-break: keep-all; }
    html { scroll-behavior: smooth; font-size: 16px; }
    body {
      background-color: var(--bg-base) !important;
      color: var(--color-text-primary) !important;
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

    /* Top Switcher Bar */
    .site-header-fixed {
      position: fixed;
      top: 0; left: 0; right: 0; width: 100%; z-index: 1100;
      background: transparent;
      box-shadow: 0 4px 20px rgba(74, 67, 62, 0.06);
    }
    .page-switch-bar {
      background: #4A433E; color: #FFFFFF; padding: 10px 24px;
      display: flex; justify-content: space-between; align-items: center; font-size: 13px;
      border-bottom: 1px solid rgba(255,255,255,0.12);
    }
    .page-switch-tabs { display: flex; gap: 8px; }
    .btn-page-tab {
      padding: 6px 14px; border-radius: var(--radius-full);
      background: rgba(255,255,255,0.12); color: #dedede; font-weight: 700; font-size: 12.5px;
      transition: var(--transition); border: 1px solid rgba(255,255,255,0.18);
    }
    .btn-page-tab:hover, .btn-page-tab.active { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); }

    /* Page Views */
    .page-view { display: none; }
    .page-view.active { display: block; animation: fadeIn 0.35s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* Header GNB */
    .header-gnb { background: rgba(253, 251, 247, 0.98); backdrop-filter: blur(12px); border-bottom: 1px solid var(--color-border); }
    .gnb-inner { display: flex; justify-content: space-between; align-items: center; height: 72px; }
    .logo { font-family: var(--font-gowun), serif; font-size: 24px; font-weight: 800; color: var(--color-text-primary); display: flex; align-items: center; gap: 6px; }
    .logo-badge { font-size: 11px; font-weight: 700; color: var(--color-primary); }
    .gnb-nav { display: flex; gap: 28px; align-items: center; }
    .gnb-link { font-size: 14.5px; font-weight: 700; color: var(--color-text-secondary); transition: var(--transition); position: relative; }
    .gnb-link:hover, .gnb-link.active { color: var(--color-primary); }
    .gnb-link.active::after { content: ''; position: absolute; bottom: -8px; left: 0; width: 100%; height: 2px; background: var(--color-primary); }
    .gnb-actions { display: flex; gap: 10px; align-items: center; }
    .gnb-text-btn {
      padding: 7px 16px; border-radius: var(--radius-full); background: var(--bg-surface);
      border: 1px solid var(--color-border); font-size: 12.5px; font-weight: 700; color: var(--color-text-primary);
      display: flex; align-items: center; gap: 6px;
    }
    .gnb-text-btn .btn-badge { background: var(--color-primary); color: #FFFFFF; font-size: 10px; font-weight: 800; padding: 2px 6px; border-radius: var(--radius-full); }

    /* 1px 미세선 이솝 스타일 */
    .section-tag, .hero-eyebrow, .catalog-tag, .journey-tag {
      display: flex !important; align-items: center !important; justify-content: center !important; gap: 14px !important;
      color: var(--color-primary) !important; font-family: var(--font-gowun), serif !important; font-size: 13.5px !important;
      font-weight: 700 !important; background: transparent !important; border: none !important; padding: 0 !important;
    }
    .section-tag::before, .section-tag::after,
    .hero-eyebrow::before, .hero-eyebrow::after,
    .catalog-tag::before, .catalog-tag::after,
    .journey-tag::before, .journey-tag::after {
      content: '' !important; display: inline-block !important; width: 28px !important; height: 1px !important;
      background: var(--color-primary) !important; opacity: 0.85 !important;
    }

    /* 4번: 피치 코랄 틴트 띠 */
    .highlight-peach {
      background: linear-gradient(180deg, transparent 60%, rgba(229, 169, 155, 0.34) 60%) !important;
      display: inline !important; padding: 0 4px !important;
    }

    /* 조약돌 둥근 듀얼 CTA */
    .btn-primary, .btn-accent, .floating-bottom-bar .btn-accent {
      background: var(--color-primary) !important; color: #FFFFFF !important;
      border: 1.5px solid var(--color-primary) !important; border-radius: var(--radius-full) !important;
      box-shadow: 0 4px 14px rgba(229, 169, 155, 0.35) !important; font-weight: 700 !important;
      padding: 12px 26px !important; font-size: 14px !important; display: inline-flex !important;
      align-items: center !important; justify-content: center !important; gap: 6px !important; transition: var(--transition) !important;
    }
    .btn-primary:hover, .btn-accent:hover { background: var(--color-primary-hover) !important; border-color: var(--color-primary-hover) !important; transform: translateY(-1px) !important; }
    .btn-secondary {
      background: #FFFFFF !important; color: var(--color-text-primary) !important;
      border: 1.5px solid var(--color-primary) !important; border-radius: var(--radius-full) !important;
      font-weight: 700 !important; padding: 12px 26px !important; font-size: 14px !important;
      display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; transition: var(--transition) !important;
    }
    .btn-secondary:hover { background: var(--color-primary-light) !important; color: var(--color-primary-hover) !important; border-color: var(--color-primary-hover) !important; }

    /* 히어로 2열 스플릿 앵커 레이아웃 */
    .hero-section { padding: 60px 0 40px; background: var(--bg-base); }
    .hero-split-grid { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 44px; align-items: center; margin-bottom: 48px; }
    .hero-content-left { text-align: left; }
    .hero-content-left .hero-eyebrow { justify-content: flex-start !important; margin-bottom: 14px; }
    .hero-manifesto-title { font-family: var(--font-gowun), serif; font-size: 40px; font-weight: 800; line-height: 1.35; color: var(--color-text-primary); letter-spacing: -0.02em; margin-bottom: 18px; }
    .hero-subcopy { font-size: 16px; color: var(--color-text-secondary); line-height: 1.75; margin-bottom: 28px; max-width: 520px; }
    .hero-cta-group { display: flex; gap: 14px; align-items: center; flex-wrap: wrap; }

    .hero-visual-anchor {
      background: var(--bg-surface); border: 1.5px solid var(--color-border); border-radius: var(--radius-xl);
      padding: 24px; box-shadow: var(--shadow-md); display: flex; flex-direction: column; justify-content: space-between; height: 380px;
    }
    .hero-visual-inner {
      background: #FFFFFF; border: 1px dashed var(--color-border); border-radius: 22px; height: 240px;
      display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 20px; position: relative;
    }
    .hero-visual-badge-top { position: absolute; top: 14px; left: 14px; background: #EFF4EE; color: #4C6649; border: 1px solid #B4C4B1; padding: 4px 10px; border-radius: var(--radius-full); font-size: 11px; font-weight: 800; }
    .hero-visual-caption { margin-top: 14px; display: flex; justify-content: space-between; align-items: center; }
    .hero-caption-title { font-family: var(--font-gowun), serif; font-size: 15px; font-weight: 800; color: var(--color-text-primary); }
    .hero-caption-desc { font-size: 12.5px; color: var(--color-text-secondary); }

    /* 4대 자부심 지표 바 */
    .pride-metrics-bar {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-xl);
      padding: 28px 36px; box-shadow: var(--shadow-sm); display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center;
    }
    .metric-item { position: relative; }
    .metric-item:not(:last-child)::after { content: ''; position: absolute; right: 0; top: 15%; height: 70%; width: 1px; background: var(--color-border); }
    .metric-num { font-size: 34px; font-weight: 900; color: var(--color-text-primary); line-height: 1.1; margin-bottom: 6px; }
    .metric-label { font-size: 13.5px; font-weight: 800; color: var(--color-text-primary); }
    .metric-sub { font-size: 11.5px; color: var(--color-text-muted); margin-top: 3px; }

    /* 탈박스화 브랜드 스토리 섹션 */
    .journey-section { padding: 80px 0; background: var(--bg-base); }
    .journey-grid { display: flex; flex-direction: column; gap: 64px; max-width: 1080px; margin: 0 auto; }
    .journey-chapter-row { display: grid; grid-template-columns: 1fr 1.2fr; gap: 48px; align-items: center; padding-bottom: 56px; border-bottom: 1px solid var(--color-border); }
    .journey-chapter-row:last-child { border-bottom: none; padding-bottom: 0; }
    .journey-visual-open { background: var(--bg-surface); border: 1px solid var(--color-border); border-radius: 22px; padding: 32px 24px; text-align: center; box-shadow: var(--shadow-sm); }
    .journey-text-open .journey-tag { justify-content: flex-start !important; margin-bottom: 10px; }
    .journey-text-open h3 { font-family: var(--font-gowun), serif; font-size: 25px; font-weight: 800; color: var(--color-text-primary); line-height: 1.45; margin-bottom: 16px; }
    .journey-text-open p { font-size: 15px; color: var(--color-text-secondary); line-height: 1.8; margin-bottom: 14px; }
    .journey-quote-box { background: var(--bg-surface); border-left: 3px solid var(--color-primary); border-radius: 0 12px 12px 0; padding: 14px 18px; margin-top: 16px; }
    .journey-quote-box p { margin: 0; font-size: 14px; color: var(--color-text-primary); font-weight: 600; }

    /* 3대 대표작 집중 조명 */
    .featured-grid { display: flex; flex-direction: column; gap: 36px; margin: 40px 0; }
    .featured-card {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-lg);
      padding: 36px; display: grid; grid-template-columns: 1fr 1fr; gap: 36px; align-items: center; box-shadow: var(--shadow-md);
    }

    /* 7번: 3초 자가진단 위젯 */
    .balance-checker-container {
      background: var(--bg-surface); border: 1.5px solid var(--color-border); border-radius: var(--radius-xl);
      padding: 36px 32px; margin: 48px auto; max-width: 980px; box-shadow: var(--shadow-sm); text-align: center;
    }
    .checker-chip-grid { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 20px 0 24px; }
    .checker-chip {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-full);
      padding: 10px 18px; font-size: 13.5px; font-weight: 700; color: var(--color-text-primary);
      transition: var(--transition); font-family: var(--font-gowun), serif;
    }
    .checker-chip:hover { border-color: var(--color-primary); transform: translateY(-2px); }
    .checker-chip.active { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); box-shadow: 0 4px 12px rgba(229, 169, 155, 0.35); }
    .checker-result-card {
      background: #FFFFFF; border: 1.5px solid var(--color-secondary); border-radius: var(--radius-md);
      padding: 18px 22px; display: flex; align-items: center; justify-content: space-between; gap: 16px; text-align: left;
    }

    /* 6번: 15종 가로 스냅 슬라이더 */
    .showcase-tabs { display: flex; justify-content: center; gap: 10px; margin: 28px 0 32px; flex-wrap: wrap; }
    .tab-btn {
      padding: 9px 20px; border-radius: var(--radius-full); background: #FFFFFF;
      border: 1.5px solid var(--color-border); font-size: 13.5px; font-weight: 700; color: var(--color-text-secondary); transition: var(--transition);
    }
    .tab-btn:hover, .tab-btn.active { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); }

    .horizontal-slider-wrapper { position: relative; margin: 24px 0; }
    .horizontal-snap-track {
      display: flex; gap: 20px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-behavior: smooth;
      padding: 12px 4px 24px; -webkit-overflow-scrolling: touch;
    }
    .horizontal-snap-track::-webkit-scrollbar { height: 6px; }
    .horizontal-snap-track::-webkit-scrollbar-track { background: var(--bg-surface); border-radius: var(--radius-full); }
    .horizontal-snap-track::-webkit-scrollbar-thumb { background: var(--color-primary); border-radius: var(--radius-full); }
    .horizontal-snap-track > * { scroll-snap-align: start; flex: 0 0 280px; max-width: 280px; }
    .slider-nav-btn {
      position: absolute; top: 45%; transform: translateY(-50%); width: 40px; height: 40px; border-radius: var(--radius-full);
      background: #FFFFFF; border: 1.5px solid var(--color-border); color: var(--color-text-primary); font-size: 18px;
      display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: var(--shadow-sm); z-index: 10; transition: var(--transition);
    }
    .slider-nav-btn:hover { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); }
    .slider-nav-prev { left: -16px; }
    .slider-nav-next { right: -16px; }

    /* 15종 One-View 카드 */
    .one-view-card {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-md);
      padding: 22px; box-shadow: var(--shadow-sm); display: flex; flex-direction: column; justify-content: space-between; transition: var(--transition);
    }
    .one-view-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); border-color: var(--color-primary); }

    /* 9번: 300인 전문가 임상 갤러리 */
    .clinical-proof-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 28px 0; }
    .clinical-card { background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-md); padding: 24px; text-align: left; box-shadow: var(--shadow-sm); }
    .clinical-rating { color: var(--color-primary); font-size: 14px; font-weight: 800; margin-bottom: 8px; }

    /* 10번: 조약돌 아코디언 FAQ */
    .faq-container { max-width: 880px; margin: 60px auto; }
    .faq-item {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-md);
      padding: 20px 24px; margin-bottom: 14px; cursor: pointer; transition: var(--transition);
    }
    .faq-item:hover { border-color: var(--color-primary); box-shadow: var(--shadow-sm); }
    .faq-item.open { background: var(--bg-card-alt); border-color: var(--color-secondary); }
    .faq-question { display: flex; justify-content: space-between; align-items: center; font-family: var(--font-gowun), serif; font-size: 16px; font-weight: 800; color: var(--color-text-primary); }
    .faq-answer { margin-top: 14px; padding-top: 14px; border-top: 1px dashed var(--color-border); font-size: 14.5px; color: var(--color-text-secondary); line-height: 1.7; }

    /* HUD & 케어 센터 & 기타 공통 카드 */
    .hud-card, .center-card, .proof-stat-card, .review-card, .explore-catalog-banner, .fit-finder-banner {
      background: #FFFFFF; border: 1.5px solid var(--color-border); border-radius: var(--radius-md); padding: 28px; box-shadow: var(--shadow-sm);
    }

    /* 플로팅 바 */
    .floating-bottom-bar {
      position: fixed; bottom: 0; left: 0; right: 0; background: #4A433E; color: #FDFBF7;
      padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; z-index: 1000;
      border-top: 1px solid rgba(255,255,255,0.12); box-shadow: 0 -4px 20px rgba(74, 67, 62, 0.12);
    }
    .floating-bottom-bar .badge-price { background: var(--color-primary); color: #FFFFFF; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: var(--radius-full); margin-right: 8px; }

    /* 반응형 */
    @media (max-width: 992px) {
      .hero-split-grid { grid-template-columns: 1fr; gap: 32px; }
      .hero-content-left { text-align: center; }
      .hero-content-left .hero-eyebrow { justify-content: center !important; }
      .hero-cta-group { justify-content: center; }
      .pride-metrics-bar { grid-template-columns: repeat(2, 1fr); }
      .metric-item:nth-child(2)::after { display: none; }
      .featured-card { grid-template-columns: 1fr; }
      .clinical-proof-grid { grid-template-columns: 1fr; }
      .journey-chapter-row { grid-template-columns: 1fr; }
    }
"""

# 3. HTML 마크업 업데이트 (히어로 2열 앵커, 탈박스화 스토리, 7번 자가진단 위젯 주입)
hero_html = """<section class="hero-section" id="sec-manifesto">
      <div class="container">
        <div class="hero-split-grid">
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

story_html = """<section class="journey-section" id="sec-philosophy">
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

checker_html = """
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

body_inner = re.sub(r'<section class="hero-section"[^>]*>.*?</section>', hero_html, body_inner, flags=re.DOTALL)
body_inner = re.sub(r'<section class="journey-section"[^>]*>.*?</section>', story_html, body_inner, flags=re.DOTALL)

if 'id="self-checker-sec"' not in body_inner:
    body_inner = re.sub(
        r'(</section>\s*<!-- ==========================================================================\s*\[SEC-06)',
        r'\n' + checker_html + r'\n\1',
        body_inner
    )

# 4. 완전체 HTML 조립
final_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEUMIM (스밈) - 수정 와이어프레임 (Refined Master Wireframe)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gowun+Dodum&family=IBM+Plex+Mono:wght@400;600&family=Noto+Serif+KR:wght@400;700&family=Pretendard:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
{master_css}
  </style>
</head>
<body>
{body_inner}
</body>
</html>
"""

output_files = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

for out_path in output_files:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Completely rebuilt without breaking: {out_path}")
