# 张走走想在月球盖座城

微信贴图号科普系列「张走走想在月球盖座城」——波普撞色小卡片。每期一个月球工程概念，1080×1350px。

## 关键参数

- 画布：1080×1350px，overflow: hidden
- 模板：`template-v2.html`，CSS 不动
- 配色：深蓝黑底 `#0B121C`／黄 `#FFE53B`／粉 `#FF5E8A`／青 `#00E5FF`／白 `#FFFFFF`／灰 `#8899AA`

## 内容结构（8 板块）

```
顶部四段撞色条（黄/粉/青/黄）
品牌条（黄底黑字+白框+粉投影）
系列标签（青，纯文字无 emoji）
标题（黄 100px 粗字+双层粉阴影，≤9 字，含「月」）
━━━ block ×2（青方块+青小标题+左青竖线白字正文，恰好三行，各 65–85 字）
━━━ tidbit（粉框深青底卡片，无标签，恰好两行，45–50 字）
━━━ 参考文献（24px 灰，居中，≥2 条 ≤3 条，真实可查）
━━━ 免责声明（24px 青，居中，独立一行）
```

## 文件

```
issues/
├── moon-city-01~08.html/.png   旧格式（Pillow）
├── moon-city-09~69.html/.png   新格式（HTML + Playwright，第一版模板）
├── moon-city-70~.html/.png     新版式（template-v2，波普撞色）
template-v2.html                当前模板
count_chars_v2.py               字数检查脚本
```

## 工作流

见 skill `moon-city-lite`。选题 → 核实 → HTML → 去 AI 味 → 计数 → 截图 → 高度检查 → README → push。

## 制图

制图提示词规范见 skill `moon-city-lite` 和 memory `moon-city-graphic-constitution`。
波普美漫质感，三色域（钴蓝/工业黄/亮洋红），粗黑描边 + 波普网点，七模块模板。
