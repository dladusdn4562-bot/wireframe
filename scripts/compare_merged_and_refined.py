# -*- coding: utf-8 -*-
import re
import os

merged_path = r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\와이어프레임_병합.html'
refined_path = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\수정 와이어프레임.html'

with open(merged_path, 'r', encoding='utf-8') as f:
    merged_content = f.read()

with open(refined_path, 'r', encoding='utf-8') as f:
    refined_content = f.read()

print(f"Merged size: {len(merged_content)} chars, {len(merged_content.splitlines())} lines")
print(f"Refined size: {len(refined_content)} chars, {len(refined_content.splitlines())} lines")

# 섹션 및 주요 ID 비교
merged_ids = re.findall(r'id=["\']([^"\']+)["\']', merged_content)
refined_ids = re.findall(r'id=["\']([^"\']+)["\']', refined_content)

print(f"Merged IDs count: {len(merged_ids)}, Unique: {len(set(merged_ids))}")
print(f"Refined IDs count: {len(refined_ids)}, Unique: {len(set(refined_ids))}")

# Merged에는 있는데 Refined에 없는 ID
missing_ids = [i for i in set(merged_ids) if i not in set(refined_ids)]
print(f"Missing IDs in Refined ({len(missing_ids)}): {missing_ids[:20]}")

# CSS 클래스 비교
merged_classes = re.findall(r'class=["\']([^"\']+)["\']', merged_content)
refined_classes = re.findall(r'class=["\']([^"\']+)["\']', refined_content)

merged_c_set = set(' '.join(merged_classes).split())
refined_c_set = set(' '.join(refined_classes).split())
missing_classes = [c for c in merged_c_set if c not in refined_c_set]
print(f"Missing classes in Refined ({len(missing_classes)}): {missing_classes[:20]}")
