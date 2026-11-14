"""Guide (14 Nov 2026), complaint technique: watching video on a car screen from an iPhone without paying for an app
that does not work. EN only. Our app: CarScreen (id 6833951195), one option among others, no ownership line in the
article (footer, About and llms.txt name our apps); our link carries pt+ct via {CARSCREEN}, competitors plain links.

Data checked 14 Nov 2026:
- 1,210 US reviews downloaded with ios-playbook/tools/app_reviews.py from 8 apps (myCar, Car Connect, CarTV, CarDash,
  CarTube, APTV, Car TV IPTV, CarPlay Screen Mirroring); 863 of them 1-2 stars. Complaints counted by keywords, so the
  counts are approximate and one review can count in several groups.
- iTunes lookup of each named app on 14 Nov 2026 (name, price, rating to 1 decimal); features only from their listings.
- CarScreen: lookup returned 0 results (indexing delay), so the page https://apps.apple.com/us/app/id6833951195 was
  used (200): free, rating shown as "New". Features only from that listing.
- Apple support pages: 118223 (refunds) and 118428 (cancel a subscription).
"""

D = "2026-11-14"
AS_OF = "as of Nov 14, 2026"


def a(u, t):
    return f'<a href="{u}">{t}</a>'


def ul(items):
    return "<ul>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ul>\n"


def store(i, name):
    return a(f"https://apps.apple.com/us/app/id{i}", name)


REFUND = "https://support.apple.com/en-us/118223"
CANCEL = "https://support.apple.com/en-us/118428"
CARSCREEN = "{CARSCREEN}"

