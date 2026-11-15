"""Guide (15 Nov 2026), complaint technique: translator apps without a surprise subscription, offline surprises or network errors.
EN only. No Saga Labs app is named (our translator is not on sale yet); footer, About and llms.txt carry the ownership
notice as before. All links are plain links to third-party apps and Apple support pages.

Data: 157 one- and two-star reviews from the US App Store customer-review feed, most recent page of each app (up to 100 per app),
downloaded on 15 Nov 2026: Translate Now 30, Google Translate 55, Microsoft Translator 57, iTranslate 15. Counts come from
keyword matching, so they are approximate and one review can count in more than one group. Quotes are literal.
App facts: iTunes lookup of the four apps on 15 Nov 2026. Apple support pages checked 15 Nov 2026 (200): 118428 (cancel a
subscription), 118223 (request a refund).
"""

D = "2026-11-15"
AS_OF = "as of Nov 15, 2026"


def a(u, t):
    return f'<a href="{u}">{t}</a>'


def ul(items):
    return "<ul>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ul>\n"


def ol(items):
    return "<ol>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ol>\n"


CANCEL = "https://support.apple.com/en-us/118428"
REFUND = "https://support.apple.com/en-us/118223"
GT = "https://apps.apple.com/us/app/id414706506"
MT = "https://apps.apple.com/us/app/id1018949559"
IT = "https://apps.apple.com/us/app/id288113403"
TN = "https://apps.apple.com/us/app/id1348028646"

_B = {
    "data": (
        "<p>We read the most recent one- and two-star reviews of four translation apps on the US App Store: "
        + a(TN, "Translate Now - AI Translator") + " (30 reviews), "
        + a(GT, "Google Translate") + " (55), "
        + a(MT, "Microsoft Translator") + " (57) and "
        + a(IT, "iTranslate Translator") + " (15). That is 157 reviews in all, the most recent reviews of each app (up to 100 per app), downloaded "
        + AS_OF + ". Three groups come up again and again: money (subscriptions, paywalls, charges after cancelling), "
        "offline mode that does not work as expected, and network errors.</p>\n"
        + ul([
            "Subscriptions, paywalls and charges: about half of the Translate Now reviews (14 of 30), and 4 of 15 for iTranslate.",
            "Offline or &ldquo;no internet&rdquo; problems: 5 of 55 for Google Translate and 6 of 57 for Microsoft Translator.",
            "Wrong or poor translations: 10 of 55 for Google Translate.",
        ]) +
        "<p>Reviews are the opinions of people who were unhappy. They are not a test of the apps.</p>\n"),
    "money": (
        "<p>This is the biggest group for Translate Now. A reviewer: &ldquo;I canceled the subscription and it still charged me&rdquo; "
        "(Translate Now, 1 star). Another: &ldquo;Did not realize they were taking $10.98 a WEEK on a subscription fee&rdquo; "
        "(Translate Now, 1 star). For iTranslate, the complaint is the trial: &ldquo;Be sure to cancel after trial or pay $40 per month "
        "every month!&rdquo; (iTranslate, 1 star). Some reviewers say the free part is too small: &ldquo;You have to pay for common "
        "languages&rdquo; (Translate Now, 1 star). These are the reviewers' words, not facts we checked in each app.</p>\n"
        "<p>The App Store pages say what each app sells. Translate Now's page promotes a subscription called Air Apps One. "
        "iTranslate's page says a free trial turns into a paid subscription unless auto-renew is turned off at least 24 hours before the end of the trial.</p>\n"
        "<p><strong>Fix, before you download and before any trial:</strong></p>\n"
        + ol([
            "Scroll to the end of the App Store page and read the subscription terms: the price, how often it renews and when a free trial ends.",
            "Set a calendar reminder for the day before the trial ends.",
            "To check or stop a subscription: open Settings, tap your name, tap Subscriptions, tap the subscription, then Cancel Subscription. Apple's steps are on "
            + a(CANCEL, "Cancel a subscription from Apple") + ". Deleting the app does not cancel it.",
            "If you were charged after cancelling, you can ask Apple for a refund: " + a(REFUND, "Request a refund for apps or content that you bought from Apple") + ". Apple decides.",
        ])),
    "offline": (
        "<p>A translator is most useful when you have no signal, on a plane or in a foreign subway. The reviews say that is when several apps fail. "
        "A Google Translate reviewer: &ldquo;It DOES NOT work offline as advertised…&rdquo; (1 star). Another, in Japan: &ldquo;This app was unusable if /when I wasn't connected to the internet&rdquo; "
        "(2 stars). A Microsoft Translator reviewer says the app &ldquo;removed the ability to download languages for offline use&rdquo; (1 star).</p>\n"
        "<p>iTranslate's App Store page says the same thing from its side: to use offline mode, you need to download language packs first.</p>\n"
        "<p><strong>Fix:</strong> test offline mode at home, on Wi-Fi, before you travel. Turn Wi-Fi and mobile data off, open the app, and translate one "
        "sentence. If it fails, the language pack is missing or the app does not offer offline mode for that language. Check the app's own settings "
        "for downloadable languages, and check the App Store page first if you cannot find them.</p>\n"),
    "network": (
        "<p>Microsoft Translator has the most network complaints in this set, mostly about its live conversation mode: &ldquo;Keeps getting network error "
        "when trying to use live translation&rdquo; (2 stars), from a reviewer who was on Wi-Fi. Another reviewer says the app kept asking them to check the network while they were on Wi-Fi.</p>\n"
        "<p><strong>Fix:</strong> close the app fully, turn Wi-Fi off and on, and try with mobile data. If it still fails, use the text mode, which is slower but often works. "
        "If you need a reliable offline mode, decide before you travel, not in the middle of a conversation.</p>\n"),
    "checklist": ul([
        "Did I read the subscription terms and the trial length on the App Store page before I downloaded?",
        "Did I set a reminder for the day before the trial ends?",
        "Did I test offline mode at home, with Wi-Fi and mobile data off?",
        "Did I check which languages I can download and whether I need them before I leave?",
        "Do I know where to cancel (" + a(CANCEL, "Apple: cancel a subscription") + ") and how to ask for a refund (" + a(REFUND, "Apple: request a refund") + ")?"]),
}

