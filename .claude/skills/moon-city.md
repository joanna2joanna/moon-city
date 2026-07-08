---
name: moon-city
description: 月球科普系列「张走走想在月球盖座城」——微信贴图号，1080×1350px
---

## 工作流

1. 讨论确定主题（不重复 README 已有选题）
2. **在 Python 计数脚本内逐模块写文字，每个模块字数通过才往下写。** 不要先写完全文再回头计数——轮次太多。
3. 全部模块通过后，用脚本批量替换模板 → 生成 HTML，CSS 不动
4. 截图 + 检查 scrollHeight ≤ 1350
5. 更新 README 选题表
6. 确认完成后：`cd /Users/joanna/Projects/moon-city && git add -A && git commit -m "moon-city #N-M" && git push`（Pages 自动部署到 https://joanna2joanna.github.io/moon-city/ ）

## 红线

- 高度 1350px，overflow: hidden，scrollHeight > 1350 必须删内容
- 标题 ≤9 字，带「月球」前缀，口语化优先（如「打哪来」「慢一秒」），避免「怎么」「什么」
- 正文第三人称客观科普，不出现「我」「我们」
- 无句首标点、句尾左括号、孤字行
- 参考文献真实，≤3 条
- CSS 不修改

## 结构

3 个 block + 1 个 highlight + 1 个 insight + 参考文献

| 模块 | 安全范围 | 行数 |
|------|---------|------|
| Block Text（每个） | 100–150 字 | 3–4 行 |
| Highlight（金句框） | 30–35 字 | 1 行 |
| Insight Text（总结） | 65–70 字 | ≤2 行 |

总正文 460–510 字（基准 480 字左右）。

## 生成脚本

模板: `issues/moon-city-15.html` → `issues/moon-city-NN.html`
截图: `NODE_PATH=/Users/joanna/.workbuddy/binaries/node/workspace/node_modules node screenshot.js issues/moon-city-NN.html issues/moon-city-NN.png`