PAGES = [{
    "group": "car-video-complaints", "kind": "news", "lang": "en", "store": "us",
    "path": "watch-videos-car-screen-app-that-works-iphone/",
    "ct": "rd-car-video-complaints",
    "category": "UtilitiesApplication",
    "published": D, "updated": D, "checked": D, "apps": [],
    "kicker": "Car screen guide",
    "title": "How to Watch Videos on Your Car Screen Without Paying for an App That Doesn't Work (2026)",
    "h1": "How to watch videos on your car screen without paying for an app that doesn't work (2026)",
    "description": ("Car video apps get 1 and 2 star reviews that say \"doesn't work in my car\", \"paid and nothing happened\" and "
                    "\"scam\". Five complaints from 863 reviews, and how to avoid each one before you pay."),
    "llms": ("Guide, 14 November 2026: the five most repeated complaints in 863 one- and two-star US App Store reviews of car video "
             "and car widget apps for iPhone (CarTV, CarDash, CarTube, APTV, myCar, Car Connect): \"scam\" and refund requests, "
             "\"doesn't work in my car\", paid before testing, unexpected charges and \"stopped working after the iOS update\", with a fix "
             "for each. Video on the car screen plays only while parked and only in cars whose maker supports it. Counts are approximate."),
    "llms_note": "CarScreen, one of the apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Complaints from US App Store reviews, and a check you can do for each before you pay.",
    "answer": [
        "<strong>To watch videos on your car screen without paying for an app that doesn't work, find out first whether your car "
        "supports video at all, and only pay for an app that lets you test it in your own car for free.</strong> Video on the car "
        "screen plays only while the car is parked and only in cars whose maker supports it, so the same app can work in one car and "
        "do nothing in another.",
        "<strong>Free test first:</strong> CarScreen: Car Widgets &amp; Video (free to download, rating: New) plays a 5-second test clip "
        "and tells you clearly whether video works in your car before you pay. "
        + a(CARSCREEN, "Get CarScreen on the App Store") + ".",
    ],
    "sections": [
        ("data", "What we looked at",
         "<p>We downloaded 1,210 recent US App Store reviews of eight car video and car widget apps and kept the 863 with one or two "
         "stars. The five complaints below are the ones that repeat most. Counts come from keyword matching, so they are approximate "
         "and one review can count in more than one group.</p>\n" + ul([
             "&ldquo;Scam&rdquo;, &ldquo;fraud&rdquo;, &ldquo;want my money back&rdquo;: about 320 reviews.",
             "&ldquo;Doesn't work in my car&rdquo; or &ldquo;car not supported&rdquo;: about 170.",
             "&ldquo;Paid and it didn't work&rdquo;, with no way to try first: about 120.",
             "&ldquo;Charged again&rdquo; or &ldquo;can't cancel&rdquo;: about 100.",
             "&ldquo;Stopped working after the iOS update&rdquo;: about 45."]) +
         "<p>Apps in the reviews, with their US App Store data " + AS_OF + ": "
         + store(6800211040, "CarTV - M3U IPTV Player &amp; Cast") + " (free, 4.5), "
         + store(6797764175, "CarDash: Video Player for Cars") + " (free, 4.6), "
         + store(6756518125, "CarTube") + " (free, 3.8), "
         + store(1665625393, "Car Connect, Play, Widgets") + " (free, 4.7), "
         + store(6755033589, "myCar: Car Widgets・Play Themes") + " (free, 4.6) and "
         + store(6476621657, "APTV - Car TV Player &amp; Cast") + " (free, 4.3). Free means free to download; most sell a subscription "
         "or a lifetime plan inside.</p>\n"),
        ("scam", "“Scam” and “I want my money back”", ""),
        ("notmycar", "“Doesn't work in my car”", ""),
        ("paidfirst", "“Paid and it didn't work”", ""),
        ("charged", "“Charged again” and “can't cancel”", ""),
        ("iosupdate", "“Stopped working after the iOS update”", ""),
        ("checklist", "Before you pay: a 5-line check", ul([
            "Is your car one whose maker supports video on the car screen? If you cannot find it, treat it as not supported.",
            "Does the app test it in your car for free, before the paywall?",
            "Is the plan a subscription or a one-time purchase, and what is the price on the screen before you confirm?",
            "Do you know where to cancel (" + a(CANCEL, "Apple: cancel a subscription") + ") and ask for a refund (" + a(REFUND, "Apple: request a refund") + ")?",
            "Are you parked? Never watch while driving."])),
    ],
    "faq": [
        ("Can I watch videos on my car screen from my iPhone?",
         "Sometimes. According to the listings of CarScreen, CarDash and APTV, video reaches the car screen only while the car is parked and only on cars whose maker supports it. Many cars do not."),
        ("Why does a car video app work in one car and not in another?",
         "Because it depends on the car, not only on the app. APTV's listing says many vehicles do not support CarPlay video yet, and CarDash's listing says a CarPlay audio connection alone does not guarantee video support."),
        ("How can I check before paying?",
         "Use an app that tests your car first. CarScreen plays a free 5-second test clip and tells you whether video works in your car; CarDash's listing offers a limited free car-playback allowance."),
        ("Can I get a refund from the App Store?",
         "You can ask. Apple explains how on its page about requesting a refund for apps or content bought from Apple; approval is up to Apple."),
        ("Is it safe to watch video in the car?",
         "Only while parked. Every app listing mentioned here says never to watch while driving."),
    ],
    "sources_html": [
        "Reviews: US App Store, 1,210 downloaded from 8 apps, 863 with 1 or 2 stars, 14 November 2026; counts by keyword, approximate.",
        a(REFUND, "Request a refund for apps or content that you bought from Apple") + ", Apple Support.",
        a(CANCEL, "Cancel a subscription from Apple") + ", Apple Support.",
        "Apps: their US App Store pages and Apple lookup data, 14 November 2026. CarScreen: its App Store page, "
        + a(CARSCREEN, "CarScreen: Car Widgets &amp; Video") + ".",
    ],
    "fix": 'If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
}]

