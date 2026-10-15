"""Gera as ilustrações provisórias (SVG) usadas no portfólio.
Uso: python3 scripts/portfolio/ilustracoes.py  -> grava em scripts/portfolio/img/
Todas são marcadas como IMAGEM ILUSTRATIVA no portfólio; substitua por fotos reais.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

NAVY, ORANGE, STEEL = "#00188f", "#fe7501", "#48657f"
W, H = 1200, 800


def svg(body, sky=("#bcd3ea", "#eef3f9")):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky[0]}"/><stop offset="1" stop-color="{sky[1]}"/></linearGradient>
  <linearGradient id="soil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b08a62"/><stop offset="1" stop-color="#7d5c3d"/></linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a5fa8"/><stop offset="1" stop-color="#1b2f6b"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<circle cx="1040" cy="120" r="60" fill="#fff6e0" opacity=".9"/>
{clouds()}
{body}
</svg>"""


def clouds():
    c = ""
    for x, y, s in [(180, 110, 1), (620, 70, .8), (860, 170, .6)]:
        c += f'<g fill="#fff" opacity=".85" transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="70" ry="24"/><ellipse cx="40" cy="-14" rx="44" ry="26"/><ellipse cx="-36" cy="-8" rx="36" ry="20"/></g>'
    return c


def excavator(x, y, s=1.0, flip=False, arm="up"):
    """Escavadeira estilizada; (x,y) = base das esteiras."""
    t = f"translate({x},{y}) scale({-s if flip else s},{s})"
    if arm == "up":
        boom = "M150,-120 L260,-230 L340,-150"
        bucket = '<path d="M330,-160 l40,10 l-6,48 l-44,-16 z" fill="#3b3f46"/>'
    else:  # alcançando para baixo (vala)
        boom = "M150,-120 L270,-210 L330,-40"
        bucket = '<path d="M318,-50 l44,6 l-8,46 l-44,-14 z" fill="#3b3f46"/>'
    return f"""<g transform="{t}">
  <rect x="-10" y="-46" width="220" height="46" rx="23" fill="#2e333b"/>
  <g fill="#555c66">{''.join(f'<circle cx="{cx}" cy="-23" r="14"/>' for cx in (16, 66, 116, 166))}</g>
  <rect x="10" y="-80" width="180" height="34" rx="6" fill="#3b3f46"/>
  <rect x="0" y="-150" width="170" height="72" rx="8" fill="{ORANGE}"/>
  <rect x="20" y="-210" width="80" height="64" rx="8" fill="{ORANGE}"/>
  <rect x="32" y="-200" width="58" height="42" rx="4" fill="#1c3d73" opacity=".85"/>
  <rect x="120" y="-140" width="40" height="10" fill="#2e333b"/>
  <path d="{boom}" fill="none" stroke="{ORANGE}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="{boom}" fill="none" stroke="#c95c00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity=".5" transform="translate(0,10)"/>
  {bucket}
</g>"""


def dump_truck(x, y, s=1.0):
    return f"""<g transform="translate({x},{y}) scale({s})">
  <path d="M0,-150 L230,-150 L250,-60 L0,-60 z" fill="{ORANGE}"/>
  <path d="M10,-150 L220,-150 L236,-80" fill="none" stroke="#c95c00" stroke-width="6"/>
  <path d="M-20,-70 L270,-70 L270,-40 L-20,-40 z" fill="#3b3f46"/>
  <path d="M270,-150 L340,-150 L370,-100 L370,-40 L270,-40 z" fill="#e9edf2"/>
  <path d="M285,-140 L335,-140 L355,-104 L285,-104 z" fill="#1c3d73" opacity=".85"/>
  <g fill="#2e333b">{''.join(f'<circle cx="{cx}" cy="-30" r="32"/>' for cx in (40, 120, 320))}</g>
  <g fill="#8a919b">{''.join(f'<circle cx="{cx}" cy="-30" r="12"/>' for cx in (40, 120, 320))}</g>
</g>"""


