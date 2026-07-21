#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重写 1999 panel-analysis 为 4 大块结构 + 真实数据"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-1999.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 新的 panel-analysis（4 大块 + 真实数据 + 真人化措辞 + 主题色 #3c5fa8 蓝色）
new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 二游黑马：卡牌 RPG 的"文艺复兴"</h4>
      <p>《重返未来：1999》（以下简称"1999"）由深蓝互动（广州深蓝互动网络科技）开发，<strong>2023-05-31 国内全平台公测</strong>（信达证券研报，2023-06），海外版本 2023-10-26 上线 170+ 国家。游戏讲述了 1999 年 12 月 31 日"暴雨"降临世界后，主角维尔汀与不同时代、国家的神秘学家伙伴逃离灾厄的故事。</p>
      <p>2023 年被业内称为"二游大逃杀"——《崩坏：星穹铁道》4 月公测、《尘白禁区》紧随其后，再加上老牌《原神》、《明日方舟》，整个赛道被挤压。但 1999 用一套<strong>"砍礼装池+剧情驱动+复古美术"</strong>的差异化打法跑了出来：<strong>公测前预约 600 万+</strong>（游戏茶馆，2023-06），首日登顶 AppStore 免费榜 2 天，畅销榜最高第 3，<strong>首月全平台流水约 2 亿元</strong>（知乎估算 + 信达证券），是 2023 年仅次于星铁的新二游。</p>

      <h4>1.2 商业化的"壮士断腕"：主动剥离米家式武器池</h4>
      <p>1999 最具行业意义的决策是<strong>三测后主动砍掉"礼装池"（武器/圣遗物池）</strong>（知乎"知行合一"，2023-12）。这意味着：玩家只抽角色，没有配套的"配装池"反复收割。这与米哈游的"角色池+武器池+叠命座+刷圣遗物词条"四件套形成鲜明对比。</p>
      <p>这背后的逻辑是：<strong>"不是米哈游的产品规模，就不要用米哈游式 f2p 商业化"</strong>（同上）。米哈游这套之所以赚钱，不是因为定价合理，而是因为产品质量让玩家"没有其他选择"。中小厂盲目跟进，只会被"米哈游定价凭什么"的舆论反噬。1999 的解法是：<strong>主动放弃武器池的二次收割，把商业化聚焦在"角色情感价值"上</strong>。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#3c5fa8;font-weight:700;margin-bottom:6px;">⚙️ 米哈游式 f2p</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费结构：</strong>角色池 + 武器池 + 命座 + 圣遗物</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费深度：</strong>4 层，每层都能拉付费</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>用户认知：</strong>贵、但不得不</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>适用对象：</strong>头部 3A 制作规模</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#3c5fa8;font-weight:700;margin-bottom:6px;">🎭 1999 式 f2p</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费结构：</strong>仅角色池 + 通行证</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费深度：</strong>1 层，靠情感驱动</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>用户认知：</strong>便宜、福利好</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>适用对象：</strong>中小厂的"内容向"路径</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：剧情驱动 × 角色养成 × 版本叙事</h4>
      <p>1999 的核心循环与米家抽卡游戏类似，但<strong>剧情权重被显著拉高</strong>：版本叙事（6 周一个大版本）→ 主线剧情推进（多视角）→ 角色池开放 + 角色故事解锁 → 用户为"喜欢的角色"付费。卡牌玩法是次要的，剧情与角色才是驱动付费的核心。</p>
      <div class="mermaid">
flowchart LR
    A[新版本开启] --> B[主线剧情推进]
    B --> C[新角色开放]
    C --> D[角色养成/练度]
    D --> E[卡牌战斗/梦境训练]
    E --> F[体力消耗完毕]
    F --> G[等下一版本]
    B --> H[支线/角色故事]
    H --> I[好感度解锁]
    I --> J[抽卡动力]
    J --> C
      </div>
      <p>从这组流程可以看出，1999 主动把"剧情→角色情感→付费"这条路做长了。区别于米家"角色强度→深渊竞速→抽卡动力"的玩法驱动循环，<strong>1999 是"剧情→情感→付费"</strong>——付费动力不来自强度焦虑，而来自对角色的情感认同。</p>

      <h4>2.2 战斗循环：3 主力 + 卡牌合成 + 激情点攒大招</h4>
      <p>战斗内的循环相对简化：每回合补充手牌到 7 张，3 个行动点，相同卡牌可合成（最高 3 级），<strong>使用/合成神秘术会增加激情点（5 点满）</strong>，满激情后下回合自动送一张大招卡。整体节奏比米家动作游戏慢，更接近策略回合制。</p>
      <div class="mermaid">
