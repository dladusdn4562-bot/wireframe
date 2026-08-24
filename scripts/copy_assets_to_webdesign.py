# -*- coding: utf-8 -*-
import shutil
import os

src_assets = r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\assets'
dst_assets = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\assets'

if os.path.exists(src_assets):
    if os.path.exists(dst_assets):
        shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)
    print(f"Copied assets to {dst_assets} successfully!")
else:
    print(f"Source assets not found: {src_assets}")
