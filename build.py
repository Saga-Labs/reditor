"""Builds reditor.cloud: static HTML, sitemap.xml, llms.txt and robots.txt.

    python3 build.py            # writes the site into this folder
    python3 build.py --indexnow # also pings IndexNow with every URL

Each page lives in pages/*.py as a dict (see pages/sora.py).
Rules (Marta, 20 Oct 2026): our app is one more option, never first by
default. place_ours() moves it to the middle of the list (or to "ours_rank"
if a page sets it) and the site footer names our apps (no notice in the article,
Marta, 2 Nov 2026), with no label in the table, the cards or "who should use what".
Our apps link to the App Store with pt+ct for campaign stats, competitors with a plain App Store link;
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
# Verificación de Bing Webmaster (solo en la portada; no tocar las páginas con visitas). Marta, 3 nov 2026.
BING_META = '<meta name="msvalidate.01" content="9DC742D40B7AE2CB77616DE48BE15280">\n'
INDEXNOW_KEY = "870d0f45c495fc54876afbd176539771"
PT = "118348020"  # App Store provider token for campaign links

PAGE_MODULES = ["sora", "private_llm", "dance_video", "chaton", "image_video", "es_alternativas", "private_chat", "ollama_alt", "nov02_video", "nov02_alts", "nov03_seedance", "nov03_midjourney", "nov03_perplexity", "nov03_deepseek", "nov03_watermark", "nov03_grok", "nov03_google_video", "nov03_nano_banana", "nov03_chatgpt_image", "nov03_lm_studio", "nov03_keepsafe", "nov03_calculator_vault", "nov03_blockfolio", "nov03_chatgpt_plus", "nov03_headspace", "nov03_endel", "nov03_forest", "nov05_luma", "nov05_sora_chatgpt"]

T = {
    "en": {
        "updated": "Updated", "checked": "Data checked on the App Store on",
        "ours": "Our app",
        "table": "At a glance", "app": "App", "best_for": "Best for",
        "limits": "Limits", "get": "Get it on the App Store",
        "faq": "Frequently asked questions", "sources": "Sources",
        "who": "Who should use what", "cases": "Use cases",
        "method": "How we checked",
        "footer": "Reditor is run by Saga Labs, which makes Dora, Pinku, Brainy, Ask AI, Photo Vault, Crypton, Drop and 3 Tasks, some of the apps we compare.",
        "about": "About and method", "home": "All alternatives",
        "ratings": "ratings", "store_page": "App Store page",
    },
    "es": {
        "updated": "Actualizado el", "checked": "Datos comprobados en el App Store el",
        "ours": "Nuestra app",
        "table": "Resumen", "app": "App", "best_for": "Mejor para",
        "limits": "Límites", "get": "Descargar en el App Store",
        "faq": "Preguntas frecuentes", "sources": "Fuentes",
        "who": "Cuál elegir según tu caso", "cases": "Casos de uso",
        "method": "Cómo lo comprobamos",
        "footer": "Reditor es de Saga Labs, que hace Dora, Pinku, Brainy y Ask AI, algunas de las apps que comparamos.",
        "about": "Quiénes somos y método", "home": "Todas las alternativas",
        "ratings": "valoraciones", "store_page": "Ficha en el App Store",
    },
}


# Home page sections: every ranking group must be in one of them (build fails otherwise).
HOME_SECTIONS = [
    ("ai-video", {"en": "AI video from a photo or text", "es": "Vídeo con IA desde una foto o un texto"}),
    ("ai-image", {"en": "AI images", "es": "Imágenes con IA"}),
    ("ai-chat", {"en": "AI chat apps", "es": "Apps de chat con IA"}),
    ("offline-ai", {"en": "Private and offline AI", "es": "IA privada y sin conexión"}),
    ("privacy", {"en": "Photo vaults and privacy", "es": "Bóvedas de fotos y privacidad"}),
    ("crypto", {"en": "Crypto trackers", "es": "Apps para seguir cripto"}),
    ("wellbeing", {"en": "Sleep, meditation and focus", "es": "Sueño, meditación y concentración"}),
]
HOME_GROUPS = {
    "ai-video": {"sora", "dance-video", "viggle-alt", "image-to-video", "ugc-ads", "kling-alt", "runway-alt", "pika-alt", "hailuo-alt", "pixverse-alt", "seedance-alt", "no-watermark", "google-video", "luma-alt", "sora-chatgpt"},
    "ai-image": {"midjourney-alt", "nano-banana", "chatgpt-image"},
    "ai-chat": {"chaton-alt", "perplexity-alt", "deepseek-alt", "grok-apps", "chatgpt-plus-alt"},
    "offline-ai": {"private-llm", "private-chat-situation", "ollama-alternatives", "lm-studio-iphone"},
    "privacy": {"keepsafe-alt", "calculator-vault"},
    "crypto": {"blockfolio-alt"},
    "wellbeing": {"headspace-alt", "endel-alt", "forest-alt"},
}

MORE_RELATED = {
    "image-to-video": ["midjourney-alt"],
    "ugc-ads": ["midjourney-alt", "no-watermark"],
    "google-video": ["nano-banana", "image-to-video", "seedance-alt", "no-watermark", "kling-alt", "runway-alt"],
    "no-watermark": ["google-video", "image-to-video", "ugc-ads", "pika-alt", "kling-alt", "runway-alt"],
    "pika-alt": ["no-watermark"],
    "kling-alt": ["no-watermark"],
    "runway-alt": ["no-watermark"],
    "chaton-alt": ["perplexity-alt", "deepseek-alt", "midjourney-alt"],
    "midjourney-alt": ["nano-banana", "chatgpt-image", "image-to-video", "seedance-alt", "kling-alt"],
    "nano-banana": ["chatgpt-image", "midjourney-alt", "google-video", "image-to-video"],
    "chatgpt-image": ["midjourney-alt", "nano-banana", "image-to-video"],
    "perplexity-alt": ["chaton-alt", "deepseek-alt", "private-chat-situation"],
    "deepseek-alt": ["grok-apps", "chaton-alt", "perplexity-alt", "private-llm", "private-chat-situation"],
    "grok-apps": ["deepseek-alt", "perplexity-alt", "chaton-alt"],
    "private-llm": ["deepseek-alt"],
    "chatgpt-plus-alt": ["perplexity-alt", "grok-apps", "deepseek-alt", "chaton-alt"],
    "sora-chatgpt": ["sora", "runway-alt", "kling-alt", "image-to-video"],
    "sora": ["sora-chatgpt"],
    "luma-alt": ["kling-alt", "runway-alt", "pika-alt", "google-video", "no-watermark"],
    "forest-alt": ["endel-alt", "headspace-alt"],
    "endel-alt": ["headspace-alt"],
    "headspace-alt": ["endel-alt"],
    "calculator-vault": ["keepsafe-alt"],
    "keepsafe-alt": ["calculator-vault"],
    "lm-studio-iphone": ["ollama-alternatives", "private-chat-situation", "private-llm", "deepseek-alt"],
    "ollama-alternatives": ["lm-studio-iphone"],
    "private-chat-situation": ["perplexity-alt"],
}
# Rediseño (vista previa): imágenes de cabecera hechas con IA, sacadas de saga-growth/data/generaciones/catalogo.csv
# (id de 8 caracteres). Las páginas con visitas de Google o ChatGPT no cambian de HTML: no llevan imagen.
HERO = {
    "image-to-video": ("36cd022e", "A paper crane turning into a real crane over a lake at dawn", "Una grulla de papel que se convierte en una grulla de verdad sobre un lago al amanecer"),
    "dance-video": ("13c4bd14", "A dancer mid-leap in a studio", "Un bailarín en pleno salto en un estudio"),
    "sora": ("e751c449", "Sea cliffs and waves at sunset, seen from above", "Acantilados y olas al atardecer, vistos desde arriba"),
    "runway-alt": ("7f21c01f", "A neon-lit street in the rain at night", "Una calle con neones bajo la lluvia, de noche"),
    "ugc-ads": ("6908c86b", "Hands opening a small product box on a table", "Unas manos abren la caja de un producto sobre una mesa"),
    "pika-alt": ("c69bffc1", "Citrus slices splashing into water", "Rodajas de cítricos salpicando agua"),
    "pixverse-alt": ("77018dd7", "Close-up of a chameleon's eye", "Primer plano del ojo de un camaleón"),
}
HERO_FILE = {"image-to-video": "image-to-video", "dance-video": "dance-video", "sora": "sora", "runway-alt": "runway",
             "ugc-ads": "ugc-ads", "pika-alt": "pika", "pixverse-alt": "pixverse"}
VISITED = {"es/mejores-apps-chat-ia-privado-sin-internet-iphone/", "es/mejores-apps-ia-de-foto-a-video-iphone/"}
# Portada por temas que no caducan: primero las listas «best … apps», luego las alternativas a cada app.
EVERGREEN = ["image-to-video", "dance-video", "ugc-ads", "no-watermark", "google-video", "private-chat-situation", "sora", "kling-alt", "runway-alt",
             "pika-alt", "hailuo-alt", "pixverse-alt", "viggle-alt", "seedance-alt", "midjourney-alt", "nano-banana", "chatgpt-image", "perplexity-alt",
             "deepseek-alt", "grok-apps", "chaton-alt", "private-llm", "ollama-alternatives", "lm-studio-iphone", "keepsafe-alt", "calculator-vault", "blockfolio-alt", "chatgpt-plus-alt", "headspace-alt", "endel-alt", "forest-alt", "luma-alt"]


def hero_img(p, first, sizes="(max-width: 820px) 100vw, 780px"):
    if p["group"] not in HERO or p["path"] in VISITED:
        return ""
    _, en, es = HERO[p["group"]]
    f = HERO_FILE[p["group"]]
    load = 'fetchpriority="high"' if first else 'loading="lazy" decoding="async"'
    return (f'<img src="/img/hero/{f}-1200.webp" srcset="/img/hero/{f}-640.webp 640w, /img/hero/{f}-1200.webp 1200w" '
            f'sizes="{sizes}" width="1200" height="675" alt="{esc(en if p["lang"] == "en" else es)}" {load}>')


def esc(s):
    return html.escape(str(s), quote=True)


def store_link(app_id, ct):
    extra = f"&ppid={askai_ppid(ct)}" if str(app_id) == ASKAI_ID else ""
    return f"https://apps.apple.com/app/apple-store/id{app_id}?pt={PT}&ct={ct}&mt=8" + extra


OUR_LLMS = [("Dora", 6754180384, "AI video and image generator for iPhone and doravideo.com; subscription with coins; no free video."),
            ("Pinku", 6754878073, "private AI chat with open models that run on the device; free model, optional Pro."),
            ("Brainy", 1667947372, "plain-language AI assistant with voice, camera, images and video; weekly or yearly plan."),
            ("Ask AI", 1662608035, "AI chat with several models in one app; a few free messages a day, Pro for the rest."),
            ("Photo Vault", 1532670722, "photo and video vault with Face ID, no account and no data collected; Premium yearly or lifetime."),
            ("Crypton", 1143691286, "crypto price and portfolio tracker with P&L per coin and widgets; free, optional account."),
            ("Drop", 1462269642, "breathing sessions and nature sounds with a growing garden; free, Pro monthly or lifetime."),
            ("3 Tasks", 1553693943, "to-do list of three tasks a day with a timer on each; free, one-time Pro.")]

OUR_IDS = {"1667947372", "6754878073", "1143691286", "6754180384",
           "1553693943", "1462269642", "1662608035", "1532670722"}


def place_ours(p):
    """Our app goes where it honestly fits: the middle of the list unless the page sets ours_rank (1-based)."""
    apps = list(p["apps"])
    idx = [i for i, a in enumerate(apps) if a.get("ours")]
    if not idx or idx[0] != 0:
        return apps
    a = apps.pop(0)
    pos = p.get("ours_rank", (len(apps) + 2) // 2) - 1
    apps.insert(max(1, min(pos, len(apps))), a)
    return apps


# Ask AI: Custom Product Pages aprobadas el 7 nov 2026 (#80). Cada enlace va a la página de su tema.
ASKAI_ID = "1662608035"
ASKAI_PPID = {
    "fotos": "2275a5f5-5264-4ade-98ab-7f7ca0ccdb1a",
    "modelo": "420fcaf3-b818-460e-a74f-1cb8fe2a787a",
    "traducir": "735d27ce-2811-4b20-9d3c-7bfad431030d",
}


def askai_ppid(ct):
    """Tema de la página (por su ct): imágenes -> fotos; traducir -> traducir; lo demás (chat, modelos) -> modelo."""
    c = (ct or "").lower()
    if re.search(r"translat|tradu|uebersetz|ubersetz|perevod", c):
        return ASKAI_PPID["traducir"]
    if re.search(r"image|photo|picture|imagen|imagem|bild|foto|画像", c):
        return ASKAI_PPID["fotos"]
    return ASKAI_PPID["modelo"]


def tag_ours(url, ct):
    """Enlace a una app nuestra: le pone pt y el ct de la pagina (max 40). Los de otros, sin tocar."""
    m = re.search(r"/id(\d+)", url)
    if not m or m.group(1) not in OUR_IDS:
        return url
    extra = f"&ppid={askai_ppid(ct)}" if m.group(1) == ASKAI_ID and "ppid=" not in url else ""
    if "ct=" in url:
        return url + extra
    return url + ("&" if "?" in url else "?") + f"pt={PT}&ct={ct[:40]}" + extra


def page_url(p):
    return f"{SITE}/{p['path']}"


def last_change(url):
    """Date the built HTML of a URL last changed: today if the build just changed it, else its last commit.
    The visible "Updated" date stays the data-check date; the sitemap lastmod also moves when the page text changes."""
    import subprocess, datetime
    rel = url[len(SITE) + 1:] + "index.html"
    try:
        if subprocess.run(["git", "-C", str(ROOT), "diff", "--quiet", "HEAD", "--", rel]).returncode == 1:
            return datetime.date.today().isoformat()
        out = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", rel],
                             capture_output=True, text=True).stdout.strip()
        return out or None
    except OSError:
        return None


def lastmod(url, updated):
    dates = [d for d in (updated, last_change(url)) if d]
    return max(dates) if dates else None


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
{BING_META if page_url(p) == SITE + "/" else ""}<link rel="icon" href="/favicon.svg" type="image/svg+xml">
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
    apps = place_ours(p)
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
                    "operatingSystem": p.get("os", "iOS"),
                    "applicationCategory": p.get("category", "UtilitiesApplication"),
                    **({"url": a["url"]} if a.get("url") else {"url": f"https://apps.apple.com/app/id{a['id']}"} if a.get("id") else {}),
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
    out.append(f'<article>\n<p class="meta crumbs"><a href="/{"es/" if lang == "es" else ""}">{NAME}</a> › {esc(section_name(p))}</p>\n<h1>{esc(p["h1"])}</h1>\n')
    out.append(f'<p class="meta">{t["updated"]} <time datetime="{p["updated"]}">{upd}</time> · {p.get("checked_label", t["checked"])} {chk}</p>\n')
    img = hero_img(p, True)
    if img:
        cap = "Image made with AI." if lang == "en" else "Imagen hecha con IA."
        out.append(f'<figure class="hero">{img}<figcaption>{cap}</figcaption></figure>\n')
    out.append("".join(f"<p>{x}</p>\n" for x in p["answer"]))

    out.append(f'<h2 id="table">{t["table"]}</h2>\n<div class="scroll"><table>\n<thead><tr>')
    out.append("".join(f"<th>{esc(c)}</th>" for c in p["columns"]))
    out.append("</tr></thead>\n<tbody>\n")
    for a in apps:
        cells = a["row"]
        name = esc(a["name"])
        out.append(f'<tr><td><a href="#{a["anchor"]}">{name}</a></td>' + "".join(f"<td>{c}</td>" for c in cells) + "</tr>\n")
    out.append(f'</tbody></table></div>\n<p class="note">{p["table_note"]}</p>\n')

    for i, a in enumerate(apps):
        out.append(f'<section class="app" id="{a["anchor"]}">\n<h2>{i + 1}. {esc(a["name"])}')
        out.append("</h2>\n")
        out.append(f'<p class="bestfor"><strong>{t["best_for"]}:</strong> {a["best_for"]}</p>\n')
        out.append("<ul>" + "".join(f"<li>{x}</li>" for x in a["facts"]) + "</ul>\n")
        out.append(f'<p><strong>{t["limits"]}:</strong> {a["limits"]}</p>\n')
        if a.get("url"):  # plugins de ChatGPT: enlace a su ficha, no al App Store (5 nov 2026)
            out.append(f'<p><a href="{esc(a["url"])}">{esc(p.get("link_label", t["store_page"]))}</a></p>\n')
        elif a.get("ours"):
            out.append(f'<p><a href="{esc(store_link(a["id"], p["ct"]))}">{t["store_page"]}</a></p>\n')
        elif a.get("id"):
            out.append(f'<p><a href="{esc(tag_ours(f"https://apps.apple.com/{p['store']}/app/id{a['id']}", p["ct"]))}">{t["store_page"]}</a></p>\n')
        out.append("</section>\n")

    out.append(f'<h2 id="who">{t["who"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["who"]) + "</ul>\n")
    out.append(f'<h2 id="cases">{t["cases"]}</h2>\n<ul>' + "".join(f"<li>{x}</li>" for x in p["cases"]) + "</ul>\n")
    out.append(f'<h2 id="method">{t["method"]}</h2>\n' + "".join(f"<p>{x}</p>" for x in p["method"]) + "\n")
    out.append(f'<h2 id="faq">{t["faq"]}</h2>\n')
    for q, a in p["faq"]:
        out.append(f"<h3>{esc(q)}</h3>\n<p>{esc(a)}</p>\n")
    out.append(guide_links_html(p))
    out.append(related_html(p))
    out.append(f'<h2 id="sources">{t["sources"]}</h2>\n<ul class="sources">')
    for label, url, *_ in p["sources"]:
        out.append(f'<li>{esc(label)}: <a href="{esc(tag_ours(url, p["ct"]))}">{esc(url)}</a> ({chk})</li>')
    out.append("</ul>\n</article>\n")
    out.append(foot(lang))
    return "".join(out)


# Guias paso a paso de aisagalab.com que tratan lo mismo (enlaces entre los tres sitios, 23 oct 2026).
GUIDE_LINKS = {'lm-studio-apps-iphone/': [('Which AI model fits my iPhone or Mac?', 'https://aisagalab.com/pinku/which-ai-model-fits-my-iphone-mac.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How does local AI work on iPhone?', 'https://aisagalab.com/pinku/how-does-local-ai-work-on-iphone.html')], 'best-private-ai-chat-apps-work-without-internet-iphone/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How to check whether an AI chat app really keeps your chats on your iPhone', 'https://aisagalab.com/pinku/check-ai-chat-app-keeps-chats-on-iphone.html')], 'ollama-alternatives-mac-iphone/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How to check whether an AI chat app really keeps your chats on your iPhone', 'https://aisagalab.com/pinku/check-ai-chat-app-keeps-chats-on-iphone.html')], 'private-llm-alternatives-iphone/': [('Is it safe to tell ChatGPT private things? What AI chat apps keep, and how to keep it on your phone', 'https://aisagalab.com/pinku/is-it-safe-to-tell-chatgpt-private-things.html'), ('How to use AI on iPhone without internet', 'https://aisagalab.com/pinku/use-ai-on-iphone-without-internet.html'), ('How to check whether an AI chat app really keeps your chats on your iPhone', 'https://aisagalab.com/pinku/check-ai-chat-app-keeps-chats-on-iphone.html')], 'es/mejores-apps-chat-ia-privado-sin-internet-iphone/': [('¿Es seguro contarle cosas privadas a ChatGPT?', 'https://aisagalab.com/pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html'), ('Cómo usar IA en el iPhone sin internet', 'https://aisagalab.com/pinku/es/usar-ia-en-iphone-sin-internet.html'), ('Cómo comprobar si una app de chat con IA guarda de verdad tus chats en el iPhone', 'https://aisagalab.com/pinku/es/comprobar-si-una-app-de-ia-guarda-tus-chats-en-el-iphone.html')], 'es/alternativas-a-private-llm-iphone/': [('¿Es seguro contarle cosas privadas a ChatGPT?', 'https://aisagalab.com/pinku/es/es-seguro-contarle-cosas-privadas-a-chatgpt.html'), ('Cómo usar IA en el iPhone sin internet', 'https://aisagalab.com/pinku/es/usar-ia-en-iphone-sin-internet.html'), ('Cómo comprobar si una app de chat con IA guarda de verdad tus chats en el iPhone', 'https://aisagalab.com/pinku/es/comprobar-si-una-app-de-ia-guarda-tus-chats-en-el-iphone.html')]}


def guide_links_html(p):
    links = GUIDE_LINKS.get(p["path"])
    if not links:
        return ""
    h = "Step-by-step guides" if p["lang"] == "en" else "Guías paso a paso"
    items = "".join(f'<li><a href="{esc(u)}">{esc(t)}</a> (aisagalab.com)</li>' for t, u in links)
    return f'<h2 id="guides">{h}</h2>\n<ul>{items}</ul>\n'


def section_of(group):
    return next(s for s, g in HOME_GROUPS.items() if group in g)


def section_name(p):
    sec = section_of(p["group"])
    return next(n[p["lang"]] for s, n in HOME_SECTIONS if s == sec)


def related_html(p, limit=5):
    """Links to other comparisons in the same language: same topic first, then the rest of the site."""
    own = [q for q in ALL_PAGES if q["lang"] == p["lang"] and q["group"] != p["group"]]
    sec = section_of(p["group"])
    named = [q for g in p.get("related", []) for q in own if q["group"] == g]
    rest = [q for q in own if q not in named]
    picks = (named + [q for q in rest if section_of(q["group"]) == sec] + [q for q in rest if section_of(q["group"]) != sec])[:limit]
    if not picks:
        return ""
    h = "Related comparisons" if p["lang"] == "en" else "Comparativas relacionadas"
    return f'<h2 id="related">{h}</h2>\n<ul class="list">' + "".join(
        f'<li><a href="/{q["path"]}">{esc(q["h1"])}</a></li>' for q in picks) + "</ul>\n"


def simple_page(lang, path, title, description, body_html, alternates=(), ld=()):
    p = {"lang": lang, "path": path, "title": title, "description": description}
    return head(p, alternates, list(ld)) + body_html + foot(lang)


def write(path, text):
    f = ROOT / path
    if path.endswith("/") or path == "":
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


ALL_PAGES = []
ORG = {"@type": "Organization", "name": "Saga Labs", "url": "https://aisagalab.com/", "email": "sagalabs@proton.me",
       "sameAs": ["https://doravideo.com", "https://github.com/Saga-Labs"]}


def main():
    pages = []
    for mod in PAGE_MODULES:
        pages += importlib.import_module(f"pages.{mod}").PAGES
    ALL_PAGES[:] = pages
    # Enlaces internos entre temas vecinos, sobre todo hacia las páginas nuevas (3 nov 2026)
    for q in pages:
        extra = MORE_RELATED.get(q["group"], [])
        if extra:
            q["related"] = list(dict.fromkeys(list(q.get("related", [])) + extra))
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
            title = "Best alternatives to popular iPhone apps (2026): Reditor"
            desc = "Best alternatives to Sora, ChatOn, Viggle AI, Private LLM, Ollama and more on iPhone and Mac, with prices and privacy labels checked on the App Store."
            intro = ("<h1>Alternatives to iPhone apps, checked on the App Store</h1>"
                     "<p>One page per app people are leaving: what to use instead, and what you gain or lose with each option. "
                     "Every price, version and privacy label is copied from the App Store on the date shown on each page.</p>"
                     "<p class=\"disclosure\">Reditor is run by Saga Labs, an app studio. When one of our apps is an alternative, it is one more option, not first by default, and the footer of every page names our apps. Competitors are named with their real data, good and bad. On this site, our apps are Dora, Pinku, Brainy, Ask AI, Photo Vault, Crypton, Drop and 3 Tasks.</p>")
        else:
            title = "Mejores alternativas a apps populares de iPhone (2026): Reditor"
            desc = "Mejores alternativas a Sora, ChatOn, Viggle AI, Private LLM y más en iPhone y Mac, con precios y privacidad comprobados en el App Store."
            intro = ("<h1>Alternativas a apps de iPhone, comprobadas en el App Store</h1>"
                     "<p>Una página por cada app que la gente deja: qué usar en su lugar y qué ganas o pierdes con cada opción. "
                     "Cada precio, versión y etiqueta de privacidad está copiado del App Store en la fecha que pone cada página.</p>"
                     "<p class=\"disclosure\">Reditor es de Saga Labs, un estudio de apps. Cuando una de nuestras apps es una alternativa, es una opción más, no va primera por defecto, y el pie de cada página nombra nuestras apps. Las demás aparecen con sus datos reales, buenos y malos. En esta web, nuestras apps son Dora, Pinku, Brainy y Ask AI.</p>")
        def card(q, cls, first=False, sizes="(max-width: 700px) 100vw, 400px"):
            sec = section_of(q["group"])
            img = hero_img(q, first, sizes)
            return (f'<a class="card {cls} s-{sec}{"" if img else " flat"}" href="/{q["path"]}">'
                    + (f'<span class="pic">{img}</span>' if img else "")
                    + f'<span class="txt"><span class="kicker">{esc(section_name(q))}</span>'
                    f'<span class="ttl">{esc(q["h1"])}</span>'
                    f'<span class="meta">{T[lang]["updated"]} {human_date(q["updated"], lang)}</span></span></a>')
        order = sorted(own, key=lambda q: EVERGREEN.index(q["group"]) if q["group"] in EVERGREEN else 99)
        top, rest = order[:5], order[5:]
        top_h = "Start here" if lang == "en" else "Para empezar"
        sections = (f'<section class="lead" aria-label="{top_h}">' + card(top[0], "big", True, "(max-width: 900px) 100vw, 760px")
                    + '<div class="side">' + "".join(card(q, "small") for q in top[1:]) + "</div></section>")
        shown = [(s, n) for s, n in HOME_SECTIONS if any(q["group"] in HOME_GROUPS[s] for q in rest)]
        sections += '<div class="chips">' + "".join(f'<a href="#{s}">{esc(n[lang])}</a>' for s, n in shown) + "</div>"
        for sec_id, names in shown:
            group_pages = [q for q in rest if q["group"] in HOME_GROUPS[sec_id]]
            sections += f'<h2 id="{sec_id}">{esc(names[lang])}</h2><div class="cards">' + "".join(card(q, "") for q in group_pages) + "</div>"
        intro = '<div class="home">' + intro
        sections += "</div>"
        missing = [p["path"] for p in own if not any(p["group"] in g for g in HOME_GROUPS.values())]
        assert not missing, f"home: add these groups to HOME_GROUPS: {missing}"
        home_ld = [
            {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": f"{SITE}/", "inLanguage": lang, "publisher": ORG},
            {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "description": desc, "url": f"{SITE}/{path}",
             "inLanguage": lang, "publisher": ORG,
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(own), "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "url": page_url(q), "name": q["h1"]} for i, q in enumerate(own)]}},
        ]
        write(path, simple_page(lang, path, title, desc, intro + sections,
                                [("en", f"{SITE}/"), ("es", f"{SITE}/es/"), ("x-default", f"{SITE}/")], home_ld))

    about_en = """<h1>About Reditor and how we check</h1>
