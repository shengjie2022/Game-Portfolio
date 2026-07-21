#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug genshin pattern"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-genshin.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 测试 pattern
old_pattern = re.compile(r'panel-analysis" class="tab-panel active">.*?</div>\s*<div id="panel-think"', re.DOTALL)
m = old_pattern.search(html)
if m:
    print(f'Matched: {m.start()} to {m.end()} ({m.end()-m.start()} chars)')
else:
    print('NOT matched')

# 找 panel-analysis 之前的 panel-thinking
i_think = html.find('panel-think')
print(f'panel-think at: {i_think}')

# 找 panel-analysis
i_analysis = html.find('panel-analysis')
print(f'panel-analysis at: {i_analysis}')

# 找 panel-analysis 后面第一个 </div>
i_end = html.find('</div>', i_analysis)
print(f'first </div> after panel-analysis at: {i_end}')
print(f'text: {html[i_end-50:i_end+200]!r}')
