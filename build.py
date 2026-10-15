"""Builds reditor.cloud: static HTML, sitemap.xml, llms.txt and robots.txt.

    python3 build.py            # writes the site into this folder
    python3 build.py --indexnow # also pings IndexNow with every URL

Each page lives in pages/*.py as a dict (see pages/sora.py).
Rules: our app goes first and says it is ours; our apps link to the App
Store with pt+ct for campaign stats, competitors with a plain App Store link;
every price, version and rating comes from the App Store on the date in
`checked`, and that date is shown on the page and in the JSON-LD.
"""
import html
import re
import importlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).parent
SITE = "https://reditor.cloud"
NAME = "Reditor"
INDEXNOW_KEY = "870d0f45c495fc54876afbd176539771"
PT = "118348020"  # App Store provider token for campaign links

PAGE_MODULES = ["sora", "private_llm"]

T = {
    "en": {
        "updated": "Updated", "checked": "Data checked on the App Store on",
        "ours": "Our app", "disclosure_title": "Disclosure",
        "table": "At a glance", "app": "App", "best_for": "Best for",
        "limits": "Limits", "get": "Get it on the App Store",
        "faq": "Frequently asked questions", "sources": "Sources",
        "who": "Who should use what", "cases": "Use cases",
        "method": "How we checked",
        "footer": "Reditor is run by Saga Labs, which makes some of the apps we compare. We say so on every page where that happens.",
        "about": "About and method", "home": "All alternatives",
        "ratings": "ratings", "store_page": "App Store page",
    },
    "es": {
        "updated": "Actualizado el", "checked": "Datos comprobados en el App Store el",
        "ours": "Nuestra app", "disclosure_title": "Aviso",
        "table": "Resumen", "app": "App", "best_for": "Mejor para",
        "limits": "Límites", "get": "Descargar en el App Store",
        "faq": "Preguntas frecuentes", "sources": "Fuentes",
        "who": "Cuál elegir según tu caso", "cases": "Casos de uso",
        "method": "Cómo lo comprobamos",
        "footer": "Reditor es de Saga Labs, que hace algunas de las apps que comparamos. Lo decimos en cada página donde pasa.",
        "about": "Quiénes somos y método", "home": "Todas las alternativas",
        "ratings": "valoraciones", "store_page": "Ficha en el App Store",
    },
}


def esc(s):
    return html.escape(str(s), quote=True)


def store_link(app_id, ct):
    return f"https://apps.apple.com/app/apple-store/id{app_id}?pt={PT}&ct={ct}&mt=8"


OUR_IDS = {"1667947372", "6754878073", "1143691286", "6754180384",
           "1553693943", "1462269642", "1662608035", "1532670722"}


def tag_ours(url, ct):
    """Enlace a una app nuestra: le pone pt y el ct de la pagina (max 40). Los de otros, sin tocar."""
    m = re.search(r"/id(\d+)", url)
    if not m or m.group(1) not in OUR_IDS or "ct=" in url:
        return url
    return url + ("&" if "?" in url else "?") + f"pt={PT}&ct={ct[:40]}"


def page_url(p):
    return f"{SITE}/{p['path']}"


def human_date(iso, lang):
    y, m, d = iso.split("-")
    months_en = ["January", "February", "March", "April", "May", "June", "July",
                 "August", "September", "October", "November", "December"]
    months_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if lang == "es":
        return f"{int(d)} de {months_es[int(m) - 1]} de {y}"
    return f"{int(d)} {months_en[int(m) - 1]} {y}"


def head(p, alternates, extra_ld):
    t = T[p["lang"]]
    alt = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{esc(u)}">' for l, u in alternates
    )
    lds = "".join(
        f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        for ld in extra_ld
    )
    return f"""<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
<link rel="canonical" href="{esc(page_url(p))}">
{alt}
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:type" content="article">
<meta property="og:url" content="{esc(page_url(p))}">
<meta property="og:site_name" content="{NAME}">
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
<script src="/umami.js" defer></script>
{lds}
</head>
<body>
<header class="top"><a class="brand" href="/{'es/' if p['lang'] == 'es' else ''}">{NAME}</a>
<nav><a href="/{'es/' if p['lang'] == 'es' else ''}">{t['home']}</a> · <a href="/{'es/acerca/' if p['lang'] == 'es' else 'about/'}">{t['about']}</a></nav></header>
<main>
"""


