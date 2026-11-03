"""AI video apps without a watermark on iPhone, EN. Our app: Dora (id6754180384), whose listing says «No watermark on your videos».

Checked 2026-11-03: iTunes lookup and the US App Store page of every app (price list, privacy label); the watermark
facts come only from each developer: its App Store listing or its own plan page (pika.art/pricing,
app.klingai.com membership plans, runwayml.com/pricing, CapCut newsroom on Dreamina Seedance 2.0). Third-party
«how to remove the watermark» pages were not used. PixVerse is left out: its plan page is for pixverse.ai, and the
iPhone app «PixVerse Lite» is published by another company (AIVORA PTE. LTD.). Gemini is left out: no current
Google page on watermarks for its video model was found. Why this topic: Google suggests «ai video generator
without watermark», «... free», «ai video maker without watermark» (3 Nov) and no page on the 4 sites has
«watermark» in its URL (sitemaps read 3 Nov); registered in ios-playbook references/temas-webs.md. No quality test,
nothing generated.
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
    "group": "no-watermark", "lang": "en", "store": "us",
    "path": "ai-video-apps-without-watermark-iphone/",
    "ct": "rd-no-watermark-video-iphone",
    "category": "PhotoVideoApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "AI Video Apps Without a Watermark on iPhone (2026): 7 Apps Checked",
    "h1": "AI video apps without a watermark on iPhone in 2026",
    "description": "Which iPhone AI video apps add a watermark and which plan removes it, per each developer: Pika, Kling, Runway, Dora, VIDIOAI, MagicLight and CapCut.",
    "llms": "Checks seven iPhone AI video apps for a visible watermark, using only each developer's App Store listing or plan page: Pika (no watermark on any plan, per pika.art), Kling and Runway (removed from the cheapest paid plan), Dora and VIDIOAI (listings say no watermark), MagicLight (watermark control needs a subscription) and CapCut (labels AI-generated video with visible watermarks), with US App Store prices and privacy labels.",
    "answer": [
        "<strong>Most AI video apps put a watermark on free videos and remove it once you pay.</strong> We checked what each developer says itself, on 3 November 2026. Pika is the exception: its plan page lists «No watermark» on every plan, including the free one, which works with credit packs. Kling's and Runway's plan pages list watermark removal from their cheapest paid plan (Standard), and MagicLight says watermark control needs a subscription.",
        "Dora and VIDIOAI say in their App Store listings that videos have no watermark, but neither listing mentions free videos: Dora needs its Pro plan, and VIDIOAI sells a weekly or yearly plan and credits. CapCut goes the other way: it says it labels AI-generated video, such as clips made with Seedance, with a visible watermark and Content Credentials. Some apps also add invisible marks or metadata that a watermark-free file can still carry; we only report the visible watermark each developer describes.",
    ],
    "columns": ["App", "Watermark, per the developer", "Price (US App Store)", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Watermark facts come from each developer's App Store listing or plan page on 3 November 2026; plan pages are for the developer's website and may differ from what is sold in the app. Prices are in-app purchases listed on each US App Store page that day; pages list only some. All are free to download.",
    "apps": [
        app("Pika - AI Video", 6680155400, "pika", "Mellis, Inc.", 4.73, 4321,
            "watermark-free clips without a subscription, using credit packs.",
            ["pika.art's plan page lists «No watermark» on every plan, including Free, which has no monthly credits and works with credit packs.",
             "Effects and swaps on your own photos and videos: Pikaswaps, Pikadditions, Pikaffects and Pikascenes, per its App Store listing.",
             "Version 2.0.0 came out on 2 November 2026."],
            "English only, the Free plan has no commercial license per pika.art, and the app is built around effects rather than long scenes from text.",
            ["No watermark on any plan, including Free (pika.art)",
             "Standard $8.99 a week, $16 a month or $96 a year; Pro $14.99 a week, $35 a month or $199 a year",
             "1", "Data Linked to You; Data Not Linked to You", "2.0.0 (2 Nov 2026)"]),
        app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32798,
            "people who want Kling's own models and are ready for the Standard plan.",
            ["Kling's membership page lists «Brand watermark removal» on Standard, Pro, Premier and Ultra+, so it is part of every paid plan.",
             "Up to 15 seconds in native 1080p or 4K, and Video Extension up to 3 minutes, per its listing.",
             "A one-week Standard membership is listed from $1.19 on the App Store."],
            "the free plan does not list watermark removal, and credits are sold on top of the plans.",
            ["Removed on every paid plan, from Standard (Kling membership page)",
             "Standard $10 a month, Pro $37, Premier $92; one-week Standard from $1.19; credits $1.49 to $50",
             "5", T3, "3.9.32 (2 Nov 2026)"]),
        app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19176,
            "several models in one app (Seedance 2.5, Kling 3 Pro, Gen-4.5) with no watermark from Standard.",
            ["runwayml.com/pricing lists «No watermarks» on Standard and higher plans; the Free plan, 125 one-time credits, does not list it.",
             "Its listing names Seedance 2.5, Kling 3 Pro, Gen-4.5, Nano Banana Pro and Nano Banana 2 in one app.",
             "Runway Agent plans, generates and assembles a whole video from a conversation."],
            "English only, and its Standard plan costs more in the app ($14.99 a month) than on the website ($12 a month billed yearly).",
            ["«No watermarks» from Standard; not listed on Free (runwayml.com/pricing)",
             "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits from $10",
             "1", T3, "103.0.0 (1 Nov 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
            "short videos from a photo or an idea, with no watermark and the coin cost shown first.",
            ["Its App Store listing says «No watermark on your videos», and doravideo.com says paid-plan videos need no attribution.",
             "Vertical 9:16 for TikTok, Reels and Shorts, up to 1080p, saved to the camera roll or shared from the app.",
             "The coin cost shows before you generate, and failed generations refund the coins."],
            "no free videos: you need the Pro plan, and coin packs are for subscribers. Only 16 ratings.",
            ["No watermark, per its listing (no free plan)",
             "Pro weekly $4.99 or $6.99, yearly $119.99; coin packs $3.99 to $224.99",
             "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("AI Video Generator: VIDIOAI", 6478830556, "vidioai", "Joy Sarkar", 4.42, 2135,
            "trying several outside models in one app, with exports its listing says have no watermark.",
            ["Its listing says «Up to 1080p, no watermark».",
             "It names Kling AI, Seedance 2.0, Veo 3, Sora 2 and Wan 2.1 as the models behind it, and says it is not affiliated with Google, OpenAI or ByteDance.",
             "Text to video, image to video, effects and face animation."],
            "made by an individual developer, its subscription is weekly or yearly only, and the listing does not say how it reaches those models.",
            ["No watermark, per its listing",
             "Pro $9.99 a week or $59.99 a year; credits and coins $5.99 to $99.99",
             "3", "Data Used to Track You; Data Not Linked to You", "5.8 (22 Oct 2026)"]),
        app("MagicLight: AI Video generator", 6748646938, "magiclight", "MAGICLIGHTHKLIMITED", 4.55, 131,
            "longer animated story videos with the same characters, up to 30 minutes.",
            ["Its listing says watermark control, longer exports, some styles and higher resolutions require a subscription.",
             "Turns a script into an animated video with consistent characters, voiceover and lip-sync.",
             "Exports up to 30 minutes per video with a subscription."],
            "English only, few ratings (131), and the listing does not say which plan removes the watermark.",
            ["Watermark control needs a subscription, per its listing",
             "Standard $10.90 to $12 a month or $72 a year, Plus $26, Pro $31.90 to $35 a month; credits $18 to $88",
             "1", T3, "1.2.22 (7 Oct 2026)"]),
        app("CapCut: Photo & Video Editor", 1500855883, "capcut", "BYTEDANCE PTE. LTD.", 4.61, 1125712,
            "editing a video with captions and effects, if a label on the AI part is fine.",
            ["CapCut's newsroom says it labels AI-generated content made with Dreamina Seedance 2.0 with visible watermarks and embeds C2PA Content Credentials.",
             "It also says it adds invisible watermarking to identify content made with that model.",
             "A full editor: timeline, keyframes, auto captions and background removal."],
            "the AI-made part of a video carries a visible label by design, and the App Store listing does not say a plan removes it.",
            ["Visible watermark on AI-generated video (CapCut newsroom)",
             "Standard $9.99 a month, Pro $19.99; yearly $89.99",
             "20", "Data Used to Track You; Data Linked to You", "19.9.0 (27 Oct 2026)"]),
    ],
    "who": [
        "<strong>No watermark without a subscription:</strong> Pika, with credit packs.",
        "<strong>Kling's own models, watermark-free:</strong> Kling on any paid plan.",
        "<strong>Several models in one app:</strong> Runway from Standard.",
        "<strong>Short social videos from a photo, cost shown first:</strong> Dora.",
        "<strong>Long animated stories:</strong> MagicLight with a subscription.",
        "<strong>Editing, where an AI label is acceptable:</strong> CapCut.",
    ],
    "cases": ["Posting a clip on TikTok or Reels without another app's logo.", "Using an AI video in an ad.", "Checking whether a free plan is enough."],
    "method": [
        "On 3 November 2026 we read each app's US App Store page and Apple's lookup data, and, for watermarks, only what each developer says: its App Store listing or its own plan page (pika.art, Kling's membership page, runwayml.com/pricing, CapCut's newsroom). We did not use third-party guides and ran no test, so we did not check the files ourselves.",
        "We left out PixVerse because its plan page covers pixverse.ai while its iPhone app, PixVerse Lite, is published by another company, and Google Gemini because we found no current Google page on watermarks for its video model.",
        "Prices and plans change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Which AI video app has no watermark on the free plan?",
         "Of the apps we checked, Pika: pika.art lists «No watermark» on its Free plan, which works with credit packs rather than monthly credits."),
        ("Does paying remove the watermark in Kling and Runway?",
         "Yes, according to their own plan pages: Kling lists brand watermark removal on every paid plan from Standard, and Runway lists no watermarks from Standard. Neither lists it on its free plan."),
        ("Does a video without a visible watermark have no AI marks at all?",
         "Not necessarily. CapCut says it also adds invisible watermarking and Content Credentials, and other developers may add metadata. We only report the visible watermark each developer describes."),
        ("Is it allowed to remove a watermark with another app?",
         "Check each app's terms first. The developers' own way to get files without a watermark is the plan or listing described above."),
    ],
    "sources": [
        ("Pika plans (pika.art)", "https://pika.art/pricing"),
        ("Pika - AI Video (App Store)", "https://apps.apple.com/us/app/id6680155400"),
        ("Kling AI membership plans", "https://app.klingai.com/global/membership/membership-plan"),
        ("Kling AI (App Store)", "https://apps.apple.com/us/app/id6738049229"),
        ("Runway pricing", "https://runwayml.com/pricing"),
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora pricing", "https://doravideo.com/pricing"),
        ("AI Video Generator: VIDIOAI (App Store)", "https://apps.apple.com/us/app/id6478830556"),
        ("MagicLight (App Store)", "https://apps.apple.com/us/app/id6748646938"),
        ("CapCut (App Store)", "https://apps.apple.com/us/app/id1500855883"),
        ("Dreamina Seedance 2.0, CapCut newsroom", "https://www.capcut.com/newsroom/dreamina-seedance-2"),
    ],
}]
