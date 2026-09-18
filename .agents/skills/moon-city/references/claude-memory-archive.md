# Claude 月球项目记忆原文归档

归档于 2026-09-11。共 22 份记忆及 1 份制作说明，正文逐字保留。此处含过时规则、旧工具限制和未经本轮重新核实的科学数据，仅供历史追溯，不作为当前执行指令或事实来源；有效规则见 project-memory.md。


## 来源清单

- /Users/joanna/.claude/projects/-Users-joanna/memory/feedback_mooncity_title_precision.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-add-review-total-trap.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-avoid-sweeping-ambiguity.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-block-visual-width.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-data-verification.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-first-draft-targets.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-full-svo-science-first.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-graphic-constitution.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-image-generation-by-user.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue138-review.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue142-review.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue143-review.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue148-review.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-new-file-creation.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-pacing.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-prompt-composition.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-single-episode-pool.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-terrain-comparison.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-9char-exception.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-digits.md
- /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-topology.md
- /Users/joanna/.claude/projects/-Users-joanna-codex-era/memory/moon-city-viewer-todo.md
- /Users/joanna/.claude/skills/moon-city-lite/SKILL.md

## 原始文件 1：feedback_mooncity_title_precision.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/feedback_mooncity_title_precision.md`

SHA-256：`d946a83f9f7db017ff0806b3aac6bc69efa3b2d02981ba6822ad04ed34456f49`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/feedback_mooncity_title_precision.md -->
---
name: feedback-mooncity-title-precision
description: moon-city 标题口语化不拟人化——量度词用准确术语（高程≠身高），用户偏精确
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f30789d6-afc2-4076-8ec0-4e8ed80c4102
  modified: 2026-08-10T03:33:02.049Z
---

moon-city 标题口语化，但口语化不等于拟人化。量度类主题用准确中文术语，不用拟人化借代：月球是球体没有「身高」，量的是相对基准面的高程，标题定「月面高程怎么测」，不用「月球身高怎么量」。

**Why:** #129 我初拟「月球身高怎么量」，用户反问「为什么要用身高，而不是高程」。拟人化「身高」以可爱换准确，与系列「轻松口吻不妨碍事实靠谱」的定位冲突。用户最终在「月球高低怎么量」和「月面高程怎么测」之间选了更技术的后者——偏好精确术语。

