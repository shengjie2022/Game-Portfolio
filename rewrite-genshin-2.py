#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rewriting genshin panel-analysis using hard slicing"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-genshin.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 中国游戏出海的天花板：4 年 640 亿元</h4>
      <p>《原神》由米哈游（miHoYo）开发，<strong>2020-09-28 全球同步公测</strong>（移动端；PC 端 2020-09-15 提前上线），登陆 PC、iOS、Android、PlayStation 4/5 平台，实现多端互通（Sensor Tower / GameRes，2020-10）。</p>
      <p>从 2020 年 9 月公测到 2024 年，<strong>《原神》全球移动端总收入已突破 90 亿美元（约 640.31 亿元人民币）</strong>（Niko Partners 2024-10 报告）。其中，<strong>中国市场贡献 50 亿美元（55%）、海外市场 40 亿美元（45%）</strong>。海外部分，日本 23.2%、美国 16.5%、韩国 6.1%——3 个国家合计占海外收入 46% 左右。</p>
      <p>这组数据让原神成为中国游戏史上的<strong>三连冠</strong>：<strong>首月移动端 2.45 亿美元（仅次于《Pokémon GO》2.83 亿美元）</strong>（Sensor Tower，2020-10）；<strong>2021 年 9 月单月 3.41 亿美元（刷新全球手游月收入纪录，超过《PUBG Mobile》3 亿美元）</strong>（Sensor Tower，2021-10）；<strong>2024 年仍居全球手游年度收入榜第 3（仅次于《王者荣耀》和《PUBG Mobile》）</strong>。连续 4 年保持在全球前 3，这在手游史上是绝无仅有的成绩。</p>

      <h4>1.2 国产 3A 级开放世界：1 亿美元 + 4 年磨一剑</h4>
      <p>原神的研发投入是国产游戏的天花板级别：<strong>300+ 人团队，4 年研发周期，总预算约 1 亿美元</strong>（GameRes 引 Niko Partners，2020-10）。这个数字在国产手游"半年研发-月卡付费"的标准下是反常的。米哈游用 4 年时间赌了一件事：<strong>把"主机级开放世界体验"带到移动端</strong>。</p>
      <p>这个赌注的结果是：<strong>2020-2024 年累计 640 亿元收入（中国出海游戏第一）、全球下载 2.18 亿次（Niko Partners 2024）、首周 1700 万次下载</strong>（App Annie，2020-10）。<strong>开放世界 ARPG 在移动端的可行性被验证</strong>——这是原神给中国游戏行业最大的贡献。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#d4a200;font-weight:700;margin-bottom:6px;">📜 传统国产二游</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>研发：</strong>100 人 / 1-2 年 / 几千万</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>类型：</strong>卡牌回合 / 动作卡牌</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>平台：</strong>仅移动端</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标：</strong>国内二次元用户</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#d4a200;font-weight:700;margin-bottom:6px;">🌍 原神（开放世界）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>研发：</strong>300+ 人 / 4 年 / 1 亿美元</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>类型：</strong>开放世界 ARPG</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>平台：</strong>PC/手机/PS4/PS5 多端</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标：</strong>全球泛二次元用户</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：探索 × 角色养成 × 元素反应</h4>
      <p>原神的核心循环分三层：<strong>大世界探索（资源获取）→ 角色养成（资源消耗）→ 元素反应战斗（强度验证）</strong>。这套循环与传统的"副本-抽卡-强化"循环不同——它把"探索"作为日常活跃度的核心，而不是把"副本"作为核心。</p>
      <div class="mermaid">
flowchart LR
    A[大世界探索] --> B[资源/宝箱/原粹树脂]
    B --> C[角色/武器养成]
    C --> D[角色强度提升]
    D --> E[深渊/SLG 挑战]
    E --> F{达成?}
    F -->|是| G[原粹奖励/星辉]
    F -->|否| H[继续养成]
    H --> C
    C --> I[抽卡获取新角色]
    I --> C
    E --> J[版本活动/主线剧情]
    J --> A
      </div>
      <p>这套循环的关键设计是"<strong>用'原粹树脂'限制日活跃时长</strong>"——每天只能打 4-6 次秘境副本（每次 20 树脂），剩下的"探索"是无限制的。这让<strong>休闲玩家可以每天只玩 30 分钟，硬核玩家可以每天玩 3 小时</strong>——同一套循环覆盖两类用户。</p>

      <h4>2.2 战斗循环：4 人队伍 + 元素反应</h4>
      <p>战斗内的循环采用了 4 人队伍（1 主控 + 3 队友），加入"<strong>元素反应</strong>"机制——火+水=蒸发、火+冰=融化、雷+水=感电等 8 种元素反应。这套机制让"4 人队伍"成为有意义的策略单位：不是"4 个角色分别输出"，而是"4 个角色元素如何连携打出最高伤害"。</p>
      <div class="mermaid">
