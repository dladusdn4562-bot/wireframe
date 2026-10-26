"""Extract the standalone Shop All wireframe from the refined master HTML."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "웹디자인" / "수정 와이어프레임.html"
OUTPUT = ROOT / "가상클라이언트 설계 결과" / "설계 출력물" / "화면 설계서" / "전체 상품 서브페이지.html"


def between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


source = SOURCE.read_text(encoding="utf-8")
fonts = between(source, "  <!-- Web Fonts:", "  <style>")
fonts = "  <!-- Web Fonts:" + fonts
css = between(source, "  <style>", "  </style>")
shop = "<main id=\"page-shop\"" + between(source, '<main id="page-shop"', "</main>") + "</main>"
shop = shop.replace('class="page-view container"', 'class="page-view container active"', 1)
modals_start = source.index("  <!-- 1. 찜 목록 모달 -->")
modals_end = source.index("  <!-- ==========================================================================", source.index('id="modal-checkout"'))
modals = source[modals_start:modals_end]
modals = modals.replace("switchPage('page-shop');", "window.scrollTo({ top: 0, behavior: 'smooth' });")
modals = modals.replace("총 시착 신청 상품 (1개)", "총 시착 신청 상품 (<span id=\"cart-item-count\">0</span>개)")
modals = modals.replace(
    "onclick=\"closeModal('modal-cart'); openCheckoutModal('0.1mm 심리스 넥&숄더 밴드', 'M (95~100)');\"",
    "onclick=\"checkoutCart()\"",
)

script = "\n".join(
    (
        "    const PRODUCTS_15 = [" + between(source, "    const PRODUCTS_15 = [", "    document.addEventListener('DOMContentLoaded'").split("    let cartList", 1)[0],
        "    let cartList = [];\n",
        "    document.addEventListener('DOMContentLoaded', () => {\n      renderProducts('shop-products-grid', PRODUCTS_15);\n      updateBadges();\n    });\n",
        "    function renderProducts" + between(source, "    function renderProducts", "    function navigateToSection"),
        "    function filterShopPage" + between(source, "    function filterShopPage", "    function filterCatalogByTag"),
        "    function updateFitFinder" + between(source, "    function updateFitFinder", "    function openCenterModal"),
        "    function closeModal" + between(source, "    function closeModal", "    function openQuickView"),
        "    function openQuickView" + between(source, "    function openQuickView", "    function toggleFaq"),
    )
)
script = script.replace(
    "if (h < 165 && w < 55) size = 'S (90~95)';\n      else if (h > 182 || w > 82) size = 'L (100~105)';\n      else if (h > 188 || w > 95) size = 'XL (105~110)';",
    "if (h < 165 && w < 55) size = 'S (90~95)';\n      else if (h > 188 || w > 95) size = 'XL (105~110)';\n      else if (h > 182 || w > 82) size = 'L (100~105)';",
)
cart_start = script.index("    function openCartModal() {")
cart_end = script.index("    function addToCartAndCheckout", cart_start)
script = script[:cart_start] + """    function openCartModal() {
      const container = document.getElementById('cart-items-container');
      container.innerHTML = cartList.length ? cartList.map(item => `
        <div style="background:var(--bg-card); padding:12px 16px; border-radius:var(--radius-sm); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-weight:800; font-size:14px; color:var(--color-forest);">${item.name}</div>
            <div style="font-size:12px; color:var(--color-text-secondary);">사이즈: ${item.size}</div>
          </div>
          <div style="text-align:right; color:var(--color-terracotta); font-weight:800;">0원 (시착)</div>
        </div>
      `).join('') : '<p style="padding:20px 0; text-align:center; color:var(--color-text-muted);">담긴 상품이 없습니다.</p>';
      document.getElementById('cart-item-count').innerText = cartList.length;
      document.getElementById('modal-cart').classList.add('active');
    }

    function checkoutCart() {
      if (!cartList.length) return;
      closeModal('modal-cart');
      openCheckoutModal(cartList.map(item => item.name).join(' · '), cartList.map(item => item.size).join(' · '));
    }