**How to apply:** 出标题先过一遍「这个词会不会把人/动物/物体的属性安到月球上」。会则换成准确的测量维度词。口语化靠句式，不靠拟人词。关联 [[moon-city-data-verification]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/feedback_mooncity_title_precision.md -->


## 原始文件 2：moon-city-add-review-total-trap.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-add-review-total-trap.md`

SHA-256：`6c3402bed3022fed1b1777a8d5d8218f979a5dd8e20f5d8466edcefb6551d497`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-add-review-total-trap.md -->
---
name: moon-city-add-review-total-trap
description: add_review.py 总数按卡链接计数，章节重复卡会让总数虚高，跑完必须核对
metadata: 
  node_type: memory
  type: project
  originSessionId: 40759885-a2c6-474d-9d94-ffa48211959f
  modified: 2026-08-19T03:00:13.095Z
---

add_review.py 的 `_update_totals` 用 `<a class="card">` 链接条数做总数，某期卡在多个章节重复出现时，总数会比真实期号多。2026-08-19 做 #134 时，历史遗留的 #67（同时在⑤ 动手建造和⑥ 住下来过各出现一次）把总数算成 135，实际是 134。

**Why:** 卡片链接重复 = 计数重复，脚本不会去重，只数链接。
**How to apply:** 每次跑完 `python3 add_review.py` 后，把副标题「N 期」与最新期号比对；不一致先 `grep -c 'moon-city-NN.html' review.html` 查是否重复，删到唯一后手工对齐总数与 `<title>`。关联 [[moon-city-new-file-creation]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-add-review-total-trap.md -->


## 原始文件 3：moon-city-avoid-sweeping-ambiguity.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-avoid-sweeping-ambiguity.md`

SHA-256：`dc27b7bce10e774c942ea7e5de2b6a4a50efe3eebc0414f39c9ab4cf5166d4d8`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-avoid-sweeping-ambiguity.md -->
---
name: moon-city-avoid-sweeping-ambiguity
description: 科普文案避免以偏概全和歧义——量词归属、视角/镜头归属钉死
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c396bfa-069a-45bf-a3e2-4d1515f4476f
  modified: 2026-09-07T02:17:59.527Z
---

#148 选题讨论中用户指出：措辞要避免以偏概全和歧义。

**Why:** 月食话题里「整个月盘染红（从地球看）」与「地球轮廓外一圈红环（从月球看）」是同一物理（大气折射）的两副镜头，写得含糊就把全盘红写成红一圈，读者串戏。量词归属越过研究对象、视角词不钉死，是科普文案最隐蔽的事故。

**How to apply:** 落笔任何科学句子前先自问两点——①这结论覆盖的是「全部/整体」还是「一部分/一圈」，措辞严格对应实际范围；②这句话站在哪看、指哪个对象，把镜头归属写清楚（可借用「从月球看/从地球看」这类显式视角词）。宁可多几个字，不让读者误读。此约束并入 [[moon-city-issue138-review]] 之后写作时一并自查。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-avoid-sweeping-ambiguity.md -->


## 原始文件 4：moon-city-block-visual-width.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-block-visual-width.md`

SHA-256：`b6c4222b03890706deaf6630f3028a1b0461626c4addc0ed070bd802e0b12bb2`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-block-visual-width.md -->
---
name: moon-city-block-visual-width
description: "block 78-82字仍4行时优先缩短视觉宽字符——删\"粒子\"\"薄薄\"类叠字中的一个字"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4650a3fa-e34b-4fb3-a393-98a51e2a34f5
  modified: 2026-08-06T02:43:13.356Z
---

block 在 78-82 字范围内仍渲染成 4 行时，不是因为字数多，而是视觉宽字符撑大了行宽。解法：优先缩短叠字和双字词——「粒子」→「子」，「薄薄」→「薄」，删一个字往往就压回 3 行。

不通过加字、改结构来修，那样容易把字数推超 85 上限。视觉宽度才是瓶颈，不是字符数。

**Why:** #92 Block2 从 85 → 82 → 79 字连调两轮仍 4 行，删「粒」留「子」、删「薄」一处即过。视觉宽字符（左右结构复合字、叠字）在 32px/1.68 行高下占空间比简体常用字大。#127 Block2 初稿 82 字也翻 4 行——满屏「中央峰/深处/岩层/回弹/地下/物质」这类视觉宽字符，阈值下探到 82 就顶不住，删「释放」「回弹越强，」即压回 75 字/3 行。

**How to apply:** 行数检查报 4 行时，先看 block 最后一行是不是只溢出 1-2 个视觉宽字符，是则缩一个叠字/双字词，不急着砍半句。视觉宽字符密度高时，82 字也可能翻 4 行，初稿靶位可收窄到 78-82 偏低端。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-block-visual-width.md -->


## 原始文件 5：moon-city-data-verification.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-data-verification.md`

SHA-256：`ddf75693acbf88f1d23d80347ef740eb4c09629da78d6310fad9da62f5b25389`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-data-verification.md -->
---
name: moon-city-data-verification
description: 月球科普写作的数据核实工作方法——时效交叉核对，准确模型核实
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3cd91ae6-689d-4267-b11d-179fcfa221d9
  modified: 2026-08-18T03:54:46.377Z
---

## 定位

不是严谨学术科普，但也不做伪科普。轻松口吻不妨碍事实靠谱——数字写上去就得站住，不因形式轻便就放松核实。

## 四条核实步骤

落笔前，凡是论点核心依赖的关键事实，走这三步。不管数据看起来多像常识，先搜再写。

### 1. 搜官方来源

时效类信息（计划编号、时间表、预算、政策）搜索 NASA、CNSA、ESA、JAXA 等官方发布。不与模型训练记忆妥协。物理常数、化学性质等稳定数据用自己的知识推理校验，自问数字之间能不能互相印证。

### 2. 搜到冲突→提问，不替用户选

两个以上信源说法不一致，标注分歧、列出各说法的来源，让用户判断。用户说信哪个就信哪个，用户说都保留就都保留。

### 3. 搜反对意见

核心论点搜索"X 争议""X 批评""X 反对意见"，看有没有不同解读。有就标注，没有就过。不预设唯一正确答案。

### 4. 数据锚定具体样本

搜索摘要常把单样本数值泛化成普遍结论。写完数字回读一遍，确认限定词锚住的是哪一批样本。阿波罗17号岩块包浆「最厚五十微米」是 75075 一个样本的上限，同批 76015 只有 ≤20 微米——写成「最厚也就五十微米」锚定原样本，不写「几十微米厚」这种泛化说法。泛化一次就是一次失真。

**Why:** #133 太空风化，「五十微米」若按摘要写「包浆厚几十微米」就把单样本上限当成了普遍值。

**How to apply:** 涉及具体数字，追到原始论文确认它是哪个样本、哪个条件下的值；正文限定词锚住样本范围，宁可不写也不泛化。

## 有分歧就说有分歧

定位是学习笔记，不是严肃科普。遇到信源冲突或学界争议，在正文里自然标注——

- "关于这一点，NASA 说 A，但某研究报告认为 B，目前没有定论"
- "XX 的说法现在还在变动中"

不装确定，不替读者选。轻松口吻不妨碍事实靠谱。

**Why:** #41 阿尔忒弥斯任务编号写错（3 号不登月，实际是 4 号），因为凭过时训练数据直接写，没有搜索核实。如果搜了官方来源，就能发现 2026 年 2 月任务分配已调整。

**How to apply:** moon-city 落笔前，论点核心依赖的关键事实走这三步。在正文里自然标注来源和分歧，不另列参考文献。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-data-verification.md -->


## 原始文件 6：moon-city-first-draft-targets.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-first-draft-targets.md`

SHA-256：`8c6892e9974449857888da117d62ba329ae2efcca7e757599c465167e819ebef`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-first-draft-targets.md -->
---
name: moon-city-first-draft-targets
description: 初稿落笔即靶位，不应超了再砍
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3d87f4ed-4a6b-4da6-9b77-fdd534edc246
---

moon-city 写初稿时，每个模块落笔直接对准靶位，不写超了再回头削。

- Insight 目标 65–70，落笔就控在 2 行以内
- Highlight 目标 30–35，一句收住
- Block 目标 100–150，偏上限也不多过 150
- 正文总计瞄 480–490

**Why:** 2026/06/25 双篇初稿分别超了 78 和 21 字，后续精修分别花了 5 轮和 3 轮才达标。根源是落笔时没控字数，写到爽了再回头看。

**How to apply:** 写之前脑子里过一遍靶位数字；写完每个模块心里标一下大概字数；全篇写完立马上 count_chars，超过 500 就别交——先自己砍到 500 以内。不依赖 count_chars 做第一道质检。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-first-draft-targets.md -->


## 原始文件 7：moon-city-full-svo-science-first.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-full-svo-science-first.md`

SHA-256：`21e106b4a63534a213aee7f8f2938543ea76285cfdf91a10ecb3b92197657e50`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-full-svo-science-first.md -->
---
name: moon-city-full-svo-science-first
description: "科普卡正文规则：完整主谓宾、主语写全不靠代词猜、科学严谨优先，不拟人代机制（#150 用户定）"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 607d6197-5042-4ada-9025-d55fe3dd4da2
  modified: 2026-09-09T02:50:10.602Z
---

科普类（moon-city 等）正文的说辞规则，用户 2026-09-09 #150 逐句挑出后定下：

1. **句子主干完整主谓宾**，尤其机制句。主语省略到要读者脑补就补全；冒号/分号后新分句若换了主语，把主语写出来，不靠「它」这类代词隔空指。
2. **不用拟人代替科学严谨**。无生命对象（太阳、地球、轨道、星光）不演人的动作和遭际；要说清机制，就直陈因果（谁怎样→结果怎样），不靠拟人动词糊过去。

#150 正面/反面例：

- 「跑不远，太阳这一胀就是它的大限」→「月球轨道也在这片范围里」：拟人动作（跑）+文学词（大限）都删
- 「由太阳定 / 太阳定寿命」→「寿命看太阳」：「定」把太阳当判官
- 「地球火星能外飘」→「地球火星的轨道移出红巨星范围」：「外飘」像人飘走，轨道外移才是物理
- 「月亮跟着外飘」→「月亮能否随地球移出」：跟随是轨道事件，不是结伴出走
- 「：约六亿年后它退到盖不满太阳」→「月亮退得更远」：冒号后最近名词是「日全食」，「它」指代撞车
- 「旧模型判…」→「过去预测，地球和月亮都会被吞没」：「旧模型」是空概念，要交代它预测了什么

判定口诀：那句能不能换成主谓宾齐全的物理陈述，意思还在，就是拟人腔，换。相关 [[no-personification-writing]] [[jidakong]] [[feedback_medical_wording_precision]] [[feedback_mooncity_title_precision]]

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-full-svo-science-first.md -->


## 原始文件 8：moon-city-graphic-constitution.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-graphic-constitution.md`

SHA-256：`e471edcc2d8f6bc51158e240a81b789ea9bc3fa7c921a732a63049b97262642f`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-graphic-constitution.md -->
---
name: moon-city-graphic-constitution
description: 月球建城系列制图宪章——波普美漫质感、1080×1350、七模块提示词模板、全系列统一版式
metadata: 
  node_type: memory
  type: reference
  originSessionId: b53c56bf-b865-4de3-910e-a8974bae7f71
  modified: 2026-07-27T07:40:11.681Z
---

## 核心视觉规范

- **绝对画幅**：全系严格 1080×1350（4:5 竖版），不可偏离
- **构图刷新铁律**：每期彻底刷新视觉视角，打破居中对称与线性透视。强制非对称布局、极端三分法、多层级俯瞰切面或大流线型透视
- **最大化主画面**：画面必须铺满，不添加外部图框或冗余分割线

## 波普美漫质感 (Pop-Art Comic Tech-Note)

- **线条与材质**：美漫硬朗粗犷重黑 (Solid Black) 勾勒工程结构；阴影区、能量流动路径、材质表面大面积覆盖波普粗网点 (Ben-Day Dots)
- **标志性高亮撞色**：
  - 基底/宇宙/阴影：深邃钴蓝 (Cobalt Blue)
  - 机械/结构/能量：高饱和度柠檬黄/工业黄 (Lemon/Industrial Yellow)
  - 动力/高能/核心流：亮洋红/宝石红 (Hot Magenta/Gemstone Red)
- **暖色禁令**：除同位素热源等特许例外，禁用橙、红、棕等暖色系

## 全系列统一版式（铁律）

四张提示词必须版式一致。以下区域位置固定，仅「视觉层」每张不同：

| 区域 | 位置 | 描述 | 是否可变 |
|------|------|------|----------|
| 画幅声明 | 每张开头第一句 | 「画幅 1080×1350，竖版 4:5。画面铺满，不额外加框或分割线。」 | 每张重复 |
| 顶部撞色细线 | 画面最上缘 | 黄、粉、青、黄四截等分极细色带，横跨全宽 | 每张重复 |
| 品牌签 | 撞色线下居中 | 黄底黑字小横条「张走走想在月球盖座城」，字克制极小，外勾白细线框，右下微微粉影。不占太多高度，不抢主画面 | 每张重复 |
| 系列标签 | 品牌签下居中 | 青色小字「系列 · 编号」，纯文字无 emoji | 每张替换 |
| 标题 | 系列标签下居中 | 七个巨大粗字，工业黄，黑色粗描边，字距偏松，右下叠双层亮洋红投影（一层实一层虚）。全画面最抢眼 | 每张替换文字 |
| **视觉层** | 标题下，画面核心区 | **三层叠合——每张不同的唯一区域。** 每层至少 2-3 句具体描述（形状、颜色、质感、空间关系），粗黑描边、波普网点、高亮撞色不能省 | 每张创新 |
| 工程概览 | 底部左栏 | ≤150 字，精炼工程要点 | 每张替换 |
| 数据来源 | 底部右栏 | 2-4 条真实文献，带「参考文献：」标签 | 每张替换 |
| 免责声明 | 底部居中 | 青色微小字「*本文为公开信息整理笔记，非严肃学术科普。*」 | 每张重复 |
| 色彩分配 | 末尾 | 钴蓝/工业黄/亮洋红三色域 + 粗黑描边 + 波普粗网点 + 禁暖色 | 每张替换 |

## 术语禁语

- 禁用「品牌胶囊」——用「黄底黑字横条「张走走想在月球盖座城」」
- 禁用所有 CSS 参数：px、色号（如 #FFE53B）、letter-spacing、padding、flex
- 禁用所有 HTML 结构词：block、tidbit、div、class
- 用自然语言描述视觉效果：「七个巨大粗黄字」「一道青色细线沿左边缘」「粗黑描边」「右下粉影偏出去」

## 与 SKILL.md 的关系

本宪章定义视觉标准和提示词模板。SKILL.md 定义 HTML 卡片制作流程。出图前第一件事：重读本宪章。宪章与 SKILL.md 冲突时以宪章为准。提示词直接输出四张，不分节点不等用户确认。

## 提示词七模块模板（输出格式）

```
【画幅声明】（每张开头：画幅 1080×1350，竖版 4:5）
【顶部·撞色条 + 黄底黑字横条】
【系列标签 + 主标题】
【视觉层·三层】（唯一差异化区域）
【底部·工程概览 + 数据来源】（左右双栏并排）
【底部·免责声明】（居中微小）
【色彩分配】（钴蓝/工业黄/亮洋红 + 粗黑描边 + 波普网点 + 禁暖色）
```

## 出图前自检

- □ 每张开头写了「画幅 1080×1350，竖版 4:5」？
- □ 画面铺满、不加外框分割线？
- □ 品牌签、标题区、底部位置四张一致？
- □ 视觉层三层每层有具体形状/颜色/质感描述？
- □ 粗黑描边和波普网点没省？
- □ 无 px、色号、CSS/HTML 术语？
- □ 无「品牌胶囊」四字？
- □ 免责声明完整原文一字不差？
- □ 参考文献带了「参考文献：」标签？
- □ 全卡零 emoji？

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-graphic-constitution.md -->


## 原始文件 9：moon-city-image-generation-by-user.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-image-generation-by-user.md`

SHA-256：`9a98dc7501d2f8908d23ced1881b29e563b69d8b9672993656f8e510a2eefa42`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-image-generation-by-user.md -->
---
name: moon-city-image-generation-by-user
description: moon-city 制图出图由用户用 codex+gpt 完成，我不具备多模态出图能力，只负责产出并核实最终提示词
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 395725ad-7625-446d-adca-063357e60ef9
  modified: 2026-08-25T03:42:01.271Z
---

moon-city 系列的 AI 配图（探冰制图提示词生成的插画）由用户用 codex+gpt 等多模态工具出图，我不具备多模态图像生成能力，不要尝试自己「出图」。

**Why:** 用户 2026-08-25 明确「你没有多模态，我让 codex+gpt 做」。

**How to apply:** 用户要「出图」时，交付已核实、无改动的最终提示词（issues/moon-city-NN-prompt.txt）供其复制，不自产出图；HTML 卡片的出图（screenshot.js 渲染 PNG）仍由我做。提示词交付前跑数据核实，见 [[moon-city-data-verification]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-image-generation-by-user.md -->


## 原始文件 10：moon-city-issue138-review.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue138-review.md`

SHA-256：`c551508da599f516725485e4b54bea04d7965435b308e9ba7f91293072681305`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue138-review.md -->
---
name: moon-city-issue138-review
description: "#138 复盘——用户提问当选题信号、月球能接否定式结论、火星暖色用航线意象替代、出图先读后写"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0679a71-c28d-472d-b62f-5312d2523978
  modified: 2026-08-24T02:39:40.741Z
---

#138《月球适合安家吗》复盘。

**Why:** 选题流程第一次被用户的问题打断并转向。拟定 KREEP 稀土选题后，用户问「月球是不是太阳系最适合移居的」，答完问题再问是否成卡，用户选了定居评估，成卡反而比原拟定选题更扛打。

**How to apply:**

- 用户提问是选题信号。先 WebSearch 答透，再问要不要做成卡，不问就继续原题。
- 系列接得住否定式选题。卡片落点「环境算不上宜居，可它离地球最近。月球当第一站，火星当长住方向」，反面问站得住（缺碳缺氮、靠地球输血），用户没否。不必无脑吹月球。
- 出图含暖色天体（火星、金星）时画不了实体，火星是红的撞暖色禁令。用意象替代：洋红航线甩向深空，代表「下一站还长」。凡多天体对比且含暖色天体，优先意象化，不画实体。
- 出图前先 cat 最近 3-4 张 prompt 的视觉层再动笔（先读再写），比写完再对照排查机位重样省事。
- 稀土（KREEP）选题还在池子：月正面风暴洋一带钾磷稀土钍富集区，接 #76「壳薄不等于岩浆就能上来」的悬念，伽马谱仪从轨道测钍分布。见 [[moon-city-data-verification]]。
- 孤字检查技巧：用单字符 Range 逐字量行。别用整段 Range 的 getBoundingClientRect——多行包围盒 top 不变，量不出断行。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue138-review.md -->


## 原始文件 11：moon-city-issue142-review.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue142-review.md`

SHA-256：`69262b6f996ebce36b6a86cab25012c7803a370d7b083d1dea7e8d11bcb4f799`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue142-review.md -->
---
name: moon-city-issue142-review
description: "#142 复盘——排期类数字三层核实、标题变更六处同步、换风格时先给动词意象"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 303210c9-848b-4b30-b557-583b2f1babca
  modified: 2026-08-26T03:43:50.078Z
---

#142《中国登月征途简述》复盘。

**Why:** 本期是任务排期类选题（嫦娥七号→八号→载人→科研站），暴露了 skill 数据核实规则没覆盖的一类数字：排期/年份/窗口不是「事实」而是「计划或推测」，这类数字初稿就该按分层核实到落笔即对，不留待外部工具纠的余地。

**How to apply:**

- 排期类数字分三层写正文：官方公告（照抄措辞）> 官方媒体转述（交叉验证）> 专家媒体推算（不落笔）。嫦娥七号官方只确认「不能在今年预定窗口实施」，2027年窗口是媒体推算，正文写「今年不发了」不写死年份；载人登月官方只确认「先期无人飞行、2030年前首登」，2028-2029彩排年份非工程办公告，写「先无人飞行验证」。
- 同节点两说并存取最新权威：科研站拓展型 2024-09 国家航天局说 2050，吴伟仁 2025-04 新华社专访改 2045，取 2045，参考文献标注最新源。
- 标题变更必须同步 6 处：HTML `<title>` + `.title`、README、review.html、prompt 标题文字 + 字数描述（「九个巨大粗字」→「八个」最容易漏）、count_chars 复核、全检+重截图。改完 grep 旧标题确认无残留（#142 改了两次：分几步→简介→简述）。
- 用户说「换个风格」时，不要给「简介/概况/简述」这类总结腔词——它们像栏目名不像是选题钩子，优先给动词/意象（#142：用户连问两轮后明确「换成简介、概况之类的」，最后落「简述」；下次报标题先想钩子再报）。

关联 [[moon-city-data-verification]]、[[moon-city-issue138-review]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue142-review.md -->


## 原始文件 12：moon-city-issue143-review.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue143-review.md`

SHA-256：`d3b916da9b1ad2b8869fa5892c87fba21f93065e3ddc94e84f20911950939dad`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue143-review.md -->
---
name: moon-city-issue143-review
description: "#143 复盘——标题宽度是旧模板遗产的坑、结论不明的选题不做、codex 协作吸收「稀疏证据」基调"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 65004048-b6ce-4282-bc59-d2fa2c4bc218
  modified: 2026-08-31T06:02:36.560Z
---

#143 复盘（2026-08-31）：

1. **标题溢出根因**：skill「≤9 字」沿自旧模板（3px 字距，9×103=927 约等于内容区 924），template-v2 改 5px 字距后 9 全角字 = 945px 必超。选题自检只数字数没算宽度，新版式下第一个 9 全角字标题就踩雷。修法见 [[moon-city-title-9char-exception]]（单卡字距 2px，skill 规则不改，check_card 已加标题宽度检查兜底）。

2. **选题过滤**：厄尔尼诺与月球关联结论有争议，用户拍板「结论不明就不说」。综合既有选题（极端天气各期）做综合卡被接受。结论存疑的选题不做，宁可综合已有内容。

3. **codex 协作**：事实核查通过（-173°C、1.4t/day 与我核实一致），不改数字；提供「极端只作稀疏证据」视角，吸收为提示词明示基调句。外部工具意见先自核再吸收，有用就改一行，不用硬凑。

**Why:** 模板升级会静默改变旧经验的有效性，宽度类约束以实测为准。
**How to apply:** 换模板或改 CSS 参数后，重验历史经验是否仍成立；选题先把结论是否站得住过一遍。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue143-review.md -->


## 原始文件 13：moon-city-issue148-review.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue148-review.md`

SHA-256：`0651d636b0a0c2b3878f9244f4ddf66b2cec2c1cf29b98f776f64a76b03ee504`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue148-review.md -->
---
name: moon-city-issue148-review
description: "#148 复盘——已确认标题不可静默替换、图暗根因是提示词堆暗字、出图终稿以 codex 收敛为准、火山逸事例先反搜"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c396bfa-069a-45bf-a3e2-4d1515f4476f
  modified: 2026-09-07T03:21:54.693Z
---

#148 复盘（2026-09-07，月面仰望地球遮日）：

1. **已确认标题不可静默替换**：原题「月食其实是日食」确认后，我因 #147 同画面撞车擅自改成「月亮不黑反红」，用户两连问「标题怎么改了」「什么时候改的，我并不知道」才暴露。判断「更贴切/撞画面」只是提出换题的触发点，不是直接改的授权点——要换先摆新题字面+理由等点头。定稿标题「月面仰望地球遮日」由用户在 codex 镜头建议下拍板，我只负责同步，不自己再改。并入 [[inflammation-title-no-unsanctioned-edit]] 同一条红线。

2. **图太暗的根因是提示词堆暗字**：第一版提亮前的提示词我堆了「暗」「黑」「死黑糊灰」「泛淡淡反光」，AI 按字面出死黑夜景；codex 图也暗，用户说「太暗，太没有艺术感」。教训：写图提示词，暗场景想要提亮，先删自己写过的暗词，改用正面鲜亮形容词（亮调波普海报、鲜亮、利落、有光感、印出来的漫画海报），「不要暗」这类否定指令不如正向词有力。

3. **图迭代交给 codex 后，AI 侧收尾是存档终版提示词**：本期镜头变革路径＝外部工具提方案（月面仰视）→用户拍板→用户让 codex 迭代收敛→终版英文 brand charter 提示词由我原样存档进 `moon-city-148-prompt.txt`（commit 31e57cf，一字未改）。别把初版中文提示词当交付物，仓库记录要同步到真正出图的终版。

4. **历史逸事当例证前先反搜挂没挂错现象**：原拟写「1883 喀拉喀托后月全食变蓝暗」，反搜证伪——月亮变蓝发生在平时非月全食，灰粒是挡红光让月亮偏暗蓝，不是让全食变蓝。弃用，改 1991 皮纳图博（气溶胶让全食更暗灰），正文写「有的全食」留余地。

5. **双对象镜头归属钉死**：全月盘染红（地球看）与地球轮廓红环（月球看）是同一大气折射的两副镜头，选题同含「月面/月盘」两个对象，正文用「地球视角/月球视角」分块，「站在月球正面」显式点名（LPI 明确月背看不到地球遮太阳），并入 [[moon-city-avoid-sweeping-ambiguity]]。

**Why:** 静默替换已确认标题与撞画面冲突是两件事——前者越权后者要提议；图像质感直接继承提示词的语气词，暗词越堆越暗。
**How to apply:** 标题改动一律先问；写图提示词先删暗字再谈提亮；出图以实际采用的终版提示词为准并同步仓库；捡逸事例证先反搜。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-issue148-review.md -->


## 原始文件 14：moon-city-new-file-creation.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-new-file-creation.md`

SHA-256：`86fc105b40c91a24c6cb1cd3ffa2b6e4d281ceb68c6f8d5e7af9ac644e3dfe33`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-new-file-creation.md -->
---
name: moon-city-new-file-creation
description: 全新HTML文件用bash heredoc创建，不用Write工具——Write要求文件已被Read过
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4650a3fa-e34b-4fb3-a393-98a51e2a34f5
---

新增文件（不在git中、未被Read过）用 `bash cat heredoc` 创建，Write 工具会报错。

```bash
cd /Users/joanna/Projects/moon-city
cat > issues/moon-city-NN.html << 'ENDOFFILE'
...完整HTML...
ENDOFFILE
```

已有文件的修改仍用 Edit 工具。

**Why:** Write 要求目标文件已被 Read（即存在于git并至少在本次会话中被读过），全新文件不满足条件。heredoc 不受此限。

**How to apply:** 写 HTML 前先判断文件是否已存在，不存在就用 bash heredoc。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-new-file-creation.md -->


## 原始文件 15：moon-city-pacing.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-pacing.md`

SHA-256：`cf85aa7810dacf0a1b4667fa0f27c8e7678c7399b301c2d2a3cff61bf58d42c6`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-pacing.md -->
---
name: moon-city-pacing
description: moon-city工作流节奏——选题是唯一确认点，问一次就行，此后全自动不问
metadata:
  node_type: memory
  type: feedback
  originSessionId: 76b43793-0b9a-4779-8ffb-5b6bd1799ea5
  modified: 2026-08-21T03:35:04.917Z
---

**Why:** 2026-08-21 用户两次点名：选题确认后「不需要让我确认那么多」「除了内容主题，减少需要我确认」「问一次就行」，edit skill 也不要逐处问。

**How to apply:**

- **选题是唯一确认点**：提 1 篇附带概念边界检查，用户点头后进入全自动，此后不再问第二次。
- **确认后一路走完**：核实数据 → 写 HTML → 去 AI 味 → 三连检查 → 截图 → 更新 README → 更新 review.html → push，中途不问「可以吗」「要确认吗」；出图提示词、截图、push 全自动不等确认。
- **异常才停**：三连不过、push 失败、信息存疑需重查，才停下问。
- **汇总**：全部完成后一次性汇报结果。
- 与 [[moon-city-prompt-composition]] 一致：出图直出不逐项等确认。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-pacing.md -->


## 原始文件 16：moon-city-prompt-composition.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-prompt-composition.md`

SHA-256：`3a9ae2aeea96e365bc2f2eed3e81a3b1ac3b26ebaf10a5ad31dd93c0c8c411a3`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-prompt-composition.md -->
---
name: moon-city-prompt-composition
description: moon-city制图提示词构图铁律——每期换视角，禁用标尺、禁用微观特写（2026-08 用户反馈）
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a1ea25b8-589a-4194-984b-68212d927053
  modified: 2026-08-21T03:24:01.183Z
---

**Why:** 2026-08-21 用户指出连续几期（#133-135）提示词全是「远景夜空 + 微观特写 + 标尺刻度 + 放大镜」，构图千篇一律，要求画面有变化。

**How to apply:**
- 出图前重读此条 + 制图宪章（[[moon-city-graphic-constitution]]）
- 视觉层禁用标尺/刻度尺、禁用微观颗粒特写、禁用放大镜
- 每期彻底换视角：大场景动势（飞跃器划过光暗）、宇宙系统图（太阳风穿地球奔月）、俯瞰、低角度、剖切大景等轮换；写完对照上一张的机位和主体逐项排查「不重样」
- 远景一层不要每次都写「钴蓝夜空从左上角斜压下来」这句
- 三层叠合结构保留，但每层的机位、尺度、空间关系必须不同
- **画面科学自检（2026-08-21 codex 二次纠出后定为己责）**：视觉描述不得把痕量/嵌入态现象画成可见实体——氦三在月壤是十亿分之几、注入颗粒表层，不能画成「越积越厚的发光覆盖层」，应写「粒子嵌入月壤颗粒表层 + 辉光沿表层逐渐增强」；凡涉及含量、形态的画面表达，先核对物理事实再落笔
- 与 [[moon-city-pacing]] 一致：提示词直出不逐项等确认
- 用户明确「这些都应该由你来规避」：构图重复与画面科学失真应在交付前自查拦截，不等 codex 指出

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-prompt-composition.md -->


## 原始文件 17：moon-city-single-episode-pool.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-single-episode-pool.md`

SHA-256：`da02f98b36a16c0c580f20fe39ff14dba574652372520a1d37678a03d5acb139`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-single-episode-pool.md -->
---
name: moon-city-single-episode-pool
description: moon-city 只做了一期的微系列候选池（2026-09-09 盘点），可续篇的接法，供后续选题用
metadata: 
  node_type: memory
  type: project
  originSessionId: 607d6197-5042-4ada-9025-d55fe3dd4da2
  modified: 2026-09-09T02:25:28.466Z
---

# moon-city 单期微系列候选池（盘点于 2026-09-09）

用户确认「一期期来」：每次只确认做一张，下面只是候选池，不要批量排期。

只做了一期（·01 无 ·02）且能续的线：

- 望地 ·01（#147 从月球看地球圆缺）→ 续：月面看地球不升不落、太阳绕着走
- 月食 ·01（#148）→ 续：日食=月影扫过地球（从月面/太空看自己的影子在地球上爬过）
- 观星 ·01（#149）→ 续：月面无大气星星不闪 / 月夜银河更亮（同域要再绕开）
- 日常 ·01（#143）→ 续：月球 29 天一个昼夜的作息
- 玻璃 ·01（#134 玻璃珠）→ 续：玻璃珠里封着太阳活动与撞月史（绕开 #53 玻璃当建材）
- 定居 ·01（#138）→ 续：安家先要的清单/基地分区
- 排期类慎做（分层核实）：征途 ·01（#142）、窗口 ·01（#140）、起飞 ·01（#141）、返航 ·01（#144）

#150「月亮还能活多久」是寿命 ·01，不续旧线。

**边界教训**：#33「月球正越跑越远」正文已含 500 亿年潮汐锁定、47 天、太阳红巨星、地月或吞没（moon-city-33.html L139）——选题撞「寿命/结局」时先查 #33，别重讲退行机制和 500 亿/47 天数字（#150 已改用「岁数看太阳 + 2026 新研究翻案」避开）。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-single-episode-pool.md -->


## 原始文件 18：moon-city-terrain-comparison.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-terrain-comparison.md`

SHA-256：`3d2af54c458f6c5add9d2c200472a0dc91ebfa91d3b63733a00aa31d7e267e6c`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-terrain-comparison.md -->
---
name: moon-city-terrain-comparison
description: 月球地形对比陷阱——单点极值高≠全幅高差大，地球陆海极限差约2万米与月球相当
metadata: 
  node_type: memory
  type: project
  originSessionId: f30789d6-afc2-4076-8ec0-4e8ed80c4102
  modified: 2026-08-10T03:33:07.786Z
---

月球与地球地形对比，先分清比的是「单点极值」还是「全幅高差」，两者结论相反。

#129 核实数据（2026-08-10，李春来 2010《中国科学》/ Smith 2010 GRL / NASA LROC / JAXA SELENE）：
- 月球最高点 约1.08万米（LOLA Selenean Summit 10786m 与嫦娥一号 10629m 同一位点，差121m在误差内），由南极艾特肯盆地撞击抛射物堆成，比珠峰高约1.9km
- 月球最低点 约-9千米（SELENE 首测安托尼亚迪坑底 -9178m，嫦娥证实）
- 月球全幅高差 约19.8km

**易错点**：直觉「月球最高点比珠峰高」易滑成「月球地形高差比地球大」——错。地球陆海极限差 = 珠峰8849m + 挑战者深渊10994m ≈ 19.8km，与月球相当。最高点单点高度月胜，全幅高差两者打平。

**How to apply:** 写「比地球XX」类表述前，先明确比较对象：单点高度 vs 全幅极差 vs 平均高度，逐项对数字。写进正文的对比必须双方数值都核过再落笔。关联 [[moon-city-data-verification]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-terrain-comparison.md -->


## 原始文件 19：moon-city-title-9char-exception.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-9char-exception.md`

SHA-256：`b7ecda71038cae0cc354bd964c9c671a2d2bd5b8cf1bd69dd6be9f42f45b33b4`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-9char-exception.md -->
---
name: moon-city-title-9char-exception
description: 9 全角字标题新版式下必溢出，用户决定按特例处理（收字距 2px），skill「≤9 字」规则不改
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 65004048-b6ce-4282-bc59-d2fa2c4bc218
  modified: 2026-08-31T04:18:42.641Z
---

新版式 template-v2 标题字距 5px，9 个全角字 = 945px，超内容区 924px，必溢出（#143 首例）。旧模板 3px 字距能放下 9 字，用户记得的「九字能放」是旧模板经验。

用户 2026-08-31 决定：skill 的「标题 ≤9 字」规则不改，9 全角字按特例处理。遇全检报标题宽度溢出时：标题 div 加内联 `style="letter-spacing: 2px"`（9×100+9×2=918px 放下）+ 一行例外注释，模板 CSS 不动，重截图后 push。

check_card.js 已加标题宽度检查兜底（超内容区报 ⚠️）。8 全角字 = 840px 正常；9 字符仅含窄字符（数字/字母，如 #70 月面体重为地球1/6）时才放得下。

**Why:** 用户认可 check_card 兜底，不把特例写进通用规则。
**How to apply:** 以后若再遇 9 全角字标题，直接走收字距特例，不问要不要改标题。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-9char-exception.md -->


## 原始文件 20：moon-city-title-digits.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-digits.md`

SHA-256：`44b6e3375433b3bf84966772c96f2f10befb23e1de31035a0f41028e29a5b939`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-digits.md -->
---
name: moon-city-title-digits
description: 标题中数字不计入中文字数限制
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 91832ac7-bbdf-4096-a115-42ba21a510c3
---

标题 ≤9 字的限制只算视觉宽度，数字（如 2030）视觉上远窄于等量汉字，不计入字数。遇到 count_chars.py 把数字拆成多字符超标时，不能闷声改标题，必须告知用户数字计数差异，由用户决定。

**Why:** 「阿忒弥斯2030返月」被 count_chars.py 报 10 字超标，私自砍掉「阿」改「忒弥斯2030返月」，破坏标准译名。用户指出数字不应按汉字算。

**How to apply:** 标题计数碰到数字时，人工判断视觉宽度，不盲从 count_chars.py 结果。超标先报用户，不改内容。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-digits.md -->


## 原始文件 21：moon-city-title-topology.md

来源：`/Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-topology.md`

SHA-256：`9f3f27940c34cf878aba4e72158b9832c657ec68e32165490a0a4e65fffed39e`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-topology.md -->
---
name: moon-city-title-topology
description: 制图若为主题的拓扑（结构示意），标题加「拓扑」二字，HTML 与提示词同步
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 654d1965-974c-4799-977d-23e3ad650c0e
  modified: 2026-08-06T02:33:14.425Z
---

当某期制图的视觉层呈现的是该主题的**拓扑**（结构关系示意/剖面图，而非场景叙事）时，标题加「拓扑」二字。HTML 标题与制图提示词标题同步改动。

**Why:** 用户要求标题与图的呈现性质匹配——拓扑图就明说拓扑，不藏着。

**How to apply:** 出图前先判断视觉层性质。若为拓扑：①制图提示词标题用完整标题（图内文字可缩小，不受 HTML 9 字/单行限制）；②HTML 模板 100px 字号一行最多容 8 字，9 字必换行且尾行孤字，故 HTML 标题用 8 字内紧凑版（仍带「拓扑」），改后重跑三连检查；③README 选题行同步。实例：#127 制图标题「月坑亮纹中央峰拓扑」9 字全名，HTML 标题「月坑亮纹与峰拓扑」8 字。关联 [[moon-city-graphic-constitution]]。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna/memory/moon-city-title-topology.md -->


## 原始文件 22：moon-city-viewer-todo.md

来源：`/Users/joanna/.claude/projects/-Users-joanna-codex-era/memory/moon-city-viewer-todo.md`

SHA-256：`34f43039192f7d25fc1627ae93a4e7858667016ebcc02690ea3d373ff4201c8e`

<!-- BEGIN SOURCE /Users/joanna/.claude/projects/-Users-joanna-codex-era/memory/moon-city-viewer-todo.md -->
---
name: moon-city-viewer-todo
description: moon-city review.html 全屏查看器待办，提示词已写好未执行
metadata: 
  node_type: memory
  type: project
  originSessionId: 3e6878a1-404c-4787-9970-c3dba154f11c
  modified: 2026-08-25T03:49:58.079Z
---

用户要为 moon-city 项目（张走走想在月球盖座城）的 review.html 加全屏复习查看器，效果参照 inflammation 的 iframe 版。提示词已写好交用户，执行方待定（用户自跑或我跑）。

**Why:** moon-city 与 inflammation 结构不同，提示词已预埋适配点：卡片 HTML 1080×1350px（3:4，非 inflammation 的 1438/1548 高）；索引卡只有 .num + .title 无 hook 字段；配色深蓝黑 #0B121C 配黄/粉/青波普撞色；add_review.py 维护点（grid 顶部插卡按期号重排、count、:root 的 --c6 后、footer 前）；1-69 期旧卡与 template-v2 高度可能不统一，每张卡切换时重测高度。

**How to apply:** 用户说做时按那段提示词执行。iframe 高度用 [[iframe-height-measurement]] 的 offsetHeight 法。改完 git push 等 GitHub Pages 部署后打开页面给用户看。

<!-- END SOURCE /Users/joanna/.claude/projects/-Users-joanna-codex-era/memory/moon-city-viewer-todo.md -->


## 原始文件 23：SKILL.md

来源：`/Users/joanna/.claude/skills/moon-city-lite/SKILL.md`

SHA-256：`2c3fe749f3bdecc7108a5d62b51315ad42924f9dc21cc208c1855789c1dba068`

<!-- BEGIN SOURCE /Users/joanna/.claude/skills/moon-city-lite/SKILL.md -->
---
name: moon-city-lite
description: 月球科普系列「张走走想在月球盖座城」波普小卡片版——每期两个知识点+一条粉框趣闻
---

项目路径：`/Users/joanna/Projects/moon-city`
模板：`template-v2.html`
**所有命令必须 `cd` 到项目目录执行**。

## 结构（8 板块）

```
渐变顶条（四段撞色：黄/粉/青/黄）
品牌条（黄底黑字+白框+粉投影）
系列标签（青，纯文字无 emoji，如「引力 · 01」）
标题（黄 100px+双层粉阴影）
━━━ block ×2（青 ■ 小标题 + 左青竖线正文，恰好三行）
━━━ tidbit（5px 粉框+深青底，无标签，恰好两行）
━━━ 参考文献（24px 灰，居中，≥2 条，≤3 条）
━━━ 免责声明（24px 青，居中）
```

## CSS 基准（不可动）

| 参数 | 值 |
|------|-----|
| 画布 | 1080×1350，overflow hidden |
| body | padding 48px 78px 80px, flex column space-between |
| 标题 | 100px #FFE53B，letter-spacing 5px，双粉 shadow |
| 小标题 | 34px #00E5FF，前青色方块 10px |
| 正文 | 32px #FFFFFF，line-height 1.68，左青竖线 3px + 22px padding |
| 粉框 | 5px #FF5E8A，底色 #102530，box-shadow 6px 6px 0 |
| 加粗 | #FFE53B，font-weight 800 |
| ref | 24px #8899AA，居中 |
| disclaimer | 24px #00E5FF，居中 |

## 配色

| 色值 | 用途 |
|------|------|
| `#0B121C` | 底色 |
| `#FFE53B` | 标题、加粗、品牌底 |
| `#FF5E8A` | 粉框、标题阴影 |
| `#00E5FF` | 系列标签、小标题、方块、竖线、免责 |
| `#FFFFFF` | 正文 |
| `#8899AA` | 参考文献 |
| `#102530` | 粉框底色 |

## 字数

| 模块 | 字数 | 行数 |
|------|------|------|
| 标题 | ≤9 字（数字按视觉宽度），含「月」 | — |
| block ×2 | 各 65–86 字（**初稿靶位 78-84**。86 字以上大概率 4 行；视觉宽字符多时阈值低到 84 也翻，稳 3 行的安全上限约 77 字） | 恰好 3 行 |
| tidbit | 45–53 字（**初稿靶位 48-52**。54 字以上大概率 3 行） | 恰好 2 行 |
| **正文总计** | **~180–220** | — |

> 阈值是实测均值，不绝对——渲染行数为准。视觉宽字符（「颗粒」「辐射」「热量」等）挤占行宽，同一字数下比窄字符更早换行。

## 系列规划

六大步规划，实际按兴趣自由选题，规划作参考（每天一篇）：

| 步 | 系列 | 篇数 |
|----|------|------|
| ① 认识脚下 | 引力 4 / 地质 4 / 温差 2 | 10 |
| ② 到达月面 | 着陆 4 / 轨道 4 | 8 |
| ③ 对抗环境 | 月尘 4 / 辐射 4 / 真空 2 | 10 |
| ④ 获取资源 | 水 4 / 氧气 4 / 能源 4 | 12 |
| ⑤ 动手建造 | 建材 4 / 施工 4 / 选址 4 | 12 |
| ⑥ 住下来过 | 生活系列 | 待定 |

## 工作流

1. **选题**：提 1 篇，附带与已有选题的概念边界检查。**仅此步需用户确认**
2. 选题确认后全自动：核实数据 → cp 模板写 HTML → 初稿自查 → 去 AI 味 → 全检（check_card.js）→ 截图（screenshot.js）→ 更新 README → 更新 review.html → 出图提示词 → push。**除选题主题外不再打断求确认**——标题、正文、出图提示词、截图、push 一路走完，不问「可以吗」「要确认吗」，只有异常（全检不过、push 失败、信息存疑需重查）才停下问
3. 每天一篇，选题确认后自动走完

## 更新 review.html（分类索引）

每做完一期、三连通过后，自动把新一期加进 `review.html` 分类索引再一起 push，不等用户确认。

> review.html 带全屏复习查看器，三块代码固定在 add_review.py 不碰的区域：CSS 在 `</style>` 前、弹层 HTML 在 `.wrap` 关闭后、JS 在 `</body>` 前。加卡脚本只动章节/图例/总数，**别把查看器代码挪进这些区域**。改动查看器后跑 `node smoke_viewer.js` 验证（需同源 http 服务，见脚本头注释）。

```bash
cd /Users/joanna/Projects/moon-city
python3 add_review.py <期号> <标题> <step1-6>
# 例：python3 add_review.py 134 月面样本怎么收 step1
```

**步骤：**
1. 判断新一期归入哪个「建造六步」章节（① 认识脚下 / ② 到达月面 / ③ 对抗环境 / ④ 获取资源 / ⑤ 动手建造 / ⑥ 住下来过），按内容主题归，不硬塞
2. 跑上面的命令。脚本自动完成：插到该章节顶部、章节内从新到旧重排、更新该章节期数、更新总期数
3. **必要时候开新章节**：内容不属于任何六步时，开第七章（罕见）：
   ```bash
   python3 add_review.py <期号> <标题> new --new-name "⑦ 新篇章名" --new-color "#HEX"
   ```
   脚本会自动加图例入口、:root 颜色变量和新章节块
4. 标题含特殊符号（引号等）时注意 shell 转义；期号、标题必须与 `issues/moon-city-NN.html` 一致
5. 重复期号脚本自动跳过（幂等），可放心重跑

## Git Push

```bash
cd /Users/joanna/Projects/moon-city && git add -A && git commit -m "moon-city #N：标题" && git push
```

push 一次不通则告知用户「commit 已存本地，网络恢复后手动 push」，不反复重试。

项目已配置 GitHub Pages，push 后自动部署到 https://joanna2joanna.github.io/moon-city/ 。

---

## 自检点

### 选题自检（提出选题前）

- □ 本次选题（1 篇），不重复 README 已有选题？
- □ 各篇概念彼此独立，无大篇幅重叠？
- □ 标题逐字核对：≤9 字（视觉宽度）且含「月」？——**提出选题时就数好，别写完 HTML 才被 count 脚本抓缺月**（#136：嫦娥七号启程验冰缺月，改奔月验冰）

### 成稿自检（写 HTML 后、三连前）

- □ 去 AI 味六项手动过完？
- □ jiadakong 扫过，无假大空命中？（装生动/装深沉/装简洁，命中即改）
- □ 改字眼没引入红线词？（「要命」「死」等直白情绪字眼，见下方语气与措辞）
- □ 无句首标点、句尾左括号？
- □ 无孤字行？
- □ 各模块行数初判在范围内？（block 3 / tidbit 2）

### 交付自检（三连通过后、截图后）

- □ 全检通过（行数 3/3/2、字数达标、scrollHeight ≤ 1350、无孤字、无括号问题）？
- □ README 已更新？
- □ PNG 已生成？
- □ review.html 已更新（add_review.py 跑过，章节判断正确）？
- □ 出图提示词已写（moon-city-NN-prompt.txt）并随本期提交？

## 红线

- 画布 1080×1350px，overflow: hidden，scrollHeight > 1350 必须删内容（优先缩边距行高，仍不够再裁文字）
- 标题 ≤9 字（数字按视觉宽度算），含「月」，口语化优先
- 正文第三人称客观科普，不出现「我」「我们」
- 无句首标点、句尾左括号、孤字行
- 同一事物表述全文统一，不混用近义词
- 参考文献真实可查，≥2 条且 ≤3 条
- CSS 不动（以模板 `template-v2.html` 为准）
- 免责声明独立 `<div class="disclaimer">`，ref 之后、`</body>` 之前，不可塞进 ref 末尾
- 零 emoji（全卡包括系列标签均不含 emoji）
- 旧 `moon-city` skill 不动

## 语气与措辞

- 不用「咋」——用「怎」或「怎么」
- 不用「那」做笃定指代——「那分钟」「那个字」「那份」透着「你懂的」的笃定感，删掉或换成具体名词；小标题的「XX那份」尤其禁（#137 用户点名：地球那份→地球氦三在深层）
- 不用直白情绪字眼（如「死」→ 用「终结」「结束」等中性表达）
- 不用「么」替代「怎么」
- 句式不加「的」可省略时不加，撑不满行时可适当用助词拉长
- 避免「怎么」「什么」类疑问词

## 数据核实

月球科学仍在快速推进，很多"常识"是过时结论或单一研究的一家之言。
生成前必须过以下关卡，不能盲信搜索结果，更不能盲信模型记忆。

### 核实流程（不可跳过）

0. **数字溯源**：每个写进正文的数字，必须找到原始出处——不是综述引用的二手数据，是原始论文或机构报告。搜索摘要里出现的数字不等于可信。

1. **正面搜**：每个关键数字和因果陈述至少搜两个独立信源。
   信源优先级：NASA NSSDC / 同行评审期刊 / 机构白皮书 > 知名科普媒体 > 维基百科。
   不取自媒体、微信公众号、知乎、小红书。

2. **反面问（硬门槛，跳过则整批重做）**：正面搜完必须反向搜索——
   "XX 有争议吗""XX 被推翻了吗""XX 的例外情况"。
   如果反面搜索结果指向不同结论，必须在正文中体现不确定性。
   此步不可跳。未执行反向搜索的稿件视为未核实。

3. **交叉验证**：同一事实至少两个独立信源的数字一致才可落笔。
   不一致时列出双方来源和年份，选最新或共识度最高的，参考文献如实标注。

4. **官方溯源**：引用 NASA、ESA、CNSA 等机构数据时，找到原始发布页而非二手转载。
   论文引用必须可查 DOI，不引用预印本或非同行评审来源。

5. **术语自检**：写完逐词过——每个专业术语自己能否用一句话解释清楚？
   解释不清的术语不写。不为了看起来专业而生造或堆砌术语缩写。

6. **删减红线**：去 AI 味、缩字数时，删的是修辞和冗余句式，不是事实和数据。
   数字、因果逻辑、限定词（约/大约/目前认为/多数/通常）不可删。删完必须回读确认事实完整。
   **绝对化表述是最大陷阱**——「至今做不出来」→「多数模拟土缺这层」；「完全不」→「基本不」。
   **删减不伤可读性**：「运力贵铜过重」「Kapton做绝缘」这类电报体比 AI 腔更难读，宁多两字不砍成断句。

7. **争议标注**：有活跃学术争议的结论，正文加限定词，不在科普里当定论写。

8. **没有来源的数字不落笔**

9. **外部建议需自核**：codex 或其他外部工具指出的问题，必须独立再核实后改正，不可盲信。外部工具和搜索结果一样，是线索不是结论。

10. **排期类数字分层（任务年份/发射窗口/节点）**：这类数字不是「事实」而是「计划或推测」，必须分三层，只有第一层能写进正文：
    - **官方公告**（载人航天工程办公室、国家航天局）：可写，且照官方措辞抄（官方只写「不满足条件」「先期无人飞行」就只写这句）
    - **官方媒体/发布会转述**（新华社、解放军报、神舟发布会转述）：可作参考，但需与第一层交叉验证，官方没确认的具体年份不落笔
    - **专家/媒体推算**（分析文、行业推测）：作背景，不写进正文
    例（#142）：嫦娥七号官方只确认「不能在今年预定窗口实施」，2027 年 2-3 月 / 8 月都是媒体推算，正文写「今年不发了」不写死年份；载人登月官方只确认「先期无人飞行、2030 年前首登」，2028-2029 具体彩排年份有解放军报口径但非工程办公告，正文写「先无人飞行验证」。
    **同一节点两说并存时取最新权威口径**：科研站拓展型 2024-09 国家航天局说 2050，吴伟仁 2025-04 新华社专访改 2045，取 2045，参考文献标注最新源（#142）。

### 核实时效

每次核实完成后，在 HTML 注释中标注核实日期和信源访问 URL：

```html
<!-- 数据核实于 2026-07-10，信源：NASA NSSDC / Williams 2024 -->
```

同一批数据超过一天（24h）未使用，再次落笔前必须重新搜索确认。
时效性强的选题（正在进行的任务、最新发现、政策变动）必须当天重新核实。

### 典型陷阱（警惕）

- 搜索结果第一条可能是过时的 NASA 新闻稿，翻到第二页
- 中文科普号常把"假说"写成"定论"，查到原始论文才算数
- LLM 倾向于给确定答案，即使数据本身不确定——反向问才能逼出边界
- 数字互相印证不等于正确——可能是同一错误源头被反复引用
- 综述论文引用的数字是二手数据，追到原始论文才算核实
- 搜索摘要里出现的数字不等于是那篇论文的结论——打开正文看具体怎么说的
- 去 AI 味删字时容易顺手删掉限定词（"约""大约""目前认为""多数""通常"），补回来
- 措辞从"有条件的结论"滑成"绝对陈述"是最隐蔽的事故——删字后必须逐句比对原意
- 量词归属不能越过研究对象——研究只证明「一部分」的结论，别写成「全部/大多」（#135 codex 指出「氦三封在玻璃里」会读成全部）
- 温度要带温标——「上千度」这类没有参照的写法，换成「七八百度」等有依据的值
- 术语不要凭空造——如果中文没有通用译名，保留英文原文，不要硬翻
- codex 等外部工具的审查意见是线索不是结论，采纳前必须独立核实
- 时效性新闻（发射、任务进行中）不用未官方确认的推断日期/窗口——官方只写「近日择机发射」就照抄官方措辞，SpaceNews 等推算的窗口期可作背景不写进正文（#136：窗口约 8-24 未获官方确认，正文只写「近日择机发射」）

## 去 AI 味

**≤4 篇：手动，>4 篇：走 shuorenhua 扫。** 手动更快且不引入红线词。

写 HTML 后、三连前执行。

### 手动去味（≤4 篇，改字眼不改事实）

**1. 二元对比** — 「不是……而是……」「不是……是……」删前半句，直接说后半。

**2. 概括腔** — 「堪称」「可谓」「硬通货」「刚需」「奢侈品」换具体说法，不替读者下结论。

**3. 金句收尾** — 末尾不拔高。平实收束，不喊口号。

**4. 破折号** — 全文 ≤1 个。多出来的换逗号或分号。

**5. 句长打散** — 连续三句差不多长，打散一句。读出声判断最准。

**6. 查红线词** — 「要命」「死」→ 中性表达（「终结」「结束」）。

### 自动去味（>4 篇）

提取正文纯文本 → shuorenhua（scene: public-writing, level: standard, scope: structural）→ 回写 HTML。回写后逐条过以上六项。

## 孤字行检查

渲染后逐段检查：每个 block 和 tidbit 的最后一行不得只有 1 个字符（中文字、标点或数字）。若出现孤字行，调整前文措辞使最后一行至少 3–4 字，或把孤字挤入上一行。

用命令速查里的 check_card.js 一次跑出，同时覆盖行首禁右括号、行末禁左括号。

## 高度收紧策略（当 scrollHeight 超标时，按优先级依次应用）

1. 缩 block margin（flex space-between 下用 gap 替代）
2. 缩行高：`.block .text { line-height: 1.58; }`（原 1.68）
3. 缩内边距：`.tidbit { padding: 24px 44px; }`（原 32px）
4. 缩底部 padding（原 80px）
5. 仍不够再裁文字

## 命令速查

> 每期必跑的检查只有一个：全检（check_card.js 一跑出全部）。count_chars_v2.py 仅全检不过时定位用。

```bash
cd /Users/joanna/Projects/moon-city

# 全检（一跑出：每段行数+字数、scrollHeight、孤字、行首右括号、行末左括号）
NODE_PATH=/Users/joanna/.workbuddy/binaries/node/workspace/node_modules node check_card.js NN

# 截图（screenshot.js 已内置去导航符号）
NODE_PATH=/Users/joanna/.workbuddy/binaries/node/workspace/node_modules node screenshot.js issues/moon-city-NN.html issues/moon-city-NN.png

# 超标调试：打印每个元素的 bottom 坐标
NODE_PATH=/Users/joanna/.workbuddy/binaries/node/workspace/node_modules \
  node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.setViewportSize({width:1080,height:1350});await p.goto('file://'+process.cwd()+'/issues/moon-city-NN.html');const sh=await p.evaluate(()=>document.body.scrollHeight);const positions=await p.evaluate(()=>{return Array.from(document.body.querySelectorAll('body > *')).map(e=>({cls:e.className,bottom:e.getBoundingClientRect().bottom}));});console.log('scrollHeight:',sh);console.log(JSON.stringify(positions,null,2));await b.close();})();"

# 定位用：全检不过时单独查字数/标题含月
python3 count_chars_v2.py issues/moon-city-NN.html
```

## 文件创建

**新一期 HTML 用 `cp template-v2.html` 复制骨架，再 Read 一次后 Edit 只改内容区**——CSS 整段不动，不再手写。`cp` 生成的新文件在 git 里不存在，Edit 前必须先 Read。

```bash
cd /Users/joanna/Projects/moon-city
cp template-v2.html issues/moon-city-NN.html
# 然后 Read 该文件，用 Edit 替换：<title>、.series、.title、两个 .head、两个 .text、.tidbit .txt、.ref、数据核实注释
```

写 prompt 文件仍用 heredoc（无模板可复制），先 `cd` 再写。已有文件的修改仍用 Edit 工具。

## 标题变更同步清单

标题确认后仍可能改字（#142：分几步→简介→简述，改两次）。**每次改标题必须同步 6 处 + 重跑检查**，漏一处成图就不同步：

1. HTML `<title>` 和 `.title`（同一文件两处）
2. README 选题表对应行
3. review.html 对应卡片标题（若已 add_review）
4. prompt 文件标题文字 + **字数描述**（「九个巨大粗字」→「八个」，标题字数变了必须改，最容易漏）
5. count_chars_v2 复核标题字数/含月
6. check_card.js 全检 + screenshot.js 重截图

改完 `grep -n 旧标题` 确认全文无残留，再 commit+push。

## 制图提示词

每期 HTML 完成、全检通过后自动出提示词（标准工作流一步），不等用户开口。

**输出前第一步：重读制图宪章。** 打开 memory `moon-city-graphic-constitution` 刷新波普美漫质感、三色域分配、七模块模板。以下为补充规范，与宪章冲突时以宪章为准。

提示词写完直接保存在聊天里逐张列出（用户可复制），同时用 heredoc 保存到对应 `moon-city-NN-prompt.txt` 文件，最后 add+commit+push。

**保存前先 `cd` 到项目目录**——heredoc 写文件不报错，cd 没到位会写进其他目录（常见 `~/issues/`），要到 push 才暴露（#135 第三次复发）。保存后 `ls -la` 或 `git status` 确认落点，再提交。

### 画面感铁律

提示词是写给 AI 生图工具的——描述的是**画面长什么样**，不是代码怎么排。禁止出现：
- CSS 参数：px、色号（#FFE53B）、letter-spacing、padding、flex
- HTML 结构词：block、tidbit、div、class
- 排版术语：三行矩形、左竖线缩进、行距

改**用自然语言描述视觉效果**：「七个巨大粗黄字」「一道青色细线沿左边缘」「字距偏松」「粉红色粗边框」「右下角影子偏出去」。

### 全系列统一版式

所有提示词必须版式一致。固定区域如下，仅视觉层每张不同：

| 区域 | 位置 | 内容 | 说法 |
|------|------|------|------|
| 画幅声明 | 每张开头第一句 | 画幅 1080×1350，竖版 4:5。画面铺满，不额外加框或分割线 | 每张重复 |
| 顶部撞色细线 | 画面最上缘 | 黄、粉、青、黄四截等分极细色带，横跨全宽 | 每张重复 |
| 品牌签 | 撞色线下居中 | 黄底黑字小横条「张走走想在月球盖座城」，字克制极小，外勾白细线框，右下微微粉影 | 每张重复 |
| 系列标签 | 品牌签下居中 | 青色小字「系列 · 编号」 | 每张替换 |
| 标题 | 系列标签下居中 | 七个巨大粗字，工业黄，黑色粗描边，字距偏松，右下叠双层亮洋红投影（一层实一层虚）。全画面最抢眼 | 每张替换标题文字 |
| **视觉层** | 标题下，画面核心区 | **三层叠合——每张不同，是唯一差异化区域** | 每张创新 |
| 工程概览 | 左下板块 | 左栏文字，≤150 字 | 每张替换 |
| 数据来源 | 右下板块 | 右栏文字，2-4 条真实文献，带「参考文献：」标签 | 每张替换 |
| 免责声明 | 底部居中 | 青色微小字「*本文为公开信息整理笔记，非严肃学术科普。*」 | 每张重复 |
| 色彩分配 | 末尾 | 钴蓝/工业黄/亮洋红三色域 + 粗黑描边 + 波普粗网点 + 禁暖色 | 每张替换 |

### 出图自检（发完前逐张过）

- □ 每张开头写了「画幅 1080×1350，竖版 4:5」？
- □ 画面铺满、不加外框分割线这句写了？
- □ 品牌签、标题区、底部双栏、免责声明位置各张一致？
- □ 视觉层是否仅此张独有、不跟其他张雷同？
- □ 构图视角与上一张不同（机位、主体、尺度逐项比对，自查拦截，不等外部工具指出）？
- □ 无标尺/刻度尺、无微观颗粒特写、无放大镜？（#133-135 连续三张同视角，用户点名）
- □ 远景层没写固定句式「钴蓝夜空从左上角斜压下来」？
- □ 画面科学：痕量/嵌入态现象没画成可见实体层？（氦三在月壤是十亿分之几、注入颗粒表层，不能画「越积越厚的发光覆盖层」）
- □ 无 px、色号、CSS 术语？
- □ 无「品牌胶囊」四字？
- □ 免责声明写了完整原文？
- □ 参考文献带了「参考文献：」标签？
- □ 色彩分配写了三色域 + 网点 + 禁暖色？
- □ 全卡零 emoji？

### 术语禁语

- 「品牌胶囊」→「黄底黑字横条「张走走想在月球盖座城」」
- 色号、px、letter-spacing 等一切 CSS 参数
- block / tidbit / div / padding / flex 等一切 HTML 结构词

## 经验教训

### 字数与行数
- count_chars_v2.py 把数字拆成单字符，标题 ≤9 字**以视觉宽度为准**
- block 初稿靶位 78-84 字，86 字以上大概率 4 行（视觉宽字符多时阈值更低）
- tidbit 初稿靶位 48-52 字，54 字以上大概率 3 行
- **count_chars 通过不代表行数对**，行数以全检（check_card.js）渲染为准
- block 4 行时优先删视觉宽字符（「颗粒」「效率」「结构」），删一字比加半句更有效
- 视觉宽字符多的 block（含「氦三」「十亿分之几」等）84 字就翻 4 行，压到 ~77 才稳（#135 实测）
- tidbit 3 行时优先删修饰语和重复主语，保持主干
- 去 AI 味会缩 2-5 字，Block2 最易掉出下限，写完自查
- 字数在阈值内仍可能因视觉宽字符超标，tidbit 51 字翻 3 行不罕见

### 内容质量
- 标题数字后必须带单位（「差三百」→「差三百度」）
- 两篇 block 概念必须独立，不能同概念换壳
- 标题避免误导（如「引力坑坑洼洼」——引力场不均匀 ≠ 引力砸坑）
- 量词归属：只证明「一部分」的结论不写成「全部/大多」；温度带温标（#135 codex 教训）
- 去 AI 味时警惕引入红线词（「死」「要命」）
- 删减不伤可读性，宁多两字不砍成电报体
- 缩字时最容易删掉限定词把有条件结论变成绝对陈述——回读必须逐句比对原意
- 综述引用的数据和具体数字必须追到原始论文，二手引用不算核实
- 标题含「月」在提出选题时就核对，别写完 HTML 才被抓（#136 教训）
- 小标题不用「那份」「那点」模糊指代，换成具体名词（#137 用户点名禁「那」）
- 标题避免「简介/概况/简述」这类总结腔词——它们像栏目名不像是选题钩子，用户点名要换风格时优先给有画面感的动词/意象（#142：用户把「分几步」连问两轮换成「简述」，实则想要更利落的表达；先想好钩子再报标题）
- 任务排期类选题（嫦娥七号/八号、载人登月、科研站节点）先把「官方公告 / 官方媒体转述 / 媒体推算」三层分清楚再落笔，排期数字是计划不是事实（#142：codex 纠出三处，独立核实后两处采纳一处按最新权威取 2045）

### 制图
- 出图前先读 memory `moon-city-graphic-constitution`，不凭记忆写
- 提示词是画面描述不是 HTML 描述——禁用 px/色号/block/tidbit/padding/flex
- 用自然语言：「七个巨大粗黄字」「粗黑描边」「右下粉影偏出去」
- 禁用「品牌胶囊」→「黄底黑字横条「张走走想在月球盖座城」」
- 免责声明完整原文：「*本文为公开信息整理笔记，非严肃学术科普。*」
- 参考文献必带「参考文献：」标签
- 工程概览中图层标注留在视觉层内，独立文字才独立成段
- 底部双栏固定左右并排，不随视觉层移动
- 标题固定居中偏上，不左飘右移
- 视觉层每层至少 2-3 句具体描述（形状、颜色、质感、空间关系）
- 写完用 heredoc 保存到 `moon-city-NN-prompt.txt`，随本期一起 commit+push（保存前 cd 或先 pwd，写完确认落点，见上「保存前先 cd」）
- 每期换构图视角：大场景动势（飞跃器划过光暗）/宇宙系统图（太阳风穿地球奔月）/俯瞰/低角度/剖切大景轮换；写完对照上一张的机位和主体逐项排查「不重样」（#133-135 全是远景夜空+微观特写+标尺，用户点名）
- 禁标尺/刻度尺、禁微观颗粒特写、禁放大镜
- 远景一层不写固定句式「钴蓝夜空从左上角斜压下来」，每期换说法
- 画面科学自检：痕量/嵌入态现象不画成可见实体层——氦三在月壤十亿分之几、注入颗粒表层，画「粒子嵌入月壤颗粒表层+辉光沿表层逐渐增强」，不画「越积越厚的发光覆盖层」（#137 codex 二次纠出后定为己责，不依赖外部工具）

### 工程
- 截图命令已内置 `remove nav-fixed`，不用额外处理
- push 不通一次即停，告知用户「commit 已存本地」，不重试
- 所有命令必须 `cd /Users/joanna/Projects/moon-city` 再执行，不依赖上一次调用的目录
- 写 HTML 用 cp 模板、写 prompt 用 heredoc，都要先 cd 到项目目录；写文件不报错、写错位置（常见 `~/issues/`）到 push 才暴露（#135 第三次复发）

<!-- END SOURCE /Users/joanna/.claude/skills/moon-city-lite/SKILL.md -->