flowchart LR
    A[进入战斗] --> B[4人队伍出战]
    B --> C[主控角色普攻/技能]
    C --> D[切换队友释放元素]
    D --> E[触发元素反应]
    E --> F[造成大量伤害]
    F --> G{敌人击败?}
    G -->|是| H[战斗胜利]
    G -->|否| B
    B --> I[护盾/治疗/控制]
    I --> B
      </div>
      <p>元素反应机制的设计目的：<strong>让 4 星角色也能打过高难度内容</strong>（通过元素反应和操作），而不是必须抽 5 星。这给 0 氪党/微氪党提供了"我也能打"的体验，降低了付费压力。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 营收结构：3 国占 8 成的全球化样本</h4>
      <p>原神的营收数据呈现典型的"全球化"形态：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#d4a200;font-weight:700;">🇨🇳 中国市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">50 亿美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">占全球 55%（约 355.7 亿元）。2024 累计（Niko Partners）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#d4a200;font-weight:700;">🇯🇵 日本市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">23.2%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 20.9 亿美元。稻妻国度的日本风是吸引日本玩家的关键</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#d4a200;font-weight:700;">🇺🇸 美国市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">16.5%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 14.85 亿美元。2021 年美国开放世界品类近 4.06 亿美元（Sensor Tower）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#d4a200;font-weight:700;">📊 全球累计</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">~640 亿元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">2024 移动端 90 亿美元 = 640.31 亿元。下载 2.18 亿次</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：Niko Partners 2024-10、Sensor Tower 2024、GameRes 2020-10</p>

      <h4>3.2 抽卡机制：90 抽保底 + 180 大保底（米家标准）</h4>
      <p>原神的抽卡是<strong>米哈游标准的"软保底"机制</strong>：基础 0.6% 出率（5 星）、累计 90 抽必出（小保底）、小保底歪了之后下一次 5 星必出 UP（大保底 180 抽）。5 星角色+命座满级满精的总价约 1600 元（CSDN 转载，2020-12）。</p>
      <p>这套机制的关键设计是<strong>"大小保底"分层</strong>：0 氪党靠小保底（90 抽约 14400 原石，免费攒 3-4 个月）能抽到角色，重氪党追求命座满级（180 抽/命座）。<strong>同一套机制覆盖"0 氪体验"和"重氪深度"两端</strong>。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给开放世界/全球化产品的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(212,162,0,0.1);">
          <div class="ic-num" style="color:#d4a200;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">"3A 品质 + 移动端体验"是品类突破</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#d4a200;font-weight:600;margin-bottom:8px;">迁移场景：移动端开放世界 / 高品质品类</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">原神用 1 亿美元 + 4 年时间把"主机级开放世界"带到移动端，<strong>验证了"移动端也能做 3A 品质"</strong>。这给所有想突破"移动端只能是轻量游戏"思路的产品一个标杆——只要品质够高，用户愿意为它等待数年</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(212,162,0,0.3);">📊 2024 累计 640 亿元，全球下载 2.18 亿次（Niko Partners）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(212,162,0,0.1);">
          <div class="ic-num" style="color:#d4a200;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">"7 国文化拼盘"是全球化破圈的捷径</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#d4a200;font-weight:600;margin-bottom:8px;">迁移场景：全球化 / 文化 IP 运营</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">原神用 7 个国度的设定（蒙德/璃月/稻妻/须弥/枫丹/纳塔/至冬）覆盖了欧美/中国/日本/印度/法国/非洲/俄罗斯文化。<strong>每个国家都用当地文化元素做场景+音乐+BGM，让全球玩家都能找到"熟悉的文化"共鸣点</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(212,162,0,0.3);">📊 日本 23.2% / 美国 16.5% / 韩国 6.1%（Sensor Tower）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(212,162,0,0.1);">
          <div class="ic-num" style="color:#d4a200;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">"树脂"机制 = 温和的活跃度设计</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#d4a200;font-weight:600;margin-bottom:8px;">迁移场景：长线运营 / 活跃度管理</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">原粹树脂（每天 180 点，约 4-6 次副本）让<strong>休闲玩家 30 分钟/天 + 硬核玩家 3 小时/天</strong>都能找到自己的节奏。<strong>这种"主动限制活跃度"的设计</strong>比"无限刷"更健康，是长线运营的关键</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(212,162,0,0.3);">📊 4 年保持全球手游年收入前 3（Sensor Tower，2020-2024）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5d9 100%);border:1px solid rgba(212,162,0,0.25);border-left:5px solid #d4a200;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(212,162,0,0.1);">
          <div class="ic-num" style="color:#d4a200;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">"元素反应"是策略深度的护城河</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#d4a200;font-weight:600;margin-bottom:8px;">迁移场景：战斗系统 / 角色平衡</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">火+水=蒸发、火+冰=融化等 8 种元素反应让 4 星角色也能打过 5 星角色的内容。<strong>这种"策略深度替代数值碾压"的设计</strong>是 0 氪党/微氪党的体验保障——不抽到 5 星也能体验大部分内容</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(212,162,0,0.3);">📊 90 抽小保底 + 180 抽大保底（米家标准）</div>
        </div>
      </div>

      <h4>4.2 对中小厂/独立游戏的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#fff5d9 100%);border-left:4px solid #d4a200;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#d4a200;font-weight:700;">方法论洞察 · "1 亿美元赌局"对中小厂意味着什么</div>
        <p>原神的 1 亿美元 + 4 年时间投入是<strong>中小厂永远赌不起的数字</strong>。但这并不意味着中小厂没有机会——恰恰相反，<strong>原神"逼出"了整个 2D 卡牌赛道（恋与深空、绝区零、终末地、1999）的差异化机会</strong>。米家压住"3A 开放世界"位置，中小厂可以在"2D 美术+卡牌玩法+轻量化"上找到自己的位置。原神的成功不是中小厂的失败，是中小厂"放弃正面竞争、转向细分市场"的机会。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#fff5d9 100%);border-left:4px solid #d4a200;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#d4a200;font-weight:700;">方法论洞察 · "7 国文化拼盘"是低成本的全球化策略</div>
        <p>原神 7 个国度的成本极高（每个国 6 个月开发），但"7 国"这个<strong>结构本身是低成本的</strong>——你不需要在每个国都做到原神那种深度，只需要<strong>让每个国家有"本地文化元素"的可识别度</strong>。中小厂做全球化时，<strong>用"3-5 个本地化场景 + 当地文化 BGM"就能做出"文化认同感"，比硬塞"国际化外观"有效 10 倍</strong>。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#fff5d9 100%);border-left:4px solid #d4a200;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#d4a200;font-weight:700;">方法论洞察 · "抽卡 + 树脂"组合是长线运营的核心</div>
        <p>原神的"抽卡（付费） + 树脂（活跃度）"双轨制是<strong>长线二游的"标准答案"</strong>：抽卡负责营收，树脂负责日活。中小厂做长线游戏时，<strong>必须设计"付费系统 + 日活系统"两个独立循环</strong>，不能混在一起。原神证明：<strong>树脂不卖钱但养日活，抽卡不养日活但卖钱</strong>，两套系统独立运行能形成稳定的产品节奏。</p>
      </div>

    </div>

    <div id="panel-think" class="tab-panel">'''

# 用 hard slice：从 panel-analysis 开始到 panel-think 开始
i_start = html.find('panel-analysis" class="tab-panel active">')
i_end = html.find('<div id="panel-think"')
assert i_start > 0 and i_end > 0
# 找到 panel-think div 开始之前的位置
i_end = html.rfind('</div>\n\n    <div id="panel-think"', 0, i_end)
# 如果没找到，try simpler
if i_end < 0:
    i_end = html.rfind('</div>\n\n    ', 0, i_end)

# 简单方式：直接定位到 panel-think div 之前的 </div>
end_marker = '</div>\n\n    <div id="panel-think"'
i_end = html.find(end_marker)
if i_end < 0:
    # 备选
    end_marker = '</div>\n\n  <div id="panel-think"'
    i_end = html.find(end_marker)

if i_end < 0:
    # 兜底：找 panel-think id 位置
    panel_think_id = html.find('id="panel-think"')
    # 找该 div 的开始
    i_end = panel_think_id
    # 向上找最近的 <div
    while i_end > 0 and html[i_end] != '<':
        i_end -= 1
    # 跳过 <div
    i_end_end = html.find('>', i_end) + 1
    # 向上找上一个 </div> 的结束
    i_end = html.rfind('</div>', 0, i_end)
    i_end = html.find('\n', i_end)

print(f'i_start: {i_start}, i_end: {i_end}')
print(f'replace text: {html[i_start:i_start+50]!r}')
print(f'after text: {html[i_end:i_end+50]!r}')

# 替换
new_html = html[:i_start] + new_analysis + '\n\n    ' + html[i_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'✅ panel-analysis 替换成功，新增 {len(new_html) - len(html)} 字符')
