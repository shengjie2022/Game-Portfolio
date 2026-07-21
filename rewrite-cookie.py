#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重写 cookie panel-analysis + 修复 panel-think id + 改写 panel-think"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-cookie.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 新的 panel-analysis（4 大块 + 真实数据 + 主题色 #a04000 棕红色）
new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 国民 IP 的国服化：姜饼人 10 年沉淀的"迟来"</h4>
      <p>《冲呀！饼干人：王国》由韩国 Devsisters 研发、腾讯代理国服，<strong>2023-12-28 国服公测</strong>（游民星空，2023-12-28）。它不是一款新游戏——<strong>海外版 2021 年就上线了，曾获 2021 Google Play 韩国区年度最佳游戏、年度最受欢迎游戏</strong>（腾讯官方公告，2023-12）。姜饼人 IP 系列游戏在 10 年间累计注册量超 <strong>2.5 亿人次</strong>（搜狐畅游，2023-12）。</p>
      <p>国服上线 1 个月后数据：<strong>公测首日登顶 iOS 免费榜和 APP 总榜双榜 top1</strong>（游民星空，2023-12），<strong>TapTap 评分 8.7</strong>（九游，2023-12），<strong>公测前预约 500 万+</strong>（搜狐畅游，2023-12）。但更值得关注的财务数据是<strong>上线前 3 个月 iOS 预估流水 1.26 亿元（点点数据，2024-04）</strong>，<strong>最高 iOS 畅销榜 TOP10（高流水持续约半个月），后续 2/3 月稳定在 2000 万 iOS 月流水</strong>（同上）。</p>
      <p>这组数据说明：<strong>饼干人在国服走的是"平稳长线"曲线</strong>，不是"开服爆款-快速下滑"——上线 1 个季度后依然有 2000 万月流水，iOS 畅销榜偶尔冲入 TOP20。这在 2023-2024 年的新游里是相当健康的曲线。</p>

      <h4>1.2 "模拟经营 + 卡牌 RPG" 的双循环融合</h4>
      <p>饼干人王国在玩法上做了"双循环"融合：<strong>家园模拟经营（轻松慢节奏） + 卡牌战斗 RPG（快节奏闯关）</strong>。这与传统的"模拟经营"或"卡牌战斗"单一玩法不同——它让两类用户都能找到自己的乐趣，又通过共享经济循环（家园产出 → 战斗养成）形成闭环。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#a04000;font-weight:700;margin-bottom:6px;">🏠 传统模拟经营</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>核心循环：</strong>建设 → 产出 → 升级</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标用户：</strong>休闲放置玩家</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费深度：</strong>较弱，靠外观</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>痛点：</strong>后期内容消耗快</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#a04000;font-weight:700;margin-bottom:6px;">🍪 饼干人王国（双循环）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>核心循环：</strong>家园 + 战斗 + 公会</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>目标用户：</strong>休闲 + 卡牌双层</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>付费深度：</strong>中等，饼干卡牌 + 外观</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>优势：</strong>两类玩家共享经济循环</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：家园产出 → 战斗养成 → 公会社交</h4>
      <p>饼干人王国的核心循环分三层：<strong>家园（资源产出）→ 战斗（养成消耗）→ 公会（社交与高级内容）</strong>。这套循环让 0 氪玩家也能通过"每天上线收菜"的低强度玩法稳定推进。</p>
      <div class="mermaid">
flowchart LR
    A[家园生产] --> B[收取资源]
    B --> C[饼干养成/升星]
    C --> D[世界探险/战斗]
    D --> E[新资源/章节解锁]
    E --> A
    B --> F[装饰王国]
    F --> A
    C --> G[加入公会]
    G --> H[公会讨伐/扭蛋]
    H --> I[稀有资源/奖励]
    I --> C
      </div>
      <p>这套循环的关键设计是"<strong>离线产出 + 上线收取</strong>"——家园的核心资源（饼干币、增益 buff）有一大部分是离线积累的，但需要上线收取。这创造了独特的"每日仪式感"：不是"我今天必须打副本"，而是"我昨天的产出还在那里等我"。这种"等着你回来"的粘性，比"不玩就亏"温和得多，但同样有效。</p>

      <h4>2.2 战斗循环：5 角色阵容 + 横向跑酷</h4>
      <p>战斗内的循环采用了 5 角色阵容（前排肉盾 + 中排输出 + 后排奶妈）的标准卡牌 RPG 模式，但用"<strong>偏 45° 3D 视角横向跑酷</strong>"包装战斗过程，让"点卡牌放技能"看起来像"跑步战斗"动画。这套设计降低了"卡牌刷刷刷"的视觉疲劳。</p>
      <div class="mermaid">
