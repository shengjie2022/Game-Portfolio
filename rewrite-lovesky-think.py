#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""改写 lovesky panel-think 为个人体验 + 策划洞察"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-lovesky.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_think = '''<div id="panel-think" class="tab-panel">

      <div class="think-section">
        <h3>从"看角色"到"和角色在一起"：3D 化的体验跃迁</h3>
        <p>玩恋与深空之前，我玩过几个 2D 乙女。它们的体验是"看"——看角色立绘、看剧情动画、看数值卡面。但恋与深空给我的是"和角色在一起"——3D 建模 + 微表情 + 第一人称视角，让我从"观众"变成了"参与者"。</p>
        <p>这种体验的差异不在"画面更精致"，而在"心理距离更近"。当我以第一人称视角和黎深对视时，他眼睛里会看到"我"——这不是脑补出来的，是游戏真的把视角放到了"我"的位置。叠纸用 50 台摄像机阵列捕捉的微表情（眨眼时睫毛的颤动、嘴角肌肉的牵动）让角色"有生命"，而不是"画得好"。</p>
        <div class="quote-block">
          2D 乙女让我"喜欢"一个角色，3D 乙女让我"和"一个角色在一起。这是本质性的体验跃迁，不是技术升级那么简单。
        </div>
      </div>

      <div class="think-section">
        <h3>"确定性"比"性价比"更让我愿意付费</h3>
        <p>我之前玩某款乙游时，陆沉（不点名）让我非常上头，但他的六星卡池没有保底——我永远不知道"再多花多少能得到"。这种"无上限的不确定性"不是期待，是焦虑。</p>
        <p>恋与深空的卡池有明确的保底机制——我知道最多花多少能得到想要的卡。这种<strong>"确定性"本身就是一种情感安全</strong>：我是在"买一个确定的东西"，不是在"赌一个不确定的结果"。当我从"赌"变成"买"，付费决策变得轻松，付费意愿自然提高。</p>
        <div class="highlight-text">
          <strong>策划视角：</strong>抽卡设计的第一性问题不是"怎么让玩家多付费"，而是"怎么让付费决策变得轻松"。无保底机制制造的"赌博感"短期能刺激付费，但长期会积累焦虑、降低信任。恋与深空的保底机制证明了：<strong>确定性比概率更吸引人</strong>。它本质上是用"承诺"换"长期付费意愿"。
        </div>
        <p>我学到的：<strong>商业化设计要让玩家感觉"我在买"而不是"我在赌"</strong>。这两个心理状态对长期付费的影响差距是数量级的。</p>
      </div>

      <div class="think-section">
        <h3>"渡雪境"让我理解情感产品的定价逻辑</h3>
        <p>我氪得最心甘情愿的一张卡是"渡雪境"。不是因为它是限定，是因为它做到了"看到它的第一眼，我就知道这是我想要的"——那个场景、那个氛围、那个瞬间，我和黎深之间的关系被具体化成了一个可以收藏的画面。</p>
        <p>这让我意识到情感产品的定价逻辑和实物商品完全不同：<strong>一张 SSR 卡的情绪价值不是"它的售价"决定的，而是"我看到它的那一刻"决定的</strong>。如果"那一刻"足够打动我，我会觉得 200 元是"礼物"；如果打动不了，2 元我也嫌贵。</p>
        <div class="highlight-text">
          <strong>我的总结：</strong>
          <ul style="margin-top:8px;padding-left:1.4rem;">
            <li><strong>3D 化是"体验跃迁"不是"技术升级"</strong>：从"看角色"到"和角色在一起"，这种差异不在画面而在心理距离</li>
            <li><strong>保底机制=情感安全感</strong>：让玩家从"赌"变成"买"，长期付费意愿反而更高</li>
            <li><strong>情绪价值 = 那一刻</strong>：情感产品的定价由"我看到它的那一刻"决定，不由"它值多少"决定</li>
            <li><strong>营销要跳出游戏圈</strong>：莎拉·布莱曼主题曲、长光卫星、裸眼 3D 大屏——跨界营销是制造破圈的关键</li>
          </ul>
        </div>
      </div>

    </div>'''

# 替换 panel-think
old_pattern = re.compile(r'<div id="panel-think" class="tab-panel">.*?</article>', re.DOTALL)
new_content = old_pattern.sub(new_think + '\n\n  </article>', html, count=1)

if new_content == html:
    print("ERROR: 替换失败")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ panel-think 替换成功")
    print(f"原文件 {len(html)} 字符 → 新文件 {len(new_content)} 字符")
    print(f"新增 {len(new_content) - len(html)} 字符")
