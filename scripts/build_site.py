"""Genera el sitio estático de lectura desde las páginas Markdown, sin dependencias."""
from pathlib import Path
import json, re, html

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'wiki'/'clase-01'
SITE=ROOT/'site'
SITE.mkdir(exist_ok=True)
manifest=json.loads((SOURCE/'manifest.json').read_text())
pages=manifest['pages']
esc=html.escape

def group(n):
    if n<=3:return 'Panorama'
    if n<=11:return 'Datos faltantes'
    if n<=16:return 'Atípicos'
    if n<=20:return 'Escala y geometría'
    if n<=25:return 'Transformaciones'
    if n<=28:return 'Datos mixtos'
    return 'Lotes y evaluación'

def inline(t):
    t=esc(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    return t

def paragraphs(t):return ''.join('<p>'+inline(x.replace('\n',' '))+'</p>' for x in t.strip().split('\n\n') if x.strip())

def section(t,name):
    m=re.search(r'^## '+re.escape(name)+r'\n\n(.*?)(?=^## |\Z)',t,re.S|re.M)
    return m.group(1).strip() if m else ''

def sidebar(active=0):
    rows=[];old=''
    for p in pages:
        n=p['slide'];g=group(n)
        if g!=old:rows.append(f'<h3>{esc(g)}</h3>');old=g
        text=p['title']+' '+g
        rows.append(f'<a class="lesson-link {"active" if n==active else ""}" href="/clase-01/diapositiva-{n:02}.html" data-slide="{n}" data-search="{esc(text.lower(),quote=True)}" '+('aria-current="page"' if n==active else '')+f'><span class="num">{n:02}</span><span>{esc(p["title"])}</span><span class="read-dot" aria-label="Leída"></span></a>')
    return '<aside id="sidebar"><a class="brand" href="/">ml<span>power</span><small>DATA SCIENCE EN TU NEGOCIO</small></a><label class="search-label" for="search">Buscar en la clase</label><input id="search" type="search" placeholder="KNN, pricing, leads…" autocomplete="off"><div class="progress-label"><span>Tu recorrido</span><span id="read-count">0 / 33</span></div><progress id="progress" max="33" value="0"></progress><nav aria-label="Diapositivas">'+''.join(rows)+'</nav><p id="no-results" hidden>No hay diapositivas para esta búsqueda.</p><div class="side-footer">Clase 01 · Maestría en Data Science<br><a href="/fuentes.html">Fuentes y aclaraciones</a></div></aside>'

def shell(title,body,active=0):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} · mlpower</title><meta name="description" content="Preprocesamiento de datos explicado con 99 historias del negocio inmobiliario. Una página por diapositiva."><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/styles.css"><script src="/app.js" defer></script></head><body data-current="{active}"><a class="skip" href="#main">Saltar al contenido</a><header class="mobile-header"><a href="/">mlpower</a><button id="menu" aria-expanded="false" aria-controls="sidebar">Índice</button></header>{sidebar(active)}<main id="main">{body}<footer class="main-footer"><span>mlpower · Aprender con contexto</span><a href="https://github.com/dinatalediego/ml_power" target="_blank" rel="noopener">Ver en GitHub ↗</a></footer></main></body></html>'''

cards=[]
for g in dict.fromkeys(group(p['slide']) for p in pages):
    ps=[p for p in pages if group(p['slide'])==g]
    cards.append(f'<a class="module" href="/clase-01/diapositiva-{ps[0]["slide"]:02}.html"><span class="eyebrow">SLIDES {ps[0]["slide"]:02}–{ps[-1]["slide"]:02}</span><h3>{esc(g)}</h3><p>{len(ps)*3} historias para entender la idea en tu trabajo.</p><span class="arrow">↗</span></a>')
home='''<div class="topline"><span>BIBLIOTECA DE APRENDIZAJE</span><a href="/fuentes.html">Sobre los ejemplos ↗</a></div><section class="hero"><div class="pill"><span></span> CLASE 01 · APRENDIZAJE NO SUPERVISADO</div><h1>Entiende los datos.<br><em>Reconoce el negocio.</em></h1><p class="lead">Preprocesamiento explicado con historias de leads, pricing y absorción inmobiliaria. Lee cada diapositiva y conecta la teoría con tus decisiones.</p><div class="hero-actions"><a class="button primary" href="/clase-01/diapositiva-01.html">Empezar la clase <span>→</span></a><a class="button secondary" id="resume" href="/clase-01/diapositiva-01.html">Continuar lectura</a></div><div class="stats"><div><strong>33</strong><span>Diapositivas explicadas</span></div><div><strong>99</strong><span>Historias inmobiliarias</span></div><div><strong>01</strong><span>Clase para comenzar</span></div></div></section><section class="section-head"><div><span class="eyebrow">EL RECORRIDO</span><h2>Una decisión a la vez.</h2></div><p>Elige un tema o sigue el orden de la presentación.</p></section><div class="modules">'''+''.join(cards)+'''</div><section class="note"><strong>Aprende con ejemplos, interpreta con criterio.</strong><p>Las cifras de las historias son sintéticas y similares al rubro inmobiliario. Cada página incluye el texto editable y las notas del docente para contrastar lo explicado con la clase original.</p><a href="/fuentes.html">Ver fuentes y precisiones →</a></section>'''
(SITE/'index.html').write_text(shell('Biblioteca de Data Science',home))
(SITE/'clase-01').mkdir(exist_ok=True)

