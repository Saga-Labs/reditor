"""Endel alternatives on iPhone, EN. Our app: Drop (id1462269642), breathing sessions with a few nature sounds; it does
not generate adaptive soundscapes, and the page says so.

Checked 2026-11-03: US App Store search for «endel», «brain.fm», «focus music», «dark noise», «mynoise», «noisli»,
«soundscape», «white noise», iTunes lookup and the US App Store page of every app (price list, privacy label). To avoid
repeating reviewland's free sleep sound apps page, none of its apps are used except Drop (no White Noise Lite, Dark
Noise, Rain Rain, Sleep Pillow, White Noise Deep Sleep). Health claims from the listings are left out. Why this topic:
Google suggests «endel alternative», «endel alternatives», «endel alternative free», «endel app alternative» (3 Nov);
no page on the 4 sites is about Endel. Registered in ios-playbook references/temas-webs.md (0ee8c83). Nothing tested.
"""

D = "2026-11-03"
CHECKED = "2026-11-03"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f}"]}
    if ours:
        a["ours"] = True
    return a


NL = "Data Not Linked to You"

PAGES = [{
    "group": "endel-alt", "lang": "en", "store": "us",
    "path": "endel-alternatives-iphone/",
    "ct": "rd-endel-alt-iphone",
    "category": "HealthApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Endel Alternatives for iPhone (2026): 6 Focus & Sleep Sound Apps",
    "h1": "Best Endel alternatives for iPhone in 2026",
    "description": "Endel costs up to $19.99 a month and needs iOS 26. Six iPhone apps for focus and sleep sounds compared by price, lifetime option and privacy label.",
    "llms": "Compares six iPhone alternatives to Endel (AI soundscapes for focus and sleep; up to $19.99 a month, lifetime $124.99, iOS 26, privacy label with tracking): Brain.fm (focus music), Portal (nature with spatial audio), myNoise (350+ adjustable soundscapes, one-time purchase), Drop (breathing sessions and nature sounds), (Not Boring) Vibes (generated music by time of day) and Soundscape (music plus app blocking), by price, lifetime option and App Store privacy label.",
    "llms_note": "Drop, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Endel makes soundscapes for focus, sleep and relaxing that adapt to your location, surroundings and heart rate</strong>, per its listing. On the US App Store (3 November 2026) its price list runs from $2.99 to $19.99 a month and $34.99 to $119.99 a year, with a lifetime purchase at $124.99; the latest version needs iOS 26, and its privacy label includes <em>Data Used to Track You</em>.",
        "The closest match is (Not Boring) Vibes, which also generates music through the day from your wake and sleep times. Brain.fm is focus music with an ADHD mode. For sounds you shape yourself, myNoise has 350+ soundscapes with sliders, with Full Access at $19.99. Portal is nature with spatial audio, Soundscape adds app blocking, and Drop pairs breathing sessions with a few nature sounds. Portal, myNoise, Vibes and Drop list only Data Not Linked to You.",
    ],
    "columns": ["App", "Price (US)", "Lifetime or one-time price", "What it plays, per its listing", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Endel for comparison: $2.99 to $19.99 a month, lifetime $124.99. Ratings are that day's App Store average and count.",
    "apps": [
        app("Brain.fm: Focus & Sleep Music", 1110684238, "brain-fm", "BrainFM, Inc.", 4.55, 5559,
            "music made for focus sessions, with an adjustable intensity and an ADHD mode.",
            ["Focus, relax, meditate and sleep modes, in genres from lo-fi to classical, plus nature soundscapes.",
             "Adjustable stimulation level with a boost option, a Pomodoro mode and offline downloads.",
             "Plans from $6.99 a month to $99.99 a year listed."],
            "English only, and its privacy label includes Data Used to Track You.",
            ["$6.99 to $15.99 listed; yearly $49.99 to $99.99", "Not listed",
             "Focus and sleep music", "Data Used to Track You; Data Linked to You", "3.5.60 (27 Oct 2026)"]),
        app("Portal - Escape Into Nature", 1436994560, "portal", "Portal Labs Ltd", 4.77, 10352,
            "real places in nature, from Costa Rica's cloud forests to Iceland, with spatial audio and visuals.",
            ["Immersive spatial audio with cinematic motion visuals; works with smart lighting.",
             "Membership at $2.99 a month or $29.99 a year, the cheapest yearly plan here.",
             "An Apple Editor's Pick and Mac App of the Year finalist, per its listing."],
            "English only, and the lifetime price ($99.99) is high.",
            ["$2.99 a month; $29.99 a year", "Lifetime $99.99",
             "Nature places with spatial audio", NL, "4.1.1 (28 Oct 2026)"]),
        app("myNoise - The Soundscape App", 1523675125, "mynoise", "myNoise BVBA", 4.74, 1192,
            "building your own sound with sliders.",
            ["350+ soundscapes, each with its own sliders; «White Noise & Co» covers white, brown, green, grey and pink noise.",
             "Made for long listening, to focus, sleep or mask outside noise; a meditation bell to pace sessions.",
             "Full Access is listed at $19.99; the listing does not say whether it renews."],
            "English only; nothing is generated for you, you tune it.",
            ["Full Access $19.99; All You Can Hear $14.99", "Not stated",
             "350+ adjustable soundscapes", NL, "3.21.79 (29 Oct 2026)"]),
        app("Sleep Sounds & Focus: Drop", 1462269642, "drop", "Saga Ltd.", 4.42, 12,
            "short breathing sessions with nature sounds, paid once, in your language.",
            ["Breathing sessions of 2, 5, 10 and 20 minutes with a visual guide; a garden grows as you practice.",
             "Nature sounds: campfire and forest free; rain, dewdrops and ocean with Pro.",
             "Works offline, no ads, home screen widgets; in 33 languages."],
            "only five nature sounds in its listing; it does not generate or adapt soundscapes like Endel.",
            ["Pro $4.99 a month", "Lifetime $24.99 or $49.99 (offer $9.99)",
             "Breathing sessions and 5 nature sounds", NL, "2.14 (30 Oct 2026)"], ours=True),
        app("(Not Boring) Vibes", 1661440185, "vibes", "Not Boring Software LLC", 4.84, 2885,
            "the closest idea to Endel: generated music that follows your day, with spatial audio.",
            ["Generates background music from your wake and sleep times and what you are doing; one tap to play.",
             "Spatial 3D soundscapes with head tracking; energy and presence controls; widgets and timers.",
             "No ads, no data gathering and no tracking, per its listing; Vibes Plus lifetime $59.99."],
            "it needs iOS 26, and it is a large download (333 MB).",
            ["Vibes Plus $14.99 a year; Super!Boring $7.99 a month or $29.99 a year", "Lifetime $59.99",
             "Generated music by time of day", NL, "1.30 (23 Oct 2026)"]),
        app("Soundscape: Focus Sleep Sounds", 6480119395, "soundscape", "1000 Streams AB", 4.86, 5711,
            "focus music plus blocking the apps that distract you.",
            ["Focus music with no vocals (ambient, lo-fi, classical, piano), white noise and sleep sounds; mix rain, ocean, fire or thunder under any track.",
             "Blocks chosen apps during a session; Pomodoro and custom timers; strict mode.",
             "Works with Spotify and Apple Music; to-dos beside the session."],
            "a long, confusing price list ($0.99 to $39.99), and its privacy label includes Data Used to Track You.",
            ["$0.99 to $39.99 listed; supporter $4.99 a month or $39.99 a year", "Not stated",
             "Focus music, noise, mixable sounds", "Data Used to Track You; Data Not Linked to You", "11.1.7 (24 Oct 2026)"]),
    ],
    "who": [
        "<strong>Focus music with intensity control:</strong> Brain.fm.",
        "<strong>Real places in nature:</strong> Portal.",
        "<strong>Tuning your own noise:</strong> myNoise.",
        "<strong>Breathing breaks with nature sounds, in 33 languages:</strong> Drop.",
        "<strong>Generated music through the day, like Endel:</strong> Vibes.",
        "<strong>Music plus app blocking:</strong> Soundscape.",
    ],
    "cases": ["Masking office or street noise while working.", "Falling asleep without a subscription.", "Leaving Endel because your iPhone cannot run iOS 26."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «endel», «brain.fm», «focus music», «dark noise», «mynoise», «noisli», «soundscape» and «white noise», and read Endel's and each app's US App Store page and Apple's lookup data. We left out the apps reviewland already compares among free sleep sound apps. We tested nothing.",
        "These are sound apps, not medical treatment.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a free alternative to Endel?",
         "All six are free to download with paid upgrades. Drop's listing marks three of its five nature sounds as Pro; the others limit sounds or features to their paid plans."),
        ("Which Endel alternative is most similar?",
         "(Not Boring) Vibes, which also generates music through the day from your wake and sleep times, with spatial audio."),
        ("Which ones have a lifetime purchase?",
         "Drop ($24.99 or $49.99), Vibes Plus ($59.99) and Portal ($99.99). Endel's lifetime is $124.99. myNoise lists Full Access at $19.99 without saying whether it renews."),
        ("Which work on an iPhone that cannot run iOS 26?",
         "Endel's and Vibes' current versions need iOS 26. Brain.fm and myNoise need iOS 16.4, Soundscape iOS 17, Drop iOS 18 and Portal iOS 18.4."),
    ],
    "sources": [
        ("Endel (App Store)", "https://apps.apple.com/us/app/id1346247457"),
        ("Brain.fm (App Store)", "https://apps.apple.com/us/app/id1110684238"),
        ("Portal (App Store)", "https://apps.apple.com/us/app/id1436994560"),
        ("myNoise (App Store)", "https://apps.apple.com/us/app/id1523675125"),
        ("Drop (App Store)", "https://apps.apple.com/us/app/id1462269642"),
        ("(Not Boring) Vibes (App Store)", "https://apps.apple.com/us/app/id1661440185"),
        ("Soundscape (App Store)", "https://apps.apple.com/us/app/id6480119395"),
    ],
}]
