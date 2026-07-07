# 张走走想在月球盖座城

微信贴图号科普系列。每期一个月球建城相关概念，1080×1350px 固定画布。

## 关键参数

- 画布：1080×1350px，overflow: hidden
- 配色（不修改）：深空蓝底 `#162440`／金 `#E8C565`／星光银蓝 `#8CB8D8`
- 字号（不修改）：标题 80px / 段落标题 28px / 正文 25px / 参考文献 20px

## 内容规则

- 标题 ≤9 字，带「月球」前缀，口语化优先（如「打哪来」「慢一秒」），避免「怎么」「什么」
- 3 个 block + 1 个 highlight + 1 个 insight + 参考文献
- 总正文 460–510 字（基准 480 字左右），各模块字数见 skill
- 无句首标点、句尾左括号、孤字行
- 不修改 CSS

## 文件

```
issues/
├── moon-city-01~08.html/.png   旧格式（Pillow）
├── moon-city-09~31.html/.png   新格式（HTML + Playwright）
screenshot.js                    截图脚本
```

详细工作流见 skill `moon-city`。
