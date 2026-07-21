#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重写 endfield panel-analysis + panel-think"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-endfield.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# panel-analysis 4 大块 + 真实数据 + 主题色 #008040 绿色
new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 明日方舟 IP 的 3D 化跃迁</h4>
      <p>《明日方舟：终末地》由鹰角网络（Hypergryph）旗下全球发行品牌 Gryphline 推出，<strong>2026-01-22 全球同步公测</strong>，登陆 PC、iOS、Android、PlayStation 5 全平台，账号数据互通（企鹅号/IT之家，2026-01-20）。游戏延续《明日方舟》世界观，背景设定于数百年后的"塔卫二"星球，玩家扮演"终末地工业"管理员，率领干员开拓荒野、回收技术、扩展人类文明边疆。</p>
      <p>从数据看，终末地的开局是<strong>国产二游"破圈"的代表性案例</strong>：<strong>预约 3500 万+</strong>（21 经济报道，2026-01）、<strong>上线 10 天大陆全平台流水 5 亿+</strong>（伽马数据，2026-01）、<strong>上线 2 周全球全平台累计流水 12 亿元</strong>（上海徐汇官方公众号，2026-02）、<strong>1 月全平台流水 7.94 亿元（行业第二，仅次于原神 18.64 亿元）</strong>（戒戒说游戏，2026-02）。</p>
      <p>更关键的是<strong>PC 和主机占比</strong>——<strong>国内 PC 端流水占比近 60%，海外 PC + PS 合计占比 70%</strong>（上海徐汇，2026-02）。这在长期由移动端主导的二游赛道里是<strong>反常的"破圈"形态</strong>——它意味着大量非传统二游用户（PC 端游玩家、主机玩家）被拉进了这个品类。</p>

      <h4>1.2 鹰角的关键转型：从 2D 塔防到 3D 工业化</h4>
      <p>终末地是<strong>鹰角从 2D 塔防向 3D 即时策略的里程碑式转型</strong>。制作人海猫在 Pocketgamer 采访中说："让我从《明日方舟》这样的 2D 项目转向开发全 3D 游戏，就类似于让一位摩托车手去参加 F1 锦标赛"（游戏陀螺，2025-11）。</p>
      <p>鹰角在终末地做了几个关键决策：</p>
      <p>第一，<strong>美术采用 PBR + NPR 混合渲染</strong>——用基于物理的渲染（PBR）保证 3D 真实感，用非写实渲染（NPR）保留 2D 手绘画风。这种"3A 级别品质 + 动漫风格特征"的角色设计是终末地的核心辨识度。</p>
      <p>第二，<strong>玩法从战棋到即时制</strong>——4 人小队同时在场协作战斗（不是轮切），加入失衡值/弱点击破机制。砍掉了战棋的门槛，但保留了策略深度。</p>
      <p>第三，<strong>加入"集成工业系统"</strong>——玩家可以像《异星工厂》一样规划自动化生产线。鹰角自研多平台专属着色技术 + 重写 Unity 引擎管线来适配这个新方向。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#008040;font-weight:700;margin-bottom:6px;">📜 明日方舟（2D 塔防）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>视觉：</strong>2D 立绘 + 卡通 Q 版</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>战斗：</strong>战棋 + 职业配合</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标：</strong>核心二游用户</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>门槛：</strong>战棋高门槛</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#008040;font-weight:700;margin-bottom:6px;">🚀 终末地（3D 工业化）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>视觉：</strong>3D 写实 + 2D 画风融合</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>战斗：</strong>即时制 + 工业建造</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标：</strong>二游 + PC/主机用户</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>门槛：</strong>操作简化但策略深度保留</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：战斗 × 工业建造 × 地图探索</h4>
      <p>终末地的核心循环分三层：<strong>战斗（资源获取）→ 工业建造（资源加工）→ 地图探索（新内容解锁）</strong>。这套循环和传统二游的"战斗→养成→抽卡"不同——它让"工业建造"成为与战斗并列的核心循环。</p>
      <div class="mermaid">