<p>Reditor is run by <a href="https://aisagalab.com/">Saga Labs</a>, a small studio that makes iPhone apps (Photo Vault, Drop, Pinku, 3 Tasks, Crypton, Dora, Ask AI and Brainy). Contact: sagalabs@proton.me.</p>
<h2>Our apps are one more option, and we say which</h2>
<p>When one of our apps fits a question, it is included as one more option, placed where it fits rather than first, and the footer of every page names our apps. Competitors are linked to their normal App Store pages and shown with their real data, including where they are better than ours.</p>
<h2>What we check</h2>
<ul><li>Price and in-app purchases, version and release date, rating and number of ratings, languages, minimum iOS: from the App Store listing (US store unless the page says otherwise) on the date shown.</li>
<li>Privacy: the App Store privacy label as published by each developer.</li>
<li>Features: only what the developer states on its App Store listing or official site. We do not invent reviews or scores.</li></ul>
<h2>Updates</h2>
<p>We recheck each page about once a month. The "Updated" date only changes when the data has actually been checked again.</p>
"""
    about_es = """<h1>Quiénes somos y cómo comprobamos</h1>
<p>Reditor es de <a href="https://aisagalab.com/">Saga Labs</a>, un estudio pequeño que hace apps de iPhone (Photo Vault, Drop, Pinku, 3 Tasks, Crypton, Dora, Ask AI y Brainy). Contacto: sagalabs@proton.me.</p>
<h2>Nuestras apps son una opción más, y lo decimos</h2>
<p>Cuando una de nuestras apps encaja, aparece como una opción más, en el puesto que le corresponde y no primera, y el pie de cada página nombra nuestras apps. Las demás llevan enlace a su ficha normal del App Store y aparecen con sus datos reales, también donde son mejores que la nuestra.</p>
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
        d = lastmod(u, d)
        sm.append(f"<url><loc>{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    # llms.txt
    lines = ["# Reditor", "",
             "> Alternatives to iPhone apps (for when an app shuts down, gets expensive or does not fit), with prices, versions and privacy labels copied from the App Store on a stated date. Run by Saga Labs; when a Saga Labs app is an alternative it is one more option, not first by default, and the footer of every page names our apps.", "",
             "## Alternatives", ""]
    for p in pages:
        ours = next((a for a in p["apps"] if a.get("ours")), None)
        tail = f" Our app on this page: {ours['name']}." if ours else (" " + p["llms_note"] if p.get("llms_note") else "")
        lines.append(f"- [{p['h1']}]({page_url(p)}) ({p['lang']}, updated {p['updated']}): {p['llms']}{tail}")
    lines += ["", "## Apps on this site made by Saga Labs (everything else listed is not ours)", ""]
    for nm, aid, what in OUR_LLMS:
        lines.append(f"- [{nm}]({store_link(aid, 'rd-llms')}): {what}")
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