# Section bodies (kept apart for readability).
_B = {
    "scam": (
        "<p>It is the most repeated word: &ldquo;scam&rdquo;, &ldquo;fraud&rdquo; or &ldquo;waste of money&rdquo; shows up in about 320 "
        "of the 863 reviews, usually when the app did nothing in the reviewer's car. Typical wording: &ldquo;Makes you pay and it did "
        "nothing&rdquo; (CarTube, 1 star). Part of the confusion is the product itself: CarTube's listing describes a Safari Web "
        "Extension for web video playback, while the reviews we read expect video on a CarPlay screen.</p>\n"
        "<p><strong>Fix:</strong> read what the listing says the app does before you install, and do not pay until the app has shown "
        "something on <em>your</em> car's screen. If you already paid, " + a(REFUND, "Apple explains how to request a refund") + "; "
        "it is Apple's decision.</p>\n"),
    "notmycar": (
        "<p>About 170 reviews are about the car: &ldquo;Does not work on 2023 Hyundai Tucson with wireless CarPlay!&rdquo; "
        "(CarTube, 1 star), &ldquo;MY CAR WAS NOT EVEN SUPPORTED&rdquo; (Car Connect, 1 star). The apps' own listings explain why. "
        "APTV's says video plays only while parked, needs iOS 27 or later and a vehicle that supports video in CarPlay, and that "
        "many vehicles do not yet. CarDash's says a CarPlay audio connection alone does not guarantee video support, and that "
        "output depends on your iPhone, iOS version, vehicle and content source.</p>\n"
        "<p><strong>Fix:</strong> treat car support as a separate question from the app. Test in your own car, parked. "
        + a(CARSCREEN, "CarScreen") + " is built around this: its listing says it plays a 5-second test clip and tells you "
        "clearly whether video works in your car, and that video works only when parked and only in cars whose maker supports it. "
        "If the test says no, you have lost nothing, and you can still use its free widgets.</p>\n"),
    "paidfirst": (
        "<p>About 120 reviews say the app asked for money before they could see it work, then it did not: &ldquo;just spent 5 bucks for "
        "it not to play anything on my car screen&rdquo; (CarTV, 1 star); &ldquo;No introductory trial to test app&rdquo; (myCar, 1 "
        "star); &ldquo;Charges me 31 dollar and it doesn't even work&rdquo; (Car Connect, 1 star).</p>\n"
        "<p><strong>Fix:</strong> choose an app with a free test that runs in the car, not just a free download. Two listings say "
        "so: CarScreen's 5-second test clip, free and before any payment, and CarDash's &ldquo;limited free car-playback "
        "allowance&rdquo; and one playlist source before Pro. After you have seen video work, decide. CarScreen's listing says "
        "that after the free car check, one payment unlocks video, playlists and the browser, with no subscription and no renewals.</p>\n"),
    "charged": (
        "<p>About 100 reviews are about money leaving after the first payment: &ldquo;Click on free try, charges for full year "
        "subscriptions&rdquo; (CarDash, 1 star). Several listings sell weekly, yearly or lifetime plans; APTV's lists a weekly "
        "$9.99 and a lifetime $49.99 " + AS_OF + ".</p>\n"
        "<p><strong>Fix:</strong> read the plan on the payment sheet (weekly is the easy one to miss), and set a reminder before a "
        "trial ends. To stop renewals, " + a(CANCEL, "cancel the subscription from Apple") + " in your account, not by deleting the "
        "app. A one-time purchase avoids renewals altogether.</p>\n"),
    "iosupdate": (
        "<p>About 45 reviews say an iPhone update broke video: &ldquo;Stopped working after iOS 27.2 update&rdquo; (CarTV, 1 star), "
        "often from people who had bought a lifetime plan. We cannot confirm the cause; we only report what reviewers wrote.</p>\n"
        "<p><strong>Fix:</strong> before buying a lifetime plan, check the app's last update date on its App Store page and read the "
        "newest reviews, not the average. Video on the car screen depends on your iPhone, iOS and car together (CarDash's listing says "
        "so), so a pay-once plan is a bigger bet than a free test. Do not install a major iOS update right before a long trip if you "
        "rely on it.</p>\n"),
}
for _i, (_sid, _h, _body) in enumerate(PAGES[0]["sections"]):
    if _sid in _B:
        PAGES[0]["sections"][_i] = (_sid, _h, _B[_sid])
