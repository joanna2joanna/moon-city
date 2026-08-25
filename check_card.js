#!/usr/bin/env node
// moon-city 全检：一次启动浏览器，输出每段行数+字数、scrollHeight、孤字、行首右括号、行末左括号、末行文本。
// 用法: node check_card.js <期号>   （需带 NODE_PATH 前缀，见 SKILL.md 命令速查）
const { chromium } = require('playwright');

(async () => {
  const nn = process.argv[2];
  if (!nn) { console.error('用法: node check_card.js <期号>'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.setViewportSize({ width: 1080, height: 1350 });
  await p.goto('file://' + process.cwd() + '/issues/moon-city-' + nn + '.html');
  const out = await p.evaluate(() => {
    const rows = { blocks: [], orphans: [], badStarts: [], badEnds: [] };
    const els = document.body.querySelectorAll('.block .text, .tidbit .txt');
    els.forEach((el, i) => {
      const node = el.firstChild;
      const text = node.textContent;
      const lineRects = {};
      for (let k = 0; k < text.length; k++) {
        const r = document.createRange();
        r.setStart(node, k); r.setEnd(node, k + 1);
        const top = Math.round(r.getBoundingClientRect().top);
        if (!lineRects[top]) lineRects[top] = '';
        lineRects[top] += text[k];
      }
      const lines = Object.values(lineRects);
      const h = el.getBoundingClientRect().height;
      const lh = parseFloat(getComputedStyle(el).lineHeight);
      rows.blocks.push({
        el: i,
        type: el.closest('.block') ? 'block' : 'tidbit',
        renderLines: Math.round(h / lh),
        chars: text.length,
        lastRow: lines[lines.length - 1]
      });
      if ([...lines[lines.length - 1]].length <= 1) rows.orphans.push({ el: i, lastRow: lines[lines.length - 1] });
      lines.forEach((ln, ri) => {
        if (/[」）』】]/.test(ln[0])) rows.badStarts.push({ el: i, row: ri, char: ln[0] });
        if (/[「（『【]/.test(ln[ln.length - 1])) rows.badEnds.push({ el: i, row: ri, char: ln[ln.length - 1] });
      });
    });
    return { blocks: rows.blocks, orphans: rows.orphans, badStarts: rows.badStarts, badEnds: rows.badEnds, sh: document.body.scrollHeight };
  });
  console.log('每段(渲染行/字数/末行):');
  out.blocks.forEach(x => console.log(`  ${x.type}#${x.el}: ${x.renderLines}行 / ${x.chars}字 / 末行「${x.lastRow}」`));
  console.log('scrollHeight:', out.sh, out.sh > 1350 ? '⚠️ 超标' : '✅');
  console.log('孤字:', out.orphans.length ? JSON.stringify(out.orphans) : '无');
  console.log('行首右括号:', out.badStarts.length ? JSON.stringify(out.badStarts) : '无');
  console.log('行末左括号:', out.badEnds.length ? JSON.stringify(out.badEnds) : '无');
  await b.close();
  process.exit(0);
})();
