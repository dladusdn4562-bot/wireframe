# -*- coding: utf-8 -*-
import json
import os

transcript_path = r'C:\Users\SBS\.gemini\antigravity-cli\brain\ca74266d-e76a-42db-b564-5f4e1915d88b\.system_generated\logs\transcript.jsonl'

if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line_idx, line in enumerate(f):
            data = json.loads(line)
            step_idx = data.get('step_index')
            for tc in data.get('tool_calls', []):
                args = tc.get('args', {})
                target = args.get('TargetFile', '') or args.get('CommandLine', '')
                if '기본 와이어프레임' in target or '와이어프레임' in target or '디자인_분석' in target:
                    print(f"Step {step_idx}: {tc.get('name')} -> {target[:120]}")
