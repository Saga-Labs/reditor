"""Headspace alternatives on iPhone, EN. Our app: Drop (id1462269642), breathing sessions and nature sounds, not a
voice-guided course library; the page says so.

Checked 2026-11-03: US App Store search for «headspace», «meditation», «guided meditation», «breathing exercise»,
«mindfulness», iTunes lookup and the US App Store page of every app (price list, privacy label). To avoid repeating
reviewland's Calm alternatives and free sleep sound pages, none of their apps are used except Drop (no Calm, Insight
Timer, Medito, BetterSleep). Why this topic: Google suggests «headspace alternative», «... free», «best headspace
alternative», «headspace app alternatives» (3 Nov); no page on the 4 sites is about Headspace. Health claims from the
listings (study percentages) are left out. Registered in ios-playbook references/temas-webs.md (5007d6d). Nothing tested.
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


LK = "Data Linked to You"

PAGES = [{
    "group": "headspace-alt", "lang": "en", "store": "us",
    "path": "headspace-alternatives-iphone/",
    "ct": "rd-headspace-alt-iphone",
    "category": "HealthApplication",
    "published": D, "updated": "2026-11-09", "checked": CHECKED,
    "title": "Headspace Alternatives for iPhone (2026): 6 Apps, 2 Free",
    "h1": "Best Headspace alternatives for iPhone in 2026",
    "description": "Headspace is $12.99 a month or $69.99 a year. Six iPhone alternatives for meditation and breathing, two with no purchases at all, by price and privacy.",
    "llms": "Compares six iPhone alternatives to Headspace ($12.99 a month or $69.99 a year on the US App Store): Healthy Minds Program and Smiling Mind (no in-app purchases), Balance (personalized daily meditations), Drop (breathing sessions and nature sounds, lifetime purchase), Waking Up (course with Sam Harris) and Open (breathwork), by price, what each teaches, languages and App Store privacy label.",
    "llms_note": "Drop, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Headspace costs $12.99 a month or $69.99 a year on the US App Store</strong> (3 November 2026), with Headspace Plus at $94.99. It offers 500+ guided meditations, sleep content and, for more support, therapists, coaches and an AI companion, and it is in English only.",
        "To pay nothing, the Healthy Minds Program and Smiling Mind list no in-app purchases at all. Balance builds a guided meditation for you each day. Drop is simpler: breathing sessions from 2 to 20 minutes with nature sounds, a one-time purchase, and 33 languages. Waking Up and Open cost more than Headspace and go deeper into meditation theory and breathwork. For the Calm side of the question, reviewland compares <a href=\"https://reviewland.io/calm-alternatives-iphone/\">Calm alternatives</a>.",
    ],
    "columns": ["App", "Price (US)", "What it offers, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Headspace for comparison: $12.99 a month, $69.99 a year. Ratings are that day's App Store average. Privacy labels rechecked on 9 November 2026.",
    "apps": [
        app("Healthy Minds Program by Humin", 1326310617, "healthy-minds", "Healthy Minds Innovations, Inc.", 4.88, 9244,
            "a full meditation program with lessons, for free.",
            ["Meditations and podcast-style lessons on focus, stress and relationships.",
             "Developed with neuroscientist Richard Davidson and the Center for Healthy Minds at the University of Wisconsin–Madison, per its listing.",
             "No in-app purchases listed."],
            "English only, and its privacy label lists Data Linked to You.",
            ["No purchases listed",
             "Meditations and lessons", "1", "Data Linked to You; Data Not Linked to You", "9.0.0 (28 Oct 2026)"]),
        app("Smiling Mind: Mental Wellbeing", 560442518, "smiling-mind", "SMILING MIND PTY. LTD.", 4.76, 4950,
            "families: 700+ free practices, with collections for children aged 5 to 12.",
            ["700+ lessons, practices and meditations in 50+ collections.",
             "Children's collections for ages 5 to 12 and adult collections from beginner up.",
             "No in-app purchases listed."],
            "English only, and its privacy label lists Data Linked to You.",
            ["No purchases listed",
             "Meditations and lessons, adults and children", "1", LK, "8.0.3 (28 Oct 2026)"]),
        app("Balance: Meditation & Sleep", 1361356590, "balance", "Elevate Labs, LLC", 4.88, 120758,
            "a daily guided meditation built from your answers, closest to Headspace's courses.",
            ["Each day it asks about your goals and assembles a guided meditation from thousands of audio files.",
             "10-day plans that teach the basics; short Singles for any moment; sleep meditations and sounds.",
             "Yearly plans from $39.99 to $69.99 listed."],
            "English only, and its privacy label includes Data Used to Track You.",
            ["Yearly $39.99 to $69.99; $11.99 listed",
             "Personalized guided meditations", "1", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "1.213.0 (22 Oct 2026)"]),
        app("Sleep Sounds & Focus: Drop", 1462269642, "drop", "Saga Ltd.", 4.42, 12,
            "short breathing breaks and nature sounds, paid once, in your language.",
            ["Breathing sessions of 2, 5, 10 and 20 minutes with a visual guide; a garden grows as you practice.",
             "Nature sounds: campfire and forest free; rain, dewdrops and ocean with Pro.",
             "Works offline, no ads, home screen widgets; in 33 languages."],
            "it is not a library of voice-guided courses like Headspace's.",
            ["Pro $4.99 a month; lifetime $24.99 or $49.99 (offer $9.99)",
             "Breathing sessions and nature sounds", "33", "Data Linked to You; Data Not Linked to You", "2.14 (30 Oct 2026)"], ours=True),
        app("Waking Up: Meditation & Wisdom", 1307736395, "waking-up", "Waking Up Course, LLC", 4.92, 42734,
            "going deeper, with a 28-day course and theory sessions led by Sam Harris.",
            ["A 28-day introductory course and daily meditations with Sam Harris.",
             "A large library of theory sessions, courses and conversations; a meditation timer; CarPlay.",
             "Family plan listed at $229.99 a year."],
            "English only, and it costs more than Headspace ($19.99 a month, $149.99 to $199.99 a year).",
            ["Monthly $19.99; yearly $149.99 to $199.99; family $229.99",
             "Course, daily meditations, theory", "1", LK, "3.28.0 (27 Oct 2026)"]),
        app("Open: Breathwork + Meditation", 1482725254, "open", "Open Inc.", 4.87, 17972,
            "breathwork classes next to meditation and movement.",
            ["Breathwork, meditation and movement classes designed by experts, per its listing.",
             "Also teaches in person at its studio in Los Angeles.",
             "Updated on 2 November 2026."],
            "English only, a large download (322 MB), and $19.99 a month or $149.99 a year.",
            ["Monthly $19.99; yearly $149.99",
             "Breathwork, meditation, movement", "1", LK, "26.44 (2 Nov 2026)"]),
    ],
    "who": [
        "<strong>A full free program:</strong> Healthy Minds Program.",
        "<strong>Free, with children's collections:</strong> Smiling Mind.",
        "<strong>Guided meditations made for you each day:</strong> Balance.",
        "<strong>Short breathing breaks, paid once, in 33 languages:</strong> Drop.",
        "<strong>Meditation with theory:</strong> Waking Up.",
        "<strong>Breathwork:</strong> Open.",
    ],
    "cases": ["Leaving a Headspace subscription for a free app.", "A two-minute break between meetings.", "Meditating in a language other than English."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «headspace», «meditation», «guided meditation», «breathing exercise» and «mindfulness», and read Headspace's and each app's US App Store page and Apple's lookup data. We left out the apps reviewland already compares as Calm alternatives. We tested nothing.",
        "These are wellbeing apps, not medical treatment.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a free alternative to Headspace?",
         "Yes. The Healthy Minds Program and Smiling Mind list no in-app purchases. Drop is free to download, and its listing marks three of its nature sounds as Pro."),
        ("Which Headspace alternative has no subscription?",
         "Drop sells a lifetime purchase ($24.99 or $49.99, sometimes offered at $9.99). Healthy Minds and Smiling Mind need no payment at all."),
        ("Which is most like Headspace?",
         "Balance, with daily guided meditations and 10-day plans. Waking Up has a 28-day course but costs more."),
        ("Are these apps in languages other than English?",
         "Of the six, only Drop is, in 33 languages. The others, like Headspace, list English only on the US App Store."),
    ],
    "sources": [
        ("Headspace (App Store)", "https://apps.apple.com/us/app/id493145008"),
        ("Healthy Minds Program (App Store)", "https://apps.apple.com/us/app/id1326310617"),
        ("Smiling Mind (App Store)", "https://apps.apple.com/us/app/id560442518"),
        ("Balance (App Store)", "https://apps.apple.com/us/app/id1361356590"),
        ("Drop (App Store)", "https://apps.apple.com/us/app/id1462269642"),
        ("Waking Up (App Store)", "https://apps.apple.com/us/app/id1307736395"),
        ("Open (App Store)", "https://apps.apple.com/us/app/id1482725254"),
    ],
}]
