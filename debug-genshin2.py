#!/usr/bin/env python3
with open(r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-genshin.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
for m in re.findall(r'panel-\w+', html):
    print(m)
print('---')
idx = html.find('id="panel-think"')
print(f'id panel-think at: {idx}')
if idx > 0:
    print(f'context: {html[max(0,idx-50):idx+200]}')
