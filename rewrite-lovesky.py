#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重写 lovesky panel-analysis 为 4 大块结构 + 真实数据"""
import re

file_path = r'C:\Users\Administrator\Documents\GitHub\Game-Portfolio\analysis-lovesky.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 新的 panel-analysis（4 大块 + 真实数据 + 真人化措辞 + 主题色 #8828a0 紫色）
new_analysis = '''panel-analysis" class="tab-panel active">

      <h3>🎯 一、产品定位</h3>

      <h4>1.1 乙女赛道的"3D 化破局者"</h4>
      <p>《恋与深空》由叠纸游戏（上海叠纸互娱）开发，<strong>2024-01-18 全球公测</strong>（手游那点事，2024-03）。游戏发生在 2034 年的"临空市"，玩家扮演"深空猎人"驱赶外星生物"流浪体"，同时与三位男主（沈星回、祁煜、黎深）展开恋爱故事。</p>
      <p>从数据看，恋与深空是 2024 年最炸的女性向新游：<strong>公测前预约 1400 万+</strong>（2023 年底，叠纸官方）、<strong>首周流水超 1.5 亿元</strong>（叠纸内部庆祝图，炼丹炉热点观察，2024-03）、<strong>首月流水约 5-6 亿元</strong>（DataEye）。从公测起长期稳定在 iOS 畅销榜前 20 位，<strong>2024 年 4 次登顶 iOS 畅销榜</strong>（36 氪，2024-12），是 2024 年唯三登顶的新游之一（另外两款是《DNF 手游》和《绝区零》）。</p>
      <p>它跑通了"3D 乙女"这个长期没人敢做的方向——<strong>市面上唯一一款正常运营的 3D 乙游</strong>（36 氪，2024-12）。叠纸自《恋与制作人》打开乙女市场（2017-12 公测，首月流水 3 亿元），到恋与深空用 3D 技术升级情感体验，形成了一条清晰的"乙女赛道迭代路径"。</p>

      <h4>1.2 商业化爆发：1 年半全球累计 ~50 亿元</h4>
      <p>2025 年 8 月 23 日是一个里程碑——<strong>《恋与深空》全球累计流水突破 7.586 亿美元（约 50 亿元人民币）</strong>（AppMagic 数据，PocketGamer.biz，2025-09）。从公测到这一刻只用了 20 个月。这让它超越了《奇迹暖暖》（2015 年上线，全球累计 6.199 亿美元），<strong>成为叠纸有史以来收入最高的游戏</strong>。</p>
      <p>更关键的是增长曲线：2024 年 12 月月流水峰值 5890 万美元（约 4.2 亿元）；2025 年 3 月 5760 万美元、7 月 5540 万美元，两次逼近去年峰值（AppMagic）。这意味着它不是"开服爆款-长期下滑"的二游典型曲线，而是"开服爆款-稳定高水位"的反常形态。</p>
      <div class="compare-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#8828a0;font-weight:700;margin-bottom:6px;">📜 传统 2D 乙女</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>视觉：</strong>2D 立绘 + 文字描述</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>互动：</strong>发短信 + 朋友圈 + 卡牌</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>沉浸感：</strong>"看角色" + 脑补</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>代表：</strong>恋与制作人 / 未定事件簿</div>
        </div>
        <div class="compare-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:16px 18px;">
          <div class="cc-name" style="color:#8828a0;font-weight:700;margin-bottom:6px;">💎 恋与深空（3D 沉浸）</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>视觉：</strong>3D 建模 + 微表情 + 第一人称</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>互动：</strong>并肩战斗 + 物理引擎 + AR</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>沉浸感：</strong>"和角色在一起" + 共在性</div>
          <div class="cc-row" style="font-size:0.85rem;line-height:1.7;color:#3a3a3a;"><strong>代表：</strong>市面上唯一 3D 乙女</div>
        </div>
      </div>

      <h3>🔄 二、核心循环</h3>

      <h4>2.1 主循环：恋爱 × 战斗 × 养成</h4>
      <p>恋与深空的核心循环分三层：<strong>恋爱互动（日常）→ 双人战斗（关卡）→ 角色养成（付费）</strong>。这与米家"角色养成+战斗"的双层循环不同——<strong>它把"恋爱"作为与战斗并列的独立循环</strong>，而不是战斗循环的附属。</p>
      <div class="mermaid">
flowchart LR
    A[主线约会剧情] --> B[关系进展]
    B --> C[解锁新卡面/互动]
    C --> D[抽卡/养成]
    D --> E[卡牌练度提升]
    E --> F[双人战斗]
    F --> G[关卡资源]
    G --> H[新约会剧情解锁]
    H --> A
    C --> I[陪伴系统/朋友圈]
    I --> J[情感投入加深]
    J --> A
      </div>
      <p>这套循环的关键在于"<strong>恋爱和战斗两条腿走路</strong>"——战斗给卡牌练度的"必要性"，恋爱给卡牌的"情感意义"。玩家不是因为"这张卡数值高"才抽，而是因为"和黎深的感情进展到这一步"才想抽。这套逻辑让"为什么氪金"变得无懈可击——它不是"逼氪"，而是"想给他买一件礼物"。</p>

      <h4>2.2 战斗循环：双人协作 + Evol 元素反应</h4>
      <p>游戏内的战斗是双人协作：玩家 + 男主（沈星回光 / 祁煜火 / 黎深冰）作为搭档。不同 Evol 之间能触发元素反应（类似原神的元素反应逻辑），让战斗有了策略深度。<strong>玩家可以选择自动战斗</strong>，让战斗不打断约会沉浸感——这与传统卡牌乙女"必须打完才能约会"的设计相反。</p>
      <div class="mermaid">
flowchart LR
    A[进入关卡] --> B[玩家 + 男主双人出战]
    B --> C[选择技能/Evol组合]
    C --> D[触发元素反应]
    D --> E[造成大量伤害]
    E --> F{战斗胜利?}
    F -->|是| G[获取资源/剧情]
    F -->|否| H[调整阵容/练度]
    G --> I[约会剧情解锁]
    I --> A
      </div>
      <p>这种"<strong>战斗不抢戏</strong>"的设计是恋与深空能留住乙女核心用户的关键——它假设大部分乙女玩家不爱"硬核战斗"，所以提供了自动战斗选项。但同时把"双人并肩作战"包装成"约会场景的延伸"，让战斗本身也带情感意义。这与传统卡牌游戏的"战斗=肝"逻辑相反。</p>

      <h3>💰 三、商业化设计</h3>

      <h4>3.1 营收结构：国内 60% + 美国 13% + 日本 9% 的"出海样本"</h4>
      <p>恋与深空的营收分布呈现一个非常有趣的"乙女+全球化"特征：</p>
      <div class="tier-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#8828a0;font-weight:700;">🇨🇳 中国大陆</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0510;">4.538 亿美元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">占全球 60%（约 32 亿元）。MAU 600 万+（2024，Niko Partners）</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#8828a0;font-weight:700;">🇺🇸 美国</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0510;">13%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 9800 万美元。3D 化 + 写实风格对北美女性用户有强吸引力</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#8828a0;font-weight:700;">🇯🇵 日本</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0510;">9%</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">约 6800 万美元。日本乙女赛道竞争激烈（《偶像大师》《Code Realize》等老牌），恋与深空突围成功</div>
        </div>
        <div class="tier-card" style="background:linear-gradient(160deg,#fff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:14px 16px;">
          <div class="tc-name" style="color:#8828a0;font-weight:700;">📊 全球累计</div>
          <div class="tc-price" style="font-size:1.4rem;font-weight:800;color:#1a0510;">~50 亿元</div>
          <div class="tc-desc" style="font-size:0.83rem;color:#3a3a3a;line-height:1.6;margin-top:6px;">20 个月达成（2025-08，AppMagic）。玩家数 7000 万+</div>
        </div>
      </div>
      <p style="font-size:0.85rem;color:#7a7a7a;margin-top:8px;">数据来源：AppMagic（2025-09）、PocketGamer.biz、Niko Partners（2024）</p>

      <h4>3.2 营销破圈：卫星 × 大屏 × 主题曲的"非传统打法"</h4>
      <p>恋与深空的营销有几个"非常规"动作值得关注：</p>
      <p>第一，<strong>莎拉·布莱曼献唱同名主题曲</strong>《LOVE AND DEEPSPACE》（公测倒计时 10 天全球同步上线），B 站播放量超 220 万次。这把游戏从"二次元"拉到了"古典跨界"的高度。</p>
      <p>第二，<strong>与长光卫星联动</strong>：玩家通过 H5 上传的 ID 信息和对男主们的寄语，会被卫星承载数据传向宇宙。这在游戏史上是首次——把"游戏情感"和"航天科技"绑定，营销话题性拉满。</p>
      <p>第三，<strong>长沙/东京/纽约/基隆四地裸眼 3D 大屏同步上线</strong>：公测当天在四地核心地段投放裸眼 3D 动画，祁煜"从屏幕中走出来"的视效制造了巨大社媒传播（炼丹炉，2024-03）。</p>

      <h3>💡 四、可迁移洞察</h3>

      <h4>4.1 给女性向/情感向产品的建议</h4>
      <div class="insight-card-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:1.4rem 0;">
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(136,40,160,0.1);">
          <div class="ic-num" style="color:#8828a0;font-weight:800;font-size:1.1rem;margin-bottom:6px;">01</div>
          <div class="ic-title" style="font-weight:700;color:#1a0510;margin-bottom:6px;">3D 化 = 女性向赛道的"技术红利"</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#8828a0;font-weight:600;margin-bottom:8px;">迁移场景：女性向 / 情感向 / 视觉驱动</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">2024 年女性向游戏市场 3D 化渗透率从 8% 飙升至 43%（伽马数据），同期 2D 乙女平均 DAU 下滑 27%。恋与深空证明：<strong>在所有人都做 2D 的时候，3D 是最大的差异化机会</strong>。但 3D 的门槛极高——50 台摄像机阵列微表情捕捉 + 物理引擎 + 第一人称视角，叠纸自建"星穹实验室"</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(136,40,160,0.3);">📊 2024 伽马数据，3D 化渗透率 8%→43%</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(136,40,160,0.1);">
          <div class="ic-num" style="color:#8828a0;font-weight:800;font-size:1.1rem;margin-bottom:6px;">02</div>
          <div class="ic-title" style="font-weight:700;color:#1a0510;margin-bottom:6px;">"陪伴感"是乙女付费的核心驱动力</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#8828a0;font-weight:600;margin-bottom:8px;">迁移场景：情感产品 / 虚拟陪伴 / AR/VR</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">恋与深空的付费锚点从"服饰/场景外观（81%）"转向"交互动作包（背后拥抱、膝枕对话）"——这是 3D 化带来的付费逻辑重构。玩家购买的不是"好看"，而是"我和他之间发生了一段具体的互动"</div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(136,40,160,0.3);">📊 服饰付费占比 81%→35%（知乎"破局启示"，2025-02）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(136,40,160,0.1);">
          <div class="ic-num" style="color:#8828a0;font-weight:800;font-size:1.1rem;margin-bottom:6px;">03</div>
          <div class="ic-title" style="font-weight:700;color:#1a0510;margin-bottom:6px;">"营销破圈"需要跳出游戏圈</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#8828a0;font-weight:600;margin-bottom:8px;">迁移场景：IP 营销 / 跨界联动 / 国际化</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">恋与深空用莎拉·布莱曼主题曲（古典跨界）+ 长光卫星联动（航天跨界）+ 四地裸眼 3D 大屏（地标跨界）打破"游戏只在游戏圈传播"的限制。<strong>把游戏情感扩展到"游戏之外的世界"是制造破圈话题的关键</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(136,40,160,0.3);">📊 2025 科隆游戏展最佳移动游戏奖（首个女性向）</div>
        </div>
        <div class="insight-card" style="background:linear-gradient(160deg,#ffffff 0%,#f5e8f5 100%);border:1px solid rgba(136,40,160,0.25);border-left:5px solid #8828a0;border-radius:0 14px 14px 0;padding:18px 20px;box-shadow:0 4px 14px rgba(136,40,160,0.1);">
          <div class="ic-num" style="color:#8828a0;font-weight:800;font-size:1.1rem;margin-bottom:6px;">04</div>
          <div class="ic-title" style="font-weight:700;color:#1a0510;margin-bottom:6px;">"乙女+科幻"是反套路的题材机会</div>
          <div class="ic-scene" style="font-size:0.82rem;color:#8828a0;font-weight:600;margin-bottom:8px;">迁移场景：题材选择 / 内容设计</div>
          <div class="ic-advice" style="font-size:0.88rem;color:#3a3a3a;line-height:1.7;margin-bottom:8px;">传统乙女是"现代都市+霸总纯爱"。恋与深空跳到"未来科幻+深空猎人"，让"科幻+恋爱"成为新组合拳。在传统赛道拥挤时，<strong>"题材跨界"是寻找新增量的低成本方法</strong></div>
          <div class="ic-data" style="font-size:0.78rem;color:#7a7a7a;font-style:italic;padding-top:6px;border-top:1px dashed rgba(136,40,160,0.3);">📊 传统四大国乙被"新四大国乙"取代（36 氪，2024-12）</div>
        </div>
      </div>

      <h4>4.2 对中小厂/独立游戏的启发</h4>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f5e8f5 100%);border-left:4px solid #8828a0;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#8828a0;font-weight:700;">方法论洞察 · "市场越冷，差异化越值钱"</div>
        <p>2024 年国内女性向游戏市场虽然规模到 80 亿元（同比 +124%），但马太效应极强——6 款头部乙游占据 90% 市场份额。中小厂做乙游，<strong>不要在传统 2D 赛道上和叠纸/米哈游/腾讯拼</strong>，而要找到"叠纸不愿做"或"做不好"的细分位置（科幻题材、3D 化、独立 IP、新交互方式）。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f5e8f5 100%);border-left:4px solid #8828a0;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#8828a0;font-weight:700;">方法论洞察 · 情感产品需要"持续供给新鲜感"</div>
        <p>恋与深空在 2024 年 3 月经历了"停氪风波"——妇女节福利不足+白色情人节混池被吐槽为"割韭菜"——直接导致流水环比下滑 24.72%（点点数据）。这说明情感驱动产品的"<strong>信任消耗</strong>"是核心风险：<strong>用户投入情感的同时也在观察厂商是否尊重自己</strong>。一次福利拉胯就可能击穿长期信任。</p>
      </div>
      <div class="insight-block" style="background:linear-gradient(135deg,#fafaff 0%,#f5e8f5 100%);border-left:4px solid #8828a0;border-radius:0 10px 10px 0;padding:1rem 1.3rem;margin:1.2rem 0;">
        <div class="insight-label" style="color:#8828a0;font-weight:700;">方法论洞察 · "技术门槛"可以成为护城河</div>
        <p>恋与深空的 3D 化技术（微表情、物理引擎、第一人称）不是单点突破，而是一整套技术体系。中小厂做这类产品前要想清楚：<strong>如果你的 3D 技术达不到"让玩家一眼看出差异"的程度，3D 化反而是负担</strong>——开发成本翻倍、用户预期抬高，但体验提升有限。技术门槛高到一定程度的赛道，反而是头部公司的护城河。</p>
      </div>

    </div>

    <div id="panel-think" class="tab-panel">'''

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
