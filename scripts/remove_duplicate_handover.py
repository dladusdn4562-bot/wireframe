# -*- coding: utf-8 -*-
import os

dup_path = r'C:\Users\SBS\Documents\GitHub\wireframe\웹디자인\인수인계서.md'
master_path = r'C:\Users\SBS\Documents\GitHub\wireframe\인수인계서.md'

if os.path.exists(dup_path):
    os.remove(dup_path)
    print(f"Removed duplicate file: {dup_path}")
else:
    print(f"File not found: {dup_path}")

if os.path.exists(master_path):
    print(f"Master handover document retained at: {master_path}")
