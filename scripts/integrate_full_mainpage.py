# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

# 메인페이지 완전체 마크업
main_page_html = """  <!-- ==========================================================================
       [PAGE 1: 메인 웰니스 경험 롱스크롤 랜딩페이지 (Main Landing)]
       ========================================================================== -->
  <main id="page-main" class="page-view active">

    <!-- SEC-01: 히어로 2열 스플릿 (매니페스토 + 0.1mm 일상 실착 앰비언트 비주얼 앵커) -->
    <section class="hero-section" id="sec-manifesto">
      <div class="container">
        
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
    </section>

    <!-- SEC-02: 브랜드 철학 & 걸어온 길 (완전 탈박스화 오픈 에디토리얼 레이아웃) -->
    <section class="journey-section" id="sec-philosophy">
      <div class="container">
        
        <div style="text-align:center; margin-bottom:56px;">
          <div class="journey-tag">스밈의 철학 · 우리가 걸어온 길</div>
          <h2 style="font-family:var(--font-gowun), serif; font-size:32px; font-weight:800; color:var(--color-text-primary); margin-top:12px; letter-spacing:-0.02em;">
            억지로 조이지 않고, 일상 속에 바른 균형이 스며들도록
          </h2>
          <p style="font-size:16px; color:var(--color-text-secondary); max-width:640px; margin:12px auto 0; line-height:1.7;">
            스밈(SEUMIM)이 탄생한 이유와 3년간의 인체공학 연구 및 300인 전문가 실착 검증 여정을 들려드립니다.
          </p>
        </div>

        <div class="journey-grid">
          
          <!-- 챕터 01: 탄생 배경 -->
          <div class="journey-chapter-row">
            <div class="journey-visual-open">
              <div style="font-size:36px; margin-bottom:12px;">🧵</div>
              <div style="font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">[3년 450번의 원사 배합 실험]</div>
              <p style="font-size:14px; color:var(--color-text-secondary); line-height:1.6; margin:0;">
                머리카락보다 얇은 나노 탄성 섬유를 무봉제로 직조하여 이물감 제로와 100회 물세탁 내구성을 완성했습니다.
              </p>
              <div style="margin-top:14px; display:inline-block; padding:4px 12px; background:#FFFFFF; border-radius:var(--radius-full); border:1px solid var(--color-border); font-size:12px; color:var(--color-primary); font-weight:700;">
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
              <div style="font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">[기존 강제 교정기 vs 스밈 0.1mm 코어웨어]</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:12px; text-align:left;">
                <div style="background:#FFFFFF; padding:10px 12px; border-radius:12px; border:1px solid var(--color-border); font-size:12.5px;">
                  <span style="color:#C25442; font-weight:800;">기존 교정기 ✕</span><br>
                  • 250g 무거운 쇠 와이어<br>
                  • 숨 막히는 강제 늑골 압박
                </div>
                <div style="background:#FFFFFF; padding:10px 12px; border-radius:12px; border:1px solid var(--color-secondary); font-size:12.5px;">
                  <span style="color:var(--color-secondary-text); font-weight:800;">스밈 0.1mm ◯</span><br>
                  • 38g 깃털 같은 초경량<br>
                  • 99.8% 옷 속 완벽 은폐
                </div>
              </div>
            </div>
          </div>

          <!-- 챕터 03: 전문가 실착 임상과 철학 -->
          <div class="journey-chapter-row">
            <div class="journey-visual-open">
              <div style="font-size:36px; margin-bottom:12px;">🩺</div>
              <div style="font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">[300+ 현업 전문가 실착 임상 검증]</div>
              <p style="font-size:14px; color:var(--color-text-secondary); line-height:1.6; margin:0;">
                정형외과 의사, 물리치료사, IT 개발자들이 3주간 일상에서 착용하고 통증 87% 감소 효과를 직접 검증했습니다.
              </p>
              <div style="margin-top:14px; display:inline-block; padding:4px 12px; background:var(--color-secondary-light); border-radius:var(--radius-full); border:1px solid var(--color-secondary); font-size:12px; color:var(--color-secondary-text); font-weight:700;">
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
    </section>

    <!-- SEC-03: 3대 시그니처 대표 상품 집중 조명 (Featured Masterpieces) -->
    <section class="container" id="sec-featured" style="padding:40px 24px;">
      <div style="text-align:center; margin-bottom:44px;">
        <div class="section-tag">스밈 대표 시그니처 3선</div>
        <h2 class="section-title" style="font-size:32px; font-weight:800; margin-top:10px;">
          스밈을 대표하는 3대 시그니처 마스터피스
        </h2>
        <p style="font-size:15px; color:var(--color-text-secondary); max-width:600px; margin:8px auto 0;">
          단순한 보정 속옷이 아닙니다. 특허받은 0.1mm 심리스 기술과 인체공학적 지레 탄성 구조가 집약된 3대 역작입니다.
        </p>
      </div>

      <div class="featured-grid">
        <!-- 대표 1: 0.1mm 심리스 넥&숄더 밴드 -->
        <div class="featured-card">
          <div style="background:var(--bg-surface); padding:28px; border-radius:var(--radius-md); text-align:center; border:1px solid var(--color-border);">
            <div style="font-size:38px; margin-bottom:10px;">🧣</div>
            <div style="font-family:var(--font-gowun), serif; font-size:18px; font-weight:800; color:var(--color-text-primary);">[3D 단면 분해 조립도]</div>
            <div style="font-size:13px; color:var(--color-text-secondary); margin-top:6px;">초박형 센서 원사 + 전면 네오디뮴 원터치 자석 버클</div>
            <button class="btn-secondary" style="margin-top:16px; font-size:12.5px; padding:6px 14px;" onclick="openQuickView(1)">🔍 3D 단면 분해 퀵뷰</button>
          </div>
          <div>
            <div style="display:flex; gap:8px; margin-bottom:10px;">
              <span class="section-tag" style="font-size:12px;">👑 베스트 1위 시그니처</span>
              <span style="font-size:11px; font-weight:700; color:var(--color-secondary-text); background:var(--color-secondary-light); padding:3px 8px; border-radius:var(--radius-full);">말린어깨 · 거북목 특화</span>
            </div>
            <h3 style="font-family:var(--font-gowun), serif; font-size:24px; font-weight:800; color:var(--color-text-primary); margin-bottom:10px;">
              [대표 1] 0.1mm 심리스 넥&amp;숄더 밴드
            </h3>
            <p style="font-size:14.5px; color:var(--color-text-secondary); line-height:1.7; margin-bottom:16px;">
              쇄골과 견갑골을 억지로 뒤로 꺾지 않고, 전면 자석 버클의 가벼운 당김으로 어깨가 스스로 펴지도록 유도합니다. 얇은 흰 셔츠 속 99.8% 은폐율을 자랑합니다.
            </p>
            <div style="font-size:20px; font-weight:900; color:var(--color-primary); margin-bottom:16px;">
              59,000원 <span style="font-size:14px; text-decoration:line-through; color:var(--color-text-muted); font-weight:400;">89,000원</span>
            </div>
            <div style="display:flex; gap:10px;">
              <button class="btn-primary" onclick="openCheckoutModal('[대표 1] 0.1mm 심리스 넥&숄더 밴드', 'M (95~100)')">30일 무료 시착 신청 (0원)</button>
              <button class="btn-secondary" onclick="openQuickView(1)">상세보기</button>
            </div>
          </div>
        </div>

        <!-- 대표 2: 3D 에어로 메쉬 척추 정렬 조끼 -->
        <div class="featured-card">
          <div>
            <div style="display:flex; gap:8px; margin-bottom:10px;">
              <span class="section-tag" style="font-size:12px;">⭐ 척추 기립근 강화</span>
              <span style="font-size:11px; font-weight:700; color:var(--color-secondary-text); background:var(--color-secondary-light); padding:3px 8px; border-radius:var(--radius-full);">출근복 속 은폐 지퍼</span>
            </div>
            <h3 style="font-family:var(--font-gowun), serif; font-size:24px; font-weight:800; color:var(--color-text-primary); margin-bottom:10px;">
              [대표 2] 3D 에어로 메쉬 척추 정렬 조끼
            </h3>
            <p style="font-size:14.5px; color:var(--color-text-secondary); line-height:1.7; margin-bottom:16px;">
              등 뒤 4개의 탄성 프레임이 척추 기립근의 무너짐을 막아줍니다. 쿨링 에어로 메쉬 소재로 한여름 출근 정장 속에서도 쾌적하게 착용할 수 있습니다.
            </p>
            <div style="font-size:20px; font-weight:900; color:var(--color-primary); margin-bottom:16px;">
              89,000원 <span style="font-size:14px; text-decoration:line-through; color:var(--color-text-muted); font-weight:400;">129,000원</span>
            </div>
            <div style="display:flex; gap:10px;">
              <button class="btn-primary" onclick="openCheckoutModal('[대표 2] 3D 에어로 메쉬 척추 정렬 조끼', 'L (100~105)')">30일 무료 시착 신청 (0원)</button>
              <button class="btn-secondary" onclick="openQuickView(6)">상세보기</button>
            </div>
          </div>
          <div style="background:var(--bg-surface); padding:28px; border-radius:var(--radius-md); text-align:center; border:1px solid var(--color-border);">
            <div style="font-size:38px; margin-bottom:10px;">🦺</div>
            <div style="font-family:var(--font-gowun), serif; font-size:18px; font-weight:800; color:var(--color-text-primary);">[4중 탄성 프레임 단면]</div>
            <div style="font-size:13px; color:var(--color-text-secondary); margin-top:6px;">초경량 에어로 메쉬 + 척추 좌우 비대칭 차단</div>
            <button class="btn-secondary" style="margin-top:16px; font-size:12.5px; padding:6px 14px;" onclick="openQuickView(6)">🔍 3D 단면 분해 퀵뷰</button>
          </div>
        </div>

        <!-- 대표 3: 골반 수평 유지 에어셀 벨트 -->
        <div class="featured-card">
          <div style="background:var(--bg-surface); padding:28px; border-radius:var(--radius-md); text-align:center; border:1px solid var(--color-border);">
            <div style="font-size:38px; margin-bottom:10px;">🩲</div>
            <div style="font-family:var(--font-gowun), serif; font-size:18px; font-weight:800; color:var(--color-text-primary);">[동적 에어셀 공기압 밸브]</div>
            <div style="font-size:13px; color:var(--color-text-secondary); margin-top:6px;">착석 시 다리 꼬기 물리적 방지 공기 흐름 제어</div>
            <button class="btn-secondary" style="margin-top:16px; font-size:12.5px; padding:6px 14px;" onclick="openQuickView(11)">🔍 3D 단면 분해 퀵뷰</button>
          </div>
          <div>
            <div style="display:flex; gap:8px; margin-bottom:10px;">
              <span class="section-tag" style="font-size:12px;">⭐ 골반 비대칭 차단</span>
              <span style="font-size:11px; font-weight:700; color:var(--color-secondary-text); background:var(--color-secondary-light); padding:3px 8px; border-radius:var(--radius-full);">다리 꼬기 완화</span>
            </div>
            <h3 style="font-family:var(--font-gowun), serif; font-size:24px; font-weight:800; color:var(--color-text-primary); margin-bottom:10px;">
              [대표 3] 골반 수평 유지 에어셀 벨트
            </h3>
            <p style="font-size:14.5px; color:var(--color-text-secondary); line-height:1.7; margin-bottom:16px;">
              의자에 앉았을 때 무의식적으로 다리를 꼬면 에어셀 내부 압력이 이동하여 불편함을 인지시키고, 골반 좌우 수평을 바르게 지탱해 줍니다.
            </p>
            <div style="font-size:20px; font-weight:900; color:var(--color-primary); margin-bottom:16px;">
              69,000원 <span style="font-size:14px; text-decoration:line-through; color:var(--color-text-muted); font-weight:400;">99,000원</span>
            </div>
            <div style="display:flex; gap:10px;">
              <button class="btn-primary" onclick="openCheckoutModal('[대표 3] 골반 수평 유지 에어셀 벨트', 'FREE')">30일 무료 시착 신청 (0원)</button>
              <button class="btn-secondary" onclick="openQuickView(11)">상세보기</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- [7번: 3초 체형 밸런스 파인더 자가진단 위젯] -->
    <div class="balance-checker-container" id="self-checker-sec">
      <div class="section-tag">3초 맞춤 처방 · 체형 밸런스 파인더</div>
      <h3 style="font-family:var(--font-gowun), serif; font-size:24px; font-weight:800; color:var(--color-text-primary); margin:10px 0 6px;">
        "당신의 하루 중 가장 치열한 작업 환경은 어디인가요?"
      </h3>
      <p style="font-size:14.5px; color:var(--color-text-secondary); margin:0;">
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
          <div style="font-size:32px; background:var(--color-secondary-light); width:54px; height:54px; border-radius:var(--radius-full); display:flex; align-items:center; justify-content:center;">
            🌿
          </div>
          <div>
            <div style="font-size:12.5px; color:var(--color-secondary-text); font-weight:800;">[모니터 근무 직장인 최적 처방]</div>
            <div style="font-family:var(--font-gowun), serif; font-size:17px; font-weight:800; color:var(--color-text-primary); margin:3px 0;">
              0.1mm 심리스 넥&숄더 밴드 + 척추 정렬 조끼
            </div>
            <div style="font-size:13px; color:var(--color-text-secondary);">
              키보드 타건 시 발생하는 전방 두부 쏠림 4.2kg 하중을 승모근 뒤쪽으로 0.1초 분산
            </div>
          </div>
        </div>
        <button class="btn-primary" onclick="filterCatalogByTag('cat_neck')" style="padding:10px 18px; font-size:13px; border-radius:var(--radius-full); white-space:nowrap;">
          처방 상품 보러가기 ➔
        </button>
      </div>
    </div>

    <!-- [9번: 300인 전문가 임상 증명 감성 갤러리] -->
    <section class="container" style="padding:40px 24px;">
      <div style="text-align:center; margin-bottom:36px;">
        <div class="section-tag">300인 현업 전문가 실착 증명</div>
        <h2 class="section-title" style="font-size:30px; font-weight:800; margin-top:10px;">
          "치열한 일상에서 검증된 87% 통증 완화"
        </h2>
        <p style="font-size:15px; color:var(--color-text-secondary); max-width:600px; margin:8px auto 0;">
          정형외과 전문의, 물리치료사, IT 개발자들이 3주간 일상에서 직접 착용하고 검증한 실착 임상 결과입니다.
        </p>
      </div>

      <div class="clinical-proof-grid">
        <div class="clinical-card">
          <div class="clinical-rating">★ 4.9 · 정형외과 전문의 김진우</div>
          <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">
            "강제 압박 없이 경추 C커브를 살려주는 혁신"
          </div>
          <p style="font-size:13.5px; color:var(--color-text-secondary); line-height:1.7;">
            기존 교정기는 늑골을 억누르는데, 스밈 0.1mm는 근육의 고유수용성 감각을 깨워 스스로 척추 정렬을 유지하게 돕습니다.
          </p>
        </div>
        <div class="clinical-card">
          <div class="clinical-rating">★ 5.0 · 물리치료사 이소영</div>
          <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">
            "99.8% 은폐율 덕분에 출근복에 매일 입습니다"
          </div>
          <p style="font-size:13.5px; color:var(--color-text-secondary); line-height:1.7;">
            셔츠 속에 입어도 겉으로 전혀 드러나지 않고, 하루 종일 서서 환자를 볼 때 허리와 골반의 피로도가 80% 이상 줄었습니다.
          </p>
        </div>
        <div class="clinical-card">
          <div class="clinical-rating">★ 4.9 · 풀스택 개발자 박현성</div>
          <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:8px;">
            "14시간 코딩해도 어깨 뭉침이 사라졌습니다"
          </div>
          <p style="font-size:13.5px; color:var(--color-text-secondary); line-height:1.7;">
            모니터 앞으로 목이 빨려 들어갈 때마다 지레 탄성 프레임이 부드럽게 받쳐주어 야근 후에도 목덜미가 깃털처럼 가볍습니다.
          </p>
        </div>
      </div>
    </section>

    <!-- [6번: 15종 상품 전 라인업 가로 스냅 슬라이더 쇼케이스] -->
    <section class="container" id="sec-catalog" style="padding:40px 24px;">
      <div style="text-align:center; margin-bottom:32px;">
        <div class="section-tag">스밈 전 15개 상품 라인업</div>
        <h2 class="section-title" style="font-size:30px; font-weight:800; margin-top:10px;">
          체형 부위별 0.1mm 맞춤 통합 쇼케이스
        </h2>
        <p style="font-size:15px; color:var(--color-text-secondary); max-width:600px; margin:8px auto 0;">
          4대 카테고리 탭을 선택하고 가로 스와이프로 15종 상품을 한눈에 비교해 보세요.
        </p>
      </div>

      <!-- 4대 카테고리 탭 -->
      <div class="showcase-tabs">
        <button class="tab-btn active" onclick="filterCatalog('all', this)">전체 15종 라인업</button>
        <button class="tab-btn" onclick="filterCatalog('cat_neck', this)">어깨 · 경추 케어 (5)</button>
        <button class="tab-btn" onclick="filterCatalog('cat_spine', this)">척추 · 허리 케어 (5)</button>
        <button class="tab-btn" onclick="filterCatalog('cat_pelvis', this)">골반 · 하체 케어 (5)</button>
      </div>

      <!-- 가로 스냅 슬라이더 트랙 -->
      <div class="horizontal-slider-wrapper">
        <button class="slider-nav-btn slider-nav-prev" onclick="scrollSlider('catalog-snap-track', -320)">‹</button>
        <div class="horizontal-snap-track" id="catalog-snap-track"></div>
        <button class="slider-nav-btn slider-nav-next" onclick="scrollSlider('catalog-snap-track', 320)">›</button>
      </div>
    </section>

    <!-- [10번: 조약돌 아코디언 FAQ] -->
    <section class="container faq-container" id="sec-faq">
      <div style="text-align:center; margin-bottom:36px;">
        <div class="section-tag">자주 묻는 질문 &amp; 안심 케어</div>
        <h2 class="section-title" style="font-size:28px; font-weight:800; margin-top:10px;">
          궁금한 점을 모두 풀어드릴게요
        </h2>
      </div>

      <div class="faq-item open" onclick="toggleFaqItem(this)">
        <div class="faq-question">Q. 30일 무료 시착은 정말 결제금액이 0원인가요? <span>▾</span></div>
        <div class="faq-answer">네, 맞습니다. 신청 시 결제되는 금액은 0원이며, 30일 동안 일상과 직장에서 충분히 입어보신 후 만족스러우실 때 구매를 결정하시면 됩니다.</div>
      </div>
      <div class="faq-item" onclick="toggleFaqItem(this)">
        <div class="faq-question">Q. 사이즈가 맞지 않으면 어떻게 하나요? <span>▾</span></div>
        <div class="faq-answer">30일 기간 내라면 왕복 배송비 전액 무료로 원하시는 사이즈로 100% 무료 맞교환해 드립니다.</div>
      </div>
      <div class="faq-item" onclick="toggleFaqItem(this)">
        <div class="faq-question">Q. 세탁기에 넣고 돌려도 센서가 고장 나지 않나요? <span>▾</span></div>
        <div class="faq-answer">스밈의 0.1mm 전도성 센서 섬유는 완전 방수 실링 처리되어 일반 세탁망에 넣어 세탁기 표준 코스로 100회 이상 세탁하셔도 안전합니다.</div>
      </div>
      <div class="faq-item" onclick="toggleFaqItem(this)">
        <div class="faq-question">Q. 셔츠나 정장 안에 입어도 티가 안 나나요? <span>▾</span></div>
        <div class="faq-answer">0.1mm 초슬림 무봉제 심리스 편직 기술로 제작되어 얇은 흰 셔츠 안에 착용해도 99.8% 은폐되어 겉으로 드러나지 않습니다.</div>
      </div>
    </section>

  </main>"""

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 메인페이지(<main id="page-main">...</main>)를 완전체로 교체
    content = re.sub(r'<main id="page-main"[^>]*>.*?</main>', main_page_html, content, flags=re.DOTALL)

    # 15종 상품 카탈로그 렌더링 함수 연동 보강
    render_func = """
    function renderCatalogCards(targetCat) {
      const track = document.getElementById('catalog-snap-track');
      if (!track) return;

      const filtered = targetCat === 'all' ? PRODUCTS_15 : PRODUCTS_15.filter(p => p.cat === targetCat);
      track.innerHTML = filtered.map(p => `
        <div class="one-view-card">
          <div style="background:var(--bg-surface); padding:20px; border-radius:var(--radius-md); text-align:center; margin-bottom:14px; border:1px solid var(--color-border);">
            <div style="font-size:32px; margin-bottom:6px;">${p.icon || '👕'}</div>
            <div style="font-size:11px; font-weight:800; color:var(--color-primary);">${p.tag}</div>
          </div>
          <div>
            <div style="font-family:var(--font-gowun), serif; font-size:16px; font-weight:800; color:var(--color-text-primary); margin-bottom:6px;">
              ${p.name}
            </div>
            <div style="font-size:12.5px; color:var(--color-text-secondary); line-height:1.5; margin-bottom:12px;">
              ${p.spec}
            </div>
            <div style="font-size:16px; font-weight:900; color:var(--color-primary); margin-bottom:14px;">
              ${p.priceSale} <span style="font-size:12px; text-decoration:line-through; color:var(--color-text-muted); font-weight:400;">${p.priceOrig}</span>
            </div>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="btn-primary" style="flex:1; padding:8px 12px; font-size:12.5px;" onclick="openCheckoutModal('${p.name}', 'M')">0원 시착</button>
            <button class="btn-secondary" style="padding:8px 12px; font-size:12.5px;" onclick="openQuickView(${p.id})">🔍 퀵뷰</button>
          </div>
        </div>
      `).join('');
    }

    function filterCatalog(cat, btn) {
      document.querySelectorAll('.showcase-tabs .tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderCatalogCards(cat);
    }

    function filterCatalogByTag(cat) {
      filterCatalog(cat);
      const el = document.getElementById('sec-catalog');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }
"""

    if 'function renderCatalogCards' not in content:
        content = content.replace('document.addEventListener(\'DOMContentLoaded\', () => {', render_func + '\n    document.addEventListener(\'DOMContentLoaded\', () => {\n      renderCatalogCards(\'all\');')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Completely integrated full mainpage in {path}")