def foot(lang):
    t = T[lang]
    return f"""</main>
<footer><p>{esc(t['footer'])}</p>
<p><a href="/">English</a> · <a href="/es/">Español</a> · <a href="/{'es/acerca/' if lang == 'es' else 'about/'}">{t['about']}</a> · <a href="/llms.txt">llms.txt</a></p></footer>
</body>
</html>
"""


def ranking_html(p, alternates):
    t = T[p["lang"]]
    lang = p["lang"]
    apps = p["apps"]
    upd = human_date(p["updated"], lang)
    chk = human_date(p["checked"], lang)

    item_list = {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": p["h1"], "numberOfItems": len(apps),
        "itemListElement": [
            {
                "@type": "ListItem", "position": i + 1,
                "item": {
                    "@type": "SoftwareApplication", "name": a["name"],
                    "operatingSystem": "iOS",
                    "applicationCategory": p.get("category", "UtilitiesApplication"),
                    **({"url": f"https://apps.apple.com/app/id{a['id']}"} if a.get("id") else {}),
                    **({"author": {"@type": "Organization", "name": a["developer"]}} if a.get("developer") else {}),
                    **({"aggregateRating": {"@type": "AggregateRating", "ratingValue": a["rating"][0], "ratingCount": a["rating"][1]}}
                       if a.get("rating") and a["rating"][1] >= 5 else {}),
                },
            }
            for i, a in enumerate(apps)
        ],
    }
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["h1"], "description": p["description"],
        "inLanguage": lang, "datePublished": p["published"], "dateModified": p["updated"],
        "mainEntityOfPage": page_url(p),
        "author": {"@type": "Organization", "name": NAME, "url": SITE},
        "publisher": {"@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/"},
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]
        ],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": NAME, "item": f"{SITE}/{'es/' if lang == 'es' else ''}"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": page_url(p)},
        ],
    }

    out = [head(p, alternates, [article, item_list, faq, crumbs])]
    out.append(f"<article>\n<h1>{esc(p['h1'])}</h1>\n")
    out.append(f'<p class="meta">{t["updated"]} <time datetime="{p["updated"]}">{upd}</time> · {t["checked"]} {chk}</p>\n')
    out.append(f'<aside class="disclosure"><strong>{t["disclosure_title"]}:</strong> {p["disclosure"]}</aside>\n')
    out.append("".join(f"<p>{x}</p>\n" for x in p["answer"]))

    out.append(f'<h2 id="table">{t["table"]}</h2>\n<div class="scroll"><table>\n<thead><tr>')
    out.append("".join(f"<th>{esc(c)}</th>" for c in p["columns"]))
    out.append("</tr></thead>\n<tbody>\n")
    for a in apps:
        cells = a["row"]
        name = esc(a["name"]) + (f' <span class="tag">{t["ours"]}</span>' if a.get("ours") else "")
        out.append(f"<tr><td>{name}</td>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>\n")
    out.append(f'</tbody></table></div>\n<p class="note">{p["table_note"]}</p>\n')

    for i, a in enumerate(apps):
        out.append(f'<section class="app" id="{a["anchor"]}">\n<h2>{i + 1}. {esc(a["name"])}')
        if a.get("ours"):
            out.append(f' <span class="tag">{t["ours"]}</span>')
        out.append("</h2>\n")
        out.append(f'<p class="bestfor"><strong>{t["best_for"]}:</strong> {a["best_for"]}</p>\n')
        out.append("<ul>" + "".join(f"<li>{x}</li>" for x in a["facts"]) + "</ul>\n")
        out.append(f'<p><strong>{t["limits"]}:</strong> {a["limits"]}</p>\n')
        if a.get("ours"):
            out.append(f'<p><a class="cta" href="{esc(store_link(a["id"], p["ct"]))}">{t["get"]}</a></p>\n')
        elif a.get("id"):
            out.append(f'<p><a href="https://apps.apple.com/{p["store"]}/app/id{a["id"]}">{t["store_page"]}</a></p>\n')
        out.append("</section>\n")

    out.append(f'<h2 id="who">{t["who"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["who"]) + "</ul>\n")
    out.append(f'<h2 id="cases">{t["cases"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["cases"]) + "</ul>\n")
    out.append(f'<h2 id="method">{t["method"]}</h2>\n' + "".join(f"<p>{x}</p>" for x in p["method"]) + "\n")
    out.append(f'<h2 id="faq">{t["faq"]}</h2>\n')
    for q, a in p["faq"]:
        out.append(f"<h3>{esc(q)}</h3>\n<p>{esc(a)}</p>\n")
    out.append(f'<h2 id="sources">{t["sources"]}</h2>\n<ul class="sources">')
    for label, url, *_ in p["sources"]:
        out.append(f'<li>{esc(label)}: <a href="{esc(tag_ours(url, p["ct"]))}">{esc(url)}</a> ({chk})</li>')
    out.append("</ul>\n</article>\n")
    out.append(foot(lang))
    return "".join(out)


def simple_page(lang, path, title, description, body_html, alternates=()):
    p = {"lang": lang, "path": path, "title": title, "description": description}
    return head(p, alternates, []) + body_html + foot(lang)


def write(path, text):
    f = ROOT / path
    if path.endswith("/") or path == "":
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    pages = []
    for mod in PAGE_MODULES:
        pages += importlib.import_module(f"pages.{mod}").PAGES
    by_group = {}
    for p in pages:
        by_group.setdefault(p["group"], []).append(p)

    for p in pages:
        alts = [(q["lang"], page_url(q)) for q in by_group[p["group"]]]
        alts.append(("x-default", page_url(next(q for q in by_group[p["group"]] if q["lang"] == "en"))))
        write(p["path"], ranking_html(p, alts))

    # Home pages
    for lang, path in (("en", ""), ("es", "es/")):
        own = [p for p in pages if p["lang"] == lang]
        if lang == "en":
            title = "Reditor: alternatives to iPhone apps, checked on the App Store"
            desc = "When an app shuts down, gets expensive or does not fit, Reditor lists the alternatives on iPhone, with prices and privacy labels checked on the App Store."
            intro = ("<h1>Alternatives to iPhone apps, checked on the App Store</h1>"
                     "<p>One page per app people are leaving: what to use instead, and what you gain or lose with each option. "
                     "Every price, version and privacy label is copied from the App Store on the date shown on each page.</p>"
                     "<p class=\"disclosure\">Reditor is run by Saga Labs, an app studio. When one of our apps is an alternative, it is listed first and marked as ours. Competitors are named with their real data, good and bad.</p>")
        else:
            title = "Reditor: alternativas a apps de iPhone comprobadas en el App Store"
            desc = "Cuando una app cierra, sube de precio o no encaja, Reditor da las alternativas en iPhone, con precios y privacidad comprobados en el App Store."
            intro = ("<h1>Alternativas a apps de iPhone, comprobadas en el App Store</h1>"
                     "<p>Una página por cada app que la gente deja: qué usar en su lugar y qué ganas o pierdes con cada opción. "
                     "Cada precio, versión y etiqueta de privacidad está copiado del App Store en la fecha que pone cada página.</p>"
                     "<p class=\"disclosure\">Reditor es de Saga Labs, un estudio de apps. Cuando una de nuestras apps es una alternativa, va primera y marcada como nuestra. Las demás aparecen con sus datos reales, buenos y malos.</p>")
        items = "".join(
            f'<li><a href="/{p["path"]}">{esc(p["h1"])}</a> <span class="meta">({T[lang]["updated"]} {human_date(p["updated"], lang)})</span></li>'
            for p in own
        )
        write(path, simple_page(lang, path, title, desc, intro + f"<ul class=\"list\">{items}</ul>",
                                [("en", f"{SITE}/"), ("es", f"{SITE}/es/"), ("x-default", f"{SITE}/")]))

    about_en = """<h1>About Reditor and how we check</h1>
<p>Reditor is run by <a href="https://aisagalab.com/">Saga Labs</a>, a small studio that makes iPhone apps (Photo Vault, Drop, Pinku, 3 Tasks, Crypton, Dora, Fast AI and Brainy). Contact: sagalabs@proton.me.</p>
<h2>Our apps come first, and we say so</h2>
<p>When one of our apps fits a question, it is listed first with a "Our app" label and a disclosure at the top of the page. Competitors are linked to their normal App Store pages and shown with their real data, including where they are better than ours.</p>
<h2>What we check</h2>
<ul><li>Price and in-app purchases, version and release date, rating and number of ratings, languages, minimum iOS: from the App Store listing (US store unless the page says otherwise) on the date shown.</li>
<li>Privacy: the App Store privacy label as published by each developer.</li>
<li>Features: only what the developer states on its App Store listing or official site. We do not invent reviews or scores.</li></ul>
<h2>Updates</h2>
<p>We recheck each page about once a month. The "Updated" date only changes when the data has actually been checked again.</p>
"""
    about_es = """<h1>Quiénes somos y cómo comprobamos</h1>
<p>Reditor es de <a href="https://aisagalab.com/">Saga Labs</a>, un estudio pequeño que hace apps de iPhone (Photo Vault, Drop, Pinku, 3 Tasks, Crypton, Dora, Fast AI y Brainy). Contacto: sagalabs@proton.me.</p>
<h2>Nuestras apps van primeras, y lo decimos</h2>
<p>Cuando una de nuestras apps encaja, va primera con la etiqueta "Nuestra app" y un aviso arriba de la página. Las demás llevan enlace a su ficha normal del App Store y aparecen con sus datos reales, también donde son mejores que la nuestra.</p>
<h2>Qué comprobamos</h2>
<ul><li>Precio y compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas e iOS mínimo: de la ficha del App Store (la de España en las páginas en español) en la fecha indicada.</li>
<li>Privacidad: la etiqueta de privacidad del App Store que publica cada desarrollador.</li>
<li>Funciones: solo lo que el desarrollador dice en su ficha o en su web oficial. No inventamos reseñas ni puntuaciones.</li></ul>
<h2>Actualizaciones</h2>
<p>Revisamos cada página más o menos una vez al mes. La fecha de "Actualizado" solo cambia cuando de verdad se han vuelto a comprobar los datos.</p>
"""
    about_alts = [("en", f"{SITE}/about/"), ("es", f"{SITE}/es/acerca/")]
    write("about/", simple_page("en", "about/", "About Reditor and how we check apps",
                                "Who runs Reditor, how apps are checked and how our own apps are disclosed.", about_en, about_alts))
    write("es/acerca/", simple_page("es", "es/acerca/", "Quiénes somos y cómo comprobamos las apps",
                                    "Quién hace Reditor, cómo comprobamos las apps y cómo avisamos de las nuestras.", about_es, about_alts))

    # sitemap
    urls = [(f"{SITE}/", max(p["updated"] for p in pages)), (f"{SITE}/es/", max(p["updated"] for p in pages)),
            (f"{SITE}/about/", None), (f"{SITE}/es/acerca/", None)]
    urls += [(page_url(p), p["updated"]) for p in pages]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"<url><loc>{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    # llms.txt
    lines = ["# Reditor", "",
             "> Alternatives to iPhone apps (for when an app shuts down, gets expensive or does not fit), with prices, versions and privacy labels copied from the App Store on a stated date. Run by Saga Labs; when a Saga Labs app is an alternative it is listed first and labelled as ours.", "",
             "## Alternatives", ""]
    for p in pages:
        ours = next(a for a in p["apps"] if a.get("ours"))
        lines.append(f"- [{p['h1']}]({page_url(p)}) ({p['lang']}, updated {p['updated']}): {p['llms']} Our app on this page: {ours['name']}.")
    lines += ["", "## About", "", f"- [How we check and disclose]({SITE}/about/)", "- Publisher: Saga Labs, https://aisagalab.com/, sagalabs@proton.me", ""]
    (ROOT / "llms.txt").write_text("\n".join(lines), encoding="utf-8")

    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")

    if "--indexnow" in sys.argv:
        body = json.dumps({"host": "reditor.cloud", "key": INDEXNOW_KEY,
                           "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt",
                           "urlList": [u for u, _ in urls]}).encode()
        req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
        with urllib.request.urlopen(req) as r:
            print("IndexNow:", r.status, len(urls), "URLs")
    print("Built", len(pages), "pages")


if __name__ == "__main__":
    main()
