from pathlib import Path
import json
import re


root = Path(__file__).parent
source = root / "수정 와이어프레임.html"
output = root / "브랜드소개_피그마_추출용.html"
manifest = root / "브랜드소개_피그마_프레임목록.json"
html = source.read_text(encoding="utf-8")


def element(start_marker: str, close_marker: str) -> str:
    start = html.index(start_marker)
    end = html.index(close_marker, start) + len(close_marker)
    return html[start:end]


head = html[: html.index("</head>") + len("</head>")]
header = element("<header class=", "</header>")
story = element('<main id="page-story"', "</main>")
footer = element("<footer class=", "</footer>")
header = header.replace('class="gnb-link active"', 'class="gnb-link"', 1)
header = header.replace(
    'class="gnb-link" onclick="navigateToSection(\'page-story\')">Our Story</a>',
    'class="gnb-link active" onclick="navigateToSection(\'page-story\')">Our Story</a>',
    1,
)
story = story.replace('class="page-view"', 'class="page-view active"', 1)

sections = [
    ("sec-st92-hero", "01 브랜드 매니페스토"),
    ("sec-st92-name-origin", "02 스밈의 어원과 탄생기"),
    ("sec-st92-origin", "03 세 가지 일상 문제"),
    ("sec-st92-pillars", "04 세 가지 다정한 균형"),
    ("sec-st92-macro", "05 0.1mm 심리스 혁신"),
    ("sec-st92-blueprint", "06 3D 엔지니어링 도면"),
    ("sec-st92-usecases", "07 일상 변화 전후 비교"),
    ("sec-st92-collection", "08 15종 상품 라인업"),
]
for section_id, frame_name in sections:
    before = f'<section id="{section_id}"'
    after = f'<section data-figma-frame="{frame_name}" id="{section_id}"'
    assert before in story, section_id
    story = story.replace(before, after, 1)

head = head.replace(
    "수정 와이어프레임 (Refined Master Wireframe)",
    "브랜드 소개 | Figma 프레임 추출용",
    1,
)
head = head.replace(
    "</head>",
    """<style id="figma-extraction-style">
    /* 8개 브랜드 소개 섹션을 원본 순서와 개별 DOM 경계 그대로 유지 */
    #page-story { display: block !important; animation: none !important; }
    html { scroll-behavior: auto; }
    </style>
</head>""",
    1,
)
doc = head + "\n<body>\n" + header + "\n" + story + "\n" + footer + "\n</body>\n</html>\n"
assert doc.count('data-figma-frame=') == len(sections)
assert '<main id="page-main"' not in doc
assert '<main id="page-shop"' not in doc
image_paths = set(re.findall(r"assets/img/[^'\"\s)]+", doc))
for image_path in image_paths:
    assert (root / image_path).is_file(), image_path
output.write_text(doc, encoding="utf-8")

data = {
    "source": source.name,
    "extracted_html": output.name,
    "figma_file_key": "SFcVmfkC7RPl9Hkis3esxr",
    "figma_target_node_id": "1232:5",
    "page": "브랜드 소개 / Our Story",
    "recommended_frame_width_px": 1440,
    "frames": [
        {"order": i, "name": name, "dom_id": section_id}
        for i, (section_id, name) in enumerate(sections, 1)
    ],
}
manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(output, output.stat().st_size)
print(manifest, manifest.stat().st_size)
print(f"Verified {len(sections)} sections and {len(image_paths)} local images")