""" + script[cart_end:]

header = """  <header class="site-header-fixed" id="site-header-fixed">
    <div class="header-gnb">
      <div class="container gnb-inner">
        <a class="logo" href="../../../웹디자인/수정 와이어프레임.html" aria-label="스밈 메인 와이어프레임">SEUMIM</a>
        <nav class="gnb-nav" aria-label="주 메뉴">
          <a class="gnb-link" href="../../../웹디자인/수정 와이어프레임.html">홈</a>
          <a class="gnb-link active" href="#page-shop" aria-current="page">전체 상품</a>
        </nav>
        <div class="gnb-actions">
          <button class="gnb-action-icon-btn" onclick="openWishlistModal()" title="찜 목록" aria-label="찜 목록 열기">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            <span class="gnb-cart-badge" id="gnb-wish-count">0</span>
          </button>
          <button class="gnb-action-icon-btn" onclick="openCartModal()" title="시착 장바구니" aria-label="시착 장바구니 열기">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <span class="gnb-cart-badge" id="gnb-cart-count">0</span>
          </button>
        </div>
      </div>
    </div>
  </header>"""

footer = """  <footer class="shop-footer">
    <div class="container shop-footer-inner">
      <div><div class="logo shop-footer-logo">SEUMIM <span class="logo-badge">0.1mm</span></div><p>일상 속에 바른 균형이 스며들게 합니다.</p></div>
      <nav aria-label="상품 카테고리"><strong>제품 라인업 (15)</strong>
        <a href="#page-shop" onclick="filterShopPage('cat_neck', document.querySelectorAll('#page-shop .showcase-tabs .tab-btn')[1])">어깨 · 경추 케어 라인 (5)</a>
        <a href="#page-shop" onclick="filterShopPage('cat_spine', document.querySelectorAll('#page-shop .showcase-tabs .tab-btn')[2])">척추 · 허리 케어 라인 (5)</a>
        <a href="#page-shop" onclick="filterShopPage('cat_pelvis', document.querySelectorAll('#page-shop .showcase-tabs .tab-btn')[3])">골반 · 하체 케어 라인 (5)</a>
      </nav>
      <div><strong>SEUMIM 30일 무료 시착</strong><p>사이즈와 착용감을 확인해 보세요.</p><button class="btn-primary btn-accent" onclick="openFitModal()">사이즈 가이드 보기</button></div>
    </div>
  </footer>
  <div class="sticky-trial-bar">
    <div class="sticky-inner">
      <div class="sticky-info"><span class="sticky-pill">결제금액 0원</span><span><strong>SEUMIM 30일 무료 시착</strong> | 입어보고 결정하세요</span></div>
      <button class="btn-primary btn-accent" onclick="openCheckoutModal(PRODUCTS_15[0].name, document.getElementById('fit-calc-size').innerText)">지금 0원에 시착하기 ➔</button>
    </div>
  </div>"""

extra_css = """
    /* Standalone Shop All shell */
    .site-header-fixed { background: var(--bg-surface); }
    #page-shop { padding-bottom: 110px !important; }
    .shop-footer { background: var(--color-forest-dark); color: #fff; padding: 48px 0 110px; }
    .shop-footer-inner { display: grid; grid-template-columns: 2fr 1.2fr 1.4fr; gap: 36px; }
    .shop-footer-logo { color: #fff; margin-bottom: 8px; }
    .shop-footer p, .shop-footer a { color: #c5cdc8; font-size: 13px; }
    .shop-footer nav { display: flex; flex-direction: column; gap: 8px; }
    .shop-footer strong { font-size: 14px; }
    .shop-footer a:hover { color: #fff; }
    .shop-footer .btn-primary { margin: 12px 0 0; }
    .gnb-action-icon-btn { position: relative; }
    .gnb-action-icon-btn .gnb-cart-badge { position: absolute; top: 0; right: 0; }
    @media (max-width: 700px) {
      .gnb-nav { display: flex !important; gap: 12px; }
      .gnb-link { font-size: 12px; }
      .logo { font-size: 19px; }
      .shop-footer-inner { grid-template-columns: 1fr; gap: 24px; }
      .sticky-info { display: none; }
      .sticky-inner { justify-content: center; }
    }
    @media (max-width: 390px) { .gnb-nav .gnb-link:first-child { display: none; } }
"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEUMIM (스밈) | 전체 상품 15종</title>
{fonts}  <style>{css}{extra_css}  </style>
</head>
<body>
{header}
{shop}
{footer}
{modals}
  <script>
{script}
  </script>
</body>
</html>
"""

OUTPUT.write_text(html, encoding="utf-8")
print(OUTPUT)