flowchart LR
    A[进入关卡] --> B[5 角色自动战斗]
    B --> C[能量满释放大招]
    C --> D[造成伤害/触发反应]
    D --> E{战斗胜利?}
    E -->|是| F[资源/经验获取]
    E -->|否| G[调整阵容/练度]
    F --> H[解锁下一关卡]
    H --> A
      </div>
      <p>战斗的关键设计是<strong>自动战斗 + 倍速</strong>——玩家可以把注意力放在"看"和"决策阵容"上，而不是"手操"。这与传统卡牌游戏"必须操作"的体验相反，但符合模拟经营用户的"轻操作"需求——他们来饼干人是为"看可爱饼干"，不是为"练手速"。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 营收曲线：3 个月 1.26 亿元的"平稳长线"</h4>
      <p>饼干人王国的商业化数据呈现典型的"低开高走-稳定长线"形态：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#a04000;font-weight:700;">📊 3 个月 iOS 累计</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0e00;">1.26 亿元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">上线前 3 个月 iOS 预估流水（点点数据，2024-04）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#a04000;font-weight:700;">📈 峰值畅销榜</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0e00;">TOP 10</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">高流水持续约半个月。公测首日登顶免费榜 + APP 总榜双榜 top1</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#a04000;font-weight:700;">📉 平稳月流水</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0e00;">~2000 万元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">2/3 月 iOS 月流水稳定在 2000 万左右（点点数据，2024-04）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#a04000;font-weight:700;">🌍 IP 全球注册</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0e00;">2.5 亿+</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">姜饼人 IP 系列游戏 10 年累计注册人次（搜狐畅游，2023-12）</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：点点数据（2024-04）、搜狐畅游（2023-12）、游民星空（2023-12）</p>

      <h4>3.2 国服本地化：旺旺 + 甄嬛传的双重跨界</h4>
      <p>饼干人王国国服在本地化上做了几件非常聪明的事：</p>
      <p>第一，<strong>国民零食"旺旺"联动</strong>：游戏内建"米饼村"专门为旺旺饼干生活，玩家可获得旺旺定制的专属装饰。把"国民级童年回忆"嵌进游戏，对 80/90 后玩家有极强的情感共鸣。</p>
      <p>第二，<strong>《甄嬛传》联动</strong>：经典古装剧 + 可爱饼干的反差组合，制造了大量"自来水"传播（搜狐畅游，2023-12）。</p>
      <p>第三，<strong>国风专属内容</strong>：国风民乐版 BGM + 国内顶级声优 + 国风饼干角色和剧情。这让国服不是"国际版的简单汉化"，而是"为中国玩家量身定制"。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给模拟经营/卡牌游戏的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(160,64,0,0.1);">
          <div class="ic-num" style="color:#a04000;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#1a0e00;margin-bottom:6px;">"双循环融合"扩大用户基数</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#a04000;font-weight:600;margin-bottom:8px;">迁移场景：模拟经营 + 卡牌/养成</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">传统模拟经营"只对休闲用户"或传统卡牌"只对战斗用户"都很局限。饼干人把"家园+战斗"两条循环用共享经济串联起来，让两类用户都能玩、且能互相转化。<strong>中等付费深度 + 庞大用户基数 = 长期健康营收</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(160,64,0,0.3);">📊 3 个月 iOS 1.26 亿元，2/3 月稳定 2000 万（点点数据）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(160,64,0,0.1);">
          <div class="ic-num" style="color:#a04000;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#1a0e00;margin-bottom:6px;">"离线产出" = 最温和的粘性设计</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#a04000;font-weight:600;margin-bottom:8px;">迁移场景：休闲放置 / 模拟经营</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">"等着你回来"比"不玩就亏"更温和但同样有效。离线产出 + 上线收取的循环让用户形成"每日上线收菜"的习惯，但不会让用户有"FOMO 焦虑"。<strong>这种"温和的粘性"特别适合女性向/休闲用户</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(160,64,0,0.3);">📊 公测首日免费榜 + APP 总榜双榜 top1（游民星空）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(160,64,0,0.1);">
          <div class="ic-num" style="color:#a04000;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#1a0e00;margin-bottom:6px;">"IP 联动"是国服本地化的捷径</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#a04000;font-weight:600;margin-bottom:8px;">迁移场景：海外 IP 国服化 / 本地化</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">把"旺旺"嵌进游戏 + 联动"甄嬛传"是饼干人国服最聪明的本地化操作。<strong>海外 IP 进国服，"找本土文化共鸣"比"翻译好"更重要</strong>。旺旺对应 80/90 后童年、甄嬛传对应"古装梗"，都是国民级 IP，叠加效果强</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(160,64,0,0.3);">📊 公测前预约 500 万+，TapTap 8.7（搜狐畅游）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f7e8d8 100%);border:1px solid rgba(160,64,0,0.25);border-left:5px solid #a04000;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(160,64,0,0.1);">
          <div class="ic-num" style="color:#a04000;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#1a0e00;margin-bottom:6px;">"10 年 IP 沉淀"是发行谈判的筹码</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#a04000;font-weight:600;margin-bottom:8px;">迁移场景：长生命周期 IP / 全球发行</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">姜饼人 IP 全球 2.5 亿注册，这是 Devsisters 用了 10 年积累的资产。<strong>对长线 IP 的中小厂来说，10 年磨一剑的价值会在"国服代理"或"出海授权"时集中兑现</strong>——这是耐心做内容的回报</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(160,64,0,0.3);">📊 IP 系列 10 年累计 2.5 亿注册（搜狐畅游，2023-12）</div>
        </div>
      </div>

      <h4>4.2 对中小厂/独立游戏的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f7e8d8 100%);border-left:4px solid #a04000;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#a04000;font-weight:700;">方法论洞察 · "稳定长线"比"开服爆款"更健康</div>
        <p>饼干人 3 个月累计 1.26 亿元、后续月流水稳定 2000 万，这是一份<strong>"不刺激但很健康"的成绩单</strong>。很多产品在开服期冲上畅销榜 TOP10，但 1 个月后跌出 100 名开外。饼干人证明：<strong>把"健康曲线"放在"短期爆款"之上，是中小厂更可取的策略</strong>——它需要更好的产品力，但回报是更长的产品生命周期。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f7e8d8 100%);border-left:4px solid #a04000;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#a04000;font-weight:700;">方法论洞察 · "可爱"是一种被低估的差异化</div>
        <p>2024 年游戏市场里，<strong>"可爱+治愈"是少数还在增长的细分赛道</strong>。饼干人、恋与深空、原神的部分角色、绝区零的"伊埃斯"都属于这个调性。中小厂如果没有"3A 动作"或"硬核竞技"的能力，<strong>做"可爱"反而是规避头部竞争的捷径</strong>。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f7e8d8 100%);border-left:4px solid #a04000;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#a04000;font-weight:700;">方法论洞察 · "自动战斗"是模拟经营的标配</div>
        <p>饼干人在战斗里提供自动战斗+倍速，这看似"反竞技"，但其实精准对应它的目标用户——来饼干人是为了"看可爱"，不是为了"练操作"。<strong>在以"看"为核心体验的产品里，"自动战斗"不是缺点，是设计优势</strong>。中小厂做这类产品时，要敢于把"战斗简化"做到极致。</p>
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

