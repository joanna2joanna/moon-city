#!/usr/bin/env python3
"""Count visible Chinese characters in moon-city-lite HTML modules."""
import re
import sys

def strip_tags(text):
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'\s+', '', clean)
    return clean, len(clean)

def validate_html(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # Title
    title_match = re.search(r'<div class="title">(.+?)</div>', html)
    title_text = title_match.group(1) if title_match else ''

    # Blocks (only block class, not tidbit)
    blocks = re.findall(r'<div class="block">.*?<div class="text">(.*?)</div>.*?</div>', html, re.DOTALL)

    # Tidbit
    tidbit_match = re.search(r'<div class="tidbit">.*?<div class="txt">(.*?)</div>.*?</div>', html, re.DOTALL)

    issues = []

    # Title: ≤9 chars, must contain 月
    tlen = len(title_text)
    has_yue = '月' in title_text
    t_status = '✅' if tlen <= 9 and has_yue else '⚠️'
    issues.append(f'  标题: {tlen} 字 {t_status}')

    # Blocks: 3 lines each, ~65-75 chars
    total_body = 0
    for i, block_html in enumerate(blocks):
        clean, count = strip_tags(block_html)
        total_body += count
        status = '✅' if 60 <= count <= 85 else '⚠️'
        issues.append(f'  Block {i+1}: {count} 字 {status}')

    # Tidbit: 2 lines, ~50-65 chars
    if tidbit_match:
        clean, count = strip_tags(tidbit_match.group(1))
        total_body += count
        status = '✅' if 45 <= count <= 70 else '⚠️'
        issues.append(f'  Tidbit: {count} 字 {status}')
    else:
        issues.append('  ❌ 缺少 tidbit')

    # Total
    t_status = '✅' if 150 <= total_body <= 240 else '⚠️'
    issues.append(f'  正文总计: {total_body} 字 {t_status}')

    print(f"\n{'='*60}")
    print(f"📄 {filepath}")
    print(f"📌 标题: [{title_text}] ({'含月' if has_yue else '⚠️缺月'})")
    print(f"{'='*60}")
    for issue in issues:
        print(issue)

    return all('✅' in i for i in issues) and has_yue

if __name__ == '__main__':
    if len(sys.argv) > 1:
        all_ok = True
        for fp in sys.argv[1:]:
            ok = validate_html(fp)
            all_ok = all_ok and ok
        print(f"\n{'='*60}")
        print(f"🏁 全部通过" if all_ok else "⚠️ 存在超标项")
    else:
        print("Usage: python count_chars_v2.py issues/moon-city-NN.html ...")
