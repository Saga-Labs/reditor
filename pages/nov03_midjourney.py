"""Midjourney alternatives for iPhone, EN. Our app: Dora (id6754180384), images with Nano Banana 2.

Checked 2026-11-02: US App Store search for «midjourney» and «niji journey», iTunes lookup and the US App Store
page of every app (price list, privacy label), and doravideo.com/models (Nano Banana 2: 10 credits an image).
Encargo de saga-growth (2 nov) para el 3 nov, después de las 00:00 UTC. Before writing: no Midjourney page on
reditor, reviewland or aisagalab; doravideo.com/vs/midjourney is a Dora-vs-Midjourney page, linked, not repeated.
No quality test, nothing generated.
"""

D = "2026-11-03"
CHECKED = "2026-11-02"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f} ({count:,} ratings)"]}
    if ours:
        a["ours"] = True
    return a


LN = "Data Linked to You; Data Not Linked to You"

PAGES = [{
    "group": "midjourney-alt", "lang": "en", "store": "us",
    "path": "midjourney-alternatives-iphone/",
    "ct": "rd-midjourney-alternatives-iphone",
    "category": "GraphicsDesignApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Midjourney Alternatives for iPhone (2026): 7 AI Image Apps Compared",
    "h1": "Best Midjourney alternatives for iPhone in 2026",
    "description": "There is no Midjourney app on the iPhone, only its anime app niji・journey. Seven iPhone AI image apps compared by price, models and App Store privacy label.",
    "llms": "Explains that Midjourney has no iPhone app under its own name (its developer publishes the anime-style niji・journey app) and compares seven iPhone AI image apps (niji・journey, Leonardo.Ai, Ideogram, Dora, Adobe Firefly, ChatGPT, Google Gemini) by price, image models named in each listing and App Store privacy label.",
    "answer": [
        "<strong>There is no app called Midjourney on the iPhone.</strong> On 2 November 2026, a US App Store search for «midjourney» showed no app from Midjourney under that name; Midjourney itself is used at midjourney.com, which also opens in Safari on the iPhone. The one iPhone app from Midjourney, Inc. is <a href=\"https://apps.apple.com/us/app/id6446376937\">niji・journey</a>, which makes anime-style pictures and syncs with an existing niji・journey account.",
        "For other styles, six apps do the same job natively. Leonardo.Ai and Adobe Firefly let you choose between several image models (Firefly's are trained on licensed content, per Adobe). Ideogram is known for clean text inside images, such as logos and posters. ChatGPT and Google Gemini make images inside a chat app you may already have; Gemini's listing names Nano Banana 2. Dora makes images with Nano Banana 2 too, at about 10 coins an image on doravideo.com, and also makes video.",
    ],
    "columns": ["App", "Price (US)", "What it makes, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 2 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("niji・journey - AI Anime Art", 6446376937, "niji", "Midjourney, Inc.", 4.41, 583,
            "anime and illustration styles from Midjourney's own team.",
            ["The only iPhone app from Midjourney, Inc.; type what you want to see and pick a style.",
             "A short quiz suggests a personal style, and you can remix prompts from other users.",
             "Accounts and plans sync with an existing niji・journey account, per its listing."],
            "anime style only, English only, and no free plan listed: plans start at $4.99 a month.",
            ["Mini $4.99, Basic $9.99, Standard $29.99, Pro $59.99 a month; Fast Hours from $3.99",
             "Anime-style images from text",
             "1", "Data Used to Track You; Data Not Linked to You", "1.46.0 (30 Oct 2026)"]),
        app("Leonardo.Ai - Image Generator", 1662773014, "leonardo", "Leonardo Interactive Pty Ltd", 4.83, 11289,
            "people who want Midjourney-like control and several models in one app.",
            ["Its listing names Nano Banana by Google, Seedream, FLUX and Leonardo's own models.",
             "Ready-made templates (Blueprints), an image editor that follows written changes, and background removal.",
             "Also turns images and photos into video."],
            "English only, and its cheapest plan ($15.99 a month) is the highest starting price here.",
            ["Essential $15.99, Premium $39.99, Ultimate $79.99 a month (yearly $159.99 to $749.99); tokens from $13",
             "Images with several models, editing, templates, video",
             "1", LN, "2.0.50 (1 Nov 2026)"]),
        app("Ideogram AI - Image Generator", 6476790495, "ideogram", "Ideogram AI Inc", 4.78, 2690,
            "logos, posters and any image that must contain readable text.",
            ["Free weekly credits to start, per its listing.",
             "Stylized text and precise composition, a logo maker and AI headshots from one photo.",
             "Generative fill, expanding to new aspect ratios and background removal."],
            "English only, and images only: its listing names no video.",
            ["Basic $11.99, Plus $28.99, Pro $85.99 a month (yearly $119.99 to $829.99)",
             "Images with text, logos, headshots, editing",
             "1", LN, "2026.41 (24 Oct 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
            "someone who wants images and short videos from the same coins, with the cost shown first.",
            ["Images from a description or a reference photo, up to 4K, back in about a minute, per its listing; one of its image models is Nano Banana 2, at about 10 coins an image on <a href=\"https://doravideo.com/models\">doravideo.com/models</a>.",
             "The coin cost shows before you generate, and failed generations refund the coins.",
             "The same account and coins work on doravideo.com. Dora's own page compares it with Midjourney: <a href=\"https://doravideo.com/vs/midjourney\">doravideo.com/vs/midjourney</a>."],
            "built mainly for video, with no style quiz or community feed, and no free images: coins need a Pro plan.",
            ["Pro weekly $4.99 or $6.99, yearly $119.99; coin packs $3.99 to $224.99",
             "Images up to 4K and short videos from text or a photo",
             "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("Adobe Firefly AI Video & Photo", 6742595426, "firefly", "Adobe Inc.", 4.69, 11179,
            "work you plan to use commercially, and people who already use Adobe apps.",
            ["Adobe says its own Firefly models are trained on licensed content.",
             "Also offers partner models from Google, OpenAI, Luma and Runway, plus video, sound and background removal.",
             "In 27 languages, the most here after ChatGPT and Gemini."],
            "credits are a separate purchase on top of the plan, and partner models use more of them.",
            ["Firefly Mobile $4.99 a month or $49.99 a year; credits $4.99 to $499.99",
             "Images, video and sound; Adobe and partner models",
             "27", LN, "26.19.0 (28 Oct 2026)"]),
        app("ChatGPT", 6448311069, "chatgpt", "OpenAI OpCo, LLC", 4.82, 11820399,
            "people who already use ChatGPT and want to make or edit images by describing them.",
            ["Makes images from a description, or changes an uploaded one with a few words, per its listing.",
             "The free app syncs your history across devices."],
            "it is a chat app first, with fewer image controls than Leonardo or Midjourney.",
            ["Go $8, Plus $19.99, Pro from $100 a month; credits from $4",
             "Images in chat, from text or an uploaded photo",
             "60", "Data Linked to You", "1.2026.293 (27 Oct 2026)"]),
        app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2391162,
            "people who want Google's Nano Banana 2 directly, inside an assistant.",
            ["Its listing names Nano Banana 2 for making and editing photos: camera and lighting controls, mockups that blend several images, posters with sharp text.",
             "Google AI plans also add cloud storage (from 400 GB on Plus)."],
            "it is an assistant first, and the plans bundle storage you may not need.",
            ["Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month",
             "Images with Nano Banana 2, in chat",
             "70", "Data Linked to You", "1.2026.4262206 (29 Oct 2026)"]),
    ],
    "who": [
        "<strong>Midjourney's own anime model:</strong> niji・journey.",
        "<strong>Several models and fine control:</strong> Leonardo.Ai.",
        "<strong>Readable text, logos and posters:</strong> Ideogram.",
        "<strong>Images and short videos from the same coins:</strong> Dora.",
        "<strong>Commercial work, licensed training data:</strong> Adobe Firefly.",
        "<strong>An app you already have:</strong> ChatGPT or Google Gemini.",
    ],
    "cases": ["A poster or logo with text.", "Character art in an anime style.", "Turning a rough idea into a picture on the go."],
    "method": [
        "On 2 November 2026 we searched the US App Store for «midjourney» and «niji journey», and read each app's US App Store page and Apple's lookup data. What each app does comes from its own listing. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a Midjourney app for iPhone?",
         "Not under that name. Midjourney, Inc. publishes niji・journey, an anime-style image app. Midjourney itself works at midjourney.com in a browser, including Safari on the iPhone."),
        ("Is niji・journey the same as Midjourney?",
         "It comes from the same company, Midjourney, Inc., but the app is built for anime and illustration styles and sells its own plans in the app."),
        ("Which iPhone apps use Nano Banana 2?",
         "Of the listings we read, Google Gemini names Nano Banana 2, and Dora lists it on doravideo.com/models. Leonardo.Ai names Nano Banana by Google."),
        ("Which is cheapest to try?",
         "Ideogram gives free weekly credits. Among paid plans listed: niji・journey Mini $4.99 a month, Firefly Mobile $4.99 a month, Google AI Plus $4.99 a month, ChatGPT Go $8 a month, Dora Pro weekly from $4.99."),
    ],
    "sources": [
        ("niji・journey - AI Anime Art (App Store)", "https://apps.apple.com/us/app/id6446376937"),
        ("Leonardo.Ai - Image Generator (App Store)", "https://apps.apple.com/us/app/id1662773014"),
        ("Ideogram AI - Image Generator (App Store)", "https://apps.apple.com/us/app/id6476790495"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora models and credit costs", "https://doravideo.com/models"),
        ("Dora vs Midjourney", "https://doravideo.com/vs/midjourney"),
        ("Adobe Firefly AI Video & Photo (App Store)", "https://apps.apple.com/us/app/id6742595426"),
        ("ChatGPT (App Store)", "https://apps.apple.com/us/app/id6448311069"),
        ("Google Gemini (App Store)", "https://apps.apple.com/us/app/id6477489729"),
    ],
}]