PAGES = [{
    "group": "translator-complaints", "kind": "news", "lang": "en", "store": "us",
    "path": "translator-apps-subscription-offline-complaints-iphone/",
    "ct": "rd-translator-complaints",
    "category": "UtilitiesApplication",
    "published": D, "updated": D, "checked": D, "apps": [],
    "kicker": "Translator guide",
    "title": "Translate Now Alternatives Without a Surprise Subscription (2026)",
    "h1": "Translate Now alternatives without a surprise subscription (2026)",
    "description": ("Translator apps get one- and two-star reviews about subscriptions and charges, offline mode that fails and network "
                    "errors. What 157 recent reviews of four translator apps say, and how to check each one before you pay."),
    "llms": ("Guide, 15 November 2026: the three complaints that repeat most in 157 recent one- and two-star App Store reviews of "
             "Translate Now, Google Translate, Microsoft Translator and iTranslate: subscriptions and charges after cancelling (about half "
             "of the Translate Now reviews), offline mode that does not work as advertised, and network errors. Each has a check to do "
             "before you download or travel. Counts are approximate."),
    "stand": "Complaints from 157 recent App Store reviews of four translator apps, and a check to do before you pay or travel.",
    "answer": [
        "<strong>To choose a translator without a surprise subscription, read the trial and renewal terms on its App Store page before you download, "
        "set a reminder for the day the trial ends, and know where to cancel: Settings, your name, Subscriptions.</strong> "
        "Test offline mode at home before a trip, because several apps fail there.",
        "In 157 one- and two-star reviews of Translate Now, Google Translate, Microsoft Translator and iTranslate, the most common complaints were "
        "subscriptions and charges (most of all for Translate Now), offline mode that does not work as expected, and network errors. "
        "Each has a check below.",
    ],
    "sections": [
        ("data", "What we looked at", ""),
        ("money", "“Charged after I cancelled” and the trial (the biggest group)", ""),
        ("offline", "“Doesn't work offline” (Google Translate, Microsoft Translator)", ""),
        ("network", "“Network error” (Microsoft Translator)", ""),
        ("checklist", "Before you download or travel: a 5-line check", ""),
    ],
    "related": ["car-video-complaints", "ai-companion-complaints"],
    "faq": [
        ("Which translator app has the fewest subscription complaints?",
         "The reviews do not name a winner. In this set, Translate Now had the most subscription and charge complaints (14 of 30 recent one- and two-star reviews). Read each app's App Store subscription terms before you download."),
        ("Does Google Translate work offline on iPhone?",
         "Some reviewers say it does not work as advertised offline. Test it at home with Wi-Fi and mobile data turned off, before a trip, and check which languages you can download."),
        ("How do I cancel a translator app subscription?",
         "On iPhone, open Settings, tap your name, tap Subscriptions, tap the subscription and tap Cancel Subscription. Apple explains it on its page about cancelling a subscription."),
        ("Can I get a refund for a charge after I cancelled?",
         "You can ask Apple. Its page on requesting a refund for apps or content bought from Apple explains how; the decision is Apple's."),
    ],
    "sources_html": [
        "Reviews: US App Store customer-review feed, most recent page of each app, 157 reviews with 1-2 stars, downloaded 15 November 2026; counts by keyword, approximate.",
        "Apps: the US App Store pages and Apple lookup data for Translate Now, Google Translate, Microsoft Translator and iTranslate, " + AS_OF + ".",
        a(CANCEL, "Cancel a subscription from Apple") + ", Apple Support.",
        a(REFUND, "Request a refund for apps or content that you bought from Apple") + ", Apple Support.",
    ],
    "fix": 'If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
}]

for _i, (_sid, _h, _body) in enumerate(PAGES[0]["sections"]):
    if _sid in _B:
        PAGES[0]["sections"][_i] = (_sid, _h, _B[_sid])
