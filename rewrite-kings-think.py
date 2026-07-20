#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""改写 kings panel-think 为个人体验 + 策划洞察"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-kings.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 新的 panel-think 内容（个人体验 + 策划洞察，3 段）
new_think = '''<div id="panel-think" class="tab-panel">

      <div class="think-section">
        <h3>1813 天 + 125 皮肤 + 1719 场：一个副游玩家的真实体感</h3>
        <p>说实话，我玩王者荣耀的方式很"非典型"：从不追赛季、不冲段位、有喜欢的皮肤就买、没有就偶尔打两把。这种"不追进度"的状态能坚持 1813 天，本身就说明了这款游戏在"主动玩"之外的另一层价值——<strong>它是一个社交锚点</strong>。</p>
        <p>我和固定开黑的 4 个朋友，从 2017 年一直玩到今天。我们的关系不是"一起玩游戏的人"，而是"通过游戏维系的朋友"。这款游戏在我们之间承担的是"每周固定见一次"的仪式感——皮肤送我们聊天话题、对局给我们交流机会、战令送我们共同的进度感。</p>
        <div class="quote-block">
          我发现：对很多成年人来说，王者荣耀不是"想玩的游戏"，而是"维系一段关系的方式"。这才是它真正难以被取代的地方。
        </div>
      </div>

      <div class="think-section">
        <h3>皮肤购买的"使用频率 × 情感认同"公式</h3>
        <p>我买的 125 个皮肤里，几乎没有"一次性英雄"的皮肤——也就是说，<strong>我不会为一个我从不玩的英雄花 88 元</strong>。这让我意识到：皮肤消费的核心不是"皮肤好不好看"，而是"我用不用这个英雄"。</p>
        <p>把这套逻辑推到一般化：<strong>皮肤 = 长期使用频率 × 情感认同度</strong>。使用频率决定"看到皮肤的时间"，情感认同决定"愿意为它付多少钱"。两个变量相乘，结果是皮肤的真实需求强度。</p>
        <div class="highlight-text">
          <strong>策划视角：</strong>皮肤这种商品和游戏本体不同——它没有"使用价值"（买了皮肤不会让你变强），只有"情绪价值"。情绪价值的定价逻辑是：这个皮肤让我感觉好多少？好一点点就值这个价。所以皮肤设计最重要的不是加多少特效，是<strong>能不能在选择界面里被一眼看中</strong>。王者荣耀 6 元秒杀皮肤的销量经常超过 1688 传说限定，恰好印证了这一点——选皮肤的第一步是"被看到"，不是"被喜欢"。
        </div>
        <p>我在设计自己的内购系统时，会把这条公式记在心里：<strong>玩家愿意为"看到皮肤"付费，而不是为"皮肤本身"付费</strong>。这意味着，UI 设计比美术设计更重要。</p>
      </div>

      <div class="think-section">
        <h3>辅助瑶给我的"高频小高光"启发</h3>
        <p>瑶是我玩得最多的辅助位（2019-04-16 上线、588 点券、首周折扣 388 点券）。一开始我以为是"工具人"——完全依赖队友存活，自己没存在感。但玩久了发现不是：<strong>附身、刷盾、解控</strong>这三个动作每一个都只有 1-2 秒，但足够亮眼、足够频繁。</p>
        <p>这与传统 RPG 的"大招高光"形成对比：MOBA 玩家的成就感是<strong>"每秒都能感觉到自己有用"</strong>，不是"每 5 分钟一次大爆发"。这种"高频小高光"在设计上叫"瞬时反馈"——它不需要多复杂的机制，但能让每个玩家都觉得"我在做贡献"。</p>
        <div class="highlight-text">
          <strong>我的总结：</strong>
          <ul style="margin-top:8px;padding-left:1.4rem;">
            <li><strong>皮肤生态是独立的产品线</strong>：皮肤不依赖游戏版本更新，可以随时发售，这让王者荣耀的商业化不完全依赖内容更新节奏</li>
            <li><strong>辅助的"高频小高光"范本</strong>：瑶证明了"频繁小亮点"比"低频大爆发"更适合休闲/辅助玩家——不需要多操作，但能持续感受到"我在做贡献"</li>
            <li><strong>皮肤购买的核心驱动</strong>：不是性价比，是"我现在用不用这个英雄"——这是我在设计任何内购系统时都应该记住的</li>
            <li><strong>关系链是真正的护城河</strong>：MOBA 的"我和朋友开黑"价值比"我打 5v5"价值更高——设计时要把社交闭环放在玩法闭环之上</li>
          </ul>
        </div>
      </div>

    </div>'''

# 替换 panel-think 内容
# 模式：从 <div id="panel-think" class="tab-panel"> 开始，到 </div> 之前 panel-think 关闭
# 但要小心区分 panel-analysis 的关闭
# 实际 panel-think 已经在前面 fix 修复了，现在用更精确的 pattern

old_pattern = re.compile(
    r'<div id="panel-think" class="tab-panel">.*?</article>',
    re.DOTALL
)

new_content = old_pattern.sub(
    new_think + '\n\n  </article>',
    html,
    count=1
)

if new_content == html:
    print("ERROR: 替换失败")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ panel-think 替换成功")
    print(f"原文件 {len(html)} 字符 → 新文件 {len(new_content)} 字符")
    print(f"新增 {len(new_content) - len(html)} 字符")
