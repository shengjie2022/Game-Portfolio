#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 genshin 重复的 panel-think"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-genshin.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 找到重复的 panel-think 起点
# 模式：</div>\n\n    </div>\n\n    <div id="panel-think"...>\n\n    \n\n    <!-- ===== 策划思考 ===== -->\n    <div id="panel-think"...
# 第一个 panel-think 后面有 \n\n    \n\n    <!-- 注释
# 第二个 panel-think 后面是真正的内容 <div class="think-section">

# 策略：找两个 panel-think 中间的内容，删除
parts = html.split('<div id="panel-think" class="tab-panel">')
print(f'Found {len(parts)} parts after splitting by panel-think')

if len(parts) >= 3:
    # 第一个 part + 第一个 panel-think 内容（含 think-section）+ 后面的内容
    # parts[0]: panel-analysis 之前的部分
    # parts[1]: 第一个 panel-think 后到第二个 panel-think 前的部分（这是要删除的"空 + 注释"部分）
    # parts[2]: 第二个 panel-think 之后到结尾的部分（这是真正要保留的内容）

    # 找到第一个 panel-think 后的真实开始 <div class="think-section">
    second_panel_think_content = parts[2]
    # 跳过第二个 panel-think 的开头空行/注释
    # 第二个 panel-think 实际上是真正的开始
    # 我们要重新组合：parts[0] + '<div id="panel-think"...>' + parts[2]
    new_html = parts[0] + '<div id="panel-think" class="tab-panel">' + parts[2]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'✅ 修复完成，去除 {len(html) - len(new_html)} 字符')
    print(f'最终文件: {len(new_html)} 字符')
else:
    print('未找到重复 panel-think')
