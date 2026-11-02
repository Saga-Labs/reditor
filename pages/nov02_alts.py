"""Five "X alternatives for iPhone" pages, EN. Our app: Dora. Checked 2026-11-02: iTunes lookup and US App Store
pages for every app; what each app does comes from its own listing; no quality test. Each page has its own order,
text and FAQ. Encargo de saga-growth, 2 nov (sí de Marta a entradas nuevas)."""

D = "2026-11-02"
T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"


def app(name, id_, anchor, dev, rating, count, price, langs, priv, ver):
    return {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
            "_row": (price, str(langs), priv, ver, f"{rating:.1f} ({count:,} ratings)")}


A = {
    "dora": dict(app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
                     "Pro weekly ($4.99 and $6.99 listed), yearly $119.99; coin packs for subscribers, $3.99 to $224.99",
                     11, "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"), ours=True),
    "kling": app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32632,
                 "Standard $10 a month, Pro $37, Premier $92; one-week Standard from $1.19; credits $1.49 to $50",
                 5, T3, "3.9.30 (29 Oct 2026)"),
    "runway": app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19176,
                  "Standard $14.99 a month or $143.99 a year, Pro $35, Max $95; credits from $10",
                  1, T3, "103.0.0 (1 Nov 2026)"),
    "pika": app("Pika - AI Video", 6680155400, "pika", "Mellis, Inc.", 4.73, 4314,
                "Standard $8.99 a week, $16 a month or $96 a year; Pro $14.99 a week, $35 a month or $199 a year",
                1, "Data Linked to You; Data Not Linked to You", "1.12.1 (15 Jul 2026)"),
    "pixverse": app("PixVerse Lite", 6767802142, "pixverse", "AIVORA PTE. LTD.", 4.31, 2564,
                    "Elite $5.99 a week or $49.99 a year; credit packs $5 to $100",
                    14, T3, "0.8.1 (21 Sep 2026)"),
    "luma": app("Luma Dream Machine", 6478852867, "luma", "Luma AI, Inc.", 4.5, 1799,
                "Lite $9.99 a month or $95.99 a year, Plus $29.99 or $289.99, Unlimited $94.99 or $919.99; credits from $4",
                1, "Data Linked to You", "2.0.8 (17 Apr 2026)"),
    "pollo": app("Pollo AI: AI Video & Image", 6740024098, "pollo", "COCOSOFT TECHNOLOGY PTE. LTD.", 4.47, 13568,
                 "Weekly $5.99, yearly $99.99, monthly $15 or $29; credits $6.99 to $164.99",
                 1, "Data Used to Track You; Data Linked to You", "4.3.1 (30 Oct 2026)"),
    "invideo": app("invideo: AI Video Editor", 6471394316, "invideo", "Invideo Inc", 4.55, 28012,
                   "Plus $24 or $30, Max $72, Generative $143.99; add-ons from $12",
                   1, T3, "4.5.63 (27 Oct 2026)"),
    "shots": app("Shots: Photo & Video Generator", 6745820631, "shots", "Deepix AI Yazilim Teknolojileri Anonim Sirketi", 4.46, 18492,
                 "Several weekly plans listed, $4.99 to $12.99; coin packs from $9.99",
                 5, T3, "1.7.0 (16 Aug 2026)"),
    "gemini": app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2391162,
                  "Google AI Plus $4.99, Pro $19.99, Ultra $199.99",
                  70, "Data Linked to You", "1.2026.4262206 (29 Oct 2026)"),
    "grok": app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1565158,
                "SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; extra credits from $5",
                38, T3, "1.4.60 (30 Oct 2026)"),
}