for p in pages:
    n=p['slide'];t=(SOURCE/p['file']).read_text()
    intro=section(t,'Cómo leer esta diapositiva')
    stories=re.findall(r'^## Historia ([123]): (.*?)\n\n(.*?)(?=^## |\Z)',t,re.S|re.M)
    assert len(stories)==3
    st=''.join(f'<section class="story"><span class="story-number">HISTORIA {j}</span><h2>{esc(name)}</h2>{paragraphs(body)}</section>' for j,name,body in stories)
    original=section(t,'Contenido del material entregado').split('<details>')[0].strip()
    notes=re.search(r'<summary>Notas del docente en el archivo original</summary>\n\n(.*?)\n\n</details>',t,re.S).group(1)
    prev=f'<a href="/clase-01/diapositiva-{n-1:02}.html">← Anterior</a>' if n>1 else '<a href="/">← Inicio</a>'
    nxt=f'<a href="/clase-01/diapositiva-{n+1:02}.html">Siguiente →</a>' if n<33 else '<a href="/">Volver al índice →</a>'
    body=f'''<div class="topline"><a href="/">CLASE 01</a><span>{esc(group(n))}</span></div><article class="reading"><div class="lesson-kicker">DIAPOSITIVA {n:02} <span>/ 33</span></div><h1>{esc(p['title'])}</h1><p class="example-label">Tres historias con cifras sintéticas del rubro inmobiliario.</p><section class="explanation"><h2>La idea de la diapositiva</h2>{paragraphs(intro)}</section><div class="stories">{st}</div><section class="apply"><span class="eyebrow">LLEVARLO A TU TRABAJO</span><h2>{esc(section(t,'Aplicación a tu trabajo'))}</h2></section><div class="reading-tools"><button id="mark-read" aria-pressed="false">Marcar como leída</button><button id="print">Imprimir / guardar PDF</button><span id="save-status" role="status" aria-live="polite"></span></div><div class="source-details"><details><summary>Texto editable de la diapositiva original</summary><pre class="original">{esc(original)}</pre></details><details><summary>Notas del docente</summary>{paragraphs(notes)}</details></div><div class="reading-nav">{prev}<span>{n:02} / 33</span>{nxt}</div></article>'''
    (SITE/'clase-01'/f'diapositiva-{n:02}.html').write_text(shell(p['title'],body,n))

# Página de referencias: mantener enlaces y tablas con HTML accesible.
src=(SOURCE/'fuentes-y-aclaraciones.md').read_text()
def md_small(t):
    out=[];lines=t.splitlines();i=0
    def links(x):
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<a href="{esc(m[2],quote=True)}">{inline(m[1])}</a>',inline(x))
    while i<len(lines):
        line=lines[i]
        if not line.strip():i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',c) for c in cells):rows.append(cells)
                i+=1
            out.append('<div class="table-scroll"><table><thead><tr>'+''.join('<th>'+links(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+links(c)+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody></table></div>');continue
        if line.startswith('#'):
            level=len(line)-len(line.lstrip('#'));out.append(f'<h{level}>{inline(line[level:].strip())}</h{level}>')
        elif line.startswith('- '):out.append('<p class="ref">'+links(line[2:])+'</p>')
        else:out.append('<p>'+links(line)+'</p>')
        i+=1
    return ''.join(out).replace('href="README.md"','href="/"')
(SITE/'fuentes.html').write_text(shell('Fuentes y aclaraciones','<div class="topline"><a href="/">CLASE 01</a><span>REFERENCIAS</span></div><article class="reading sources">'+md_small(src)+'</article>'))
(SITE/'404.html').write_text(shell('Página no encontrada','<section class="hero"><span class="eyebrow">404</span><h1>Volvamos al índice.</h1><p>La página que buscas no está disponible.</p><a class="button primary" href="/">Ver la clase →</a></section>'))
assert len(list((SITE/'clase-01').glob('*.html')))==33
print('Sitio generado: 33 páginas de lectura, inicio, fuentes y 404.')