def tree(x, y, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-6" y="-60" width="12" height="60" fill="#6b4a2f"/><circle cx="0" cy="-90" r="42" fill="#4f8a4a"/><circle cx="-22" cy="-70" r="28" fill="#5f9c58"/><circle cx="24" cy="-72" r="26" fill="#447d40"/></g>'


# ---------------------------------------------------------------- edificação
def edificacao():
    b = '<rect x="0" y="640" width="1200" height="160" fill="url(#soil)"/>'
    b += '<rect x="0" y="630" width="1200" height="14" fill="#9c7a55"/>'
    # prédio vizinho ao fundo
    b += '<rect x="40" y="330" width="180" height="310" fill="#cdd6e1"/>'
    for r in range(6):
        for c in range(3):
            b += f'<rect x="{62+c*54}" y="{350+r*46}" width="34" height="28" fill="#aebccd"/>'
    # estrutura principal
    x0, x1, base, fh, floors = 300, 820, 640, 72, 6
    for f in range(floors):
        top = base - (f + 1) * fh
        if f < 3:  # pavimentos fechados
            b += f'<rect x="{x0}" y="{top}" width="{x1-x0}" height="{fh}" fill="#eef1f5"/>'
            for c in range(6):
                b += f'<rect x="{x0+24+c*84}" y="{top+16}" width="56" height="40" fill="url(#glass)"/>'
        b += f'<rect x="{x0-10}" y="{top-8}" width="{x1-x0+20}" height="12" fill="#8d99a8"/>'
    for c in range(7):  # pilares
        cx = x0 + c * ((x1 - x0) / 6)
        b += f'<rect x="{cx-7}" y="{base-floors*fh}" width="14" height="{floors*fh}" fill="#9aa6b4"/>'
    # andaime
    for c in range(4):
        sx = x1 + 20 + c * 30
        b += f'<line x1="{sx}" y1="{base}" x2="{sx}" y2="{base-4*fh-10}" stroke="{STEEL}" stroke-width="5"/>'
    for r in range(5):
        sy = base - r * fh
        b += f'<line x1="{x1+15}" y1="{sy}" x2="{x1+115}" y2="{sy}" stroke="{ORANGE}" stroke-width="6"/>'
        if r < 4:
            b += f'<line x1="{x1+20}" y1="{sy}" x2="{x1+110}" y2="{sy-fh}" stroke="{STEEL}" stroke-width="3"/>'
    # grua
    mx = 980
    b += f'<rect x="{mx-16}" y="120" width="32" height="520" fill="none" stroke="{ORANGE}" stroke-width="6"/>'
    for yy in range(130, 640, 34):
        b += f'<line x1="{mx-16}" y1="{yy}" x2="{mx+16}" y2="{yy+34}" stroke="{ORANGE}" stroke-width="4"/>'
    b += f'<rect x="560" y="110" width="600" height="22" fill="none" stroke="{ORANGE}" stroke-width="6"/>'
    for xx in range(560, 1160, 30):
        b += f'<line x1="{xx}" y1="132" x2="{xx+30}" y2="110" stroke="{ORANGE}" stroke-width="3"/>'
    b += f'<path d="M{mx-16},110 L{mx},50 L{mx+16},110" fill="none" stroke="{ORANGE}" stroke-width="6"/>'
    b += f'<line x1="{mx}" y1="50" x2="580" y2="110" stroke="{STEEL}" stroke-width="3"/><line x1="{mx}" y1="50" x2="1140" y2="110" stroke="{STEEL}" stroke-width="3"/>'
    b += f'<rect x="1090" y="132" width="60" height="44" fill="#5a6370"/>'
    b += f'<rect x="{mx-30}" y="140" width="60" height="36" rx="4" fill="#e9edf2"/>'
    b += f'<line x1="680" y1="132" x2="680" y2="330" stroke="#2e333b" stroke-width="3"/>'
    b += f'<rect x="630" y="330" width="100" height="26" fill="{NAVY}"/>'
    b += dump_truck(60, 760, .75)
    return svg(b)


# ---------------------------------------------------------------- pavimentação / urbanização
def urbanizacao():
    hz = 380
    b = f'<rect x="0" y="{hz}" width="1200" height="{H-hz}" fill="#86b46f"/>'
    b += f'<path d="M0,{hz} Q300,{hz-40} 600,{hz} T1200,{hz} V{hz+10} H0z" fill="#6f9e5d"/>'
    b += f'<polygon points="530,{hz} 670,{hz} 1200,800 0,800" fill="#c9ccd1"/>'  # calçadas
    b += f'<polygon points="555,{hz} 645,{hz} 1080,800 120,800" fill="#3d4552"/>'
    b += f'<polygon points="555,{hz} 560,{hz} 140,800 120,800" fill="#f1f1f1"/><polygon points="640,{hz} 645,{hz} 1080,800 1060,800" fill="#f1f1f1"/>'
    # faixa central tracejada
    import math
    for i in range(9):
        t0, t1 = (i / 9) ** 1.6, ((i + .5) / 9) ** 1.6
        y0, y1 = hz + t0 * (H - hz), hz + t1 * (H - hz)
        w0, w1 = 2 + t0 * 14, 2 + t1 * 14
        b += f'<polygon points="{600-w0/2},{y0} {600+w0/2},{y0} {600+w1/2},{y1} {600-w1/2},{y1}" fill="#ffd200"/>'
    # postes e árvores
    for i, t in enumerate([.15, .35, .6, .95]):
        y = hz + t * (H - hz); s = .3 + t * .9
        xl = 545 - t * 520; xr = 655 + t * 520
        b += tree(xl - 40 * s, y, s) + tree(xr + 40 * s, y, s)
        b += f'<g transform="translate({xr},{y}) scale({s})"><rect x="-4" y="-200" width="8" height="200" fill="#5a6370"/><path d="M0,-196 q-50,0 -60,20" fill="none" stroke="#5a6370" stroke-width="8"/><rect x="-78" y="-180" width="36" height="12" rx="4" fill="#fff6c2"/></g>'
    # rolo compactador
    b += f"""<g transform="translate(700,700) scale(.9)">
      <rect x="0" y="-130" width="200" height="70" rx="10" fill="{ORANGE}"/>
      <rect x="110" y="-200" width="80" height="72" rx="6" fill="#e9edf2"/><rect x="122" y="-190" width="56" height="42" fill="#1c3d73" opacity=".85"/>
      <rect x="-60" y="-110" width="110" height="110" rx="55" fill="#8a919b"/><rect x="-60" y="-110" width="110" height="110" rx="55" fill="none" stroke="#5a6370" stroke-width="10"/>
      <circle cx="170" cy="-35" r="40" fill="#2e333b"/><circle cx="170" cy="-35" r="14" fill="#8a919b"/>
    </g>"""
    b += f'<g transform="translate(300,760)"><path d="M0,0 l30,-80 l30,80z" fill="{ORANGE}"/><rect x="10" y="-50" width="40" height="10" fill="#fff"/><rect x="-6" y="-6" width="72" height="8" fill="#2e333b"/></g>'
    return svg(b)


# ---------------------------------------------------------------- saneamento
def saneamento():
    gl = 360
    b = f'<rect x="0" y="{gl}" width="1200" height="{H-gl}" fill="url(#soil)"/>'
    b += f'<rect x="0" y="{gl-14}" width="1200" height="18" fill="#7fae67"/>'
    for yy in (470, 560, 650, 740):
        b += f'<path d="M0,{yy} Q300,{yy-12} 600,{yy} T1200,{yy}" fill="none" stroke="#6b4c31" stroke-width="3" opacity=".35"/>'
    # vala
    b += f'<polygon points="430,{gl} 900,{gl} 860,720 470,720" fill="#5e432b"/>'
    b += f'<polygon points="470,{gl} 860,{gl} 840,720 490,720" fill="#d8c3a2" opacity=".25"/>'
    for xx in (480, 840):
        b += f'<rect x="{xx-8}" y="{gl+10}" width="16" height="330" fill="#c9a46a"/>'
    for yy in (430, 560):
        b += f'<rect x="480" y="{yy}" width="360" height="14" fill="{STEEL}"/>'
    # tubos (corte)
    b += f'<circle cx="580" cy="650" r="58" fill="#2b6cb0"/><circle cx="580" cy="650" r="44" fill="#16437a"/>'
    b += f'<circle cx="745" cy="664" r="44" fill="{ORANGE}"/><circle cx="745" cy="664" r="32" fill="#a84d00"/>'
    # tubos empilhados na superfície
    for i, (px, py) in enumerate([(120, gl - 20), (196, gl - 20), (158, gl - 82)]):
        b += f'<circle cx="{px}" cy="{py}" r="38" fill="#2b6cb0"/><circle cx="{px}" cy="{py}" r="26" fill="#16437a"/>'
    b += excavator(930, gl, .95, flip=True, arm="down")
    # cones e fita
    for cx in (330, 1100):
        b += f'<g transform="translate({cx},{gl})"><path d="M0,0 l18,-56 l18,56z" fill="{ORANGE}"/><rect x="8" y="-34" width="20" height="8" fill="#fff"/></g>'
    b += f'<line x1="300" y1="{gl-40}" x2="430" y2="{gl-40}" stroke="{ORANGE}" stroke-width="5" stroke-dasharray="18 10"/>'
    return svg(b)


# ---------------------------------------------------------------- rede elétrica
def eletrica():
    gl = 600
    b = f'<path d="M0,{gl} Q400,{gl-50} 800,{gl-10} T1200,{gl-30} V800 H0z" fill="#86b46f"/>'
    b += f'<rect x="0" y="{gl+40}" width="1200" height="160" fill="#7aa864"/>'
    poles = [(140, 640, 1), (430, 590, .8), (660, 560, .62), (840, 540, .5), (980, 530, .4), (1090, 524, .33)]
    tops = []
    for x, y, s in poles:
        h = 420 * s
        b += f'<rect x="{x-8*s}" y="{y-h}" width="{16*s}" height="{h}" fill="#7b8794"/>'
        b += f'<rect x="{x-70*s}" y="{y-h+20*s}" width="{140*s}" height="{12*s}" fill="#5a6370"/>'
        pts = [(x - 60 * s, y - h + 16 * s), (x, y - h + 16 * s), (x + 60 * s, y - h + 16 * s)]
        for px, py in pts:
            b += f'<rect x="{px-4*s}" y="{py-14*s}" width="{8*s}" height="{16*s}" fill="#e9edf2"/>'
        tops.append(pts)
    for i in range(len(tops) - 1):
        for k in range(3):
            (x0, y0), (x1, y1) = tops[i][k], tops[i + 1][k]
            b += f'<path d="M{x0},{y0-12} Q{(x0+x1)/2},{max(y0,y1)+30} {x1},{y1-12}" fill="none" stroke="#2e333b" stroke-width="2.5"/>'
    # transformador no primeiro poste
    b += f'<rect x="160" y="330" width="70" height="90" rx="10" fill="#8a919b"/><rect x="170" y="310" width="10" height="22" fill="#e9edf2"/><rect x="210" y="310" width="10" height="22" fill="#e9edf2"/>'
    # subestação ao fundo
    b += f'<rect x="760" y="470" width="300" height="80" fill="none" stroke="#9aa6b4" stroke-width="3"/>'
    for xx in range(760, 1061, 20):
        b += f'<line x1="{xx}" y1="470" x2="{xx}" y2="550" stroke="#9aa6b4" stroke-width="1.5"/>'
    for xx in (800, 880, 960):
        b += f'<rect x="{xx}" y="420" width="50" height="60" fill="#b5bfca"/><rect x="{xx+10}" y="400" width="8" height="22" fill="#e9edf2"/><rect x="{xx+32}" y="400" width="8" height="22" fill="#e9edf2"/>'
    # caminhão cesto
    b += f"""<g transform="translate(330,720)">
      <rect x="0" y="-90" width="260" height="60" fill="#e9edf2"/><rect x="0" y="-60" width="260" height="10" fill="{ORANGE}"/>
      <path d="M260,-110 L330,-110 L360,-70 L360,-30 L260,-30z" fill="#e9edf2"/><path d="M272,-100 L326,-100 L346,-72 L272,-72z" fill="#1c3d73" opacity=".85"/>
      <circle cx="60" cy="-22" r="28" fill="#2e333b"/><circle cx="300" cy="-22" r="28" fill="#2e333b"/>
      <path d="M120,-90 L200,-250" stroke="{STEEL}" stroke-width="16" stroke-linecap="round"/>
      <rect x="180" y="-300" width="56" height="44" rx="4" fill="{ORANGE}"/>
    </g>"""
    return svg(b)


# ---------------------------------------------------------------- equipamentos
def equipamentos():
    gl = 640
    b = f'<rect x="0" y="{gl}" width="1200" height="160" fill="url(#soil)"/>'
    b += f'<path d="M760,{gl} Q900,{gl-170} 1060,{gl} z" fill="#9c7a55"/><path d="M820,{gl} Q930,{gl-110} 1040,{gl} z" fill="#b08a62"/>'
    b += excavator(80, gl, 1.0, arm="up")
    b += dump_truck(560, gl + 10, .95)
    b += f'<g transform="translate(470,{gl})"><path d="M0,0 l20,-64 l20,64z" fill="{ORANGE}"/><rect x="10" y="-40" width="20" height="9" fill="#fff"/></g>'
    return svg(b)


# ---------------------------------------------------------------- engenharia / projeto
def projeto():
    b = '<rect width="1200" height="800" fill="#0b2a7a"/>'
    for i in range(0, 1200, 40):
        b += f'<line x1="{i}" y1="0" x2="{i}" y2="800" stroke="#fff" stroke-opacity=".07"/>'
    for i in range(0, 800, 40):
        b += f'<line x1="0" y1="{i}" x2="1200" y2="{i}" stroke="#fff" stroke-opacity=".07"/>'
    s = 'fill="none" stroke="#dbe6ff" stroke-width="3"'
    b += f'<rect x="160" y="140" width="560" height="420" {s}/>'
    b += f'<path d="M160,330 H460 V140 M460,330 V560 M460,430 H720 M600,140 V300" {s}/>'
    b += f'<path d="M460,260 a70,70 0 0 1 70,70" fill="none" stroke="#dbe6ff" stroke-width="2" stroke-dasharray="6 6"/>'
    b += f'<path d="M160,600 H720 M160,590 V610 M720,590 V610" fill="none" stroke="{ORANGE}" stroke-width="3"/>'
    b += f'<path d="M120,140 V560 M110,140 H130 M110,560 H130" fill="none" stroke="{ORANGE}" stroke-width="3"/>'
    # capacete
    b += f'<g transform="translate(900,470)"><path d="M-150,0 a150,140 0 0 1 300,0z" fill="{ORANGE}"/><rect x="-190" y="-6" width="380" height="30" rx="15" fill="#e06800"/><rect x="-22" y="-150" width="44" height="150" rx="16" fill="#ff8f2e"/></g>'
    # régua
    b += f'<g transform="translate(780,650) rotate(-18)"><rect width="360" height="56" rx="6" fill="#f1d58a"/>'
    b += ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{24 if x%60==0 else 14}" stroke="#7a5d14" stroke-width="2"/>' for x in range(12, 360, 12))
    b += '</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{b}</svg>'


for name, fn in {
    "edificacao": edificacao, "urbanizacao": urbanizacao, "saneamento": saneamento,
    "eletrica": eletrica, "equipamentos": equipamentos, "projeto": projeto,
}.items():
    with open(os.path.join(OUT, name + ".svg"), "w") as fh:
        fh.write(fn())
print("ok")
