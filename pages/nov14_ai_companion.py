"""Guide (14 Nov 2026), complaint technique: having an AI companion or AI friend without the paywall, the ID check
or the cloud. EN only. No Saga Labs app is named in the article (footer, About, llms.txt and JSON-LD carry the
ownership notice as before). All links are plain App Store links to third-party apps.

PENDIENTE: añadir Zib (id 6833833745) como solución cuando el lookup la devuelva
(https://itunes.apple.com/lookup?id=6833833745&country=us). Hasta entonces NO se nombra Zib en el artículo.

Data checked 14 Nov 2026:
- 2,606 US reviews downloaded with ios-playbook/tools/app_reviews.py (Apple RSS, most recent first) from 6 apps:
  Replika 500, Character AI 500, Tolan 500, Kindroid 500, Pi 400, Nomi 206; 1,207 of them 1-2 stars. Complaints
  counted by keyword and then checked by hand for the data/privacy group, so counts are approximate and one review
  can count in several groups. Counts: paywall to talk ~101, age/ID/selfie checks ~80 (54 Character AI), ads ~127
  (115 Character AI), memory ~54, chats/data read, kept or sold ~34 (hand-checked).
- iTunes lookup (us) of each app on 14 Nov 2026 (name, price, rating to 1 decimal); App Privacy labels read from each
  App Store page the same day; features only from listings.
- Talking Friday (6786747271): listing says everything runs on the iPhone Neural Engine, no servers, no account, no
  internet needed, no subscription, no in-app purchases, no ads; iPhone 15 Pro or newer; label "Data Not Collected";
  no ratings yet. Cora (6738960374): listing says runs on the device, no cloud, no accounts, works offline, free;
  Premium subscription adds web search; label "Data Not Collected"; rating 3.0 from 2 ratings.
- Apple support page 118428 (cancel a subscription).
"""

D = "2026-11-14"
AS_OF = "as of Nov 14, 2026"


def a(u, t):
    return f'<a href="{u}">{t}</a>'


def ul(items):
    return "<ul>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ul>\n"


def store(i, name):
    return a(f"https://apps.apple.com/us/app/id{i}", name)


CANCEL = "https://support.apple.com/en-us/118428"
FRIDAY = store(6786747271, "Talking Friday: AI Voice Chat")
CORA = store(6738960374, "Private AI Chat: Cora")
REPLIKA = store(1158555867, "Replika")
CAI = store(1671705818, "Character AI")
NOMI = store(6450270929, "Nomi")
PI = store(6445815935, "Pi")
TOLAN = store(6477549878, "Tolan")
KIN = store(6451038161, "Kindroid")