flowchart LR
    A[回合开始] --> B[补充手牌7张]
    B --> C[选择3张牌]
    C --> D[使用神秘术/合成]
    D --> E[激情点 +1]
    E --> F{激情点满?}
    F -->|否| G[对手回合]
    F -->|是| H[下回合自动送大招]
    G --> A
    H --> A
    D --> I[造成伤害/减员]
    I --> J[对面掉激情]
    J --> G
      </div>
      <p>这与原神的"元素反应循环"和星铁的"行动轴循环"都不一样：1999 的循环是<strong>"积累-释放"</strong>型——激情点是大招的进度条，让玩家在"漫长铺垫"后获得"一次爆点"。这套循环的设计目的不是让玩家"打得快"，而是让玩家"打得有节奏感"——配合英伦复古的视觉，每场战斗像"舞台剧"一样有起承转合。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 营收结构：国内 67% + 海外 33% 的"文化输出"样本</h4>
      <p>1999 的营收数据呈现一个非常典型的"内容驱动"特征：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#3c5fa8;font-weight:700;">🇨🇳 国内市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">6610 万美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">占全球 67%（约 4.71 亿元）。首月流水 ~2 亿元，主要靠国服（深蓝互动，2024-10）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#3c5fa8;font-weight:700;">🇯🇵 日本市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">1430 万美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">占全球 14%（约 1.02 亿元）。海外首月双端总流水 ~8500 万元（点点数据）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#3c5fa8;font-weight:700;">🇺🇸 美国市场</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">950 万美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">占全球 10%（约 6768 万元）。英语配音版本对北美玩家友好（Pocketgamer）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#3c5fa8;font-weight:700;">📊 全球累计</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">~1 亿美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">上线一年半（2024-10）AppMagic 统计 9870 万美元，含 Steam 版约 1 亿美元</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：AppMagic、网易《上线一年半》，2024-10 / Pocketgamer，2024-10</p>

      <h4>3.2 福利底气："不逼氪"的反向商业逻辑</h4>
      <p>1999 在玩家圈的口碑标签之一是"福利好"。从商业逻辑看，<strong>这是用户画像倒推的结果</strong>：1999 的核心用户是"剧情向 + 情感投入型"玩家，他们对"强度焦虑"的敏感度低，但对付费体验的感知很敏锐（被其他游戏逼氪过）。给足福利可以让这群玩家<strong>维持好感度</strong>，而当他们真的喜欢某个角色时，愿意为"喜欢"付钱，而且付得心甘情愿。</p>
      <p>这套逻辑对中小厂的启示是：<strong>福利不是"让利"</strong>，而是"用让利换好感度，用好感度换付费意愿"。对于 1999 这类"剧情 + 美术"驱动的二游，福利本身就是商业策略的一部分。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给中小厂二游的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(60,95,168,0.1);">
          <div class="ic-num" style="color:#3c5fa8;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">主动砍礼装池：放弃"四件套"</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#3c5fa8;font-weight:600;margin-bottom:8px;">迁移场景：中小厂二游商业化设计</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">米哈游的"角色+武器+命座+圣遗物"四件套建立在"产品规模+IP 信任"双重护城河上。中小厂照搬只会触发"你也敢卖这么贵"的舆论反噬。主动放弃武器池，把付费聚焦在"角色情感价值"上，反而能赢得差异化口碑</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(60,95,168,0.3);">📊 首月流水 ~2 亿元、全球累计 ~1 亿美元（AppMagic，2024-10）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(60,95,168,0.1);">
          <div class="ic-num" style="color:#3c5fa8;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">剧情驱动循环 vs 强度驱动循环</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#3c5fa8;font-weight:600;margin-bottom:8px;">迁移场景：内容向 / 情感向二游</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">米家的循环是"角色强度→深渊竞速→抽卡动力"。1999 反过来：剧情→角色情感→抽卡动力。这套循环不依赖 PVE 难度，让 0 氪党也能享受完整体验，避免"被强度逼氪"的负面口碑</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(60,95,168,0.3);">📊 2023 全年二游流水前 10（知乎"知行合一"，2023-12）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(60,95,168,0.1);">
          <div class="ic-num" style="color:#3c5fa8;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">"美术调性" = 不可复制的护城河</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#3c5fa8;font-weight:600;margin-bottom:8px;">迁移场景：差异化定位 / 美术驱动</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">1999 的"9味"（英伦复古 + 哥特 + Live2D 立绘）建立了属于它自己的二游审美标准。这种调性的门槛是"做出独立气质"，不是"做出好看画面"——这意味着模仿视觉容易，模仿气质难</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(60,95,168,0.3);">📊 海外收入 33%（日本 14% + 美国 10% + 其他）文化输出样本（AppMagic）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#eaf0fa 100%);border:1px solid rgba(60,95,168,0.25);border-left:5px solid #3c5fa8;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(60,95,168,0.1);">
          <div class="ic-num" style="color:#3c5fa8;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">连续性叙事 = 留存护城河</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#3c5fa8;font-weight:600;margin-bottom:8px;">迁移场景：长线运营 / 剧情向设计</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">1999 的 1.4→1.7→1.9 整条叙事线有起承转合，不是"版本独立剧情"。这种"连续叙事"对手游是奢侈的——它需要策划在写每个版本前就想清楚整条弧线。但一旦做好，粘性极强，玩家不敢跳版本</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(60,95,168,0.3);">📊 1.9 周年庆机械姬露西带动 iOS 畅销榜冲第 5（AppMagic）</div>
        </div>
      </div>

      <h4>4.2 对内容向产品 / 独立游戏的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#eaf0fa 100%);border-left:4px solid #3c5fa8;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#3c5fa8;font-weight:700;">方法论洞察 · "不做头部"也是一种定位</div>
        <p>1999 主动放弃了与米家"四件套"商业化体系的对抗，选择"做头部不愿做的内容向"——复古英伦 + 砍武器池 + 福利好 + 连续叙事。这给中小厂一个启示：<strong>不要在头部的主战场上和头部拼规模</strong>，而是找到头部"不愿意做"或"做不好"的细分位置，站稳这个位置比"挤进头部"更有商业价值。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#eaf0fa 100%);border-left:4px solid #3c5fa8;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#3c5fa8;font-weight:700;">方法论洞察 · "卡牌慢节奏"在动作时代的反潮流机会</div>
        <p>当米家全员动作化（星铁的回合制已经算"慢"了），1999 选了更慢的卡牌回合制。3 主力+5 激情点的设计让每场战斗像"舞台剧"。中小厂在动作化拥挤的当下，<strong>卡牌策略这种"慢节奏"反而成了差异化机会</strong>——它适合"边玩边看剧情"的休闲玩家，避开了动作游戏的高操作门槛。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#eaf0fa 100%);border-left:4px solid #3c5fa8;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#3c5fa8;font-weight:700;">方法论洞察 · 内容驱动产品的"产能瓶颈"</div>
        <p>1999 的护城河是"剧情+美术"，但这恰恰是它最大的产能瓶颈：2D 强表现力的剧情制作成本甚至比 3D 动画还贵（高成本美术 + 多视角叙事 + 多语种配音）。一旦产能跟不上，流水下滑会非常快。<strong>对内容驱动产品来说，"产能稳定性"是核心指标</strong>，比"开服爆发力"更决定长期营收。</p>
      </div>

    </div>

    <div id="'''

# 替换
old_pattern = re.compile(r'panel-analysis" class="tab-panel active">.*?</div>\s*<div id="panel-think"', re.DOTALL)
new_content = old_pattern.sub(new_analysis, html, count=1)

if new_content == html:
    print("ERROR: 替换失败")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ panel-analysis 替换成功")
    print(f"原文件 {len(html)} 字符 → 新文件 {len(new_content)} 字符")
    print(f"新增 {len(new_content) - len(html)} 字符")
