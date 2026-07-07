#!/usr/bin/env python3
"""Count visible Chinese characters in moon-city HTML modules for validation."""
import re
import sys

def strip_tags(text):
    """Remove HTML tags and count only visible characters."""
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'\s+', '', clean)
    return clean, len(clean)

def validate_html(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # Extract title
    title_match = re.search(r'<div class="title">(.+?)</div>', html)
    title_text = title_match.group(1) if title_match else ''

    # Extract blocks
    blocks = re.findall(r'<div class="block">.*?<div class="text">(.*?)</div>.*?</div>', html, re.DOTALL)
    highlight = re.search(r'<div class="highlight">.*?<div class="text">(.*?)</div>.*?</div>', html, re.DOTALL)
    insight = re.search(r'<div class="insight">.*?<div class="text">(.*?)</div>.*?</div>', html, re.DOTALL)

    results = {'title': title_text, 'blocks': [], 'highlight': '', 'insight': '', 'total': 0}
    issues = []

    # Title check
    if len(title_text) > 9:
        issues.append(f'  ❌ 标题 {len(title_text)} 字，超过 9 字上限')
    else:
        issues.append(f'  ✅ 标题 {len(title_text)} 字')

    # Blocks
    for i, block_html in enumerate(blocks):
        clean, count = strip_tags(block_html)
        results['blocks'].append({'html': block_html, 'clean': clean, 'count': count})
        status = '✅' if 100 <= count <= 150 else '⚠️'
        issues.append(f'  Block {i+1}: {count} 字 {status}')

    # Highlight
    if highlight:
        clean, count = strip_tags(highlight.group(1))
        results['highlight'] = {'clean': clean, 'count': count}
        status = '✅' if 30 <= count <= 35 else '⚠️'
        issues.append(f'  Highlight: {count} 字 {status}')
    else:
        issues.append('  ❌ 缺少 highlight')

    # Insight
    if insight:
        clean, count = strip_tags(insight.group(1))
        results['insight'] = {'clean': clean, 'count': count}
        status = '✅' if 65 <= count <= 70 else '⚠️'
        issues.append(f'  Insight: {count} 字 {status}')
    else:
        issues.append('  ❌ 缺少 insight')

    # Total (blocks + highlight + insight, no refs)
    total = sum(b['count'] for b in results['blocks']) + results['highlight']['count'] + results['insight']['count']
    results['total'] = total
    status = '✅' if 460 <= total <= 510 else '⚠️'
    issues.append(f'  正文总计: {total} 字 {status}')

    # Display
    print(f"\n{'='*60}")
    print(f"📄 {filepath}")
    print(f"📌 标题: {results['title']}")
    print(f"{'='*60}")
    for issue in issues:
        print(issue)

    # Show cleaned text for manual review
    print(f"\n📝 正文全文（去标签）:")
    for i, b in enumerate(results['blocks']):
        print(f"\n  Block {i+1}: {b['clean']}")
    if results['highlight']:
        print(f"\n  Highlight: {results['highlight']['clean']}")
    if results['insight']:
        print(f"\n  Insight: {results['insight']['clean']}")

    return all('✅' in i for i in issues)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        all_ok = True
        for fp in sys.argv[1:]:
            ok = validate_html(fp)
            all_ok = all_ok and ok
        print(f"\n{'='*60}")
        print(f"🏁 全部通过" if all_ok else "⚠️ 存在超标项")
    else:
        print("Usage: python count_chars.py issues/moon-city-NN.html ...")
