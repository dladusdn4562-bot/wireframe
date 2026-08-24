# -*- coding: utf-8 -*-
import subprocess

res = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True, cwd=r'C:\Users\SBS\Documents\GitHub\wireframe')
print("Git log:")
print(res.stdout)

for commit in ['d8c9a05', '917beb9', '3f504d5', '9f606ee']:
    r = subprocess.run(['git', 'show', f'{commit}:가상클라이언트 설계 결과/설계 출력물/병합/기본 와이어프레임.html'], capture_output=True, text=True, cwd=r'C:\Users\SBS\Documents\GitHub\wireframe')
    if r.returncode == 0:
        print(f"Commit {commit} has 기본 와이어프레임.html (length {len(r.stdout)})")
    else:
        print(f"Commit {commit} does not have it in merge folder")
