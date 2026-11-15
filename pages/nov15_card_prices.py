"""Guide (15 Nov 2026), complaint technique: checking Pokémon card prices without wrong values or a scan paywall.
EN only. No Saga Labs app is named (the card scanner is not on sale yet); footer, About and llms.txt carry the ownership
notice as before. All links are plain links to third-party apps and public sites.

Data: 895 one- to three-star reviews (FoilSnap 283, HoloDex 284, Collectr 328) from 7 App Store countries, downloaded on
15 Nov 2026 and grouped by keyword (saga-growth data/mercado/tcg-2026-11-15/quejas-resumen.md); counts are approximate and
one review can fall in several groups. Quotes are literal. App facts: iTunes lookup of the three apps on 15 Nov 2026.
Apple support pages: 118428 (cancel a subscription), 118223 (request a refund). Public sites checked 15 Nov 2026:
tcgplayer.com Pokémon category (200), eBay advanced search help (200), cardmarket.com/en/Pokemon (403 to scripts, opens in a browser).
"""

D = "2026-11-15"
AS_OF = "as of Nov 15, 2026"


def a(u, t):
    return f'<a href="{u}">{t}</a>'


def ul(items):
    return "<ul>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ul>\n"


def ol(items):
    return "<ol>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ol>\n"


CANCEL = "https://support.apple.com/en-us/118428"
REFUND = "https://support.apple.com/en-us/118223"
TCGP = "https://www.tcgplayer.com/categories/trading-and-collectible-card-games/pokemon"
CM = "https://www.cardmarket.com/en/Pokemon"
EBAY = "https://www.ebay.com/help/buying/search-tips/advanced-search?id=4044"
RANK = "https://reviewland.io/best-pokemon-card-scanner-apps-iphone/"