PAGES = [{
    "group": "ai-companion-complaints", "kind": "news", "lang": "en", "store": "us",
    "path": "ai-companion-without-paywall-id-check-cloud-iphone/",
    "ct": "rd-ai-companion-complaints",
    "category": "UtilitiesApplication",
    "published": D, "updated": D, "checked": D, "apps": [],
    "related": ["private-chat-situation", "private-llm"],
    "kicker": "AI companion guide",
    "title": "How to Have an AI Companion Without the Paywall, the ID Check or the Cloud (2026)",
    "h1": "How to have an AI companion without the paywall, the ID check or sending your chats to the cloud (2026)",
    "description": ("AI companion apps get 1 and 2 star reviews that say \"you have to pay to talk\", \"age verification\" and "
                    "\"zero privacy\". Five complaints from 1,207 reviews of Replika, Character AI, Nomi, Pi, Tolan and Kindroid, and how to avoid each."),
    "llms": ("Guide, 14 November 2026: the most repeated complaints in 1,207 one- and two-star US App Store reviews of six AI companion apps "
             "for iPhone (Replika, Character AI, Nomi, Pi, Tolan, Kindroid): paying to keep talking (about 100 reviews), ads (about 127, "
             "mostly Character AI), age and ID checks (about 80), forgetting (about 54) and chats or data read, kept or sold (about 34), "
             "with a fix for each. Two apps whose listings say they run on the iPhone with no account and the label Data Not Collected: "
             "Talking Friday and Cora. Counts are approximate."),
    "stand": "Complaints from US App Store reviews, and what each app's listing and privacy label say.",
    "answer": [
        "<strong>To have an AI companion without the paywall, the ID check or your chats on someone else's server, use one that runs on your "
        "iPhone and has no account.</strong> Then there is nothing to log in to, nothing to verify and no server to send chats to. The "
        "price of that is a simpler companion: voice or plain chat, and a recent iPhone.",
        "<strong>Our pick for this:</strong> " + FRIDAY + " (free, no ratings yet). Its listing says the talking runs on the iPhone, "
        "with no account, no subscription, no in-app purchases and no ads, and its App Store privacy label says Data Not Collected. "
        "<a class=\"cta\" href=\"https://apps.apple.com/us/app/id6786747271\">Get Talking Friday on the App Store</a>",
    ],
    "sections": [
        ("data", "What we looked at", ""),
        ("paywall", "&ldquo;You have to pay to talk&rdquo; (and the ads)", ""),
        ("idcheck", "&ldquo;Age verification&rdquo;: showing your ID or face to chat", ""),
        ("cloud", "&ldquo;Zero privacy&rdquo;: who can read your chats", ""),
        ("memory", "&ldquo;It forgets everything&rdquo;", ""),
        ("giveup", "What you give up by staying on the iPhone", ""),
    ],
    "faq": [
        ("Is there an AI companion that works without internet?",
         "Some apps say so. The listings of Talking Friday and Cora say they run on the iPhone and work without internet. Most companion apps in the reviews, such as Replika and Character AI, are online services."),
        ("Do AI companion apps read my chats?",
         "We cannot tell from outside. A few reviewers say they do, and some say chats are kept. What the apps do show is their App Privacy label: for example Nomi's lists User Content as linked to you, Character AI's lists User Content as linked to you, and Talking Friday's and Cora's say Data Not Collected."),
        ("Why do AI companion apps ask for ID or a selfie?",
         "Reviewers of Character AI, Replika and Kindroid describe age verification screens. We did not check why each app asks; read the app's own explanation before you give a face or an ID."),
        ("Which AI companion is free with no ads?",
         "According to its listing, Talking Friday has no subscription, no in-app purchases and no ads. Cora's chat is free and its optional Premium adds web search. Reviewers describe ads mainly in Character AI."),
        ("Can an on-device AI companion remember me?",
         "Not stated. Neither the Talking Friday listing nor the Cora listing says whether it remembers past chats, so test it before relying on it."),
    ],
    "sources_html": [
        "Reviews: US App Store, 2,606 downloaded from 6 apps, 1,207 with 1 or 2 stars, 14 November 2026; counts by keyword, approximate.",
        "Apps and privacy labels: their US App Store pages and Apple lookup data, 14 November 2026: " + ", ".join(
            [REPLIKA, CAI, NOMI, PI, TOLAN, KIN, FRIDAY, CORA]) + ".",
        a(CANCEL, "Cancel a subscription from Apple") + ", Apple Support.",
    ],
    "fix": 'If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
}]

