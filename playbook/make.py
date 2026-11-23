# -*- coding: utf-8 -*-
# '10억 경영 플레이북' 랜딩을 혼자 서는 파일로 만든다.
# 쓰는 법: python3 playbook/make.py <아티팩트에서 받은 index.html> playbook/index.html
# 글은 아티팩트 페이지에서 고치고, 여기서는 저장된 글을 구워 넣기만 한다. 공개본에서는 글 고치기와 저장 막대를 뺀다.
import re, json, sys
from bs4 import BeautifulSoup
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def grab(pat):
    m = re.search(pat, s, re.S); assert m, pat; return m.group(1)
d = json.loads(grab(r'<script type="application/json" id="doc">(.*?)</script>'))
css = grab(r'<style id="css">(.*?)</style>')
js = grab(r'<script id="main">(.*?)</script>')
font = grab(r'(<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>)')

b = BeautifulSoup(d['base'], 'html.parser')
for k, v in d['edits'].items():
    el = b.find(attrs={'data-e': k}); assert el is not None, k
    el.clear(); el.append(BeautifulSoup(v, 'html.parser'))
base = str(b)

# 공개본: 고친 글 임시 보관, 더블클릭 수정, 저장 막대를 뺀다
def cut(a, z):
    global js
    i = js.index(a); j = js.index(z, i); js = js[:i] + js[j:]
cut('var HEAD=', 'var app=')
cut('var S;try', '/* 자세히 보기 */')
cut('/* 더블클릭하면 그 자리에서 글을 고친다 */', '})();')
for w in ('pending', 'contenteditable', 'claude', 'bar(', 'localStorage'): assert w not in js, w
css = re.sub(r'#bar[^{]*\{[^}]*\}', '', css).replace(',#bar button:focus-visible', '')
assert '#bar' not in css

TITLE = '월매출 10억을 만드는 경영 플레이북'
DESC = '월매출 10억까지 가는 길은 순서와 방법이 정해져 있어요. 플레이북대로 하도록 돕는 피부과 경영 소프트웨어, 세르클.'
URL = 'https://bk-nam.github.io/cercle-landing/playbook/'
ICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23151515'/%3E%3Ccircle cx='16' cy='16' r='8' fill='none' stroke='%23fff' stroke-width='3'/%3E%3C/svg%3E"
RESET = ':root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}'
out = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<meta name="robots" content="noindex">
<meta property="og:type" content="website">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<link rel="icon" href="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
%s
<style>%s</style>
<style id="css">%s</style>
</head>
<body>
<main id="app">%s</main>
<script id="main">%s</script>
</body>
</html>
''' % (TITLE, DESC, TITLE, DESC, URL, ICON, font, RESET, css, base, js)
open(dst, 'w', encoding='utf-8').write(out)
print('ok', len(out.encode()), 'bytes, edits baked:', len(d['edits']))
