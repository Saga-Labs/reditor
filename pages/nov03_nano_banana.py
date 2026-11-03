"""Apps to use Nano Banana (Google's image models) on iPhone, EN. Our app: Dora (id6754180384), which lists Nano Banana, Nano Banana 2 and Nano Banana Pro on doravideo.com/models.

Checked 2026-11-03: US App Store search for «nano banana», «nano banana pro», «ai image generator», «ai photo editor»,
iTunes lookup and the US App Store page of every app (price list, privacy label), and doravideo.com/models for Dora
(its App Store listing does not name the models). Only apps whose listing (or, for Dora, own site) names Nano Banana.
Why this topic: Google suggests «nano banana app for iphone», «nano banana ios app», «nano banana 2 app iphone»,
«nano banana pro app iphone» (3 Nov); on the 4 sites only doravideo.com has Nano Banana model pages, no apps page.
Registered in ios-playbook references/temas-webs.md. No quality test, nothing generated.
"""

D = "2026-11-03"
CHECKED = "2026-11-03"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f} ({count:,} ratings)"]}
    if ours:
        a["ours"] = True
    return a


T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"
TL = "Data Used to Track You; Data Linked to You"

PAGES = [{
    "group": "nano-banana", "lang": "en", "store": "us",
    "path": "nano-banana-apps-iphone/",
    "ct": "rd-nano-banana-apps-iphone",
    "category": "GraphicsDesignApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Nano Banana on iPhone (2026): 7 Apps That Offer It Besides Gemini",
    "h1": "Apps to use Nano Banana on iPhone in 2026",
    "description": "Nano Banana has no app of its own: Google offers it in Gemini and the Google app. Seven other iPhone apps that name Nano Banana, by price and privacy label.",
    "llms": "Explains how to use Google's Nano Banana image models (Nano Banana, Nano Banana 2, Nano Banana Pro) on an iPhone: there is no app with that name from Google; Gemini names Nano Banana 2 and the Google app names Nano Banana in AI Mode. Compares seven other iPhone apps that name Nano Banana (Picsart, Runway, starryai, Dora, Leonardo.Ai, ChatNow, ARTA) by price, which Nano Banana model and App Store privacy label.",
    "answer": [
        "<strong>Nano Banana is a family of Google image models, not an app.</strong> On iPhone, Google offers it in two of its own apps: <a href=\"https://apps.apple.com/us/app/id6477489729\">Google Gemini</a>, whose listing says you can generate and edit photos with Nano Banana 2 (camera and lighting controls, mockups that blend images, posters with sharp text), and the <a href=\"https://apps.apple.com/us/app/id284815942\">Google</a> app, which names Nano Banana for creating images in AI Mode, in select languages and locations.",
        "Seven other apps name Nano Banana too. Runway, ChatNow and Dora offer Nano Banana Pro, Google's highest-quality version, as well as Nano Banana 2; Picsart, starryai, Leonardo.Ai and ARTA name Nano Banana or Nano Banana 2 inside wider photo and art apps. Which version you get matters: Dora's model page, for example, lists Nano Banana at 4 coins, Nano Banana 2 at 10 and Nano Banana Pro at 18 (24 at 4K).",
    ],
    "columns": ["App", "Price (US)", "Nano Banana model, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Picsart AI Photo Editor, Video", 587366035, "picsart", "PicsArt, Inc.", 4.66, 1196453,
            "editing your own photos, with Nano Banana for new images inside the same editor.",
            ["Its Aura feature uses Nano Banana for image generation, next to video models such as Veo 3, Kling, Runway and Luma.",
             "A full photo and video editor around it.",
             "In 30 languages; its listing says availability may vary."],
            "several overlapping plans (Plus, Gold, Pro), and the listing does not say which Nano Banana version or which plan includes it.",
            ["Gold $4.99 a week, $12.99 a month or $57 a year; Plus and Pro from $11.99 a month",
             "Nano Banana (version not named)",
             "30", T3, "30.9.2 (6 Oct 2026)"]),
        app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19253,
            "Nano Banana Pro and Nano Banana 2 next to video models, for images that become shots.",
            ["Its listing names Nano Banana Pro and Nano Banana 2, with Seedance 2.5, Kling 3 Pro and Gen-4.5 for video.",
             "Keeps the same character, object or location across generations.",
             "Runway Agent can plan and assemble a whole video from a conversation."],
            "English only, and extra credits are sold on top of the plans.",
            ["Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits from $10",
             "Nano Banana Pro and Nano Banana 2",
             "1", T3, "103.0.0 (1 Nov 2026)"]),
        app("starryai - AI Image Generator", 1580512844, "starryai", "starryai, Inc.", 4.61, 22246,
            "an art app built for images, with photoreal edits on Nano Banana.",
            ["Its listing names Nano Banana for photoreal images and edits.",
             "Weekly and monthly Pro plans, including unlimited options, plus Lumens packs.",
             "Version 3.0.1 came out on 29 October 2026."],
            "English only, and its long list of plans makes the real price hard to read before you open the app.",
            ["Pro from $4.99 a week; Unlimited Pro $9.99 to $39.99; Lumens packs $7.99 or $15.99",
             "Nano Banana (version not named)",
             "1", T3, "3.0.1 (29 Oct 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
            "all three Nano Banana versions with the coin cost shown before each image, and video from the same coins.",
            ["doravideo.com/models lists Nano Banana (4 coins), Nano Banana 2 (10 coins, up to 4K) and Nano Banana Pro (18 coins at 1K or 2K, 24 at 4K).",
             "Images from a description or a reference photo, back in about a minute, per its App Store listing.",
             "The same coins make videos and work on doravideo.com and in Claude and ChatGPT; failed generations refund the coins."],
            "its App Store listing does not name Nano Banana (the model list is on its website), and there are no free images: coins need the Pro plan.",
            ["Pro weekly $4.99 or $6.99, yearly $119.99; coin packs $3.99 to $224.99",
             "Nano Banana, 2 and Pro, per doravideo.com/models",
             "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("Leonardo.Ai - Image Generator", 1662773014, "leonardo", "Leonardo Interactive Pty Ltd", 4.83, 11289,
            "trying Nano Banana next to Seedream, FLUX and Leonardo's own models, starting free.",
            ["Its listing names Nano Banana by Google among its image models, with Seedream, FLUX and Leonardo's own.",
             "Its listing calls the image maker free; paid plans add tokens.",
             "Templates, an editor that follows written changes, and background removal."],
            "English only, and its cheapest plan ($15.99 a month) is the highest starting price here.",
            ["Essential $15.99, Premium $39.99, Ultimate $79.99 a month (yearly $159.99 to $749.99); tokens from $13",
             "Nano Banana (version not named)",
             "1", "Data Linked to You; Data Not Linked to You", "2.0.50 (1 Nov 2026)"]),
        app("AI Chat Assistant – ChatNow", 1667518571, "chatnow", "Tappz GmbH", 4.80, 146222,
            "a chat app where you can make and edit images with Nano Banana Pro under the same subscription.",
            ["Its listing names Nano Banana Pro and Nano Banana 2 for images, with GPT Image 2 and Flux.",
             "Generates images and edits photos, and also makes short videos with Veo 3.1 and Sora 2.",
             "Chat with 30+ models in the same app."],
            "it needs iOS 26, it is a chat app first, and the plans range widely ($6.99 to $79.99 listed).",
            ["Plus from $6.99 to $79.99 listed, yearly $59.99; credits $9.99 or $19.99",
             "Nano Banana Pro and Nano Banana 2",
             "13", "Data Used to Track You; Data Not Linked to You", "5.13 (24 Oct 2026)"]),
        app("AI Photo Generator: ARTA", 1642969698, "arta", "AIBY Incorporated", 4.30, 81540,
            "AI avatars and art styles, with Nano Banana 2 among the models.",
            ["Its listing's FAQ names Nano Banana 2 among its models, with Veo 3.1, Kling, PixVerse, Runway and Flux 2.",
             "Avatar packs and art styles from your photos.",
             "In 11 languages."],
            "weekly plans dominate the price list, its last update was 10 September 2026, and its privacy label includes Data Used to Track You.",
            ["Weekly $4.99 to $9.99, yearly $39.99; avatar packs $7.99 or $9.99",
             "Nano Banana 2 among several models",
             "11", TL, "4.39 (10 Sep 2026)"]),
    ],
    "who": [
        "<strong>Google's own apps:</strong> Gemini (Nano Banana 2) or the Google app (AI Mode).",
        "<strong>Editing your photos:</strong> Picsart.",
        "<strong>Nano Banana Pro for images that become video shots:</strong> Runway.",
        "<strong>All three versions, cost shown first:</strong> Dora.",
        "<strong>Comparing Nano Banana with other image models:</strong> Leonardo.Ai.",
        "<strong>Images inside a chat app:</strong> ChatNow.",
    ],
    "cases": ["A product mockup or poster with readable text.", "Editing a photo by describing the change.", "A 4K image for print or a thumbnail."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «nano banana», «nano banana pro», «ai image generator» and «ai photo editor», and read each app's US App Store page and Apple's lookup data. We only included apps whose listing names Nano Banana; for Dora, whose listing does not, we used its own model page. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a Nano Banana app for iPhone?",
         "Not under that name. Nano Banana is Google's family of image models; Google offers it in the Gemini app (Nano Banana 2) and in the Google app's AI Mode."),
        ("What is the difference between Nano Banana, Nano Banana 2 and Nano Banana Pro?",
         "They are three versions with different quality and cost. Dora's model page describes Nano Banana as the fast entry model, Nano Banana 2 as up to 4K at lower cost, and Nano Banana Pro as the highest quality, with photorealistic faces at 4K."),
        ("Which apps offer Nano Banana Pro?",
         "Of the listings we read, Runway and ChatNow name Nano Banana Pro, and Dora lists it on doravideo.com/models."),
        ("Can I use Nano Banana for free?",
         "Leonardo.Ai's listing calls its image maker free. Gemini's listing names Nano Banana 2 without saying which plan includes it, so check inside the app."),
    ],
    "sources": [
        ("Google Gemini (App Store)", "https://apps.apple.com/us/app/id6477489729"),
        ("Google (App Store)", "https://apps.apple.com/us/app/id284815942"),
        ("Picsart (App Store)", "https://apps.apple.com/us/app/id587366035"),
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"),
        ("starryai (App Store)", "https://apps.apple.com/us/app/id1580512844"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora models and costs", "https://doravideo.com/models"),
        ("Leonardo.Ai (App Store)", "https://apps.apple.com/us/app/id1662773014"),
        ("AI Chat Assistant – ChatNow (App Store)", "https://apps.apple.com/us/app/id1667518571"),
        ("AI Photo Generator: ARTA (App Store)", "https://apps.apple.com/us/app/id1642969698"),
    ],
}]
