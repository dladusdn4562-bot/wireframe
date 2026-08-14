# -*- coding: utf-8 -*-
"""
가상클라이언트 1~82번별 전용 폴더 생성 및 7대 Phase 산출물 1:1 패키징 스크립트
"""

import os
import shutil
import re

def organize_clients_by_id():
    base_dir = r"C:\yyw"
    
    # 원본 디렉터리들
    src_dirs = {
        "p1": os.path.join(base_dir, r"가상 클라이언트 모음\가상클라이언트"),
        "p2": os.path.join(base_dir, r"가상 클라이언트 모음\가상클라이언트 분석"),
        "p3": os.path.join(base_dir, r"가상 클라이언트 모음\사이트 분석 결과"),
        "p4": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\사이트 구조맵"),
        "p5": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\서비스 흐름도"),
        "p6": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\화면 설계서"),
        "p7": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\스토리보드 결과")
    }

    # 대상 타깃 루트 디렉터리
    target_root = os.path.join(base_dir, r"클라이언트별_설계_모음")
    os.makedirs(target_root, exist_ok=True)

    summary = {
        "total_clients_organized": 0,
        "total_files_copied": 0,
        "client_folders": []
    }

    for cid in range(1, 83):
        # 각 클라이언트별 폴더 생성 (예: C:\yyw\클라이언트별_설계_모음\클라이언트_1\)
        client_folder = os.path.join(target_root, f"클라이언트_{cid}")
        os.makedirs(client_folder, exist_ok=True)

        copied_count = 0

        # Phase 1: 가상클라이언트 원본
        if os.path.exists(src_dirs["p1"]):
            for f in os.listdir(src_dirs["p1"]):
                if re.search(rf"가상클라이언트_{cid}(_.*)?\.md$", f):
                    shutil.copy2(os.path.join(src_dirs["p1"], f), os.path.join(client_folder, f))
                    copied_count += 1

        # Phase 2: 가상클라이언트 분석결과
        if os.path.exists(src_dirs["p2"]):
            for f in os.listdir(src_dirs["p2"]):
                if re.search(rf"가상클라이언트_{cid}(_.*)?_분석결과\.md$", f):
                    shutil.copy2(os.path.join(src_dirs["p2"], f), os.path.join(client_folder, f))
                    copied_count += 1

        # Phase 3: 사이트분석결과
        if os.path.exists(src_dirs["p3"]):
            for f in os.listdir(src_dirs["p3"]):
                if re.search(rf"사이트분석결과_가상클라이언트_{cid}(_.*)?\.md$", f):
                    shutil.copy2(os.path.join(src_dirs["p3"], f), os.path.join(client_folder, f))
                    copied_count += 1

        # Phase 4: 사이트 구조맵 (md, mmd, svg)
        if os.path.exists(src_dirs["p4"]):
            for ext in [".md", ".mmd", ".svg"]:
                fname = f"사이트맵_{cid}{ext}"
                fpath = os.path.join(src_dirs["p4"], fname)
                if os.path.exists(fpath):
                    shutil.copy2(fpath, os.path.join(client_folder, fname))
                    copied_count += 1

        # Phase 5: 서비스 흐름도 (md, mmd, svg)
        if os.path.exists(src_dirs["p5"]):
            for ext in [".md", ".mmd", ".svg"]:
                fname = f"서비스_흐름도_{cid}{ext}"
                fpath = os.path.join(src_dirs["p5"], fname)
                if os.path.exists(fpath):
                    shutil.copy2(fpath, os.path.join(client_folder, fname))
                    copied_count += 1

        # Phase 6: 화면 설계서 (md, json, html)
        if os.path.exists(src_dirs["p6"]):
            for fname in [f"화면_설계서_{cid}.md", f"화면_목록_{cid}.json", f"와이어프레임_{cid}.html"]:
                fpath = os.path.join(src_dirs["p6"], fname)
                if os.path.exists(fpath):
                    shutil.copy2(fpath, os.path.join(client_folder, fname))
                    copied_count += 1

        # Phase 7: 스토리보드 (md, json)
        if os.path.exists(src_dirs["p7"]):
            for fname in [f"메인페이지_스토리보드_{cid}.md", f"스토리보드_목록_{cid}.json"]:
                fpath = os.path.join(src_dirs["p7"], fname)
                if os.path.exists(fpath):
                    shutil.copy2(fpath, os.path.join(client_folder, fname))
                    copied_count += 1

        summary["total_clients_organized"] += 1
        summary["total_files_copied"] += copied_count

    print(f"총 {summary['total_clients_organized']}개 클라이언트 폴더 생성 완료! (총 {summary['total_files_copied']}개 파일 분류 복사 완료)")

if __name__ == "__main__":
    organize_clients_by_id()