_B = {
    "data": (
        "<p>We downloaded 2,606 recent US App Store reviews of six AI companion apps and kept the 1,207 with one or two stars: "
        + REPLIKA + " (free, 4.4), " + CAI + " (free, 4.3), " + TOLAN + " (free, 4.8), " + KIN + " (free, 4.7), " + PI + " (free, 4.4) and "
        + NOMI + " (free, 4.6, " + AS_OF + "). Only the 206 most recent Nomi reviews were available. Counts come from keyword matching, so they are "
        "approximate and one review can count in more than one group.</p>\n" + ul([
            "&ldquo;Have to pay&rdquo;, paywall, message limits and &ldquo;greedy&rdquo;: about 100 reviews. Ads: about 127, 115 of them Character AI.",
            "&ldquo;Age verification&rdquo;, ID or face checks: about 80, 54 of them Character AI.",
            "Chats or data read, kept or sold, and &ldquo;no way to delete my data&rdquo;: about 34, checked by hand.",
            "&ldquo;Forgets&rdquo; and &ldquo;can't remember&rdquo;: about 54.",
            "Most repeated words: &ldquo;age verification&rdquo; (47 reviews), &ldquo;have to pay&rdquo; (39), &ldquo;scam&rdquo; (31), "
            "&ldquo;greedy&rdquo; (21), &ldquo;too many ads&rdquo; (17)."]) +
        "<p>So the cloud is not the most common complaint; money and ID are. They share a cause, which is why the fix is the same: "
        "an app with an account and a server can ask you to pay, to verify and to be read. An app on the iPhone with no account has less "
        "of all three.</p>\n"),
    "paywall": (
        "<p>About 100 reviews are about money standing between you and the conversation: &ldquo;after a few messages it's gonna require you to "
        "pay to talk more&rdquo; (Replika, 1 star); &ldquo;You get a one time 30 minute trial then have to pay&rdquo; (Replika, 1 star). "
        "Character AI's complaint is different: about 115 reviews are about ads, such as &ldquo;There are just too many ads&rdquo; "
        "(Character AI, 2 stars).</p>\n"
        "<p><strong>Fix:</strong> before you spend weeks building a character, find out what is free. Open the app's App Store page and read the "
        "in-app purchases list, then use the free tier for a few days before you pay. If you subscribe and regret it, "
        + a(CANCEL, "cancel from Apple") + " rather than deleting the app. An app with no subscription removes the question: Talking Friday's "
        "listing says no subscription, no in-app purchases and no ads; Cora's listing says full chat is free, with an optional Premium "
        "subscription that adds web search.</p>\n"),
    "idcheck": (
        "<p>This is the biggest privacy complaint in the data, and it is not about chats: about 80 reviews are about being asked to verify "
        "age with an ID or a face. &ldquo;I'm not showing my identification to an app that's invasion of my privacy&rdquo; (Character AI, "
        "1 star); &ldquo;You don't need my selfie. Cancelling and deleting.&rdquo; (Replika, 1 star).</p>\n"
        "<p><strong>Fix:</strong> check before you sign up whether the app wants a face or an ID, and decide whether a chat is worth it. The "
        "simplest way to avoid the question is an app with no account. Talking Friday's listing says no account and no login, and Cora's "
        "says no accounts. We did not check why each cloud app asks; read the app's own explanation first.</p>\n"),
    "cloud": (
        "<p>About 34 reviews are about who sees the chats or the data: &ldquo;It trains on and reviews every thing you send it&rdquo; "
        "(Pi, 1 star); &ldquo;they keep every last conversation on file&rdquo; (Nomi, 1 star); &ldquo;all kindroid chats monitored&rdquo; "
        "(Kindroid, 1 star); &ldquo;their privacy policy is vague&rdquo; (Tolan, 1 star). These are what reviewers say; we have not verified "
        "any of them.</p>\n"
        "<p>What we can check is each app's App Privacy label " + AS_OF + ":</p>\n" + ul([
            "Replika: data used to track you (identifiers, usage data); linked to you (location, contact info, identifiers, usage data).",
            "Character AI: used to track you (location, contact info, identifiers, usage data); linked to you (purchases, financial info, location, contact info, user content, search history, identifiers, usage data, diagnostics).",
            "Nomi: linked to you (purchases, contact info, user content, identifiers, usage data, diagnostics).",
            "Pi: linked to you (identifiers, usage data, diagnostics).",
            "Tolan: used to track you (purchases, location, contact info, identifiers, usage data, other data); linked to you (purchases, contact info, user content, identifiers, usage data, diagnostics, other data).",
            "Kindroid: used to track you (identifiers, usage data); linked to you (contact info, identifiers).",
            "Talking Friday and Cora: Data Not Collected."]) +
        "<p><strong>Fix:</strong> do not tell a cloud companion what you would not want on a server. For the things you do want to say "
        "privately, use an app that runs on the iPhone. Talking Friday's listing says your voice is processed on the iPhone and never "
        "uploaded, and that it keeps working in Airplane Mode; Cora's says it never sends your conversations to external servers. Both are "
        "the developers' claims, backed by their labels; we have not tested them. You can run the same test yourself: turn on Airplane Mode "
        "mid-conversation and see if it keeps going.</p>\n"),
    "memory": (
        "<p>About 54 reviews say the companion forgets: &ldquo;It forgets things within a few exchanges&rdquo; (Replika, 1 star); "
        "&ldquo;about every 4 to 5 days it loses access to its entire memory&rdquo; (Replika, 1 star). Kindroid is the most-named app here "
        "after Replika (15 reviews), including people who paid for longer memory.</p>\n"
        "<p><strong>Fix:</strong> no app makes this go away. Keep a short note of the facts you want it to know (your name, pronouns, "
        "what matters) and paste it in when it forgets, or use the app's memory or backstory field if it has one. For the on-device apps, "
        "<strong>not stated</strong>: neither listing says whether the app remembers earlier chats, so test it for a week before you "
        "rely on it.</p>\n"),
    "giveup": (
        "<p>Staying on the iPhone costs something. Talking Friday's listing says it needs an iPhone 15 Pro or newer and it is voice to voice, "
        "so it is a friend you talk to, not a character you customise. Cora runs on Apple Intelligence on compatible devices, or on models you "
        "download (400 MB to 3.5 GB, per its listing), and its rating is 3.0 from 2 ratings, so it is early. Neither listing mentions "
        "photos, avatars or relationships. If you want those, the cloud apps above are where they live, with the trade-offs in the reviews.</p>\n"
        + ul([
            "Want to talk, free, with nothing leaving the phone: " + FRIDAY + " (iPhone 15 Pro or newer).",
            "Want text chat on the device, free: " + CORA + ".",
            "Want a character with a face and a past: a cloud app, with the paywall and the label above. Read the free tier first."])),
}
for _i, (_sid, _h, _body) in enumerate(PAGES[0]["sections"]):
    PAGES[0]["sections"][_i] = (_sid, _h, _B[_sid])