flowchart LR
    A[探索地图] --> B[获取原材料]
    B --> C[工业系统加工]
    C --> D[生产装备/资源]
    D --> E[角色养成/战斗]
    E --> F[击败敌人]
    F --> G[解锁新地图]
    G --> A
    E --> H[抽卡解锁新角色]
    H --> E
    C --> I[优化生产效率]
    I --> C
      </div>
      <p>这套循环的关键设计是"<strong>用工业建造来延长战斗之外的活跃度</strong>"。传统二游的"战斗→抽卡"循环一旦玩家抽完卡、练完级就会进入长草期。终末地把"工业建造"作为"长草期"的核心内容——玩家可以花几小时优化一条生产线，这种"持续优化"体验不是抽卡能给的。</p>

      <h4>2.2 战斗循环：4 人小队 + 失衡值机制</h4>
      <p>战斗内的循环采用 4 人小队即时制（不是轮切），玩家可在 4 个角色间切换操作。每个角色的战斗由普通攻击、追加攻击、常驻技能、终极技能 4 种形态组成，加入了"<strong>失衡值"和"弱点击破"</strong>机制——敌人累积失衡值后会进入虚弱状态，玩家可趁机打出高额伤害（3DM 单机，2026-01）。</p>
      <div class="mermaid">
flowchart LR
    A[进入战斗] --> B[4 人小队协作]
    B --> C[技能连携/角色切换]
    C --> D[累积敌人失衡值]
    D --> E{失衡值满?}
    E -->|否| B
    E -->|是| F[弱点击破]
    F --> G[高额伤害]
    G --> H[敌人虚弱状态]
    H --> I[战斗胜利]
      </div>
      <p>这套循环的设计目的是<strong>让"4 人小队"成为有意义的策略单位</strong>——不是"切一个角色打一套"的简单循环，而是"4 个角色技能如何连携才能最大化失衡伤害"的复杂决策。这与原神的"元素反应"循环思路类似，但加入了"失衡"这个独立维度。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 营收结构：PC/主机主导的"反移动端"样本</h4>
      <p>终末地的营收结构是国产二游中<strong>罕见的"PC/主机主导"</strong>形态：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#008040;font-weight:700;">💻 国内 PC 端</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#0a1a10;">~60%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">国内全平台占比近 60%（上海徐汇，2026-02）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#008040;font-weight:700;">🎮 海外 PC + PS</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#0a1a10;">~70%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">海外 PC + PS5 合计占比 70%（上海徐汇，2026-02）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#008040;font-weight:700;">📱 全球移动端</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#0a1a10;">4600 万美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">首月移动端 3.3 亿元（AppMagic，2026-02）。iOS 61% + GP 39%</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#008040;font-weight:700;">📊 全球总流水</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#0a1a10;">~12 亿元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">上线 2 周全平台累计（上海徐汇官方，2026-02）</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：上海徐汇官方公众号（2026-02）、AppMagic（2026-02）、伽马数据（2026-01）</p>

      <h4>3.2 抽卡机制：80 抽小保底 + 120 抽大保底</h4>
      <p>终末地的抽卡采用经典的"渐进保底"机制：基础出货率 0.8%，从第 66 抽开始每次递增 5%，<strong>第 80 抽小保底（六星）</strong>。联合寻访池（UP 池）有 120 抽大保底（必出当期 UP）。新手 50 抽 8 折 + 必出六星（终生一次，错过不复刻）（心愿游戏，2025-10）。</p>
      <p>这与米哈游的"90 抽保底"和绝区零的"80 抽保底不歪"形成对比——终末地的"80 抽小保底 + 120 抽大保底"是介于米哈游和绝区零之间的中庸设计。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给传统 2D IP 转型 3D 的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(0,128,64,0.1);">
          <div class="ic-num" style="color:#008040;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#0a1a10;margin-bottom:6px;">PBR + NPR 混合：3D 与 2D 画风的桥梁</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#008040;font-weight:600;margin-bottom:8px;">迁移场景：2D IP 升级 3D / 美术风格转型</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">直接做 3D 写实会失去原 IP 的"动漫风"用户，纯 2D 又无法突破视觉天花板。终末地的解法是<strong>PBR（保证 3D 真实感）+ NPR（保留 2D 画风）混合渲染</strong>——这种"3A 级别品质 + 动漫风格特征"是 2D IP 3D 化的最优解</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(0,128,64,0.3);">📊 预约 3500 万+，开服 iOS/PC/PS5 多端霸榜（21 经济报道）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(0,128,64,0.1);">
          <div class="ic-num" style="color:#008040;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#0a1a10;margin-bottom:6px;">"工业建造" = 长草期的核心内容</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#008040;font-weight:600;margin-bottom:8px;">迁移场景：长线二游 / 内容型游戏</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">传统二游"战斗→抽卡"循环一旦玩家抽完卡就进入长草。终末地把"工业建造"做成与战斗并列的核心循环——<strong>用"持续优化生产线"的体验填充长草期</strong>。这与"模拟经营+卡牌"双循环的思路一致</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(0,128,64,0.3);">📊 上线 2 周全平台 12 亿元（上海徐汇官方公众号）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(0,128,64,0.1);">
          <div class="ic-num" style="color:#008040;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#0a1a10;margin-bottom:6px;">"多端互通"是破圈的核心机制</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#008040;font-weight:600;margin-bottom:8px;">迁移场景：跨平台产品 / PC/主机市场</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">终末地国内 PC 占 60%、海外 PC+PS 占 70%——这是<strong>国产二游"打破移动端依赖"的标志性案例</strong>。多端互通 + 数据同步让 PC 端游玩家和主机玩家可以无障碍进入二游品类，<strong>扩大用户池</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(0,128,64,0.3);">📊 国内 PC 占 60%、海外 PC+PS 占 70%（上海徐汇，2026-02）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#e8f5ec 100%);border:1px solid rgba(0,128,64,0.25);border-left:5px solid #008040;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(0,128,64,0.1);">
          <div class="ic-num" style="color:#008040;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#0a1a10;margin-bottom:6px;">"抽卡机制分层"对应不同用户</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#008040;font-weight:600;margin-bottom:8px;">迁移场景：商业化设计 / 抽卡机制</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">"80 抽小保底 + 120 抽大保底 + 新手 50 抽 8 折"是分层的抽卡设计：新手 8 折对应"短保底、零压力入门"；80 抽小保底对应"非歪保底"；120 抽大保底对应"必出 UP"。<strong>三层保底对应三类用户（0 氪/中氪/重氪）的不同期待</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(0,128,64,0.3);">📊 抽卡：基础 0.8% + 大保底 80 抽 + UP 池 120 抽（心愿游戏，2025-10）</div>
        </div>
      </div>

      <h4>4.2 对国产二游/工业系统的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#e8f5ec 100%);border-left:4px solid #008040;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#008040;font-weight:700;">方法论洞察 · "工业化玩法"是二游差异化的新机会</div>
        <p>当所有二游都在做"角色养成+抽卡"时，终末地把"工业建造"做成核心循环。这给中小厂一个启示：<strong>寻找一个非二游核心玩家也熟悉的小玩法（异星工厂、塔防、模拟经营），把它和二游循环融合</strong>，是 2026 年二游差异化的新机会——异星工厂玩家、塔防玩家、模拟经营玩家都可能成为新增量。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#e8f5ec 100%);border-left:4px solid #008040;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#008040;font-weight:700;">方法论洞察 · "IP 转型"需要新的视觉语言</div>
        <p>鹰角从 2D 塔防转向 3D 即时策略的"代价"是 4 年研发 + 全新引擎管线 + 重写 Unity 渲染。中小厂如果要做类似转型，<strong>必须提前规划好"视觉语言"的过渡方案</strong>，不能用"渐进式过渡"——那会两边不讨好。终末地的"3A 品质 + 动漫风格"混合渲染是一个完整的解决方案。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#e8f5ec 100%);border-left:4px solid #008040;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#008040;font-weight:700;">方法论洞察 · "海外发行"是 PC/主机用户拉新的关键</div>
        <p>终末地由 Gryphline（鹰角全球发行品牌）负责全球同步发行，这是鹰角首次全球自发行。<strong>结果：海外 PC + PS 占比 70%</strong>。这说明：当你的产品定位包含 PC/主机体验时，<strong>必须用全球自发行+多端同步</strong>来触达 PC 端游玩家和主机玩家——这两群人对"渠道买量"几乎免疫，只有"直接上架"才能触达。</p>
      </div>

    </div>

    <div id="panel-think" class="tab-panel">'''

# 替换
old_pattern = re.compile(r'panel-analysis" class="tab-panel active">.*?</div>\s*<div id="panel-think"', re.DOTALL)
new_content = old_pattern.sub(new_analysis, html, count=1)

if new_content == html:
    print("ERROR: 替换失败")
else:
    print(f"✅ panel-analysis 替换成功，新增 {len(new_content) - len(html)} 字符")
    html = new_content

# panel-think
new_think = '''<div id="panel-think" class="tab-panel">

      <div class="think-section">
        <h3>从"QQ 人"到"3A 品质"：明日方舟 IP 的视觉进化</h3>
        <p>明日方舟本体的视觉风格是以"QQ 人"（可爱小方块）为核心的。这个风格帮助它在早期吸引了大量用户，但也形成了某种"天花板"的印象——很多核心玩家玩了 3-4 年后，对"萌系 Q 版"的视觉刺激逐渐脱敏。</p>
        <p>终末地直接把视觉语言推倒重建——精致的 3D 建模、电影感的镜头语言、细腻的场景渲染。这意味着它不是在"做一个更好的明日方舟"，而是在"探索明日方舟这个 IP 能承载什么样的视觉体验"。</p>
        <p>这种"老 IP 的视觉再造"是有风险的——老用户可能因为"它不再像明日方舟"而离开，新用户可能因为"它和明日方舟太像"而不来。但终末地的解法是<strong>PBR + NPR 混合渲染</strong>——既保留 3A 级别的真实感，又保留 2D 动漫画风的辨识度。从 3500 万预约、12 亿元 2 周流水的成绩看，这个解法跑通了。</p>
        <div class="quote-block">
          我意识到：IP 的生命力不是"永远保留原样"，而是"找到新形态承载原 IP 的核心价值"。终末地用 3D 写实包裹 2D 灵魂，是 IP 进化的高级形态。
        </div>
      </div>

      <div class="think-section">
        <h3>"工业建造"是长草期的救星</h3>
        <p>玩终末地之前，我对"长草期"的理解是"硬等新内容"。但终末地的"集成工业系统"（拉电线、接管道、建工厂）改变了这个认知。</p>
        <p>这类系统的设计难点是"简单 vs 复杂"的平衡——太简单就变成"按教程点按钮"，太复杂就劝退 0 氪党。终末地的处理方式是<strong>用物理约束来创造挑战</strong>：电力传输有损耗、管道长度有上限、生产流程需要平衡。这些约束让"建工厂"变成一道开放题——<strong>玩家可以有自己的解法</strong>，这正是探索建造类游戏最吸引人的地方。</p>
        <p>更重要的是，工业建造给"长草期"提供了核心内容。传统二游"战斗→抽卡"循环一旦玩家抽完卡就进入等待新版本的状态，但终末地玩家可以花几小时优化一条生产线——这种"持续优化"体验是抽卡给不了的。</p>
        <div class="highlight-text">
          <strong>策划视角：</strong>长线游戏的核心问题是"玩家抽完卡/练完级后做什么"。<strong>把"持续优化"作为核心循环的一部分</strong>（不是附属内容），是给长草期一个"做事理由"的关键——这与原神"尘世巡游"和星铁"模拟宇宙"的设计思路一脉相承。
        </div>
      </div>

      <div class="think-section">
        <h3>从战棋到即时制：砍掉门槛不是砍掉深度</h3>
        <p>明日方舟本体的战棋玩法对不熟悉的玩家来说是有门槛的——需要理解职业配合、站位仇恨、费用分配这些概念。</p>
        <p>终末地换成动作+探索的玩法，等于是在说：<strong>我们不需要这些门槛，我们用别的方式让游戏有深度</strong>。这个决策让终末地能吸引到"想体验明日方舟世界观但玩不来战棋"的玩家，扩大了用户池。</p>
        <p>但同时，终末地没有砍掉策略深度——4 人小队协作战斗 + 失衡值 + 弱点击破机制，让战斗依然需要"思考哪个技能先手、哪个角色切出来输出最高"。这种"<strong>操作简化但策略保留</strong>"的设计是 3D 即时制二游的关键平衡点。</p>
        <div class="highlight-text">
          <strong>我的总结：</strong>
          <ul style="margin-top:8px;padding-left:1.4rem;">
            <li><strong>"3A 品质 + 动漫风格"是 2D IP 3D 化的最优解</strong>：PBR + NPR 混合渲染保留了原 IP 的视觉辨识度</li>
            <li><strong>"工业建造"是长草期的救星</strong>：把"持续优化"作为核心循环的一部分，不是附属内容</li>
            <li><strong>"操作简化 + 策略保留"是 3D 即时制的关键</strong>：砍掉门槛不是砍掉深度，是砍掉学习成本</li>
            <li><strong>"多端互通"是国产二游破圈的关键</strong>：PC + PS5 占比 70% 说明非移动用户是可以被拉进来的</li>
            <li><strong>"全球自发行"是 PC/主机市场拉新的必要条件</strong>：渠道买量触达不到 PC 端游玩家，必须直接上架</li>
          </ul>
        </div>
      </div>

    </div>'''

old_think_pattern = re.compile(r'<div id="panel-think" class="tab-panel">.*?</article>', re.DOTALL)
new_content2 = old_think_pattern.sub(new_think + '\n\n  </article>', html, count=1)

if new_content2 == html:
    print("ERROR: panel-think 替换失败")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content2)
    print(f"✅ panel-think 替换成功")
    print(f"最终文件 {len(new_content2)} 字符")
