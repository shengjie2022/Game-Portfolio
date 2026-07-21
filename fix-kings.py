#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 panel-think id 缺失 bug"""
file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-kings.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

old = '<div id=" class="tab-panel">'
new = '<div id="panel-think" class="tab-panel">'

count = html.count(old)
print(f'Found {count} occurrences of broken tag')

if count > 0:
    fixed = html.replace(old, new, 1)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('✅ Fixed panel-think id')
else:
    print('No fix needed')
