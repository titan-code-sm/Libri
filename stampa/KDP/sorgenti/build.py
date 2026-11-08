"""Costruisce i PDF KDP (interno con bleed + copertina avvolgente) dal libro HTML.
Uso: python3 build.py <libro.html> <cartella_jpg_hires> <cartella_output>
"""
import re, sys, os, html as H

src, imgdir, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
h = open(src, encoding="utf-8").read()
style = h.split("<style>")[1].split("</style>")[0]
book = h.split('<div id="book">')[1].split("</div></main>")[0]
parts = re.split(r'\n(?=<div class="page)', book.strip())
pages = {re.search(r'data-label="([^"]*)"', p).group(1): p for p in parts}

hires = {"Copertina": "libro1-copertina.jpg",
         "Da colorare 1": "libro1-colorare.jpg", "Da colorare 2": "libro1-colorare-2.jpg",
         "Da colorare 3": "libro1-colorare-3.jpg", "Da colorare 4": "libro1-colorare-4.jpg"}
for n in range(2, 25, 2):
    hires[f"Pagina {n}"] = f"libro1-p{n-1:02d}-{n:02d}.jpg"

def swap(label):
    p = pages[label]
    if label in hires:
        uri = "file://" + os.path.abspath(os.path.join(imgdir, hires[label]))
        p, k = re.subn(r'src="data:image/[^"]+"', f'src="{uri}"', p, count=1)
        assert k == 1, label
        p = p.replace(' loading="lazy"', "")
    return p

# Colophon: niente segnaposto stampato
pages["Colophon"] = pages["Colophon"].replace('<p class="isbn">ISBN [DA DEFINIRE]</p>', "")
# Retro: area codice a barre lasciata vuota (KDP stampa il suo)
pages["Retro"] = pages["Retro"].replace('<div class="barcode">Spazio<br>codice a barre</div>', '<div class="barcode-space"></div>')

old_author = "<b>L'autore</b> Mat guida l'ambulanza a San Marino. In questo libro racconta il suo lavoro ai bambini, con Sirena Blu e la sua squadra."
assert old_author in pages["Retro"]
pages["Retro"] = pages["Retro"].replace(old_author, "<b>L'autore</b> Da bambino, Mat si fermava incantato ogni volta che passava un'ambulanza. Oggi è un soccorritore del servizio di emergenza sanitaria e, con Sirena Blu e la sua squadra, racconta ai bambini il suo lavoro.")

# Ordine di stampa: pagina 1 del PDF = pagina destra. Il testo va a sinistra (pari), l'illustrazione a destra (dispari).
order = ["Ex libris", "Dedica", "Frontespizio"] + [f"Pagina {n}" for n in range(1, 25)] + \
        ["Fine", "Per i genitori 1", "Per i genitori 2", "Per i genitori 3", "Per i genitori 4",
         "Da colorare 1", "Da colorare 2", "Da colorare 3", "Da colorare 4", "Il mio disegno", "Colophon"]
assert len(order) % 2 == 0 and len(order) >= 24

TRIM, BLEED = 8.5, 0.125
fonts = '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">'

interior_css = f"""
@page {{ size: {TRIM+BLEED}in {TRIM+2*BLEED}in; margin: 0 }}
html,body{{margin:0;padding:0;background:#fff;display:block;min-height:0;height:auto}}
.page{{position:relative;width:{TRIM+BLEED}in;height:{TRIM+2*BLEED}in;overflow:hidden;break-after:page;background:#fffaf1}}
.page.art{{background:#eef3ea}} .page.art.white{{background:#fff}}
.pin{{inset:auto;top:{BLEED}in;width:{TRIM}in;height:{TRIM}in;overflow:visible}}
.page.recto .pin{{left:0}} .page.verso .pin{{left:{BLEED}in}}
.page.paper .pin::after{{display:none}}
.full{{inset:auto;top:-{BLEED}in;width:{TRIM+BLEED}in;height:{TRIM+2*BLEED}in;max-width:none}}
.page.recto .full{{left:0}} .page.verso .full{{left:-{BLEED}in}}
.folio{{bottom:5.5cqh}}
.folio.light{{padding-right:6cqw}}
.page.verso .folio.light{{text-align:left;padding-left:6cqw;padding-right:0}}
.tp-siren{{display:none}}
.deco{{top:-6cqh}}
"""

body = []
for i, lab in enumerate(order, start=1):
    p = swap(lab)
    side = "recto" if i % 2 else "verso"
    p = p.replace('<div class="page ', f'<div class="page {side} ', 1)
    body.append(p)
doc = f'<!doctype html><html lang="it"><head><meta charset="utf-8">{fonts}<style>{style}{interior_css}</style></head><body>{"".join(body)}</body></html>'
open(os.path.join(out, "interno.html"), "w", encoding="utf-8").write(doc)

# ---------- Copertina ----------
n = len(order)
spine = round(n * 0.002347, 4)  # carta premium a colori
W = BLEED + TRIM + spine + TRIM + BLEED
Hh = TRIM + 2 * BLEED
cover_css = f"""
@page {{ size: {W}in {Hh}in; margin:0 }}
html,body{{margin:0;padding:0;display:block;min-height:0;height:auto;background:#f4c430}}
.wrap{{position:relative;width:{W}in;height:{Hh}in;overflow:hidden;background:#f4c430}}
.wrap>.page{{position:absolute;top:0;height:{Hh}in}}
.wrap>.backcover{{left:0;width:{BLEED+TRIM+spine/2}in}}
.wrap>.cover{{left:{BLEED+TRIM+spine/2}in;width:{TRIM+BLEED+spine/2}in}}
.backcover .pin{{inset:auto;top:{BLEED}in;left:{BLEED}in;width:{TRIM}in;height:{TRIM}in;overflow:visible}}
.backcover .pin{{background:none}}
.wrap>.backcover{{background:#f4c430 repeating-linear-gradient(135deg,transparent 0 0.77in,rgba(217,71,43,.10) 0.77in 1.1in)}}
.cover .pin{{inset:auto;top:{BLEED}in;left:{spine/2}in;width:{TRIM}in;height:{TRIM}in;overflow:visible;background:none}}
.cover .full{{inset:auto;top:-{BLEED}in;left:-{spine/2}in;width:{TRIM+BLEED+spine/2}in;height:{Hh}in;object-fit:cover;object-position:right center}}
.cover-author{{right:5cqw;bottom:5cqw}}
.back{{padding:8cqh 9cqw 6cqh}}
.barcode-space{{position:absolute;right:.25in;bottom:.25in;width:2in;height:1.2in;background:#fff}}
.b-foot{{align-items:flex-end}}
"""
cdoc = f'<!doctype html><html lang="it"><head><meta charset="utf-8">{fonts}<style>{style}{cover_css}</style></head><body><div class="wrap">{swap("Retro")}{swap("Copertina")}</div></body></html>'
open(os.path.join(out, "copertina.html"), "w", encoding="utf-8").write(cdoc)

open(os.path.join(out,"dims.txt"),"w").write(f"{TRIM+BLEED} {Hh} {W}")
print("pagine", n, "dorso", spine, "copertina", round(W, 4), "x", Hh)