FACTS = {
    "dora": ["Starts from a photo or a written description; a video takes about two minutes, per its listing.",
             "Vertical, horizontal or square, up to 1080p, no watermark. The coin cost shows before you generate, and failed generations refund the coins.",
             "The same account and coins work on doravideo.com and in AI assistants through its connector."],
    "kling": ["Up to 15 seconds in native 1080p or 4K, and Video Extension up to 3 minutes, per its listing.",
              "A community feed with Clone & Try: copy a work you like and try the idea yourself."],
    "runway": ["Lists Seedance 2.5, Kling 3 Pro, Gen-4.5, Nano Banana Pro and Nano Banana 2 in one app.",
               "Runway Agent plans shots, generates them and assembles the video from a conversation."],
    "pika": ["Built around changing what you already have: Pikaswaps replaces elements in your video and Pikadditions drops new objects into it.",
             "Pikaffects such as Melt, Explode and Squish on your photos; custom reaction GIFs from one selfie."],
    "pixverse": ["Text to video and image to video on PixVerse V6, plus access to outside models, per its listing.",
                 "Modify Video edits selected parts, Transition joins a first and last frame, and upscaling goes up to 4K."],
    "luma": ["Talk to it instead of writing prompts; Modify edits images and videos from a description.",
             "Reference up to 4 images, and keep a character consistent from one photo of their face."],
    "pollo": ["Takes ideas, scripts, photos, product images, URLs or reference videos, per its listing.",
              "Also has an image generator, an ad maker and design tools."],
    "invideo": ["Agent Two develops a video from everyday language, and every AI edit stays editable on a multitrack timeline.",
                "Its listing says 200+ AI models for image, video, voice, sound and music."],
    "shots": ["Text to video and photo to video, from a prompt or a style, with no timeline.",
              "Also restores old or blurry photos and makes AI portraits."],
    "gemini": ["A general AI assistant; its listing says cinematic videos with Gemini Omni are for Google AI Plus, Pro, Ultra and Workspace users.",
               "Comes with a chat assistant and storage on the Google AI plans, so it can make sense if you already pay for them."],
    "grok": ["A general AI assistant; Grok Imagine makes short videos with sound from text, or from your photos.",
             "Plans also cover chat and research, so it is not a pure video purchase."],
}

LIMITS = {
    "dora": "no free video (a plan is needed; coin packs are for subscribers), no timeline editing of long videos and no publishing to your accounts.",
    "kling": "credits are sold on top of the plans, so check what a long video costs first; 5 languages.",
    "runway": "the App Store lists one language (English), and extra credits are sold on top of the plans.",
    "pika": "last updated on 15 July 2026, English only, and its listing is about effects and swaps rather than long scenes from text.",
    "pixverse": "still version 0.8.1.",
    "luma": "last updated on 17 April 2026, English only, and the top plans are the most expensive listed here.",
    "pollo": "English only, and credits are not cheap at the small packs ($6.99 for 100).",
    "invideo": "English only, the highest entry price here, and more complex than an app that makes one clip.",
    "shots": "last updated on 16 August 2026, and many weekly plans are listed, so check which one you are offered.",
    "gemini": "no video on the free plan according to its listing, and no video-specific tools such as templates in the listing.",
    "grok": "its privacy label lists all three data groups, and its listing says little about clip length or resolution.",
}

COLUMNS = ["App", "Price (US)", "Good for", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"]
NOTE = "Prices are in-app purchases listed on each US App Store page on 2 November 2026; pages list only some of them. All are free to download. Ratings are that day's App Store average and count."
METHOD = ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data: purchases, version, rating, languages and privacy label. What each app does comes from its own listing. We ran no quality test, so this page does not say which video looks best.",
          "Prices change often. Check inside each app before paying."]


