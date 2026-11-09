"""Keepsafe alternatives on iPhone, EN. Our app: Photo Vault (id1532670722).

Checked 2026-11-03: US App Store search for «keepsafe», «photo vault», «private photo vault», «secret photo album»,
«hide photos», iTunes lookup and the US App Store page of every app (price list, privacy label). Keepsafe itself goes in
the intro. Why this topic: Google suggests «keepsafe alternative», «best keepsafe alternative», «keepsafe free
alternative», «apps like keepsafe for iphone», «keepsafe vs private photo vault» (3 Nov); no page on the 4 sites is
about Keepsafe (reviewland has Private Photo Vault alternatives, hide photos and no-data-collection vaults; aisagalab
has general vault guides). Registered in ios-playbook references/temas-webs.md (dffbfb8). Nothing installed or tested.
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


NC = "Data Not Collected"
NL = "Data Not Linked to You"
TN = "Data Used to Track You; Data Not Linked to You"
TL = "Data Used to Track You; Data Linked to You"

PAGES = [{
    "group": "keepsafe-alt", "lang": "en", "store": "us",
    "path": "keepsafe-alternatives-iphone/",
    "ct": "rd-keepsafe-alt-iphone",
    "category": "PhotographyApplication",
    "published": D, "updated": "2026-11-09", "checked": CHECKED,
    "title": "Keepsafe Alternatives for iPhone (2026): 7 Photo Vault Apps",
    "h1": "Best Keepsafe alternatives for iPhone in 2026",
    "description": "Keepsafe's free version shows ads and its label includes tracking. Seven iPhone photo vaults compared by price, privacy label, decoy PIN and backup.",
    "llms": "Compares seven iPhone alternatives to Keepsafe (Secret Photo Vault), the photo locker whose free Basic version is ad supported and whose App Store privacy label includes Data Used to Track You: Private Photo Vault, Safe Lock, Secret Photo Album 1Locker, Photo Vault, Hide it Pro, SPV and Secret Photo Album SA, by price, privacy label, decoy or fake PIN, and where backups go.",
    "llms_note": "Photo Vault, one of the seven, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Keepsafe is still a big, maintained photo vault</strong>: <a href=\"https://apps.apple.com/us/app/id510873505\">Secret Photo Vault: Keepsafe</a> has 4.8 stars in the US and was updated on 26 October 2026. People look elsewhere for three reasons its own listing shows: Keepsafe Basic is ad supported, Premium is a subscription (listed at $9.99 a month or $23.99 a year, among other prices), and its privacy label includes <em>Data Used to Track You</em>.",
        "Of the seven below, only Safe Lock has the label <em>Data Not Collected</em>; Photo Vault, Hide it Pro and 1Locker list only Data Not Linked to You (for Photo Vault, purchases only). 1Locker and Photo Vault list a one-time purchase next to their subscriptions, and Hide it Pro charges only for cloud storage and a password reset. Private Photo Vault is the closest match feature for feature, with an encrypted cloud backup and a break-in report, but its label also includes tracking. To compare it on its own, reviewland has <a href=\"https://reviewland.io/private-photo-vault-alternatives-iphone/\">Private Photo Vault alternatives</a>.",
    ],
    "columns": ["App", "Price (US)", "Decoy or fake PIN, per its listing", "Backup, per its listing", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average. Privacy labels rechecked on 9 November 2026.",
    "apps": [
        app("Private Photo Vault - Pic Safe", 417571834, "private-photo-vault", "Legendary Software Labs LLC", 4.82, 1018879,
            "the closest match to Keepsafe's features, with the most ratings of any vault.",
            ["Password, PIN or pattern lock, password-protected albums, a decoy password and a face-down lock.",
             "Break-in report with a photo and GPS location; a private web browser.",
             "Cloud Vault backup encrypted with a password only you know; the free version has no cloud backup, per its listing."],
            "its privacy label includes Data Used to Track You and Data Linked to You, and backup to its cloud needs Premium.",
            ["Premium $6.99 to $39.99 listed; Upgrade $39.99",
             "Yes (decoy password)", "Encrypted Cloud Vault (Premium)", TL, "26.0 (2 Nov 2026)"]),
        app("Safe Lock - Hidden Photo Vault", 1195429570, "safe-lock", "Katerina Akhlebinina", 4.81, 24924,
            "a vault with no data collected per its label, and backups to the cloud you already use.",
            ["PIN, pattern, alphabetic password, Face ID or Touch ID; shake or flip the phone to lock.",
             "A fake password opens a fake gallery; break-in reports with photos; hidden camera.",
             "Exports to and imports from Dropbox, Google Drive, iCloud, Box and Yandex.Disk, or over Wi-Fi."],
            "its last update was 17 August 2026, and its listing only says the Premium subscription «unlocks all features», without listing them.",
            ["Premium Account $4.99, $19.99 or $29.99",
             "Yes (fake gallery)", "Your own Dropbox, Google Drive, iCloud or Box", NC, "3.1 (17 Aug 2026)"]),
        app("Secret Photo Album · 1Locker", 1462756877, "1locker", "Touchberry Inc", 4.68, 13711,
            "no ads and a one-time payment option, with passwords and notes in the same vault.",
            ["PIN, Face ID or Touch ID, or an alphabetic password; a decoy account hides the real content.",
             "Also stores passwords, notes and contacts, and has a private browser.",
             "No ads, per its listing; a one-time plan is offered next to monthly and yearly ones."],
            "cloud backup is an in-app purchase, and it is in 5 languages.",
            ["One-time $24.99 («Entire Life»); storage $2.99 to $49.99; $7.99 listed",
             "Yes (decoy account)", "Wi-Fi backup; cloud backup paid", NL, "4.0.4 (26 Oct 2026)"]),
        app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6,
            "no account and a short privacy label (only purchases, not linked to you), with a disguised icon and a backup file you keep yourself.",
            ["Face ID, Touch ID or a passcode, plus a separate password for each album.",
             "Disguised icon (Calculator, Notes or Weather); flip the phone face down and it jumps to Safari, Calendar or Messages.",
             "Encrypted backup to one password-locked file you keep in Files or on your computer; optional encrypted copy in your own iCloud, and the vault is left out of regular iCloud backups."],
            "no decoy PIN or break-in report in its listing, and unlimited photos and the iCloud copy need Premium.",
            ["Premium $19.99 or $29.99 a year; lifetime $14.99 or $29.99",
             "No (disguised icon instead)", "Encrypted file you keep; your own iCloud (Premium)", "Data Not Linked to You (purchases)", "1.3.1 (1 Nov 2026)"], ours=True),
        app("Hide Photos Video -Hide it Pro", 523488488, "hide-it-pro", "Anuj Tenani", 4.65, 24796,
            "hiding photos with no subscription for the basics, in an app that can pretend to crash.",
            ["A disguise screen makes the app look as if it crashed when someone else opens it.",
             "An escape code makes the vault look empty.",
             "USB export of all files in one tap; unhide back to the photo library."],
            "English only, its last update was 11 January 2026, and resetting a forgotten password is a paid purchase ($4.99).",
            ["Cloud storage $9.99 a month; password reset $4.99",
             "Yes (escape code shows an empty vault)", "Cloud storage (subscription); USB export", NL, "6.3.0 (11 Jan 2026)"]),
        app("SPV - Secret Photo Vault", 1449239240, "spv", "MAPLE LABS COMPANY LIMITED", 4.59, 70045,
            "photos, contacts and passwords behind one PIN, kept on the device.",
            ["Stores photos, videos, contacts, passwords and browser data behind a PIN.",
             "Keeps nothing on any server, per its listing: everything stays in the phone's storage.",
             "Weekly, monthly and yearly Premium, from $2.99 per its listing."],
            "deleting the app deletes the photos, its label includes Data Used to Track You, it is in 4 languages, and the listing names no decoy PIN.",
            ["Premium $4.99 to $39.99 listed (from $2.99 a week, per its listing)",
             "Not named", "None: device only", TN, "7.6.1 (30 Aug 2026)"]),
        app("Secret Photo Album - SA", 1174964304, "secret-album", "BP Mobile LLC", 4.59, 38908,
            "an encrypted cloud album you can open on several devices, with break-in alerts.",
            ["Decoy PIN; break-in alerts with photos of intruders.",
             "Encrypted cloud storage to open the album from different devices; unlimited storage with Premium.",
             "A private browser with an ad blocker."],
            "its privacy label includes Data Used to Track You and Data Linked to You, and the price list is long ($1.99 to $51.99).",
            ["Premium $1.99 to $51.99 listed",
             "Yes (decoy PIN)", "Encrypted cloud", TL, "2.18 (6 Oct 2026)"]),
    ],
    "who": [
        "<strong>Keepsafe's features, more ratings:</strong> Private Photo Vault.",
        "<strong>No data collected, backup to your own Dropbox or Drive:</strong> Safe Lock.",
        "<strong>One payment, no ads:</strong> 1Locker.",
        "<strong>No account, disguised icon, backup file you keep:</strong> Photo Vault.",
        "<strong>Free basics, app that pretends to crash:</strong> Hide it Pro.",
        "<strong>Album on several devices:</strong> Secret Photo Album SA.",
    ],
    "cases": ["Moving off Keepsafe without losing photos.", "Keeping ID and card photos out of the camera roll.", "Handing your phone to someone without showing private albums."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «keepsafe», «photo vault», «private photo vault», «secret photo album» and «hide photos», and read Keepsafe's and each app's US App Store page and Apple's lookup data. We installed nothing and did not test encryption.",
        "Before you delete Keepsafe, export your photos back to the Photos app or check that your new vault has them: several vaults, SPV for example, say photos are deleted with the app.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a free alternative to Keepsafe?",
         "All seven are free to download. Hide it Pro sells only cloud storage and a password reset; the others limit some features to Premium. Check what the free version stores before moving everything."),
        ("Which Keepsafe alternative does not track you?",
         "Safe Lock has the App Store label Data Not Collected; Photo Vault (purchases only), Hide it Pro and 1Locker list Data Not Linked to You. Keepsafe, Private Photo Vault, SPV and Secret Photo Album SA include Data Used to Track You."),
        ("Keepsafe or Private Photo Vault?",
         "Both are large, maintained vaults with decoy features and a cloud backup on Premium, and both labels include tracking. Private Photo Vault adds a break-in report with GPS and a private browser."),
        ("Which ones have a one-time price instead of a subscription?",
         "1Locker («Entire Life», $24.99) and Photo Vault (lifetime $14.99 or $29.99) list one; Hide it Pro needs no subscription for its basics."),
    ],
    "sources": [
        ("Secret Photo Vault: Keepsafe (App Store)", "https://apps.apple.com/us/app/id510873505"),
        ("Private Photo Vault (App Store)", "https://apps.apple.com/us/app/id417571834"),
        ("Safe Lock (App Store)", "https://apps.apple.com/us/app/id1195429570"),
        ("Secret Photo Album · 1Locker (App Store)", "https://apps.apple.com/us/app/id1462756877"),
        ("Photo Vault: Hide Pics Video (App Store)", "https://apps.apple.com/us/app/id1532670722"),
        ("Hide it Pro (App Store)", "https://apps.apple.com/us/app/id523488488"),
        ("SPV - Secret Photo Vault (App Store)", "https://apps.apple.com/us/app/id1449239240"),
        ("Secret Photo Album - SA (App Store)", "https://apps.apple.com/us/app/id1174964304"),
    ],
}]
