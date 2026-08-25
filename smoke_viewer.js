#!/usr/bin/env node
// review.html 全屏复习查看器冒烟测试（需同源 http 服务，file:// 挡 iframe contentDocument）
// 用法: node smoke_viewer.js [url]   默认 http://127.0.0.1:8123/review.html
// 启动服务: cd /Users/joanna/Projects/moon-city && python3 -m http.server 8123
const { chromium } = require('playwright');

(async () => {
  const URL = process.argv[2] || 'http://127.0.0.1:8123/review.html';
  const b = await chromium.launch();
  const p = await b.newPage();
  const errors = [];
  p.on('pageerror', e => errors.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errors.push('console.error: ' + m.text()); });
  const count = () => p.textContent('#viewer-count');
  const isOpen = () => p.evaluate(() => document.getElementById('viewer').classList.contains('open'));
  const assert = (cond, msg) => { if (!cond) throw new Error('FAIL: ' + msg); console.log('  ok ' + msg); };

  await p.goto(URL, { waitUntil: 'networkidle' });
  const N = (await p.$$('.card')).length;
  assert(N > 0, `索引共 ${N} 张卡`);

  // 1. 点第一张卡 → 弹层、滚动锁、计数、说明、frame src
  await p.click('.card');
  await p.waitForSelector('.viewer.open');
  assert(await isOpen(), '点卡弹出查看器');
  assert(await p.evaluate(() => document.body.style.overflow) === 'hidden', '弹层打开时背景滚动锁定');
  await p.waitForTimeout(800);
  assert((await count()) === `1 / ${N}`, `初始计数 1 / ${N}`);
  const expected = await p.evaluate(() => {
    const c = document.querySelector('a.card');
    return (c.querySelector('.num').textContent + ' ' + c.querySelector('.title').textContent).trim();
  });
  const title1 = await p.textContent('#viewer-title');
  assert(title1.trim() === expected, `说明栏与首张卡一致（${title1.trim()}）`);
  const frameSrc1 = await p.evaluate(() => document.getElementById('viewer-frame').src);
  assert(/moon-city-\d+\.html/.test(frameSrc1), '主 frame 加载卡页面');

  // 2. 右箭头 → 下一张
  await p.click('#viewer-next');
  await p.waitForTimeout(400);
  assert((await count()) === `2 / ${N}`, `右箭头切到 2 / ${N}`);

  // 3. 左箭头 → 回退
  await p.click('#viewer-prev');
  await p.waitForTimeout(400);
  assert((await count()) === `1 / ${N}`, `左箭头回到 1 / ${N}`);

  // 4. 键盘 →
  await p.keyboard.press('ArrowRight');
  await p.waitForTimeout(400);
  assert((await count()) === `2 / ${N}`, `键盘 → 到 2 / ${N}`);

  // 5. 键盘 ←
  await p.keyboard.press('ArrowLeft');
  await p.waitForTimeout(400);
  assert((await count()) === `1 / ${N}`, `键盘 ← 回到 1 / ${N}`);

  // 6. 随机按钮（格式正确）
  await p.click('#viewer-rand');
  await p.waitForTimeout(400);
  assert(new RegExp(`^\\d+ / ${N}$`).test(await count()), '随机按钮计数格式正确');

  // 7. 点第 3 张缩略图 → 3 / N，且高亮
  const thumbs = await p.$$('.viewer-thumb');
  assert(thumbs.length === N, `缩略图共 ${N} 个`);
  await thumbs[2].click();
  await p.waitForTimeout(400);
  assert((await count()) === `3 / ${N}`, `点第 3 张缩略图跳到 3 / ${N}`);
  const on = await p.evaluate(() => Array.from(document.querySelectorAll('.viewer-thumb')).findIndex(t => t.classList.contains('on')));
  assert(on === 2, '第 3 张缩略图高亮');

  // 8. Esc → 关闭、滚动解锁
  await p.keyboard.press('Escape');
  await p.waitForTimeout(300);
  assert(!(await isOpen()), 'Esc 关闭查看器');
  assert(await p.evaluate(() => document.body.style.overflow) === '', '关闭后背景滚动恢复');

  // 9. 再开一张 → 「完整卡」按钮指向当前卡
  await p.click('.card');
  await p.waitForSelector('.viewer.open');
  await p.waitForTimeout(400);
  const openHref = await p.evaluate(() => document.getElementById('viewer-open').getAttribute('href'));
  assert(/moon-city-\d+\.html/.test(openHref), '「完整卡」链接指向当前卡');
  await p.keyboard.press('Escape');

  // 10. 无 JS 报错
  assert(errors.length === 0, '无 pageerror / console.error' + (errors.length ? ' → ' + errors.join(' | ') : ''));

  console.log('\n冒烟测试全过');
  await b.close();
  process.exit(0);
})().catch(e => { console.error(e.message); process.exit(1); });
