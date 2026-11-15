"""Builds a translated page from an English one (Vaultaire method, 9 Nov 2026).

The translator writes the words (tr_<code>.py: TEXT[group]); this module adds everything that must come from the
App Store of the page's country on the day it is checked: price range in local currency, rating (stars only, never the
number of ratings), version and date. Apps that are not in that country's store are left out and the table note says so.
Our AI apps are never listed or linked for China mainland (cc "cn"): Apple removes unlicensed generative-AI apps there.
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
STORE = json.loads((ROOT / "data" / "store-2026-11-09.json").read_text(encoding="utf-8"))
CHECKED = "2026-11-09"
# Car-screen guide (news page, 14 Nov 2026): its own store file and date; the 9 Nov pages keep theirs.
CAR_STORE = json.loads((ROOT / "data" / "store-2026-11-14.json").read_text(encoding="utf-8"))
CAR_CHECKED = "2026-11-14"
CAR_KEY = {6833951195: "carscreen", 6800211040: "cartv", 6797764175: "cardash", 6756518125: "cartube",
           1665625393: "carconnect", 6755033589: "mycar", 6476621657: "aptv"}
CARSCREEN_ID = 6833951195
# which app id is which key in the store file
KEY = {6754180384: "dora", 6738049229: "kling", 1665024375: "runway", 6767802142: "pixverse", 6745820631: "shots",
       1381206010: "motionleap", 1667947372: "brainy", 1661308505: "chaton", 1658377526: "genie",
       1669007652: "nova", 1660877567: "chatai", 1662608035: "askai"}
AI_OURS = {"dora", "brainy", "askai"}  # plus Pinku, not on these pages


def info(app_id, cc):
    return STORE.get(f"{KEY[app_id]}|{cc}")


# Companion guide (news page, 14 Nov 2026): lookups of 15 Nov 2026 per storefront. Only the name and whether the app is
# on sale in that country are used; the ratings and prices in the text stay as the English page has them.
COMP_STORE = json.loads((ROOT / "data" / "store-companion-2026-11-15.json").read_text(encoding="utf-8"))


def news_app(i, cc):
    """Store entry of an app named in a news guide, for the page's country (the car and companion lookups never share ids)."""
    if i in CAR_KEY:
        return CAR_STORE[f"{CAR_KEY[i]}|{cc}"]
    return COMP_STORE[f"{i}|{cc}"]


def fill_news(s, cc, text, missing):
    """Tokens in news prose: {app:ID} = store link with the store's name (plain name, and noted in the sources, when the
    app is not on sale in that country); {href:ID} = that store's URL; {rating:ID} = stars or the 'no rating' word."""
    def app(m):
        i = int(m.group(1))
        d = news_app(i, cc)
        if not d.get("avail", True):
            missing.add(i)
            return html.escape(COMP_STORE[f"{i}|us"]["name"], quote=False)
        name = html.escape(d["name"], quote=False)
        if i == CARSCREEN_ID:
            return f'<a href="{{CARSCREEN}}">{name}</a>'
        return f'<a href="https://apps.apple.com/{cc}/app/id{i}">{name}</a>'

    def href(m):
        return f"https://apps.apple.com/{cc}/app/id{m.group(1)}"

    def rating(m):
        d = news_app(int(m.group(1)), cc)
        if not d.get("rating"):
            return text["no_rating"]
        return f"{d['rating']:.1f}".replace(".", text["decimal"])

    s = re.sub(r"\{app:(\d+)\}", app, s)
    s = re.sub(r"\{href:(\d+)\}", href, s)
    return re.sub(r"\{rating:(\d+)\}", rating, s)


def localize_news(base, lang, L, text):
    """News guide (no price table): the words come from tr_<code>.py TEXT[group]; the names and store links come from
    the store file of the page's country (car: data/store-<CAR_CHECKED>.json; companion: data/store-companion-*.json).
    Prices in the text are the developer's own. An app not on sale in the country keeps its name, without a link, and
    the sources say so (text["not_on_sale"], with {names})."""
    cc = L["cc"]
    missing = set()
    F = lambda s: fill_news(s, cc, text, missing)
    pg = dict(base)
    pg.update(lang=lang, store=cc, ct=f"{base['ct']}-{lang.lower()}"[:40], path=text["path"], checked=CAR_CHECKED,
              updated=CAR_CHECKED, apps=[], related=list(base.get("related", [])))
    for k in ("kicker", "title", "h1", "description", "llms", "stand", "fix"):
        pg[k] = text[k]
    pg["answer"] = [F(x) for x in text["answer"]]
    pg["sections"] = [(sid, h, F(body)) for sid, h, body in text["sections"]]
    pg["faq"] = [tuple(x) for x in text["faq"]]
    pg["sources_html"] = [F(x) for x in text["sources_html"]]
    if missing:
        names = ", ".join(COMP_STORE[f"{i}|us"]["name"] for i in sorted(missing))
        pg["sources_html"].append(text["not_on_sale"].format(names=html.escape(names, quote=False)))
    if "llms_note" in text:
        pg["llms_note"] = text["llms_note"]
    else:
        pg.pop("llms_note", None)
    return pg


def localize(base, lang, L, text, ui, human_date):
    if base.get("kind") == "news":
        return localize_news(base, lang, L, text)
    cc = L["cc"]
    apps, dropped = [], []
    for a in base["apps"]:
        d = info(a["id"], cc)
        if not d or not d.get("avail") or (cc == "cn" and KEY[a["id"]] in AI_OURS):
            dropped.append(a["name"])
            continue
        tx = text["apps"][a["anchor"]]
        lo, hi = d.get("pmin"), d.get("pmax")
        if lo and hi:
            price = ui["price_one"].format(lo=lo) if lo == hi else ui["price_range"].format(lo=lo, hi=hi)
        else:
            price = ui["price_none"]
        row = base_row(a, tx, ui, d, price, human_date, lang)
        n = {k: v for k, v in a.items() if k not in ("row", "rating", "best_for", "facts", "limits")}
        n.update(row=row, best_for=tx["best_for"], facts=tx["facts"], limits=tx["limits"])
        apps.append(n)
    note = text["table_note"]
    if dropped:
        note += " " + ui["unavail"].format(names=", ".join(dropped), country=ui["country"])
    ids = {a["id"] for a in apps}
    sources = []
    for (label, url), lab in zip(base["sources"], text["sources"]):
        sid = int(url.rsplit("id", 1)[1])
        if sid in ids:
            sources.append((lab, f"https://apps.apple.com/{cc}/app/id{sid}"))
    ct = f"{base['ct']}-{lang.lower()}"[:40]
    pg = dict(base)
    pg.update(lang=lang, store=cc, ct=ct, path=text["path"], published=CHECKED, updated=CHECKED, checked=CHECKED, apps=apps,
              table_note=note, sources=sources, related=list(base.get("related", [])))
    for k in ("title", "h1", "description", "llms", "answer", "columns", "who", "cases", "method", "faq"):
        pg[k] = text[k]
    pg["faq"] = [tuple(x) for x in text["faq"]]
    pg.pop("checked_label", None)
    return pg


def base_row(a, tx, ui, d, price, human_date, lang):
    base = a["row"]
    priv = "; ".join(ui["priv"].get(x.strip(), x.strip()) for x in base[3].split(";"))
    langs = tx.get("langs", base[2])
    ver = f"{d['version']} ({human_date(d['date'], lang)})"
    rating = f"{d['rating']:.1f}" if d.get("rating") else "—"
    return [price, tx["how"], langs, priv, ver, rating]
