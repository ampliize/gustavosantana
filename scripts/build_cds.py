"""Gera a lista CDS (os 6 mais recentes) do index.html a partir dos dados lidos do Sua Música.

Uso: python3 scripts/build_cds.py <next.json do perfil> <covers.json dos álbuns>
As capas ficam em assets/capas/<slug>.webp (500px quando disponível).
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
profile = json.load(open(sys.argv[1]))["props"]["pageProps"]
covers = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}

NAMES = {
    "puro-sentimento-gustavo-santana": "Puro Sentimento",
    "esquema-cafajeste-gustavo-santana": "Esquema Cafajeste",
    "repertorio-fim-de-ano-gustavo-santana": "Repertório Fim de Ano",
    "tudo-vira-arrocha-5-0-gustavo-santana": "Tudo Vira Arrocha 5.0",
    "brega-y-funk-gustavo-santana": "Brega y Funk",
    "gustavo-santana-tudo-vira-arrocha-4-0": "Tudo Vira Arrocha 4.0",
    "gustavo-santana-tudo-vira-arrocha-3-0": "Tudo Vira Arrocha 3.0",
    "gustavo-santana-tudo-vira-arrocha-2": "Tudo Vira Arrocha 2",
    "gustavo-santana-promocional-de-junho": "Promocional de Junho",
    "gustavo-santana-tudo-vira-arrocha": "Tudo Vira Arrocha",
    "uma-dose-com-o-gustavo": "Uma Dose com o Gustavo",
    "gustavo-santana-pra-beber-e-se-apaixonar-2-0": "Pra Beber e Se Apaixonar 2.0",
}

albums = {}
for a in profile["userAlbums"] + profile["userTops"]:
    albums.setdefault(a["slug"], a)
# ordem: do mais novo para o mais antigo (id do álbum cresce com o tempo)
rows = []
for slug, a in sorted(albums.items(), key=lambda kv: -kv[1]["id"]):
    c = covers.get(slug, {})
    img = "assets/capas/" + slug + ".webp"
    if slug == "puro-sentimento-gustavo-santana":
        img = "assets/disco-puro-sentimento.webp"
    rows.append({
        "slug": slug, "title": NAMES.get(slug, a["title"].title()),
        "plays": c.get("plays", a["plays"]), "downloads": c.get("downloads", a["downloads"]),
        "date": (c.get("date") or a.get("sendDate") or "")[:10],
        "faixas": len(c["files"]) if c.get("files") else None, "img": img,
    })

LIMITE = 6  # só os CDs mais recentes
rows = rows[:LIMITE]

js = "const CDS = [\n" + "".join("  " + json.dumps(r, ensure_ascii=False) + ",\n" for r in rows) + "]"
html = (ROOT / "index.html").read_text()
html = re.sub(r"/\*CDS\*/.*?/\*/CDS\*/", lambda m: "/*CDS*/\n" + js + "\n/*/CDS*/", html, flags=re.S)
(ROOT / "index.html").write_text(html)
print(len(rows), "CDs")
