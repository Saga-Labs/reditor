"""Apps to use Google's video models (Gemini Omni, Veo) on iPhone, EN. Our app: Dora (id6754180384), which lists Gemini Omni on doravideo.com/models.

Checked 2026-11-03 (Google Flow found via «google flow»; its listing names no model, so it is in the intro, not the list): US App Store search for «veo 3», «veo», «gemini omni», «google veo», «ai video generator veo»,
iTunes lookup and the US App Store page of every app (price list, privacy label), and doravideo.com/models for Dora
(its App Store listing does not name the model). Only apps whose listing (or, for Dora, own site) names Veo or Gemini
Omni. Why this topic: Google suggests «gemini omni app», «veo 3 for iphone», «google veo 3 iphone app» and «gemini
video generator app» (3 Nov); no page on the 4 sites is about apps for Google's video models (reviewland's
/seedance-2-mini-vs-veo-3-1-vs-kling/ compares models). Registered in ios-playbook references/temas-webs.md.
No quality test, nothing generated.
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

PAGES = [{
    "group": "google-video", "lang": "en", "store": "us",
    "path": "google-video-apps-iphone/",
    "ct": "rd-google-video-apps-iphone",
    "category": "PhotoVideoApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Gemini Omni and Veo on iPhone (2026): 7 Apps That Offer Them",
    "h1": "Apps to use Gemini Omni and Veo on iPhone in 2026",
    "description": "No Veo app exists: Google's video models come in Gemini and Google Flow. Seven other iPhone apps offering Veo or Gemini Omni, by price and privacy label.",
    "llms": "Explains how to make video with Google's models (Gemini Omni and Veo) on an iPhone: there is no app called Veo from Google; the Gemini app offers Gemini Omni video on Google AI Plus, Pro and Ultra, and Google Flow is Google's creative studio app. Compares seven other iPhone apps that name Veo or Gemini Omni (Canva, Picsart, Leonardo.Ai, Dora, ChatNow, Pollo AI, Flashloop) by price and App Store privacy label.",
    "answer": [
        "<strong>Google has no app called Veo on the iPhone.</strong> On 3 November 2026, the apps named «Veo» on the US App Store were a scooter service and a sports camera, not Google. Google's main route is the <a href=\"https://apps.apple.com/us/app/id6477489729\">Google Gemini</a> app, whose listing says it makes cinematic videos with Gemini Omni for Google AI Plus ($4.99 a month), Pro ($19.99) and Ultra ($199.99) users, so free Gemini accounts do not get video. Google also publishes <a href=\"https://apps.apple.com/us/app/id6751294549\">Google Flow</a>, an AI creative studio synced with Flow on the desktop; its listing says it uses «Google's most advanced generative models» without naming them, lists no in-app purchases, and had a 3.8 rating from 130 ratings.",
        "Seven other apps offer Google's video models. Canva, Picsart and Leonardo.Ai add Veo 3 to an editor or image app; ChatNow, Pollo AI and Flashloop offer Veo next to Sora, Kling and Seedance; and Dora lists Gemini Omni, Google's any-to-any model, on its website, with the cost per clip shown before you generate.",
    ],
    "columns": ["App", "Price (US)", "Google model, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Canva AI Photo & Video Editor", 897446215, "canva", "Canva Pty Ltd", 4.87, 3600426,
            "making a Veo 3 clip and finishing it into a post, ad or presentation in the same app.",
            ["Its listing describes Veo 3 for videos with sound from a text prompt.",
             "The clip goes straight into Canva's editor, templates and brand tools.",
             "In 83 languages, the most here."],
            "Veo is one feature inside a large design app, and the listing does not say how many clips a plan includes.",
            ["Pro $14.99 to $18 a month or $119.99 to $143.99 a year; credits from $1.99",
             "Veo 3, with sound",
             "83", "Data Used to Track You; Data Linked to You", "4.233.0 (27 Oct 2026)"]),
        app("Picsart AI Photo Editor, Video", 587366035, "picsart", "PicsArt, Inc.", 4.66, 1196453,
            "photo editing first, with Veo 3 and other video models when you need motion.",
            ["Its Aura feature names Veo 3 next to Kling, Runway and Luma, with Nano Banana for images.",
             "A full photo and video editor around it.",
             "Its listing says availability may vary."],
            "several overlapping plans (Plus, Gold, Pro) and a weekly option, and the listing does not say which includes Veo.",
            ["Gold $4.99 a week, $12.99 a month or $57 a year; Plus and Pro from $11.99 a month",
             "Veo 3 among several video models",
             "30", T3, "30.9.2 (6 Oct 2026)"]),
        app("Leonardo.Ai - Image Generator", 1662773014, "leonardo", "Leonardo Interactive Pty Ltd", 4.83, 11289,
            "images and video together, with camera controls, starting from its free plan.",
            ["Its listing names Veo 3 by Google among its video models, with camera controls and animation effects.",
             "Brings generated images and real photos to life with motion.",
             "Its listing calls the video maker free; paid plans add tokens."],
            "English only, and its cheapest plan ($15.99 a month) is among the highest starting prices here.",
            ["Essential $15.99, Premium $39.99, Ultimate $79.99 a month (yearly $159.99 to $749.99); tokens from $13",
             "Veo 3 among several video models",
             "1", "Data Linked to You; Data Not Linked to You", "2.0.50 (1 Nov 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
            "Gemini Omni without a Google AI plan, with the coin cost shown before each clip.",
            ["doravideo.com/models lists Gemini Omni (Gemini Omni Flash) from Google: video from text, reference photos or a video clip, 720p to 4K, 4 to 10 seconds.",
             "A 6-second clip at 720p or 1080p costs 120 coins there; 4K starts at 210.",
             "The same coins work in the app, on doravideo.com and in Claude and ChatGPT; failed generations refund the coins."],
            "it does not offer Veo, its App Store listing does not name Gemini Omni (the model list is on its website), and there are no free videos.",
            ["Pro weekly $4.99 or $6.99, yearly $119.99; coin packs $3.99 to $224.99",
             "Gemini Omni, per doravideo.com/models",
             "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("AI Chat Assistant – ChatNow", 1667518571, "chatnow", "Tappz GmbH", 4.80, 146222,
            "a chat app that also makes Veo 3.1 and Omni Flash videos under one subscription.",
            ["Its listing names Veo 3.1 and Omni Flash for video, next to Sora 2, Kling 2.1 and Seedance 2.5.",
             "Chat with 30+ models, including Gemini 3.1 Pro, GPT-6 Astra and Claude Fable 5.1.",
             "Images with Nano Banana Pro and GPT Image 2."],
            "it needs iOS 26, it is a chat app first, and the plans range widely ($6.99 to $79.99 listed).",
            ["Plus from $6.99 to $79.99 listed, yearly $59.99; credits $9.99 or $19.99",
             "Veo 3.1 and Omni Flash",
             "13", "Data Used to Track You; Data Not Linked to You", "5.13 (24 Oct 2026)"]),
        app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13581,
            "the widest model list: Veo 3.1 next to Seedance 2.5, Sora 2, Kling, Hailuo and more.",
            ["Its listing names Veo 3.1 among more than a dozen video models.",
             "Also image models such as Nano Banana, Midjourney and Ideogram.",
             "Weekly, monthly and yearly plans, plus credits."],
            "English only, and its privacy label includes Data Used to Track You.",
            ["Weekly $5.99, yearly $99.99, Lite $15 or Pro $29 a month; credits $6.99 to $164.99",
             "Veo 3.1 among many video models",
             "1", "Data Used to Track You; Data Linked to You", "4.3.1 (30 Oct 2026)"]),
        app("Flashloop: AI Video Generator", 6746771178, "flashloop", "15557640 Canada Inc.", 4.73, 12417,
            "Veo 3 with sound effects, from an app whose label says it collects no data.",
            ["Its listing names Google Veo 3 for cinematic realism and sound effects, next to Sora 2, Grok Imagine and Kling 2.6.",
             "Text to video, image to video and an image generator.",
             "Its App Store privacy label is Data Not Collected."],
            "English only, and the listing still names Seedance 1.5 Pro, which ByteDance retired on 25 October 2026 according to Dora's model page.",
            ["Pro $7.99 to $24.99 listed, yearly $129.99; credits $4.99 to $59.99",
             "Veo 3 among several video models",
             "1", "Data Not Collected", "1.0.49 (15 Oct 2026)"]),
    ],
    "who": [
        "<strong>Google's own apps:</strong> Gemini on a Google AI plan, or Google Flow.",
        "<strong>Veo 3 inside a design editor:</strong> Canva.",
        "<strong>Veo 3 with photo editing:</strong> Picsart.",
        "<strong>Gemini Omni without a Google plan, cost shown first:</strong> Dora.",
        "<strong>Video and chat in one subscription:</strong> ChatNow.",
        "<strong>The most video models to compare:</strong> Pollo AI.",
    ],
    "cases": ["A short cinematic clip with sound from a sentence.", "Turning a photo into a video with a Google model.", "Trying Veo without a Google AI subscription."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «veo 3», «veo», «gemini omni», «google veo» and «ai video generator veo», and read each app's US App Store page and Apple's lookup data. We only included apps whose listing names Veo or Gemini Omni; for Dora, whose listing does not, we used its own model page. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a Veo app for iPhone?",
         "Not under that name. On 3 November 2026 the apps called Veo on the US App Store were a scooter service and a sports camera. Google offers video in the Gemini app (Gemini Omni, on Google AI Plus, Pro and Ultra) and in Google Flow, its creative studio app."),
        ("Can I make videos in Gemini for free?",
         "Its App Store listing says videos with Gemini Omni are for Google AI Plus, Pro, Ultra and Workspace users, so not on a free account."),
        ("Which apps offer Veo 3 on iPhone?",
         "Of the listings we read, Canva, Picsart, Leonardo.Ai and Flashloop name Veo 3, and ChatNow and Pollo AI name Veo 3.1."),
        ("What is Gemini Omni?",
         "Google's any-to-any video model: it makes video from text, reference photos or a video clip. Dora's model page lists it from 720p to 4K and 4 to 10 seconds."),
    ],
    "sources": [
        ("Google Gemini (App Store)", "https://apps.apple.com/us/app/id6477489729"),
        ("Google Flow (App Store)", "https://apps.apple.com/us/app/id6751294549"),
        ("Canva (App Store)", "https://apps.apple.com/us/app/id897446215"),
        ("Picsart (App Store)", "https://apps.apple.com/us/app/id587366035"),
        ("Leonardo.Ai (App Store)", "https://apps.apple.com/us/app/id1662773014"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora models and costs", "https://doravideo.com/models"),
        ("AI Chat Assistant – ChatNow (App Store)", "https://apps.apple.com/us/app/id1667518571"),
        ("Pollo AI (App Store)", "https://apps.apple.com/us/app/id6740024098"),
        ("Flashloop (App Store)", "https://apps.apple.com/us/app/id6746771178"),
    ],
}]
