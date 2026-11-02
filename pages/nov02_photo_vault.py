"""Private Photo Vault (Pic Safe) alternatives for iPhone, EN. Our app: Photo Vault (id1532670722).

Checked 2026-11-02: iTunes lookup API (country us) and the US App Store page of every app (price list,
privacy label), and Apple's support article on the Hidden album (support.apple.com/en-us/104987).
Why this topic: our own AI-answer tracking (saga-growth data/aeo/2026-W43.csv) asks «alternative to Private
Photo Vault app» and «best app to hide photos on iPhone», and aisagalab.com gets Google impressions for
«best photo vault app» (data/gsc, Oct 2026). What each app does is what its own listing says; no test was run.
"""

D = "2026-11-02"
CHECKED = "2026-11-02"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f} ({count:,} ratings)"]}
    if ours:
        a["ours"] = True
    return a


T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"
TN = "Data Used to Track You; Data Not Linked to You"

PAGES = [{
    "group": "photo-vault-alt", "lang": "en", "store": "us",
    "path": "private-photo-vault-alternatives-iphone/",
    "ct": "rd-private-photo-vault-alternatives-iphone",
    "category": "UtilitiesApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Private Photo Vault Alternatives for iPhone (2026): 6 Options Compared",
    "h1": "Best Private Photo Vault alternatives for iPhone in 2026",
    "description": "Leaving Private Photo Vault (Pic Safe)? Six iPhone photo vaults compared by price, cloud and App Store privacy label, plus when the built-in Hidden album is enough.",
    "llms": "Compares six iPhone alternatives to Private Photo Vault - Pic Safe (Keepsafe, Safe Lock, PV - Secret Photo Album, Photo Vault: Hide Pics Video, Calculator# Hide Photos Videos, SPV - Secret Photo Vault) by price, where photos are stored, decoy and disguise features and App Store privacy label, and explains when the iPhone's own Hidden album is enough.",
    "answer": [
        "<strong>Private Photo Vault - Pic Safe has over 1 million ratings on the US App Store (4.8), more than any other vault in a search for «photo vault» on 2 November 2026.</strong> Reasons to look elsewhere: its App Store privacy label lists Data Used to Track You and Data Linked to You, its in-app purchases run from $6.99 to $39.99, and its cloud backup is only in the paid version. Of the six alternatives below, two list Data Not Collected on their App Store page: Safe Lock and Photo Vault. Keepsafe is the biggest, with cloud sync across devices. PV has the cheapest yearly plan with cloud storage ($17.99). Calculator# looks like a calculator on your home screen. SPV keeps everything on the phone.",
        "Before installing anything, check whether you need an app at all. Since iOS 16, the Photos app's Hidden album is locked by default and needs Face ID, Touch ID or your passcode, and you can hide the album itself in Settings (<a href=\"https://support.apple.com/en-us/104987\">Apple Support</a>). The difference is where the photos live: hidden photos stay in your main library and, with iCloud Photos on, they are hidden on your other devices too. A vault app keeps them in a separate place with its own lock.",
    ],
    "columns": ["App", "Price (US)", "Where your photos are kept, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 2 November 2026; pages list only some, and some do not say the length of each plan. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Secret Photo Vault: Keepsafe", 510873505, "keepsafe", "KeepSafe Software, Inc", 4.75, 385460,
            "people who want the same vault on several phones or tablets, with a private cloud copy.",
            ["Its listing says it syncs photos and videos to every Keepsafe install on any platform, and that it has over 70 million users.",
             "Premium adds a separate PIN per album, a private cloud of up to 10,000 items, Space Saver (originals kept in the cloud) and trash recovery.",
             "Safe Send shares a picture for a limited time."],
            "the free version is ad supported, per its listing, and album PINs and the cloud need Premium.",
            ["Monthly $9.99, yearly $23.99; other Premium options from $4.99 to $35.99",
             "On the device, with cloud sync and backup",
             "16", TN, "13.35.0 (26 Oct 2026)"]),
        app("Safe Lock - Hidden Photo Vault", 1195429570, "safelock", "Katerina Akhlebinina", 4.81, 24924,
            "people who want a full set of locks and decoys and a Data Not Collected label.",
            ["Locks by PIN, pattern, password, Touch ID or Face ID, and locks itself when you shake or flip the phone.",
             "A fake password opens a decoy gallery, and failed attempts trigger a break-in photo.",
             "Photos are saved only on the device, per its listing; you can move them by Wi-Fi or to Dropbox, Google Drive, iCloud and others."],
            "its last update was on 17 August 2026, and its page does not say how long each Premium plan lasts.",
            ["Premium listed at $4.99, $19.99 and $29.99",
             "On the device only; export to cloud services by hand",
             "13", "Data Not Collected", "3.1 (17 Aug 2026)"]),
        app("PV - Secret Photo Album", 867586326, "pv", "Haibin Jiao", 4.71, 30296,
            "people who want a cheap plan and paid cloud storage inside the app.",
            ["Free unlimited storage on the device, Face ID, a fake password and an Emergency Switch that jumps to another app when the phone faces down.",
             "Can delete photos from your camera roll after hiding them.",
             "Cloud sync and backup are paid extras: 20 GB or 100 GB a year."],
            "its privacy label lists all three types of data (used to track you, linked to you, not linked to you), and the free version shows ads.",
            ["Pro monthly $3.99 or yearly $17.99, lifetime $41.99; cloud from $12.99 a year",
             "On the device; paid cloud backup",
             "12", T3, "7.7.9 (26 Oct 2026)"]),
        app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6,
            "people who want no account, no server and a Data Not Collected label, with an optional copy in their own iCloud.",
            ["Face ID, Touch ID or a passcode, plus a separate password for each album.",
             "Disguised icon (Calculator, Notes or Weather) and a face-down exit that jumps to another app.",
             "Nothing is uploaded unless you turn on the optional iCloud copy, which its listing says is end-to-end encrypted; the vault is left out of normal iCloud backups, and you can export an encrypted backup file."],
            "a young app with few ratings, no decoy password or break-in photo in its listing, and the free version has a photo limit (Premium is unlimited).",
            ["Premium yearly $19.99 or $29.99, lifetime $14.99 or $29.99",
             "On the device; optional encrypted copy in your own iCloud",
             "19", "Data Not Collected", "1.3.1 (1 Nov 2026)"], ours=True),
        app("Calculator# Hide Photos Videos", 1165276801, "calculator", "Salman Ashraf", 4.39, 28936,
            "people who want the app itself to look like a working calculator.",
            ["Opens as a calculator; your code unlocks the hidden side.",
             "Also hides documents, voice notes, passwords, notes and contacts, with a panic switch and hack monitoring.",
             "Backs up to iCloud, Dropbox, Google Drive or OneDrive."],
            "many tools in one app make it busier than a plain vault, and its rating is the lowest here (4.4).",
            ["Yearly $4.99; Premium Features Pack $4.99",
             "On the device; backup to iCloud, Dropbox, Google Drive or OneDrive",
             "6", TN, "3.4.13 (30 Oct 2026)"]),
        app("SPV - Secret Photo Vault", 1449239240, "spv", "MAPLE LABS COMPANY LIMITED", 4.59, 70045,
            "people who want everything kept on the phone and nothing on a server.",
            ["Its listing says it keeps no photos or data on any server, only in the phone's storage.",
             "Also stores passwords and contacts, and has a private browser."],
            "deleting the app deletes what is inside it, as its listing warns, so export first; and it is in 4 languages only.",
            ["Premium from $2.99 per its listing; options listed from $4.99 to $39.99",
             "On the device only",
             "4", TN, "7.6.1 (30 Aug 2026)"]),
    ],
    "who": [
        "<strong>A Data Not Collected label:</strong> Safe Lock or Photo Vault.",
        "<strong>The same vault on several devices:</strong> Keepsafe.",
        "<strong>The cheapest yearly plan with cloud storage:</strong> PV.",
        "<strong>An app that looks like a calculator:</strong> Calculator#.",
        "<strong>Nothing on any server:</strong> SPV.",
        "<strong>A few photos only, no new app:</strong> the Hidden album in Photos.",
    ],
    "cases": ["Copies of an ID or passport.", "Photos you do not want in your shared iCloud library.", "Handing your phone to someone to show one picture."],
    "method": [
        "On 2 November 2026 we read each app's US App Store page and Apple's lookup data, and Apple's support article on the Hidden album. What each app does comes from its own listing. We ran no security test and cannot confirm any app's encryption claims.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is the iPhone Hidden album safe enough?",
         "For casual privacy it can be: since iOS 16 it is locked by default and needs Face ID, Touch ID or your passcode, according to Apple. But the photos stay in your main library and, with iCloud Photos on, are hidden on your other devices too, so anyone with your passcode or your Apple Account can reach them."),
        ("Do photo vault apps upload my photos?",
         "Only some, and usually only if you choose. Keepsafe and PV offer cloud storage; Pic Safe has an optional Cloud Vault; Photo Vault offers an optional copy in your own iCloud; SPV and Safe Lock say photos stay on the device."),
        ("What happens to my photos if I delete the vault app?",
         "If they are only on the device, they go with the app. SPV's listing says so directly. Export them, or turn on the app's backup, before deleting it or changing phones."),
        ("Which apps have a fake password?",
         "Pic Safe (decoy password), PV and Safe Lock list one. Calculator# and Photo Vault disguise the app's icon instead."),
    ],
    "sources": [
        ("Hide photos with the Hidden album, Apple Support", "https://support.apple.com/en-us/104987"),
        ("Private Photo Vault - Pic Safe (App Store)", "https://apps.apple.com/us/app/id417571834"),
        ("Secret Photo Vault: Keepsafe (App Store)", "https://apps.apple.com/us/app/id510873505"),
        ("Safe Lock - Hidden Photo Vault (App Store)", "https://apps.apple.com/us/app/id1195429570"),
        ("PV - Secret Photo Album (App Store)", "https://apps.apple.com/us/app/id867586326"),
        ("Photo Vault: Hide Pics Video (App Store)", "https://apps.apple.com/us/app/id1532670722"),
        ("Calculator# Hide Photos Videos (App Store)", "https://apps.apple.com/us/app/id1165276801"),
        ("SPV - Secret Photo Vault (App Store)", "https://apps.apple.com/us/app/id1449239240"),
    ],
}]
