# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\수정 와이어프레임.html'
]

unboxed_story_html = """<section class="journey-section" id="sec-journey">
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
          
          <!-- 챕터 01: 탄생 배경 -->
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

          <!-- 챕터 02: 기존 한계 극복 -->
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

          <!-- 챕터 03: 전문가 검증과 철학 -->
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

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. story 치환
    content = re.sub(r'<section class="journey-section"[^>]*>.*?</section>', unboxed_story_html, content, flags=re.DOTALL)

    # 2. 3대 대표작(id="sec-featured") 바로 아래에 자가진단 위젯 주입
    if 'id="self-checker-sec"' not in content:
        content = re.sub(
            r'(<section[^>]*id="sec-featured"[^>]*>.*?</section>)',
            r'\1\n' + checker_html,
            content,
            flags=re.DOTALL
        )

    # 3. JS 스크립트 주입
    if 'function selectCheckerJob' not in content:
        content = content.replace('</body>', '<script>\n' + checker_js + '\n</script>\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Perfect Updated {path}")
