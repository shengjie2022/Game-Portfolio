#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 1999 panel-think id + 改写 panel-think 内容"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-1999.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 修复 id
old_id = '<div id=" class="tab-panel">'
new_id = '<div id="panel-think" class="tab-panel">'

if old_id in html:
    html = html.replace(old_id, new_id, 1)
    print('✅ Fixed panel-think id')
else:
    print('No broken id found')

# 替换 panel-think 内容
new_think = '''<div id="panel-think" class="tab-panel">

      <div class="think-section">
        <h3>"9味"是什么味道：一种不容易被量化的气质</h3>
        <p>玩 1999 之前，我对"二游审美"是有固有印象的：日式赛璐璐、韩式 3D 渲染、米家渲染工业化。但 1999 给我的第一感觉是"它不属于这些类别里的任何一个"——英伦复古 + 哥特 + Live2D 立绘，整体调性有一种"看着像在看一部 1920 年代的英国舞台剧"的氛围。</p>
        <p>这种"9味"不是"美术好看"能概括的——它是<strong>"气质"和"叙事"和"画面"三件套的统一</strong>。立绘是英伦绅士淑女风，剧情是 1929 股市崩盘的悬疑叙事，背景音乐是大提琴+爵士。三个维度合起来才是"9味"。这意味着：<strong>模仿 1999 的视觉容易，模仿这种气质难</strong>——气质不能"做一个一样的立绘"，而是"做一整套沉浸的英伦世界"。</p>
        <div class="quote-block">
          我意识到：对于内容向产品来说，"风格"不是"美术标签"，而是"叙事 + 视觉 + 听觉的整体氛围"。三者必须同时到位，才能立住。
        </div>
      </div>

      <div class="think-section">
        <h3>砍武器池的勇气：一种"放弃四件套"的商业哲学</h3>
        <p>1999 三测后砍掉"礼装池"（武器/圣遗物池），只留角色池。这件事在 2023 年 6 月公测时是争议很大的——很多人担心"只靠角色池能不能撑起营收"。</p>
        <p>从结果看，<strong>1999 的首月流水 2 亿元、全球累计近 1 亿美元（2024-10）的成绩证明：单角色池+福利好也能跑通</strong>。这背后是用户画像倒推的结果——1999 的核心用户是"剧情向 + 情感投入型"，对强度焦虑敏感度低、对付费体验敏感度高。给足福利维持好感度，角色池自然能撑住营收。</p>
        <div class="highlight-text">
          <strong>策划视角：</strong>1999 的"砍武器池"决策反映了一个反常识——<strong>对于中小厂二游，"放弃商业化深度"反而能赢得差异化口碑</strong>。米哈游的"角色+武器+命座+圣遗物"四件套建立在"产品规模+IP 信任"的双重护城河上。中小厂照搬这套，只会被"你也敢卖这么贵"的舆论反噬。主动放弃武器池，把付费聚焦在"角色情感价值"上，反而能吸引"对逼氪敏感"的高质量用户。
        </div>
        <p>我学到的：<strong>商业化设计的第一性问题不是"怎么赚更多"，而是"赚哪些人的钱"</strong>。选错用户群体，再精妙的商业化设计都会被舆论反噬。</p>
      </div>

      <div class="think-section">
        <h3>连续叙事的奢侈：把玩家当成认真看故事的人</h3>
        <p>我玩 1999 印象最深的是：1.4→1.7→1.9 整条叙事线有起承转合，不是"每个版本独立剧情"。这与米家"版本独立 + 角色独立故事"的设计完全不同。</p>
        <p>这种"连续叙事"对手游是奢侈的——它要求策划团队<strong>在写每个版本之前，就想清楚整条叙事弧的走向</strong>，而不是临时起意。它还会导致"跳版本"成本极高——你跳过 1.5，1.6 的剧情就接不上。这种"门槛"对短期留存不利，但对长期粘性极有利。</p>
        <div class="highlight-text">
          <strong>我的总结：</strong>
          <ul style="margin-top:8px;padding-left:1.4rem;">
            <li><strong>"气质"是统一性</strong>：美术 + 叙事 + 音乐三者必须同时到位，才能立住一种风格</li>
            <li><strong>商业化要匹配用户画像</strong>：剧情向用户对"强度焦虑"敏感度低，对"付费体验"敏感度高</li>
            <li><strong>连续叙事是高门槛但高粘性</strong>：用"门槛"换"留存"，比靠福利续命更长期</li>
            <li><strong>产能稳定性是内容驱动产品的命门</strong>：2D 强表现力剧情比 3D 动画还贵，产能跟不上会快速掉队</li>
          </ul>
        </div>
      </div>

    </div>'''

# 替换 panel-think
old_pattern = re.compile(r'<div id="panel-think" class="tab-panel">.*?</article>', re.DOTALL)
new_content = old_pattern.sub(new_think + '\n\n  </article>', html, count=1)

if new_content == html:
    print("ERROR: panel-think 替换失败")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ panel-think 替换成功")
    print(f"原文件 {len(html)} 字符 → 新文件 {len(new_content)} 字符")
    print(f"新增 {len(new_content) - len(html)} 字符")
