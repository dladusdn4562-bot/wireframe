# -*- coding: utf-8 -*-
import os

src_path = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html'
dest_path = r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'

with open(src_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. replace renderProducts with One-View Card v2.0
old_func_start = "function renderProducts(containerId, list) {"
new_func = """function renderProducts(containerId, list) {
      const container = document.getElementById(containerId);
      if (!container) return;
      container.innerHTML = list.map(p => `
        <div class="one-view-card product-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div class="one-view-card-header">
              <span class="product-cat-badge">${p.catName ? p.catName.split(' ')[0] : '케어라인'}</span>
              <div style="display:flex; align-items:center; gap:6px;">
                ${p.isTop ? '<span class="product-badge-rec" style="background:var(--color-terracotta); color:#fff; font-size:11px; padding:2px 8px; border-radius:var(--radius-full); font-weight:800;">⭐ 대표작</span>' : '<span class="product-badge-rec" style="background:var(--color-forest); color:#fff; font-size:11px; padding:2px 8px; border-radius:var(--radius-full); font-weight:700;">권장: M</span>'}
                <button class="btn-card-wish-text ${p.isWished ? 'active' : ''}" onclick="toggleWish(${p.id}, this)" style="font-size:11.5px; padding:2px 8px; border-radius:var(--radius-full); border:1px solid var(--color-border); background:var(--bg-base); cursor:pointer;">
                  ${p.isWished ? '❤️ 찜됨' : '🤍 찜하기'}
                </button>
              </div>
            </div>
            
            <div class="product-img-wrap" style="background:var(--bg-surface); border-radius:var(--radius-sm); margin:10px 0 14px; height:130px; display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden; border:1px solid var(--color-border);">
              <span style="font-size:42px; filter:drop-shadow(0 4px 10px rgba(0,0,0,0.06));">${p.icon || '🌿'}</span>
              <span class="product-tag-overlay">${p.tag}</span>
            </div>

            <h4 class="product-title" style="font-family:var(--font-serif); font-size:17px; font-weight:800; color:var(--color-text-primary); margin-bottom:4px; line-height:1.35;">${p.name}</h4>
            <p style="font-size:12px; color:var(--color-text-muted); font-family:var(--font-mono); margin-bottom:10px;">SEUMIM · 0.1mm Seamless Tech</p>
            
            <ul class="one-view-features">
              <li><strong>핵심 기능:</strong> ${p.spec}</li>
              <li><strong>일상 착용:</strong> 38g 초경량 99.8% 셔츠 속 무봉제 은폐</li>
              <li><strong>체험 보장:</strong> 30일 무료 시착 · 반품 배송비 0원</li>
            </ul>
          </div>

          <div>
            <div class="product-price-box" style="margin-top:10px; padding-top:12px; border-top:1px dashed var(--color-border); display:flex; justify-content:space-between; align-items:baseline;">
              <div>
                <span class="p-sale" style="font-family:var(--font-serif); font-size:20px; font-weight:900; color:var(--color-terracotta);">${p.priceSale}</span>
                <span class="p-orig" style="font-size:12px; color:var(--color-text-muted); text-decoration:line-through; margin-left:6px;">${p.priceOrig}</span>
              </div>
              <span style="font-size:11.5px; color:var(--color-sage); font-weight:800;">● 당일 출고</span>
            </div>

            <div class="product-card-actions" style="display:grid; grid-template-columns:1fr 1.3fr; gap:8px; margin-top:12px;">
              <button class="btn-card-quick" style="padding:9px 10px; font-size:12.5px; border-radius:var(--radius-full); border:1px solid var(--color-border); background:var(--bg-base); font-weight:700; cursor:pointer;" onclick="openQuickView(${p.id})">🔍 3D 퀵뷰</button>
              <button class="btn-card-trial btn-primary btn-accent" style="padding:9px 12px; font-size:12.5px; border-radius:var(--radius-full); font-weight:800; justify-content:center; cursor:pointer;" onclick="addToCartAndCheckout('${p.name}', 'M (95~100)')">30일 무료 시착</button>
            </div>
          </div>
        </div>
      `).join('');
    }"""

if old_func_start in content:
    idx1 = content.find(old_func_start)
    idx2 = content.find("function toggleWish", idx1)
    content = content[:idx1] + new_func + "\n\n    " + content[idx2:]
    print("renderProducts replaced successfully.")

# Save to both locations
with open(src_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated both {src_path} and {dest_path}")
