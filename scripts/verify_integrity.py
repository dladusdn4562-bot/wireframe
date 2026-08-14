# -*- coding: utf-8 -*-
"""
가상클라이언트 1~72번 전수 정밀 무결성 검증 스크립트
"""

import os
import json
import re

def verify_all():
    base_dir = r"C:\yyw"
    dirs = {
        "p1": os.path.join(base_dir, r"가상 클라이언트 모음\가상클라이언트"),
        "p2": os.path.join(base_dir, r"가상 클라이언트 모음\가상클라이언트 분석"),
        "p3": os.path.join(base_dir, r"가상 클라이언트 모음\사이트 분석 결과"),
        "p4": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\사이트 구조맵"),
        "p5": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\서비스 흐름도"),
        "p6": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\화면 설계서"),
        "p7": os.path.join(base_dir, r"가상클라이언트 설계 결과\설계 출력물\스토리보드 결과")
    }

    report = {
        "total_clients": 72,
        "phase_status": {},
        "issues": [],
        "file_counts": {}
    }

    for k, d in dirs.items():
        if os.path.exists(d):
            files = os.listdir(d)
            report["file_counts"][k] = len(files)
        else:
            report["file_counts"][k] = 0
            report["issues"].append(f"디렉터리 누락: {d}")

    p1_files = os.listdir(dirs["p1"]) if os.path.exists(dirs["p1"]) else []
    p2_files = os.listdir(dirs["p2"]) if os.path.exists(dirs["p2"]) else []
    p3_files = os.listdir(dirs["p3"]) if os.path.exists(dirs["p3"]) else []
    p4_files = os.listdir(dirs["p4"]) if os.path.exists(dirs["p4"]) else []
    p5_files = os.listdir(dirs["p5"]) if os.path.exists(dirs["p5"]) else []
    p6_files = os.listdir(dirs["p6"]) if os.path.exists(dirs["p6"]) else []
    p7_files = os.listdir(dirs["p7"]) if os.path.exists(dirs["p7"]) else []

    for cid in range(1, 73):
        # Phase 1
        p1_match = [f for f in p1_files if re.search(rf"가상클라이언트_{cid}(_.*)?\.md$", f)]
        if not p1_match:
            report["issues"].append(f"[{cid}번] Phase 1 원본 md 누락")
        
        # Phase 2
        p2_match = [f for f in p2_files if re.search(rf"가상클라이언트_{cid}(_.*)?_분석결과\.md$", f)]
        if not p2_match:
            report["issues"].append(f"[{cid}번] Phase 2 분석결과 md 누락")

        # Phase 3
        p3_match = [f for f in p3_files if re.search(rf"사이트분석결과_가상클라이언트_{cid}(_.*)?\.md$", f)]
        if not p3_match:
            report["issues"].append(f"[{cid}번] Phase 3 사이트분석결과 md 누락")

        # Phase 4 (md, mmd, svg)
        p4_md = [f for f in p4_files if f == f"사이트맵_{cid}.md"]
        p4_mmd = [f for f in p4_files if f == f"사이트맵_{cid}.mmd"]
        p4_svg = [f for f in p4_files if f == f"사이트맵_{cid}.svg"]
        if not (p4_md and p4_mmd and p4_svg):
            report["issues"].append(f"[{cid}번] Phase 4 사이트맵 3종 중 누락 발생")

        # Phase 5 (md, mmd, svg)
        p5_md = [f for f in p5_files if f == f"서비스_흐름도_{cid}.md"]
        p5_mmd = [f for f in p5_files if f == f"서비스_흐름도_{cid}.mmd"]
        p5_svg = [f for f in p5_files if f == f"서비스_흐름도_{cid}.svg"]
        if not (p5_md and p5_mmd and p5_svg):
            report["issues"].append(f"[{cid}번] Phase 5 서비스 흐름도 3종 중 누락 발생")

        # Phase 6 (md, json, html)
        p6_md = [f for f in p6_files if f == f"화면_설계서_{cid}.md"]
        p6_json = [f for f in p6_files if f == f"화면_목록_{cid}.json"]
        p6_html = [f for f in p6_files if f == f"와이어프레임_{cid}.html"]
        if not (p6_md and p6_json and p6_html):
            report["issues"].append(f"[{cid}번] Phase 6 화면설계서 3종 중 누락 발생")

        # Phase 7 (md, json)
        p7_md = [f for f in p7_files if f == f"메인페이지_스토리보드_{cid}.md"]
        p7_json = [f for f in p7_files if f == f"스토리보드_목록_{cid}.json"]
        if not (p7_md and p7_json):
            report["issues"].append(f"[{cid}번] Phase 7 스토리보드 2종 중 누락 발생")

    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    verify_all()
