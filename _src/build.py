"""
講義網站產生器：把 _src/pages/*.html 套上共用樣式，輸出成網站根目錄的單檔 HTML。
每個輸出檔都自足（樣式內嵌），可以單獨轉寄或離線開啟。

用法：python _src/build.py
新增一週：在 _src/pages/ 新增 w03.html（第一行 <!--title: ...-->），再到 index.html 的週次表加連結。
"""
import pathlib, re

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
CSS = (SRC / "style.css").read_text(encoding="utf-8")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600'
         '&family=LXGW+WenKai+TC:wght@400;700&family=Noto+Sans+TC:wght@400;600;700&display=swap">')

for page in sorted((SRC / "pages").glob("*.html")):
    body = page.read_text(encoding="utf-8")
    title = re.match(r"<!--title:\s*(.*?)-->", body).group(1)
    html = (f'<!doctype html>\n<html lang="zh-Hant-TW">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{title}</title>\n{FONTS}\n<style>\n{CSS}</style>\n</head>\n<body>\n<main class="wrap">\n'
            f'{body}\n</main>\n</body>\n</html>\n')
    (ROOT / page.name).write_text(html, encoding="utf-8")
    print("built", page.name)