_B = {
    "data": (
        "<p>We downloaded the most recent low-star reviews of the three Pokémon and TCG scanner apps with the most reviews to read: "
        + a("https://apps.apple.com/us/app/id6752642525", "TCG Card Scanner - FoilSnap") + " (283 reviews, free, 4.8), "
        + a("https://apps.apple.com/us/app/id6747442689", "HoloDex - TCG Scan &amp; Collect") + " (284, free, 4.8) and "
        + a("https://apps.apple.com/us/app/id1603892248", "Collectr - TCG Collector App") + " (328, free, 4.9), all " + AS_OF
        + ", from seven App Store countries: 895 reviews with one to three stars. Counts come from keyword matching, so they are "
        "approximate and one review can count in more than one group. The four complaints that matter most for checking prices:</p>\n"
        + ul([
            "Wrong, outdated or changing price: <strong>21%</strong> (191 reviews).",
            "Card not recognised or identified wrongly: <strong>12%</strong> (110).",
            "Paywall too early or a &ldquo;free&rdquo; app that is not free: <strong>11.5%</strong> (103), plus a free scan limit: <strong>9.7%</strong> (87).",
            "Surprise charge, cannot cancel, charged after cancelling: <strong>8%</strong> (75).",
        ]) +
        "<p>Reviews are opinions of people who were unhappy, not a test of the apps. For a ranking of seven scanner apps by what each listing says, see "
        + a(RANK, "Best Pokémon card scanner apps for iPhone (2026)") + ".</p>\n"),
    "wrongprice": (
        "<p>It is the most common complaint, in every one of the three apps. A FoilSnap reviewer: &ldquo;Results were all different "
        "values ranging from cents to $25.&rdquo; (1-3 star review, US). It hurts most when you use the price to sell or trade.</p>\n"
        "<p><strong>Fix, in five steps you can do today with no extra app:</strong></p>\n"
        + ol([
            "Find the card's own details: its name, the number printed on it (usually near the bottom edge) and its set symbol or code. Two cards with the same name can be worth very different amounts.",
            "Search that name and number on " + a(TCGP, "TCGplayer") + " and open the exact version (holo, reverse holo, first edition, language). Read the market price and the lowest listings, not one number.",
            "Check the same card on " + a(CM, "Cardmarket") + ", which shows European prices in euros. If the two sites are far apart, one of them is a different version or condition. (Cardmarket may not load for automated tools, but it opens in a normal browser.)",
            "Look at what it actually sold for: on eBay, search the card and filter to sold items (" + a(EBAY, "eBay: how advanced search works") + "). Sold prices are what people paid, asking prices are only hopes.",
            "Compare the same condition. A card in near mint and a played copy of the same card sell for different prices, and a scanner cannot see a bent corner from a photo.",
        ]) +
        "<p>Do the same check if the scanner gives a very low price, as in one reviewer's &ldquo;Most of my cards prices of 50p 30p or 10p&rdquo; (FoilSnap, GB): a price that looks too low or too high is the sign to compare, not to trust.</p>\n"),
    "notrecognised": (
        "<p>About 12% of the reviews say the app named the wrong card or the wrong set: &ldquo;Every time you scan it gives you the wrong name "
        "of the card&rdquo; (FoilSnap, US). Close to a quarter (23%) of FoilSnap's low-star reviews are about this. FoilSnap's own listing admits the "
        "problem behind it: it says standard scanners often misidentify cards because of holographic glare.</p>\n"
        "<p><strong>Fix:</strong> do not trust a name you did not read. Compare the name, number and set symbol the app shows with what is printed on "
        "the card. If they differ, search the number and set by hand on " + a(TCGP, "TCGplayer") + ". For the scan itself, lay the card flat on a plain, "
        "dark or light background and tilt it away from lamps so the foil does not glare. Another 8% of reviews say a language is missing (a reviewer: "
        "&ldquo;No support for German cards. Only English, Japanese and Chinese.&rdquo;, Collectr, DE), so if your cards are not in English, check the "
        "listing and the card list before you pay.</p>\n"),
    "paywall": (
        "<p>Another 21% of the reviews are about money before value: paywalls that arrive too early (11.5%) and a limit on free scans (9.7%). "
        "&ldquo;Immediate pay wall for core app functionality&rdquo; (HoloDex, CA). &ldquo;After you scan 35 cards they make you pay&rdquo; "
        "(Collectr, US). The listings agree: HoloDex's says in-app purchases unlock unlimited scans, exclusive filters and AI grading, and Collectr's "
        "says unlimited card scanning needs an in-app purchase. All three apps are free to download, which is not the same as free to use.</p>\n"
        "<p><strong>Fix:</strong> before you scan a collection, read the app's App Store page, in the description and in the In-App Purchases list. Look for the words "
        "&ldquo;unlimited&rdquo;, &ldquo;premium&rdquo; or &ldquo;in-app purchase&rdquo; next to the thing you want. Two listings say prices are free: Dex's says its "
        "prices from TCGplayer, Cardmarket, eBay and CardTrader are free for everyone, and PriceCharting's calls the app completely free. For a card or two, you "
        "may not need an app at all: the steps above, done on a website, cost nothing. We put the free limits we could read side by side in "
        + a(RANK, "our ranking of seven card scanner apps") + ".</p>\n"),
    "charged": (
        "<p>About 8% are about being charged: &ldquo;Tried to cancel and it wouldn't let me and it auto renewed.&rdquo; (FoilSnap, US). It is the "
        "top complaint for FoilSnap after prices (15% of its low-star reviews). The listing of FoilSnap says, like many apps, that a subscription auto-renews "
        "unless you cancel at least 24 hours before the current period ends.</p>\n"
        "<p><strong>Fix, on your iPhone, in under a minute:</strong></p>\n"
        + ol([
            "Before you start a free trial, read the payment sheet: it shows the price, how often it renews and the date the trial ends.",
            "Add a reminder in your calendar for the day before the trial ends.",
            "To check or stop it: open Settings, tap your name, tap Subscriptions, tap the subscription, then Cancel Subscription. Apple's steps are on "
            + a(CANCEL, "Cancel a subscription from Apple") + ". Deleting the app does not cancel it.",
            "If you were charged and did not mean to be, you can ask for a refund: " + a(REFUND, "Request a refund for apps or content that you bought from Apple") + ". Apple decides.",
        ])),
    "checklist": ul([
        "Did I read the card's name, number and set, and do they match what the app says?",
        "Did I compare the price on TCGplayer and Cardmarket for the same version and condition?",
        "Did I look at eBay sold listings before selling or trading?",
        "Did I read the app's In-App Purchases list and the trial terms before scanning?",
        "Do I know the date the trial ends and where to cancel (" + a(CANCEL, "Apple: cancel a subscription") + ")?"]),
}