def page(slug, ct, title, h1, desc, llms, answer, picks, good, best, who, cases, faq, extra_sources=()):
    apps = []
    for key in ["dora"] + picks:
        a = {k: v for k, v in A[key].items() if k != "_row"}
        r = A[key]["_row"]
        a.update(row=[r[0], good[key], *r[1:]], best_for=best[key], facts=FACTS[key], limits=LIMITS[key])
        apps.append(a)
    return {"group": slug, "lang": "en", "store": "us", "path": slug + "/", "ct": ct, "category": "PhotoVideoApplication",
            "published": D, "updated": D, "checked": D, "ours_rank": 4, "title": title, "h1": h1, "description": desc,
            "llms": llms, "answer": answer, "columns": COLUMNS, "table_note": NOTE, "apps": apps,
            "who": who, "cases": cases, "method": METHOD, "faq": faq, "related": RELATED,
            "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in apps] + list(extra_sources)}


RELATED = ["kling-alt", "runway-alt", "pika-alt", "hailuo-alt", "pixverse-alt"]

KLING = page("kling-ai-alternatives-iphone", "rd-kling", "Best Kling AI Alternatives for iPhone (2026)", "Best Kling AI alternatives for iPhone in 2026",
    "Six iPhone apps to use instead of Kling AI: Runway, PixVerse Lite, Luma, Dora, Pollo AI and Grok, compared by price, what each is good for and privacy label.",
    "Six iPhone alternatives to Kling AI (Runway, PixVerse Lite, Luma Dream Machine, Dora, Pollo AI, Grok) by price, use and App Store privacy label.",
    ["Kling AI's strength is length and resolution: its listing promises up to 15 seconds in native 1080p or 4K, extendable to 3 minutes, and it starts at $10 a month or a one-week Standard from $1.19. People look elsewhere for more models in one place, a simpler app, or a plan that is not based on credit packs.",
     "If you want Kling's model and others in the same app, Runway lists Kling 3 Pro next to Seedance 2.5 and Gen-4.5. For a cheap weekly plan, PixVerse Lite and Pollo AI list $5.99. For one short clip with the cost shown first, Dora. If you already pay for Grok, Grok Imagine makes short videos too."],
    ["runway", "pixverse", "luma", "pollo", "grok"],
    dict(dora="One short clip from a photo or text, cost shown first", runway="Several models, Kling 3 Pro included, in one app", pixverse="A cheap weekly plan, editing parts of a video", luma="Asking in plain words, consistent characters", pollo="Ads and store content as well as video", grok="Video as an extra on a chat plan"),
    dict(dora="someone who wants a short vertical clip and to see the coin cost before tapping.", runway="people who want to pick the model for each job, Kling's included.", pixverse="trying AI video on a weekly plan, with credit packs when needed.", luma="people who would rather describe changes than write prompts.", pollo="sellers who also need ads and product images.", grok="people already paying for Grok who want occasional clips."),
    ["<strong>Same model, more choice:</strong> Runway.", "<strong>Lowest weekly plan listed:</strong> PixVerse Lite or Pollo AI ($5.99).", "<strong>One clip, cost first:</strong> Dora.", "<strong>Long videos up to 3 minutes:</strong> stay on Kling, whose listing says so."],
    ["A longer scene built from several clips.", "Comparing models on the same idea.", "A short vertical clip for a social post."],
    [("Is there an app with Kling inside?", "Runway's App Store listing names Kling 3 Pro among its models, so you can use it there with Runway's own plans and credits."),
     ("Which Kling alternative has the lowest weekly price?", "Of those listed on 2 November 2026, PixVerse Lite and Pollo AI at $5.99 a week. Dora lists $4.99 and $6.99 weekly plans; check which one you are offered in the app."),
     ("Do any of these beat Kling on video length?", "We could not confirm that from the listings. Kling is the one that states 3 minutes with extension; PixVerse Lite mentions endless extension without a figure.")])
KLING["group"] = "kling-alt"

RUNWAY = page("runway-alternatives-iphone", "rd-runway", "Best Runway Alternatives for iPhone (2026)", "Best Runway alternatives for iPhone in 2026",
    "Six iPhone apps to use instead of Runway: Kling AI, invideo, Luma, Dora, Google Gemini and Pika, compared by price, use and App Store privacy label.",
    "Six iPhone alternatives to Runway (Kling AI, invideo, Luma Dream Machine, Dora, Google Gemini, Pika) by price, use and App Store privacy label.",
    ["Runway on iPhone is a many-models app with an agent that builds whole videos, from $14.99 a month, and the App Store lists English only. Look elsewhere if you need other languages, a lower entry price, or a real editing timeline.",
     "Kling AI starts at $10 a month and lists 5 languages. invideo gives you a multitrack timeline with its own agent. Google Gemini makes video from the $4.99 Plus plan, if you also want an assistant. Dora makes one short clip with the cost shown first, in 11 languages."],
    ["kling", "invideo", "luma", "gemini", "pika"],
    dict(dora="One short clip, 11 languages, cost shown first", kling="Longer clips and 4K from one model family", invideo="Agent plus a real timeline editor", luma="Plain-language edits, consistent characters", gemini="Video included with a Google AI plan", pika="Changing your own clips and photos"),
    dict(dora="someone who does not want to choose between models and just needs a short clip.", kling="people who want length and resolution at a lower monthly entry price.", invideo="teams who want to keep editing by hand after the AI draft.", luma="people who prefer to ask for changes in words.", gemini="people who already use or want a Google AI plan.", pika="playful edits of your own videos and photos."),
    ["<strong>Timeline editing:</strong> invideo.", "<strong>Lowest monthly plan listed:</strong> Google AI Plus ($4.99), though it is not a video plan as such.", "<strong>Length and 4K:</strong> Kling AI.", "<strong>A short clip without choosing a model:</strong> Dora."],
    ["A short film from many generated shots.", "Editing an AI draft by hand.", "A quick clip for a social post."],
    [("What is the closest app to Runway on iPhone?", "For an agent plus editing, invideo. For model quality claims we cannot say: we ran no quality test."),
     ("Is there a Runway alternative with a real timeline?", "invideo's listing describes a multitrack timeline with trimming, layers, keyframes and captions."),
     ("Is Runway available in other languages on iPhone?", "On 2 November 2026 its US listing shows one language. Kling AI shows 5, Dora 11 and Google Gemini 70.")])
RUNWAY["group"] = "runway-alt"

PIKA = page("pika-alternatives-iphone", "rd-pika", "Best Pika Alternatives for iPhone (2026)", "Best Pika alternatives for iPhone in 2026",
    "Six iPhone apps to use instead of Pika: PixVerse Lite, Shots, Kling AI, Dora, Pollo AI and Grok, compared by price, use and App Store privacy label.",
    "Six iPhone alternatives to Pika (PixVerse Lite, Shots, Kling AI, Dora, Pollo AI, Grok) by price, use and App Store privacy label.",
    ["Pika's app is about playing with what you already have: swap things in a video, add objects, or apply effects like Melt and Squish, from $8.99 a week. Its last update on the App Store is from 15 July 2026 and it lists English only.",
     "If you like effects and templates, PixVerse Lite and Shots are the closest and list more languages. If you want to generate scenes from text instead, Kling AI goes up to 15 seconds in 1080p or 4K. Dora makes one short clip from a photo or description with the cost shown first."],
    ["pixverse", "shots", "kling", "pollo", "grok"],
    dict(dora="One short clip from a photo or text, cost shown first", pixverse="Effects, templates and editing parts of a video", shots="Photo to video from a style, no timeline", kling="Scenes from text, up to 4K", pollo="Ads and store content as well as video", grok="Video as an extra on a chat plan"),
    dict(dora="someone who wants a new clip from a photo or an idea rather than an effect on an old one.", pixverse="the nearest match to Pika's effects and video edits, at a lower weekly price.", shots="quick results from one photo and a style.", kling="people moving from effects to longer generated scenes.", pollo="sellers making ads rather than memes.", grok="people already paying for Grok."),
    ["<strong>Closest to Pika's effects:</strong> PixVerse Lite.", "<strong>From one photo and a style:</strong> Shots.", "<strong>Longer scenes:</strong> Kling AI.", "<strong>A new short clip, cost first:</strong> Dora."],
    ["A funny effect on your own photo.", "Replacing something in a video you filmed.", "A short clip from a written idea."],
    [("Is Pika still updated?", "Its App Store page shows version 1.12.1 from 15 July 2026, the newest on 2 November 2026. We do not know its plans."),
     ("Which alternative edits parts of an existing video like Pikaswaps?", "PixVerse Lite's Modify Video edits selected parts using images, clips or modes, per its listing."),
     ("Is there a cheaper plan than Pika's?", "Pika lists $8.99 a week. PixVerse Lite and Pollo AI list $5.99, and Dora lists $4.99 and $6.99.")])
PIKA["group"] = "pika-alt"

HAILUO = page("hailuo-alternatives-iphone", "rd-hailuo", "Best Hailuo Alternatives for iPhone (2026)", "Best Hailuo AI alternatives for iPhone in 2026",
    "We could not find an official Hailuo app on the US App Store on 2 November 2026. Six iPhone apps to use instead: Kling, Runway, PixVerse Lite, Dora, Luma, Gemini.",
    "Notes that no official Hailuo app could be found on the US App Store on 2 November 2026 and warns about lookalikes; compares six iPhone alternatives (Kling AI, Runway, PixVerse Lite, Dora, Luma Dream Machine, Google Gemini).",
    ["<strong>On 2 November 2026 we could not find an official Hailuo app on the US App Store.</strong> Apple's lookup returned nothing for app IDs that third-party pages give for it (6741675037 and 6744235105), and its page returned 404. A US search for «hailuo» showed apps from unrelated developers, and we cannot confirm any link between them and MiniMax. Check the developer before paying. Hailuo itself is at <a href=\"https://hailuoai.video/\">hailuoai.video</a>, in the browser.",
     "If you want an app on iPhone, Kling AI is the nearest in type: one video model family, text and image to video. Runway gathers several models. PixVerse Lite has a lower weekly price. Dora makes one short clip with the cost shown first."],
    ["kling", "runway", "pixverse", "luma", "gemini"],
    dict(dora="One short clip from a photo or text, cost shown first", kling="Text and image to video, up to 4K", runway="Several models in one app", pixverse="A cheap weekly plan, 14 languages", luma="Plain-language edits, consistent characters", gemini="Video included with a Google AI plan"),
    dict(dora="someone who wants a short clip on the phone without choosing a model.", kling="the closest kind of app to Hailuo on iPhone.", runway="people who want to pick among several current models.", pixverse="trying AI video on a weekly plan.", luma="people who prefer to ask for changes in words.", gemini="people who already use a Google AI plan."),
    ["<strong>Closest in type:</strong> Kling AI.", "<strong>Many models:</strong> Runway.", "<strong>Lowest weekly plan among video apps here:</strong> Dora or PixVerse Lite.", "<strong>Staying with Hailuo:</strong> use its website in Safari."],
    ["Text to video on the phone.", "Animating a still image.", "Avoiding lookalike apps."],
    [("Is there an official Hailuo app for iPhone?", "We could not find one on the US App Store on 2 November 2026. Earlier third-party pages mention listings that no longer answer in Apple's lookup. It may be sold in other countries or come back."),
     ("Is an app called Hailuo on the App Store safe to pay for?", "We cannot tell. Look at the developer name and compare it with what hailuoai.video links to before paying."),
     ("Can I use Hailuo on iPhone without an app?", "Its website is at hailuoai.video. We did not test it on iPhone.")],
    [("Hailuo official site", "https://hailuoai.video/")])
HAILUO["group"] = "hailuo-alt"

PIXVERSE = page("pixverse-alternatives-iphone", "rd-pixverse", "Best PixVerse Alternatives for iPhone (2026)", "Best PixVerse alternatives for iPhone in 2026",
    "Six iPhone apps to use instead of PixVerse Lite: Kling AI, Pika, Shots, Dora, Pollo AI and Runway, compared by price, use and App Store privacy label.",
    "Six iPhone alternatives to PixVerse Lite (Kling AI, Pika, Shots, Dora, Pollo AI, Runway) by price, use and App Store privacy label.",
    ["On the US App Store the app is called PixVerse Lite, at version 0.8.1 from 21 September 2026, with Elite at $5.99 a week or $49.99 a year. It is hard to beat on price among these, so the reasons to leave are others: more ratings, a different way of working, or a simpler app.",
     "Kling AI has far more ratings and states length and resolution clearly. Pika is for changing your own clips. Shots works from one photo and a style. Runway gives you several outside models and an agent. Dora makes one short clip with the cost shown first and no watermark."],
    ["kling", "pika", "shots", "pollo", "runway"],
    dict(dora="One short clip, no watermark, cost shown first", kling="Stated length and resolution, many ratings", pika="Changing your own clips and photos", shots="Photo to video from a style", pollo="Ads and store content as well as video", runway="Several models and an agent in one app"),
    dict(dora="someone who wants one clip and to see the coin cost before tapping.", kling="people who want 15 seconds in 1080p or 4K, and up to 3 minutes with extension.", pika="people who like effects on what they already filmed.", shots="quick results without writing a prompt.", pollo="sellers who need ads and product images.", runway="people who want to pick the model and let an agent assemble the video."),
    ["<strong>Most ratings among video apps here:</strong> Kling AI.", "<strong>Effects on your clips:</strong> Pika.", "<strong>No prompt:</strong> Shots.", "<strong>Many models:</strong> Runway.", "<strong>A short clip, cost first:</strong> Dora."],
    ["A clip from one photo.", "An effect on your own video.", "A longer scene from text."],
    [("Is PixVerse Lite the same as PixVerse?", "Its listing says it is powered by PixVerse V6. On 2 November 2026 a US App Store search for «pixverse» showed PixVerse Lite and no other app from the same developer."),
     ("Which alternative is cheaper than PixVerse Lite?", "Few are. Pollo AI lists the same $5.99 a week, and Dora lists $4.99 and $6.99 weekly plans. Among yearly plans listed on this page, PixVerse Lite's $49.99 is the lowest."),
     ("Which has the most ratings?", "On 2 November 2026 Kling AI had 32,632 and Runway 19,176 in the US, against 2,564 for PixVerse Lite.")])
PIXVERSE["group"] = "pixverse-alt"

PAGES = [KLING, RUNWAY, PIKA, HAILUO, PIXVERSE]
for _p in PAGES:
    _p["related"] = [g for g in RELATED if g != _p["group"]]
