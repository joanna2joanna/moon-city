#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moon-city review.html 加卡脚本。
把新一期插进对应「建造六步」章节，章节内从新到旧重排，更新期数与总数。
必要时候开新章节（--new-name + --new-color）。

用法：
  python3 add_review.py <期号> <标题> <step1-6>
  python3 add_review.py 134 月面昼夜再续 step1
  python3 add_review.py 135 新主题 step1 --new-name "⑦ 新篇章" --new-color "#FF00AA"

说明：
  - 期号、标题必须与 issues/moon-city-NN.html 一致
  - 重复期号自动跳过（幂等）
"""
import re
import sys

PATH = 'review.html'

STEP_DOT = {
    'step1': 'var(--c1)', 'step2': 'var(--c2)', 'step3': 'var(--c3)',
    'step4': 'var(--c4)', 'step5': 'var(--c5)', 'step6': 'var(--c6)',
}


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    num = int(sys.argv[1])
    title = sys.argv[2]
    step = sys.argv[3]
    new_name = None
    new_color = None
    if '--new-name' in sys.argv:
        new_name = sys.argv[sys.argv.index('--new-name') + 1]
    if '--new-color' in sys.argv:
        new_color = sys.argv[sys.argv.index('--new-color') + 1]

    html = open(PATH, encoding='utf-8').read()

    # 幂等：该期已在 review 里则跳过
    if f'moon-city-{num:02d}.html' in html:
        print(f'# {num} 已在 review 中，跳过（幂等）')
        return

    dot = STEP_DOT.get(step, f'var(--c{step.replace("step", "")})') if step.startswith('step') else 'var(--c7)'
    card = (f'      <a class="card" style="border-left-color:{dot}" '
            f'href="issues/moon-city-{num:02d}.html">'
            f'<div class="num">#{num}</div><div class="title">{title}</div></a>')

    if step == 'new':
        if not new_name or not new_color:
            print('新章节需要 --new-name 与 --new-color')
            sys.exit(1)
        html = _add_new_chapter(html, num, title, new_name, new_color, card)
    else:
        html = _insert_into_step(html, step, card)

    html = _update_totals(html)
    open(PATH, 'w', encoding='utf-8').write(html)
    print(f'已加入 review.html：# {num}「{title}」→ {step or "新章节"}')


def _insert_into_step(html, step, card):
    """插到指定章节 grid 顶部，并整格按期号从新到旧重排。"""
    block_m = re.search(
        rf'<div class="cat" id="cat-{step}">(.*?)(?=<div class="cat" id="cat-|\Z)',
        html, re.S)
    if not block_m:
        print(f'!! 找不到章节 cat-{step}，用 --new-name/--new-color 开新章节')
        sys.exit(1)
    block = block_m.group(0)
    grid_m = re.search(r'<div class="grid">\s*\n(.*?)\n    </div>', block, re.S)
    cards = [card] + re.findall(r'<a class="card".*?</a>', grid_m.group(1), re.S)
    # 按期号从新到旧重排
    cards.sort(key=_num_key, reverse=True)
    new_grid = '<div class="grid">\n' + '\n'.join(cards) + '\n    </div>'
    # grid 闭合是 4 空格缩进、章节闭合是 2 空格缩进，必须精确匹配两行
    block = re.sub(r'<div class="grid">.*?\n    </div>\n  </div>', new_grid + '\n  </div>', block, count=1, flags=re.S)
    # 更新该章节期数（「N 期 — 副标题」）
    m = re.search(r'<span class="count">(\d+) 期', block)
    if m:
        block = block.replace(m.group(0), f'<span class="count">{int(m.group(1)) + 1} 期', 1)
    return html.replace(block_m.group(0), block, 1)


def _add_new_chapter(html, num, title, new_name, new_color, card):
    """开新章节：加 :root 变量、图例入口、cat 块。"""
    # :root 加 --c7 变量
    if '--c7:' not in html:
        m = re.search(r'--c6:([^;]+);', html)
        if m:
            html = html.replace(m.group(0), m.group(0) + f'\n    --c7:{new_color};', 1)
    # 图例加入口
    legend_m = re.search(r'(<div class="legend">.*?)(</div>)', html, re.S)
    if legend_m and f'href="#cat-step7"' not in html:
        entry = f'    <a href="#cat-step7"><span class="dot" style="background:var(--c7)"></span>{new_name}</a>'
        html = html.replace(legend_m.group(0), legend_m.group(1) + '\n' + entry + legend_m.group(2), 1)
    # cat 块加在最后
    cat_block = (
        '\n\n  <!-- ' + new_name + ' -->\n'
        '  <div class="cat" id="cat-step7">\n'
        '    <div class="cat-header"><span class="dot" style="background:var(--c7)"></span>'
        f'<h2>{new_name}</h2><span class="count">1 期</span></div>\n'
        '    <div class="grid">\n'
        f'{card}\n'
        '    </div>\n'
        '  </div>'
    )
    # 插在 footer 之前
    html = html.replace('<div class="footer">', cat_block + '\n\n  <div class="footer">', 1)
    return html


def _num_key(card):
    m = re.search(r'moon-city-(\d+)\.html', card)
    return int(m.group(1)) if m else 0


def _update_totals(html):
    """更新 <title> 与副标题里的总数。"""
    n = len(re.findall(r'<a class="card"[^>]*href="issues/moon-city-\d+\.html"', html))
    html = re.sub(r'<title>月球盖座城 · \d+期分类索引</title>',
                  f'<title>月球盖座城 · {n}期分类索引</title>', html)
    html = re.sub(r'<p class="sub">\d+ 期 · 按建造六步分类复习</p>',
                  f'<p class="sub">{n} 期 · 按建造六步分类复习</p>', html)
    return html


if __name__ == '__main__':
    main()
