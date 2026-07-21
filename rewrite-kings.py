#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重写 kings panel-analysis 为 4 大块结构 + 真实数据"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-kings.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 新的 panel-analysis 内容（4 大块结构 + 真实数据 + 真人化措辞）
new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 国民 MOBA：从边缘项目到日活 1 亿</h4>
      <p>《王者荣耀》于 2015 年 11 月 26 日全平台公测（腾讯官方公告），最初叫《英雄战迹》《王者联盟》，是腾讯天美 L1 工作室用 100 人团队在半年内迭代出来的产品。一开始它在腾讯内部是边缘项目，光子工作室的《全民超神》才是重点扶持对象（中国经营网，2024-10）。</p>
      <p>但《王者荣耀》用了一招"反氪"——主动去掉英雄养成线，把数值卖给符文和皮肤，而不是卖英雄——结果反而跑赢了。从 2017 年 5 月用户规模 2.01 亿、男女比 1:1.18（极光大数据《王者荣耀研究报告》），到 <strong>2020 年 11 月 1 日官方宣布 DAU 突破 1 亿</strong>，成为"全球首款日活破亿的游戏"（王者荣耀五周年盛典官方公告）。四年后的 2024 年 10 月 27 日九周年活动，官方再次公布 DAU 超 1 亿（中国经营网，2024-10）。这组数据证明：在所有"国民级应用"里——微信、抖音、淘宝、百度——王者荣耀是唯一一款不是生活必需品的游戏。</p>

      <h4>1.2 移动 MOBA 的范式创新：短局时 + 公平竞技</h4>
      <p>王者荣耀能在移动端跑赢端游 MOBA（《英雄联盟》），核心是做了三件事：</p>
      <p>第一，<strong>对局时间压到 15 分钟</strong>（端游 LOL 至少 30-40 分钟），6 分钟可投降；第二，把 LOL 复杂的"补刀、控线、眼位"简化到"技能命中 + 走位"；第三，借助 QQ/微信关系链的天然导入（2015 年 11 月后新增好友邀请功能），让"找不到人开黑"的问题彻底消失（中国经营网，2024-10）。结果是：王者荣耀把 MOBA 从"核心玩家"拉到了"全民玩家"——小学生和博士生、办公室白领和工厂工人，都能在同一场对局里厮杀。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#c89800;font-weight:700;margin-bottom:6px;">⚔️ 端游 MOBA（LOL）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>对局时长：</strong>30-40 分钟</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>操作门槛：</strong>补刀 / 控线 / 插眼</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>用户：</strong>核心玩家（80% 为男性）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>留存依赖：</strong>排位 + 段位</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#c89800;font-weight:700;margin-bottom:6px;">📱 王者荣耀（移动 MOBA）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>对局时长：</strong>~15 分钟 / 6 分钟可投降</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>操作门槛：</strong>技能 + 走位（自动补刀）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>用户：</strong>全民玩家（男女 1:1.18）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>留存依赖：</strong>关系链 + 皮肤 + 排位</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：单局对局 × 赛季 × 关系链</h4>
      <p>王者荣耀的核心循环分三个层级：单局对局（分钟级）→ 排位赛季（季度级）→ 关系链（年级）。这三层环环相扣，让玩家从"打一局"到"打一个赛季"再到"和朋友打很多年"。</p>
      <div class="mermaid">
flowchart LR
    A[匹配对局] --> B[5v5 战斗]
    B --> C{胜负?}
    C -->|胜| D[加星/加段位]
    C -->|负| E[掉星/掉段位]
    D --> F[赛季奖励]
    E --> F
    F --> G[新赛季开启]
    G --> A
    B --> H[战队/好友互动]
    H --> I[亲密度/师徒]
    I --> A
    F --> J[限时皮肤/活动]
    J --> A
      </div>
      <p>这套循环的关键在于"低门槛进、慢释放出"——单局 15 分钟就完事，但赛季要 3 个月，关系链可以维系几年。每一层都覆盖不同时间预算的玩家：想"消磨 15 分钟"的，单局就行；想"冲段位"的，赛季给目标；想"维系感情"的，关系链和开黑就够了。</p>

      <h4>2.2 战斗循环：操作 → 击杀 → 推塔 → 团战</h4>
      <p>5v5 对局内部的循环是"小循环"：补兵推线 → 消耗对手血量 → 关键技能命中 → 配合队友完成击杀 → 推掉对方防御塔。这种"短反馈 + 团队合作"的循环让 MOBA 区别于单局 ARPG：它的"成就感"不是来自"我变强了"，而是来自"我帮队伍赢了"。</p>
      <div class="mermaid">
