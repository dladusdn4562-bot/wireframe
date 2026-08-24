# -*- coding: utf-8 -*-
import json

full_transcript_path = r'C:\Users\SBS\.gemini\antigravity-cli\brain\ca74266d-e76a-42db-b564-5f4e1915d88b\.system_generated\logs\transcript_full.jsonl'

with open(full_transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') == 97:
            print("Found step 97 in full transcript!")
            for tc in data.get('tool_calls', []):
                print(tc.get('args', {}).get('CommandLine', '')[:300])
        if data.get('step_index') == 93:
            print("Found step 93 in full transcript!")