# 现在替换 panel-think
new_think = '''<div id="panel-think" class="tab-panel">

      <div class="think-section">
        <h3>"等着你回来"：家园系统里最聪明的设计</h3>
        <p>玩饼干人之前，我对"模拟经营"类游戏有偏见——大多是"挂机-收菜-升级"的死循环，没什么人情味。但饼干人王国的家园系统做了一件很聪明的事：它的核心资源（饼干币、增益 buff）有一大部分是<strong>离线积累的，但需要上线收取</strong>。</p>
        <p>这创造了一种独特的"每日仪式感"：不是"我今天必须打副本"，而是"我昨天的产出还在那里等我"。这种"等着你回来"的粘性，比"不玩就亏"温和得多，但同样有效。我从"上线是为了不被惩罚"变成了"上线是为了收我的礼物"——心理预期完全不同。</p>
        <div class="quote-block">
          好的粘性设计让用户觉得"上线是收礼物"，不是"上线是完成任务"。这两句话的语气差距是 0，但用户行为差距是数量级的。
        </div>
        <p>更关键的是家园内容本身深度可扩展——建筑升级、装饰摆放、饼干工坊的配方解锁，每一个都有独立的成长空间。你可以不推进主线，但家园不会让你无聊。这让"0 氪党"和"重氪党"都有事可做。</p>
      </div>

      <div class="think-section">
        <h3>"可爱+本地化"是国服破圈的双重保险</h3>
        <p>饼干人原版 2021 年就在韩国上线了，国服 2023-12 才上——晚了 2 年。这是个巨大挑战：海外玩家早就在国际服玩过了，国服凭什么吸引他们？</p>
        <p>腾讯的解法是<strong>"可爱+本地化"双管齐下</strong>：一方面用"卡哇伊的饼干"延续原作的治愈感（公测首日登顶 iOS 免费榜 + APP 总榜双榜 top1），另一方面用"旺旺联动 + 甄嬛传联动 + 国风 BGM + 国风声优"做本土化。这两条腿共同支撑了 500 万预约和 TapTap 8.7 的评分。</p>
        <div class="highlight-text">
          <strong>策划视角：</strong>海外 IP 进国服不是"翻译好"就够了。<strong>"找本土文化共鸣"比"翻译准确"重要 10 倍</strong>。旺旺对应 80/90 后童年、甄嬛传对应"古装梗"，都是国民级 IP，叠加效果是"自来水式"传播（公测前 B 站、微博、小红书、抖音多平台热门）。
        </div>
        <p>我学到的：<strong>本地化的核心不是"翻译"，是"找到本土文化里的情感共鸣点"</strong>。旺旺不是"好玩的零食"，是"童年回忆"——这种情感连接比任何营销动作都更有效。</p>
      </div>

      <div class="think-section">
        <h3>"平稳长线"的反思：爆款思维 vs 健康曲线</h3>
        <p>饼干人 3 个月 iOS 1.26 亿、2/3 月稳定 2000 万月流水——这份成绩单在 2023 年的新游里只能算"中上"。但从健康度看，它比那些"开服 TOP3-1 个月跌出 100"的产品好得多。</p>
        <p>我意识到这是两种不同的产品哲学：<strong>"爆款思维"追求短期峰值，"健康思维"追求长期曲线</strong>。前者适合流量产品（短视频、买量大户），后者适合内容产品（IP 沉淀、口碑积累）。</p>
        <div class="highlight-text">
          <strong>我的总结：</strong>
          <ul style="margin-top:8px;padding-left:1.4rem;">
            <li><strong>"温和的粘性"更持久</strong>：离线产出 + 上线收取的循环让用户觉得"上线是收礼物"不是"上线是被惩罚"</li>
            <li><strong>本地化的核心是"文化共鸣"</strong>：找本土 IP 联动（旺旺、甄嬛传）比翻译更有效</li>
            <li><strong>"健康曲线"比"开服爆款"更健康</strong>：中小厂应该把"长线留存"放在"短期峰值"之上</li>
            <li><strong>"可爱"是被低估的差异化</strong>：2024 年游戏市场里，"可爱+治愈"是少数还在增长的细分赛道</li>
            <li><strong>"自动战斗"是模拟经营用户的标配</strong>：在"看"为核心体验的产品里，操作简化是设计优势</li>
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
    print(f"总共新增 {len(new_content2) - len(html) - (len(new_content) - len(html))} 字符")
