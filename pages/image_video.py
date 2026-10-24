"""Two Dora pages, EN: "Viggle AI alternatives for iPhone" and "Best AI image to
video apps for iPhone". Our app: Dora (id6754180384).

Checked 2026-10-16: iTunes lookup API and US App Store web pages for Dora,
Viggle AI, Kling AI, Runway, PixVerse Lite, Shots and Motionleap. What Dora does
comes from its App Store listing (1.4.1). Competitor features are what their
own listings say; no quality test was run. Purchases shown are the ones the
App Store page lists (it lists only some).
"""

CHECKED = "2026-10-16"
PRIV3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"

DORA = {
    "name": "DORA · AI Video Generator", "id": 6754180384, "ours": True, "anchor": "dora",
    "developer": "Saga Ltd.", "rating": (4.27, 15),
    "best_for": "turning one photo into a short vertical video for TikTok or Reels, with the coin cost shown before you tap.",
    "facts": [
        "Bring a photo to life as a short video, or write a description; a video takes about two minutes.",
        "Motion Control copies the moves of a dance video onto the person in your photo.",
        "Vertical 9:16, horizontal or square, up to 1080p, no watermark. Every generation shows its cost in coins first, and failed generations refund the coins.",
        "Same account and coins on doravideo.com and inside AI assistants such as Claude through the Dora connector.",
        "11 languages, iOS 18.6 or later, 62 MB.",
    ],
    "limits": "there is no free video (you need coins or a plan), only 15 ratings in the US so far, and Motion Control needs a person in the photo. It has no community feed and no photo editor.",
}

VIGGLE_ROW_PRICE = "Pro $4.99 a week, $9.99 a month or $95.90 a year; Live plans $24.99 to $79.99 a month; extra credits $3 to $15"