flowchart LR
    A[对线补兵] --> B[技能消耗]
    B --> C[关键控制命中]
    C --> D[队友跟进]
    D --> E[完成击杀]
    E --> F[推塔/入侵野区]
    F --> G[扩大经济差]
    G --> H[团战胜利]
    H --> I[推掉基地]
    I --> J[胜利结算]
      </div>
      <p>这与原神的"角色养成循环"截然不同——MOBA 玩家的每一次胜利都是"和别人合作的结果"，没有"我一个人 carry"的独狼快感。这给商业化留了一个非常重要的空间：<strong>不卖数值</strong>。因为一旦卖数值，5v5 的公平竞技就崩了。所以王者荣耀把所有的变现都堆到了"皮肤"这个不影响对局公平性的维度上。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 皮肤分级：从 6 元到数万的"奢侈品矩阵"</h4>
      <p>王者荣耀的皮肤体系是它商业化最核心的资产。根据 2024 年的公开数据，皮肤分为 5 个档位：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#c89800;font-weight:700;">🌟 荣耀典藏</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">~2000+ 元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">需荣耀水晶兑换（保底约 21660 点券，361 幸运值）。目前 11 款，是身份的终极象征</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#c89800;font-weight:700;">💎 传说限定</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">1788 点券</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 178 元。年限 / FMVP / KPL 系列。特效 + 语音 + 独立回城，最顶级配置</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#c89800;font-weight:700;">✨ 传说</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">1688 点券</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 143 元。直售传说，独立回城特效。55 款累计，是 0 氪玩家最可能入手的顶级档</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#c89800;font-weight:700;">🎖️ 史诗</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">888 点券</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 75 元。125+ 款，是销量最大的档位。特效 + 独立语音，性价比最优</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#c89800;font-weight:700;">⚡ 勇者</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a1500;">488-588 点券</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 41-49 元。基础特效 + 10 攻击加成。KPL 系列常 6 元秒杀，是 0 氪党的福利</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：知乎《王者荣耀：史上最贵的三款皮肤》、指法芬芳张大仙《王者典藏幸运值要多少》（2025-05）</p>

      <h4>3.2 商业模式的"反常识"：低战力加成 + 抽卡限定</h4>
      <p>王者荣耀的付费设计有个反常识：<strong>皮肤只给 +10 攻击力</strong>，最多 +30。在一局 30 分钟对局里，10 点攻击力几乎可以忽略。这意味着皮肤对竞技公平性的影响约等于零——零氪玩家可以靠操作吊打 V10 玩家。</p>
      <p>但反过来，<strong>抽卡机制（积分夺宝）才是真正的"奢侈品"陷阱</strong>：荣耀水晶需要 361 幸运值保底，60 荣耀积分 = 60 点券，所以一颗水晶保底约 21660 点券（2166 元）。这与原神的 648 元充值档思路类似：<strong>让大部分人买小额的传说、史诗（30-200 元），让少数核心玩家追"荣耀典藏"（2000+ 元）</strong>。这造成了一个健康的营收结构：6 元秒杀 / 50 元史诗 / 200 元传说 / 2000 元典藏，覆盖了从学生到老板的全部人群（搜狐《王者皮肤价格降低》，2024-07）。</p>

      <h4>3.3 营收规模：上线 8 年累计 720 亿元</h4>
      <p>从财务看，王者荣耀是腾讯的现金牛：2017 年收入约 10 亿美元（71.3 亿元）→ 2020 年 15 亿美元（106.9 亿元）→ 2022 年峰值 22.2 亿美元（158.3 亿元）（AppMagic 数据，搜狐，2024-10）。<strong>上线前 8 年累计收入约 101.1 亿美元（720.8 亿元）</strong>，超过绝大多数上市公司一年的营收。2023 年收入下滑到 14.8 亿美元（105.5 亿元），但 2024 年开始回稳——上半年 iOS 端收入 8.4 亿美元（59.9 亿元），9 月单月 1.3 亿美元（9.3 亿元），稳居中国手游收入榜第一（指法芬芳张大仙，2025-05）。</p>
      <p>更有意思的是 2017 年首年，游戏团队人均年终奖 140 万（最低 60 万，核心员工 290 万）（北京晨报，转引自搜狐，2017）——这组数字后来被官方否认过真实性，但腾讯从未公开真实的年终奖数据。无论真假，它反映了一个事实：<strong>王者荣耀的利润率高到能让一家公司"传说级"地给员工发钱</strong>。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给 MOBA/竞技类产品的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(200,155,60,0.1);">
          <div class="ic-num" style="color:#c89800;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">低战力加成 + 皮肤付费</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#c89800;font-weight:600;margin-bottom:8px;">迁移场景：5v5 / 公平竞技 / 合作对局</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">MOBA 是社交游戏，"打赢朋友的爽感"是核心驱动力。一旦卖数值，公平性崩塌，社交驱动力归零。王者荣耀用 +10 攻击的微加成证明：付费只影响"仪式感"（皮肤），不影响"实力"</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(200,155,60,0.3);">📊 上线 8 年累计 720.8 亿元营收（AppMagic）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(200,155,60,0.1);">
          <div class="ic-num" style="color:#c89800;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">关系链 = MOBA 的真正护城河</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#c89800;font-weight:600;margin-bottom:8px;">迁移场景：强社交产品 / 多人协作</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">MOBA 的粘性来源不是玩法，是关系链。"和朋友开黑"比"打 5v5"更让人上瘾。微信/QQ 的关系链导入是王者荣耀压倒《全民超神》的关键。中小厂做 MOBA 必败于腾讯，就是输在"你没有关系链"</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(200,155,60,0.3);">📊 2017-05 用户 2.01 亿，男女 1:1.18（极光大数据）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(200,155,60,0.1);">
          <div class="ic-num" style="color:#c89800;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">皮肤 IP 化 = 跨界联名 + 传统文化</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#c89800;font-weight:600;margin-bottom:8px;">迁移场景：IP 长线运营 / 跨界联名</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">王者荣耀用皮肤把游戏变成了 IP 载体：2022 年和南昌滕王阁联动的"弈星-滕王阁序"让滕王阁国庆接待人次同比 +10%；2024 年和李白故居江油联动的"李白-谪仙醉月"让江油旅游收入同比 +29.82%</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(200,155,60,0.3);">📊 2022 滕王阁、2024 江油（江油市文广旅局）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#fff5dd 100%);border:1px solid rgba(200,155,60,0.25);border-left:5px solid #c89800;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(200,155,60,0.1);">
          <div class="ic-num" style="color:#c89800;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#1a1500;margin-bottom:6px;">电竞生态 = 持续生产共同记忆</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#c89800;font-weight:600;margin-bottom:8px;">迁移场景：长生命周期运营 / 玩家社区</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">KPL 联赛（2016-09 首届）+ 高校赛 + 城市赛 + 亚运会电竞（2023 杭州首金）形成完整赛事体系。电竞不只是营销，它在持续生产"我们一起看的比赛"这种共同记忆——这是 MOBA 比 RPG 更难被取代的原因</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(200,155,60,0.3);">📊 KPL 自 2016 年举办至今 9 年（腾讯电竞）</div>
        </div>
      </div>

      <h4>4.2 对独立游戏 / 中小厂的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fffaf2 0%,#fff0db 100%);border-left:4px solid #c89800;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#c89800;font-weight:700;">方法论洞察 · 边缘项目的赛马机制</div>
        <p>《王者荣耀》最初是腾讯天美的"边缘项目"，《全民超神》才是嫡系——结果边缘的跑赢了嫡系。这给中小厂一个启示：<strong>不要被"重要"项目绑架</strong>，反而要保留几个"看起来不重要"的实验项目，让它们自由生长。这与腾讯内部的"赛马机制"哲学一致：QQ 秀、QQ 空间、微信、王者荣耀都不是决策层战略决策出来的产品。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fffaf2 0%,#fff0db 100%);border-left:4px solid #c89800;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#c89800;font-weight:700;">方法论洞察 · 短局时 + 移动端 = 全民玩家</div>
        <p>MOBA 在端游上是"30-40 分钟的硬核游戏"，到了移动端被压缩到 15 分钟可投降，结果用户规模从 2000 万飙升到 2 亿。中小厂要思考：<strong>你的品类里有没有"短局时"的简化版机会</strong>？把 30 分钟对局简化到 5 分钟、把硬核操作简化为"一指流"——这不是降级，是"扩大目标用户"的机会。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fffaf2 0%,#fff0db 100%);border-left:4px solid #c89800;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#c89800;font-weight:700;">方法论洞察 · 辅助的"高频小高光"设计</div>
        <p>辅助英雄（以 2019-04-16 上线、588 点券的瑶为代表）被设计成"完全依赖队友 + 独特机制"，但通过<strong>短而频繁的高光</strong>（附身、刷盾、解控）让每个玩家都感受到"我在做贡献"。中小厂做合作类游戏时，<strong>不要让辅助/辅助位变成"工具人"</strong>，要给辅助位独立的高光时刻——这是降低辅助位玩家流失的关键。</p>
      </div>

    </div>

    <div id="'''

# 替换 panel-analysis 内容
old_pattern = re.compile(r'panel-analysis" class="tab-panel active">.*?</div>\s*<div id="panel-think"', re.DOTALL)
new_content = old_pattern.sub(new_analysis, html, count=1)

if new_content == html:
    print("ERROR: 替换失败，pattern 没匹配到")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ panel-analysis 替换成功")
    print(f"原文件 {len(html)} 字符 → 新文件 {len(new_content)} 字符")
    print(f"新增 {len(new_content) - len(html)} 字符")
