# -*- coding: utf-8 -*-
import re

file_paths = [
    r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\기본 와이어프레임.html',
    r'C:\Users\SBS\Documents\GitHub\wireframe\가상클라이언트 설계 결과\설계 출력물\병합\기본 와이어프레임.html'
]

for path in file_paths:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 템플릿 리터럴 내의 잘못된 백슬래시 이스케이프 제거
    content = content.replace(
        r"${p.isWished ? \'active\' : \'\'}",
        "${p.isWished ? 'active' : ''}"
    )
    content = content.replace(
        r"${p.isWished ? \'[찜됨]\' : \'[찜하기]\'}",
        "${p.isWished ? '[찜됨]' : '[찜하기]'}"
    )

    # 2. 혹시 남아있는 다른 백슬래시 따옴표들도 검사하여 정리
    content = re.sub(r"\\\’", "'", content)
    content = re.sub(r"\\'", "'", content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed JS escaping bugs in {path}")