PAGES = [{
    "group": "tcg-price-complaints", "kind": "news", "lang": "en", "store": "us",
    "path": "check-pokemon-card-prices-without-wrong-values-or-scan-paywall-iphone/",
    "ct": "rd-pokemon-card-prices",
    "category": "UtilitiesApplication",
    "published": D, "updated": D, "checked": D, "apps": [],
    "kicker": "Card price guide",
    "title": "How to Check Pokémon Card Prices Without Wrong Values or a Scan Paywall (2026)",
    "h1": "How to check Pokémon card prices without wrong values or a scan paywall (2026)",
    "description": ("Card scanner apps get 1-3 star reviews about wrong or changing prices (21%), paywalls and scan limits (21%), cards "
                    "not recognised (12%) and surprise charges (8%). What 895 reviews say, and how to check a price yourself."),
    "llms": ("Guide, 15 November 2026: the four most repeated complaints in 895 one- to three-star App Store reviews of the card scanner "
             "apps FoilSnap, HoloDex and Collectr: wrong or changing price (21%), paywall or scan limit (about 21%), card not recognised (12%) "
             "and surprise charges (8%), with a fix for each: compare TCGplayer and Cardmarket, check eBay sold listings, match the printed "
             "number and set, and read the trial terms and Apple's cancel steps first. Counts are approximate."),
    "stand": "Complaints from 895 App Store reviews, and a check you can do for each without any app.",
    "answer": [
        "<strong>To check a Pokémon card price without a wrong value, treat a scanner's price as a first guess: confirm the exact card on "
        "TCGplayer and Cardmarket, then look at what the same card sold for in eBay's sold listings.</strong> To avoid a scan paywall, read the app's "
        "free limits and trial terms on its App Store page before you scan, and know where to cancel in Settings, under your name, then Subscriptions.",
        "In 895 one- to three-star reviews of FoilSnap, HoloDex and Collectr, the top complaints were a wrong or changing price (21%), a paywall or scan "
        "limit (about 21%), a card not recognised (12%) and a surprise charge (8%). Each has a fix below that works today.",
    ],
    "sections": [
        ("data", "What we looked at", ""),
        ("wrongprice", "“Wrong price” and “different value every scan” (21%)", ""),
        ("notrecognised", "“Doesn't recognise my card” (12%)", ""),
        ("paywall", "“Paywall” and “only 10 scans” (about 21%)", ""),
        ("charged", "“Charged me” and “wouldn't let me cancel” (8%)", ""),
        ("checklist", "Before you trust a price or start a trial: a 5-line check", ""),
    ],
    "related": ["car-video-complaints", "ai-companion-complaints"],
    "faq": [
        ("How accurate are Pokémon card scanner apps?",
         "It varies. In 895 one- to three-star reviews of FoilSnap, HoloDex and Collectr, 21% mention a wrong, outdated or changing price and 12% a card not recognised. Use the app's value as a first guess and check the exact card on TCGplayer and Cardmarket."),
        ("Why does a scanner show a different price every time?",
         "The reviews do not say why. One FoilSnap reviewer got values from cents to $25 for the same card across ten scans. A different version, condition or source can change the number, so confirm on a marketplace."),
        ("Where can I check Pokémon card prices for free?",
         "TCGplayer and Cardmarket list prices for Pokémon cards on their websites, and eBay's sold listings show what cards sold for. Dex's App Store listing says its prices are free for everyone."),
        ("How do I cancel a card scanner subscription?",
         "On iPhone, open Settings, tap your name, tap Subscriptions, tap the subscription and tap Cancel Subscription. Apple explains it on its page about cancelling a subscription."),
        ("Can I get a refund from the App Store?",
         "You can ask. Apple explains how on its page about requesting a refund for apps or content bought from Apple; approval is up to Apple."),
    ],
    "sources_html": [
        "Reviews: US, CA, GB, DE, AU, FR and JP App Store, 895 reviews with 1-3 stars from three apps, downloaded 15 November 2026; counts by keyword, approximate.",
        a(CANCEL, "Cancel a subscription from Apple") + ", Apple Support.",
        a(REFUND, "Request a refund for apps or content that you bought from Apple") + ", Apple Support.",
        a(TCGP, "TCGplayer: Pokémon") + "; " + a(CM, "Cardmarket: Pokémon") + "; " + a(EBAY, "eBay: advanced search") + ".",
        "Apps: their US App Store pages and Apple lookup data, 15 November 2026. " + a(RANK, "Best Pokémon card scanner apps for iPhone (2026)") + ", Reviewland.",
    ],
    "fix": 'If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
}]

for _i, (_sid, _h, _body) in enumerate(PAGES[0]["sections"]):
    if _sid in _B:
        PAGES[0]["sections"][_i] = (_sid, _h, _B[_sid])
