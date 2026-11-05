"""Luma Dream Machine alternatives on iPhone, EN. Our app: Dora (id6754180384).

Checked 2026-11-05: US App Store search for «luma dream machine», «luma ai», «ai video generator», «text to video»,
iTunes lookup and the US App Store page of every app (price list, privacy label), and doravideo.com/models for Dora (no
Veo). Why this topic: Google suggests «luma dream machine alternative», «... free», «luma ai dream machine
alternative» (5 Nov); no page on the 4 sites is about Luma (reviewland has Higgsfield, Pollo, Grok Imagine, VideoGPT).
Luma's iPhone app was last updated on 17 April 2026. Registered in ios-playbook references/temas-webs.md (29d6c85).
No quality test, nothing generated.
"""

D = "2026-11-05"
CHECKED = "2026-11-05"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f} ({count:,} ratings)"]}
    if ours:
        a["ours"] = True
    return a


T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"

PAGES = [{
    "group": "luma-alt", "lang": "en", "store": "us",
    "path": "luma-dream-machine-alternatives-iphone/",
    "ct": "rd-luma-alt-iphone",
    "category": "PhotoVideoApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Luma Dream Machine Alternatives for iPhone (2026): 6 Apps",
    "h1": "Best Luma Dream Machine alternatives for iPhone in 2026",
    "description": "Luma's iPhone app has not been updated since April 2026. Six AI video apps compared by price, models and privacy, one of them with Luma's models.",
    "llms": "Compares six iPhone alternatives to Luma Dream Machine (AI images and video; iPhone app last updated 17 April 2026; Lite $9.99 to Unlimited $94.99 a month): Kling AI, Runway, Adobe Firefly (offers Luma among partner models), Dora (Seedance 2, Kling 2.6, Gemini Omni and Grok, paid per video in coins), Pika and Pollo AI, by price, models, video length and App Store privacy label.",
    "llms_note": "Dora, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Luma Dream Machine still works on iPhone, but its app was last updated on 17 April 2026</strong>, more than six months before this check (5 November 2026). It makes images and videos you edit by describing changes, with up to 4 reference images and a consistent character from one face photo. Plans run from Lite at $9.99 a month to Unlimited at $94.99, and the app is in English only.",
        "To keep using Luma's models, Adobe Firefly lists Luma among its partner models, next to Google, OpenAI and Runway. For an actively updated video app, Kling AI makes up to 15 seconds in 1080p or 4K and extends to 3 minutes; Runway puts Seedance 2.5, Kling 3 Pro and Gen-4.5 in one app; Dora charges per video in coins, with Seedance 2, Kling 2.6, Gemini Omni and Grok on its model page. Pika is for playful effects and Pollo AI for ads.",
    ],
    "columns": ["App", "Price (US)", "Video models, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 5 November 2026; pages list only some. All are free to download. Luma for comparison: Lite $9.99, Plus $29.99, Unlimited $94.99 a month. Ratings are that day's App Store average and count.",
    "apps": [
        app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 33114,
            "long clips: up to 15 seconds in 1080p or 4K, extended to 3 minutes.",
            ["Text and image to video, up to 15 seconds in native 1080p or 4K; Video Extension up to 3 minutes.",
             "4K images from text or references, with batch variations.",
             "A community feed where you can clone another creator's idea and try it."],
            "its privacy label includes Data Used to Track You, and the price list mixes weekly, monthly and credit packs.",
            ["Standard $10, Pro $37, Premier $92 a month; credits $5 to $100",
             "Kling", "5", T3, "3.10.10 (4 Nov 2026)"]),
        app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19437,
            "several top video models in one app, plus an agent that assembles a whole video.",
            ["Its listing names Seedance 2.5, Kling 3 Pro and Gen-4.5 for video, and Nano Banana Pro and 2 for images.",
             "Consistent characters, objects and locations across shots.",
             "Runway Agent plans, generates and assembles a video from a conversation."],
            "English only, extra credits on top of the plans, and its privacy label includes Data Used to Track You.",
            ["Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits from $10",
             "Seedance 2.5, Kling 3 Pro, Gen-4.5", "1", T3, "103.0.0 (1 Nov 2026)"]),
        app("Adobe Firefly AI Video & Photo", 6742595426, "firefly", "Adobe Inc.", 4.69, 11271,
            "staying with Luma's models, next to Adobe's, Google's, OpenAI's and Runway's.",
            ["Its listing names partner models from Adobe, Google, OpenAI, Luma and Runway.",
             "Adobe's own models are trained on licensed content, per Adobe.",
             "Text to video, image and sound; background removal; in 27 languages."],
            "credits are bought on top of the plan, and the listing does not say which Luma model it offers.",
            ["Firefly Mobile $4.99 a month or $49.99 a year; credits $4.99 to $499.99",
             "Adobe, Google, OpenAI, Luma, Runway", "27", "Data Linked to You; Data Not Linked to You", "26.19.0 (28 Oct 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.12, 17,
            "paying per video, with the cost shown first, across several video models.",
            ["doravideo.com/models lists Seedance 2 (from 16 coins with Seedance 2 Mini), Kling 2.6, Gemini Omni and Grok for video.",
             "Photo to video, text to video, templates and Motion Control (copy a dance onto your photo); no watermark; up to 1080p.",
             "The cost shows before you generate, failed generations refund the coins, and coins also work on doravideo.com and in Claude and ChatGPT."],
            "only 17 US ratings, its App Store listing does not name the models (the list is on its website), and coins need the Pro plan.",
            ["Pro weekly $4.99 or $6.99, yearly $119.99; coins $4.99 to $224.99",
             "Seedance 2, Kling 2.6, Gemini Omni, Grok, per doravideo.com/models", "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("Pika - AI Video", 6680155400, "pika", "Mellis, Inc.", 4.73, 4324,
            "playful effects on your own photos and videos: swaps, additions, melt and squish.",
            ["Pikaswaps replace any element in a video; Pikadditions drop new objects or people into it.",
             "Pikaffects such as Melt, Explode, Squish and Levitate; meme GIFs from a selfie.",
             "Scenes you fill with your own characters and backgrounds."],
            "it needs iOS 26, it is English only, and the price list is high (weekly plans to $48).",
            ["Standard $8.99 a week or $16 a month, Pro $35 a month or $199 a year",
             "Pika", "1", "Data Linked to You; Data Not Linked to You", "2.1.0 (4 Nov 2026)"]),
        app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13617,
            "ads, product videos and UGC-style clips for a shop.",
            ["Turns scripts, product photos, URLs or reference videos into ads and social videos.",
             "UGC ads, product demos, virtual try-on and multiple hooks for testing.",
             "Also story videos, music videos and viral templates."],
            "English only, and its privacy label includes Data Used to Track You and Data Linked to You.",
            ["Weekly $5.99, Lite $15 or Pro $29 a month, yearly $99.99; credits $6.99 to $164.99",
             "Not named in the listing", "1", "Data Used to Track You; Data Linked to You", "4.3.1 (30 Oct 2026)"]),
    ],
    "who": [
        "<strong>Longest clips, up to 3 minutes:</strong> Kling AI.",
        "<strong>Several top models and an agent:</strong> Runway.",
        "<strong>Keep using Luma's models:</strong> Adobe Firefly.",
        "<strong>Pay per video, cost shown first:</strong> Dora.",
        "<strong>Playful effects on your photos:</strong> Pika.",
        "<strong>Ads for a shop:</strong> Pollo AI.",
    ],
    "cases": ["A short film shot from a single character photo.", "A product clip for social media.", "Moving off an app that has stopped updating."],
    "method": [
        "On 5 November 2026 we searched the US App Store for «luma dream machine», «luma ai», «ai video generator» and «text to video», and read Luma's and each app's US App Store page and Apple's lookup data. For Dora, whose listing does not name its models, we used its own model page. We generated nothing and ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is Luma Dream Machine still available on iPhone?",
         "Yes. It was on the US App Store on 5 November 2026, but its last update was 17 April 2026."),
        ("Which app lets me keep using Luma's models?",
         "Adobe Firefly lists Luma among its partner models; its listing does not say which Luma model."),
        ("Which alternative is cheapest to start?",
         "Adobe Firefly Mobile is $4.99 a month and Dora Pro is $4.99 a week; Kling's Standard plan is $10 a month. Video costs credits or coins on top in Firefly, Kling and Dora."),
        ("Which makes the longest videos?",
         "Kling AI, which lists up to 15 seconds per clip and Video Extension up to 3 minutes."),
    ],
    "sources": [
        ("Luma Dream Machine (App Store)", "https://apps.apple.com/us/app/id6478852867"),
        ("Kling AI (App Store)", "https://apps.apple.com/us/app/id6738049229"),
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"),
        ("Adobe Firefly (App Store)", "https://apps.apple.com/us/app/id6742595426"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora models and costs", "https://doravideo.com/models"),
        ("Pika (App Store)", "https://apps.apple.com/us/app/id6680155400"),
        ("Pollo AI (App Store)", "https://apps.apple.com/us/app/id6740024098"),
    ],
}]
