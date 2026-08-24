# -*- coding: utf-8 -*-
import json
import os

# transcript_full.jsonl에서 Step 97 시점 또는 Step 93 시점의 replace/write 내역을 확인하거나
# Step 100 이전의 전체 파일 상태를 재구성합니다.

transcript_path = r'C:\Users\SBS\.gemini\antigravity-cli\brain\ca74266d-e76a-42db-b564-5f4e1915d88b\.system_generated\logs\transcript.jsonl'
full_transcript_path = r'C:\Users\SBS\.gemini\antigravity-cli\brain\ca74266d-e76a-42db-b564-5f4e1915d88b\.system_generated\logs\transcript_full.jsonl'

# Step 97 시점의 명령어 및 전후 기록 확인
with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') in [37, 39, 59, 63, 69, 73, 79, 83, 89, 93, 97, 100]:
            print(f"Step {data.get('step_index')}: {data.get('type')}")
            for tc in data.get('tool_calls', []):
                print(f"  Tool: {tc.get('name')}, Args: {list(tc.get('args', {}).keys())}")