EN1 = {
    "group": "viggle-alt", "lang": "en", "store": "us",
    "path": "viggle-ai-alternatives-iphone/",
    "ct": "rd-viggle",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Viggle AI Alternatives for iPhone (2026)",
    "h1": "Viggle AI alternatives for iPhone in 2026",
    "description": "Five iPhone apps to use instead of, or next to, Viggle AI: Dora, PixVerse Lite, Kling AI, Runway and Shots. Prices, ratings and privacy checked.",
    "llms": "Compares Viggle AI with five iPhone alternatives (Dora, PixVerse Lite, Kling AI, Runway, Shots) by price, how each animates a photo, ratings, languages and App Store privacy label.",
    "disclosure": "Dora is made by Saga Labs, the company behind Reditor. It is one more option in this list, not placed first because it is ours, and it has far fewer ratings than most apps here. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "Viggle AI is built around putting your photo into a video clip or one of its 8,000+ templates. If you want that same move-copying, Dora and PixVerse Lite both have a Motion Control feature that takes a photo plus a reference video. If you would rather have a general AI video tool, Kling AI and Runway generate video from images and text with longer clips and more models, at higher prices. Shots is a template-driven app in the style of Viggle.",
        "Viggle itself has an English-only interface (so does Runway) and a Pro plan from $4.99 a week; all six apps are free to download and charge to make videos.",
    ],
    "columns": ["App", "Price (US)", "How it animates a photo", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the in-app purchases listed on each US App Store page on 16 October 2026 (pages list only some of them). Ratings are the App Store average and number of ratings that day. Viggle is included for comparison; the other five are the alternatives.",
    "apps": [
        dict(DORA, row=["Pro weekly $4.99 or $9.99, Pro yearly $119.99; coin packs from $2.99 to $199.99",
                        "Photo or text to video; Motion Control copies a dance video onto your photo",
                        "11", "Data Used to Track You; Data Not Linked to You", "1.4.1 (9 Oct 2026)", "4.3 (15 ratings)"]),
        {
            "name": "PixVerse Lite", "id": 6767802142, "anchor": "pixverse",
            "developer": "AIVORA PTE. LTD.", "rating": (4.31, 1695),
            "row": ["Elite $5.99 a week or $49.99 a year; credit packs $5 to $100",
                    "Image to video, Motion Control (character image plus reference motion video), templates",
                    "14", PRIV3, "0.8.1 (21 Sep 2026)", "4.3 (1,695 ratings)"],
            "best_for": "people who want Motion Control plus dance and effect templates in a broader video toolbox.",
            "facts": [
                "Its listing describes Motion Control as uploading a character image and a reference motion video.",
                "Also text to video, transitions, video extension and upscaling up to 4K.",
                "14 languages, iOS 15 or later, 121 MB.",
            ],
            "limits": "a version number below 1.0 (0.8.1), a broad interface where the motion feature takes more taps to find, and a privacy label with tracking and linked data.",
        },
        {
            "name": "Kling AI: AI Image&Video Maker", "id": 6738049229, "anchor": "kling",
            "developer": "KLING AI PTE. LTD.", "rating": (4.68, 31671),
            "row": ["Standard $10 a month, Pro $37, Premier $92; short memberships from $1.19 a week; credits $5 to $100",
                    "Image or text to video, up to 15 s in 1080p or 4K, extension up to 3 minutes",
                    "5", PRIV3, "3.8.20 (11 Sep 2026)", "4.7 (31,671 ratings)"],
            "best_for": "longer, higher-quality clips and 4K images, with a community to browse and clone ideas from.",
            "facts": [
                "Its listing says clips of up to 15 seconds in native 1080p or 4K, and Video Extension to reach up to 3 minutes.",
                "Image generation at 4K, and a community feed where you can clone other people's ideas.",
                "5 languages, iOS 14 or later, 238 MB.",
            ],
            "limits": "it is a full creative platform, not a one-tap dance or meme app, and the higher plans cost much more per month than Viggle's weekly plan.",
        },
        {
            "name": "Runway: AI Image & Video", "id": 1665024375, "anchor": "runway",
            "developer": "Runway AI, Inc.", "rating": (4.48, 17539),
            "row": ["Standard $14.99 a month or $143.99 a year; Pro $35; Max $95; credits $10 to $100",
                    "Text, image and video to video with several models, plus an Agent that builds a video from a conversation",
                    "1 (English)", PRIV3, "100.0.0 (13 Oct 2026)", "4.5 (17,539 ratings)"],
            "best_for": "polished, controlled video where you want to pick the model, aimed at ads and short films.",
            "facts": [
                "Its listing says it bundles several named video and image models in one app.",
                "Runway Agent plans shots and assembles a video from a plain-language chat.",
                "English interface, iOS 16.4 or later, 129 MB.",
            ],
            "limits": "the cheapest listed plan is $14.99 a month, it is built for professional-style video rather than viral memes, and the interface is English only.",
        },
        {
            "name": "Shots: Photo & Video Generator", "id": 6745820631, "anchor": "shots",
            "developer": "Deepix AI Yazilim Teknolojileri Anonim Sirketi", "rating": (4.47, 18177),
            "row": ["Weekly $6.99 to $12.99; yearly $39.99 or $79.99; coin packs $9.99 to $34.99",
                    "Photo or text to video, a library of dance templates, photo restore",
                    "5", PRIV3, "1.7.0 (16 Aug 2026)", "4.5 (18,177 ratings)"],
            "best_for": "quick dance and trend templates from a selfie or a pet photo.",
            "facts": [
                "Its listing says a growing library of viral dance templates; upload your photo or pet.",
                "Also portraits, business shots and one-tap enhancing of old or blurry photos.",
                "5 languages, iOS 16 or later, 114 MB.",
            ],
            "limits": "weekly plans with several prices plus coin packs, and its listing does not say you can bring your own reference video.",
        },
        {
            "name": "Viggle AI: Meme Maker (for comparison)", "id": 6503272013, "anchor": "viggle",
            "developer": "WarpEngine Canada Inc.", "rating": (4.76, 28091),
            "row": [VIGGLE_ROW_PRICE,
                    "Mix: one photo plus one video, or 8,000+ templates; lip-sync; multi-character editor",
                    "1 (English)", PRIV3, "2.0.7 (13 Oct 2026)", "4.8 (28,091 ratings)"],
            "best_for": "the reference point: viral dances, memes and sports moments from one photo.",
            "facts": [
                "Its listing describes motion-controlled video generation, with 8,000+ templates or your own clip.",
                "Lip-sync, a multi-character editor and a live webcam character swap in the Live plans.",
                "English interface, iOS 16 or later, 140 MB.",
            ],
            "limits": "English only, and the listing does not say how many credits one video costs.",
        },
    ],
    "who": [
        "<strong>You want Viggle-style move copying with your own reference video:</strong> Dora or PixVerse Lite.",
        "<strong>You want a bigger template library like Viggle's:</strong> Shots, or stay with Viggle.",
        "<strong>You want longer, higher-quality clips:</strong> Kling AI.",
        "<strong>You want to choose between several video models:</strong> Runway.",
        "<strong>You want an interface in your language:</strong> Dora (11 languages) or PixVerse Lite (14); Viggle and Runway are English only.",
    ],
    "cases": [
        "A dance or meme video starring you or a friend.",
        "A vertical clip for TikTok, Reels or YouTube Shorts.",
        "Animating a product photo or a portrait.",
        "Testing an idea before you film it.",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchase prices, version and release date, rating and number of ratings, languages, size, minimum iOS and privacy label categories. What each app does is taken from its own App Store description; what Dora does was also checked against its listing for version 1.4.1. We did not run a quality test of the videos, so this page does not say which app makes the best-looking video. We did not invent ratings or reviews.",
        "Subscriptions and credits change often, and App Store pages list only some purchases. Check the price shown inside each app before paying.",
    ],
    "faq": [
        ("What is the best alternative to Viggle AI on iPhone?",
         "It depends on what you use Viggle for. For copying a dance or move from a video onto your photo, Dora and PixVerse Lite have Motion Control. For longer, higher-quality generated video, Kling AI and Runway. For quick dance templates, Shots."),
        ("Is there a free alternative to Viggle AI?",
         "All six apps are free to download, but each charges to make videos with a subscription, credits or both, according to their App Store listings. Free allowances change; check inside each app."),
        ("Which Viggle alternative has an interface in other languages?",
         "Dora lists 11 languages and PixVerse Lite 14, Kling AI 5 and Shots 5. Viggle and Runway list English only."),
        ("Does Dora have a watermark?",
         "Dora's App Store listing says there is no watermark on its videos. We did not verify watermarks in the other apps, so check before you pay."),
        ("Can Dora make a person in my photo dance?",
         "Yes, with Motion Control: it takes your photo and a reference dance video and makes the person in the photo move the same way. It needs a person in the photo."),
    ],
    "sources": [
        ("Dora (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("PixVerse Lite (App Store)", "https://apps.apple.com/us/app/id6767802142"),
        ("Kling AI (App Store)", "https://apps.apple.com/us/app/id6738049229"),
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"),
        ("Shots (App Store)", "https://apps.apple.com/us/app/id6745820631"),
        ("Viggle AI (App Store)", "https://apps.apple.com/us/app/id6503272013"),
    ],
}

EN2 = {
    "group": "image-to-video", "lang": "en", "store": "us",
    "path": "best-ai-image-to-video-apps-iphone/",
    "ct": "rd-img2video",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best AI Apps to Turn a Photo Into a Video on iPhone (2026)",
    "h1": "Best AI image to video apps for iPhone in 2026",
    "description": "Six iPhone apps that turn a photo into a video, compared by price, how they animate and privacy label: Dora, Kling AI, Runway, PixVerse Lite and more.",
    "llms": "Compares six iPhone apps that turn a photo into a video (Dora, Kling AI, Runway, PixVerse Lite, Shots, Motionleap) by price, whether they generate new motion with AI or animate by hand, languages, ratings and App Store privacy label.",
    "disclosure": "Dora is made by Saga Labs, the company behind Reditor. It is one more option in this list, not placed first because it is ours, and it has only 15 ratings in the US. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "There are two kinds of photo-to-video apps on iPhone. AI generators (Dora, Kling AI, Runway, PixVerse Lite, Shots) make new movement from your photo and charge for each video through credits, coins or a subscription. Motionleap animates a photo by hand (you mark which parts move), so the result is a loop rather than a generated clip.",
        "For short vertical clips for TikTok or Reels with the cost shown before you generate, Dora and PixVerse Lite fit. For the longest, highest-quality clips, Kling AI and Runway, from $10 and $14.99 a month. For a hand-made moving photo, Motionleap.",
    ],
    "columns": ["App", "Price (US)", "How it animates", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the in-app purchases listed on each US App Store page on 16 October 2026 (pages list only some of them); all six are free to download. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        dict(DORA, row=["Pro weekly $4.99 or $9.99, Pro yearly $119.99; coin packs from $2.99 to $199.99",
                        "AI generates a video from your photo or a description in about two minutes",
                        "11", "Data Used to Track You; Data Not Linked to You", "1.4.1 (9 Oct 2026)", "4.3 (15 ratings)"]),
        {
            "name": "Kling AI: AI Image&Video Maker", "id": 6738049229, "anchor": "kling",
            "developer": "KLING AI PTE. LTD.", "rating": (4.68, 31671),
            "row": ["Standard $10 a month, Pro $37, Premier $92; weekly memberships from $1.19; credits $5 to $100",
                    "AI image to video, up to 15 s in 1080p or 4K; extension up to 3 minutes",
                    "5", PRIV3, "3.8.20 (11 Sep 2026)", "4.7 (31,671 ratings)"],
            "best_for": "longer, higher-resolution clips.",
            "facts": [
                "Its listing says clips up to 15 seconds in native 1080p or 4K, with extension to 3 minutes.",
                "Also image generation and a community to browse.",
                "5 languages, iOS 14 or later, 238 MB.",
            ],
            "limits": "plans from $10 a month up to $92, and a bigger, more complex app than a one-tap tool.",
        },
        {
            "name": "Runway: AI Image & Video", "id": 1665024375, "anchor": "runway",
            "developer": "Runway AI, Inc.", "rating": (4.48, 17539),
            "row": ["Standard $14.99 a month or $143.99 a year; Pro $35; Max $95; credits $10 to $100",
                    "AI text, image and video to video with several models; Agent builds a video from chat",
                    "1 (English)", PRIV3, "100.0.0 (13 Oct 2026)", "4.5 (17,539 ratings)"],
            "best_for": "controlled, cinematic video where you pick the model.",
            "facts": [
                "Its listing says it turns any photo into motion and bundles several named video models.",
                "Runway Agent plans shots and assembles a finished video from a conversation.",
                "English interface, iOS 16.4 or later, 129 MB.",
            ],
            "limits": "the cheapest listed plan is $14.99 a month and the interface is English only.",
        },
        {
            "name": "PixVerse Lite", "id": 6767802142, "anchor": "pixverse",
            "developer": "AIVORA PTE. LTD.", "rating": (4.31, 1695),
            "row": ["Elite $5.99 a week or $49.99 a year; credit packs $5 to $100",
                    "AI image to video, templates, transitions, Motion Control, upscaling to 4K",
                    "14", PRIV3, "0.8.1 (21 Sep 2026)", "4.3 (1,695 ratings)"],
            "best_for": "an all-in-one AI video toolbox with many languages.",
            "facts": [
                "Its listing names image to video, text to video, templates, Motion Control, video extension and upscaling up to 4K.",
                "14 languages, iOS 15 or later, 121 MB.",
            ],
            "limits": "version 0.8.1, so still pre-1.0, and a crowded interface.",
        },
        {
            "name": "Shots: Photo & Video Generator", "id": 6745820631, "anchor": "shots",
            "developer": "Deepix AI Yazilim Teknolojileri Anonim Sirketi", "rating": (4.47, 18177),
            "row": ["Weekly $6.99 to $12.99; yearly $39.99 or $79.99; coin packs $9.99 to $34.99",
                    "AI photo to video, dance templates, photo enhancing and restoring",
                    "5", PRIV3, "1.7.0 (16 Aug 2026)", "4.5 (18,177 ratings)"],
            "best_for": "selfies and pet photos with ready-made dance and trend templates, plus restoring old photos.",
            "facts": [
                "Its listing offers text to video, photo to video, dance templates and portraits.",
                "One-tap enhance and restore for old or blurry photos.",
                "5 languages, iOS 16 or later, 114 MB.",
            ],
            "limits": "weekly plans from $6.99 with several prices, plus coin packs.",
        },
        {
            "name": "Motionleap: 3D Photo Animator", "id": 1381206010, "anchor": "motionleap",
            "developer": "Lightricks Ltd.", "rating": (4.77, 117323),
            "row": ["Unlimited access plans from $3.99 to $59.99 listed",
                    "You mark what moves with arrows and anchor points; photos loop like a GIF",
                    "14", PRIV3, "1.9.38 (2 Aug 2026)", "4.8 (117,323 ratings)"],
            "best_for": "moving photo art (water, clouds, hair) that you control by hand, with no credits.",
            "facts": [
                "Its listing describes animating one or several elements with arrows and anchor points, plus overlays and speed control.",
                "Videos boomerang or flow like a GIF.",
                "14 languages, iOS 17 or later, 245 MB.",
            ],
            "limits": "it is not a text-to-video or AI-generated-motion tool, and its listing does not say it makes people dance or walk.",
        },
    ],
    "who": [
        "<strong>You want a short vertical AI clip from one photo, with the cost shown first:</strong> Dora or PixVerse Lite.",
        "<strong>You want the longest and sharpest clips:</strong> Kling AI.",
        "<strong>You want to choose the model and plan shots:</strong> Runway.",
        "<strong>You want dance and trend templates:</strong> Shots.",
        "<strong>You want a looping moving photo without AI credits:</strong> Motionleap.",
    ],
    "cases": [
        "Bringing an old family photo to life.",
        "A product photo turned into a short ad clip.",
        "A portrait that moves, for a profile or story.",
        "Landscape photos with moving water or clouds (Motionleap).",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchase prices, version and release date, rating and number of ratings, languages, size, minimum iOS and privacy label categories. What each app does is taken from its own App Store description. We did not run a quality test, so this page does not say which app makes the best-looking video. We did not invent ratings or reviews.",
        "Subscriptions and credits change often, and App Store pages list only some purchases. Check the price shown inside each app before paying.",
    ],
    "faq": [
        ("What is the best AI image to video app for iPhone?",
         "It depends on what you need. Kling AI and Runway make the longest and highest-quality clips but cost from $10 and $14.99 a month. Dora and PixVerse Lite make short vertical clips with credits or coins. Shots has dance templates. Motionleap animates by hand with no AI credits."),
        ("Can I turn a photo into a video for free on iPhone?",
         "All six apps are free to download, but the five AI generators charge to make videos, by subscription, credits or coins. Free allowances change, so check inside each app."),
        ("How does AI turn a photo into a video?",
         "You give the app a photo and optionally a short description or a reference video. The AI model then generates new frames so the people or objects move. This takes from about a minute to a few minutes."),
        ("Which of these apps shows the price before generating?",
         "Dora's listing says every video or image shows its coin cost before you generate, and failed generations refund the coins. We did not verify this in the other apps."),
        ("Does Dora work in other languages?",
         "Dora lists 11 languages. PixVerse Lite lists 14, Kling AI 5, Shots 5, Motionleap 14, and Runway English only."),
    ],
    "sources": [
        ("Dora (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Kling AI (App Store)", "https://apps.apple.com/us/app/id6738049229"),
        ("Runway (App Store)", "https://apps.apple.com/us/app/id1665024375"),
        ("PixVerse Lite (App Store)", "https://apps.apple.com/us/app/id6767802142"),
        ("Shots (App Store)", "https://apps.apple.com/us/app/id6745820631"),
        ("Motionleap (App Store)", "https://apps.apple.com/us/app/id1381206010"),
    ],
}

PAGES = [EN1, EN2]
