"""Calculator vault apps (vaults disguised as a calculator) on iPhone, EN. Our app: Photo Vault (id1532670722), whose
icon can look like Calculator, Notes or Weather; it is NOT a working calculator, and the page says so.

Checked 2026-11-03: US App Store search for «calculator vault», «secret calculator», «calculator hide photos»,
«calculator lock», «calculator vault hide photos», «hidden calculator», iTunes lookup and the US App Store page of every
app (price list, privacy label). Left out: apps whose listing does not describe a calculator (Secret Safe Lock, HideU,
whose description is for «VaultMate»), and apps not updated since 2024 or earlier (Calculator Lock by Zipo, Secret Photo
Album ++). Why this topic: Google suggests «calculator vault app iphone», «secret calculator app iphone», «hidden
calculator app iphone», «calculator photo vault ios», «fake calculator app iphone» (3 Nov); no page on the 4 sites is
about calculator vaults (reviewland's hide-photos page lists Calculator# among general vaults). Registered in
ios-playbook references/temas-webs.md (dbfbf0e). Nothing installed or tested.
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

PAGES = [{
    "group": "calculator-vault", "lang": "en", "store": "us",
    "path": "calculator-vault-apps-iphone/",
    "ct": "rd-calculator-vault-iphone",
    "category": "PhotographyApplication",
    "published": D, "updated": "2026-11-09", "checked": CHECKED,
    "title": "Calculator Vault Apps for iPhone (2026): 6 Secret Photo Vaults",
    "h1": "Best calculator vault apps for iPhone in 2026",
    "description": "Six iPhone vaults that hide photos behind a calculator, a converter or a calculator icon: which ones really calculate, decoy PINs, backups and price.",
    "llms": "Compares six iPhone photo vaults disguised as a calculator or converter: Calculator#, Calculator Vault (Cloud Honest), Converter: Hidden Photo Vault, Photo Vault (calculator-style icon only), CalcX Vault and Secret Calculator Vault, by whether the calculator works, how you unlock it, decoy or emergency PIN, backup, price and App Store privacy label.",
    "llms_note": "Photo Vault, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>A calculator vault is a photo vault that looks like a calculator on your home screen.</strong> There are two kinds. Some are a working calculator: you type your PIN and press «=», and the vault opens; Calculator Vault by Cloud Honest, Calculator#, CalcX and Secret Calculator work this way, and Converter does the same with a currency converter. Others, like Photo Vault, only change the icon to look like Calculator and open with Face ID or a passcode; the name under the icon does not change.",
        "Of the six, Calculator Vault (Cloud Honest) adds an emergency PIN that shows an empty vault and a photo of whoever types a wrong PIN; Calculator# has the most ratings and backs up to iCloud, Dropbox, Google Drive or OneDrive. Converter and Secret Calculator have the label <em>Data Not Collected</em>; Photo Vault lists only purchases, not linked to you, and nothing used to track you. If you only want to hide a few photos, the iPhone's own Hidden album may be enough; aisagalab explains <a href=\"https://aisagalab.com/photo-vault/is-iphone-hidden-album-safe.html\">how safe the Hidden album is</a>.",
    ],
    "columns": ["App", "Price (US)", "Disguise and unlock, per its listing", "Decoy or emergency PIN", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average. Privacy labels rechecked on 9 November 2026.",
    "apps": [
        app("Calculator Vault : Hide Photo", 6767042215, "calculator-vault", "CLOUD HONEST LLC", 4.65, 37,
            "a working calculator with an emergency PIN and an intruder photo, and a clear free plan.",
            ["A real calculator for standard math; type your PIN and press «=» to open the vault.",
             "An emergency PIN shows an empty vault; a wrong PIN takes a front-camera photo with time and location; several vaults, each with its own PIN.",
             "Free plan: up to 20 items, per its listing. No account and no servers; optional backup to your own iCloud with Pro."],
            "unlimited storage and iCloud backup need Pro.",
            ["Pro $2.99 to $3.99 a month, $14.99 to $24.99 a year, lifetime $39.99 or $59.99",
             "Working calculator; PIN then «=»", "Yes (emergency PIN shows an empty vault)", NL, "1.9 (19 Sep 2026)"]),
        app("Calculator# Hide Photos Videos", 1165276801, "calculator-hash", "Salman Ashraf", 4.39, 28938,
            "the most ratings, and the most things to hide: photos, documents, passwords, notes and contacts.",
            ["Looks like a calculator; opens with the calculator, a PIN, password, pattern, Touch ID or Face ID.",
             "Panic switch, disguise mode and a log of break-in attempts.",
             "Backup to iCloud, Dropbox, Google Drive or OneDrive; Wi-Fi transfer from a computer."],
            "free with ads and limits, per its listing, and its privacy label includes Data Used to Track You.",
            ["Yearly $4.99; Premium Features Pack $4.99",
             "Calculator screen; code or Face ID", "Panic switch (decoy not named)", TN, "3.4.13 (30 Oct 2026)"]),
        app("Converter: Hidden Photo Vault", 1536734125, "converter", "Dmitry Petrov", 4.86, 3657,
            "paying once, with a currency converter instead of the usual calculator.",
            ["Disguised as a currency converter; a password opens the vault.",
             "Files are encrypted and kept on the phone and in your iCloud; they close again when you leave the app.",
             "One purchase, no subscription: Full Access Forever is listed at $19.99."],
            "English only, iOS 18.2 or later, and its last update was 2 December 2025.",
            ["Full Access Forever $19.99 (also listed at $9.99 and $14.99)",
             "Currency converter; password", "Not named", NC, "3.0.7 (2 Dec 2025)"]),
        app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6,
            "a vault whose icon can pass for Calculator, Notes or Weather, with Face ID and no account.",
            ["Disguised icon: Calculator, Notes or Weather. It is not a working calculator: it opens with Face ID, Touch ID or a passcode.",
             "A separate password for each album; flip the phone face down and it jumps to Safari, Calendar or Messages.",
             "Encrypted backup to one file you keep, optional encrypted copy in your own iCloud; the vault is left out of regular iCloud backups."],
            "the disguise is the icon only: the name under it on the home screen still reads Photo Vault. There is no decoy PIN in its listing, and unlimited photos need Premium.",
            ["Premium $19.99 or $29.99 a year; lifetime $14.99 or $29.99",
             "Calculator-style icon; Face ID or passcode", "No (face-down exit instead)", "Data Not Linked to You (purchases)", "1.3.1 (1 Nov 2026)"], ours=True),
        app("CalcX Vault Secret Photo Lock", 1577144445, "calcx", "Vasilkoff Ltd", 4.48, 202,
            "a calculator-style entry screen with photos, contacts and notes in one vault.",
            ["Enter your password and press «=» to open the vault.",
             "Stores photos, videos, contacts, notes and files; albums, rename, restore and delete.",
             "Its listing names a fake vault and icon concealment among paid features."],
            "a long list of weekly to lifetime prices, and its privacy label includes Data Used to Track You.",
            ["Weekly $0.99 to $5.99, monthly $3.49 or $9.99, yearly $17.99, lifetime $29.99 or $33.99",
             "Calculator-style screen; PIN then «=»", "Fake vault (paid)", TN, "2.21 (29 Oct 2026)"]),
        app("Secret Calculator Vault Photo", 1479873340, "secret-calculator", "Joao Victor Flores da Costa", 4.38, 952,
            "a calculator front that also keeps passwords, with no data collected per its label.",
            ["Appears as a standard calculator, per its listing.",
             "Encrypted vault for photos and videos, plus a password manager kept on the device.",
             "Lifetime premium is listed at $19.99."],
            "its last update was 9 October 2025, and the listing names no decoy PIN or backup.",
            ["Monthly $9.99, yearly $23.99, lifetime $19.99",
             "Calculator front; passcode", "Not named", NC, "1.4.0 (9 Oct 2025)"]),
    ],
    "who": [
        "<strong>A real calculator with an emergency PIN:</strong> Calculator Vault (Cloud Honest).",
        "<strong>Most ratings, documents and passwords too:</strong> Calculator#.",
        "<strong>One payment, converter disguise:</strong> Converter.",
        "<strong>Calculator icon with Face ID, no account:</strong> Photo Vault.",
        "<strong>Calculator front plus a password manager:</strong> Secret Calculator.",
    ],
    "cases": ["Lending your phone without anyone seeing a vault app.", "Hiding ID and card photos from the camera roll.", "Being asked to unlock the vault in front of someone."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «calculator vault», «secret calculator», «calculator hide photos», «calculator lock», «calculator vault hide photos» and «hidden calculator», and read each app's US App Store page and Apple's lookup data. We left out apps whose listing does not describe a calculator and apps last updated in 2024 or earlier. We installed nothing and did not test encryption.",
        "A disguise helps against a quick look at your home screen. Someone who searches Settings or your App Store purchase history can still see which vault app you installed.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("What is a calculator vault app?",
         "A photo vault that looks like a calculator. In most, the calculator works, and typing your PIN followed by «=» opens the hidden photos. In others, only the home-screen icon looks like a calculator."),
        ("Which calculator vault is free?",
         "All six are free to download. Calculator Vault (Cloud Honest) lists a free plan of up to 20 items; Calculator# is free with ads and limits. Check what the free version stores before moving everything."),
        ("Can someone still find a calculator vault?",
         "Yes, with a careful search. Every app appears in Settings and in your App Store purchase history under its App Store name, so the disguise works against a quick look at the home screen, not a search."),
        ("What happens to my photos if I delete the app?",
         "In vaults that keep photos only on the phone, they go with the app. Calculator#, Converter, Calculator Vault (Pro) and Photo Vault list a backup to iCloud or a file you keep; turn it on before deleting."),
    ],
    "sources": [
        ("Calculator Vault : Hide Photo (App Store)", "https://apps.apple.com/us/app/id6767042215"),
        ("Calculator# Hide Photos Videos (App Store)", "https://apps.apple.com/us/app/id1165276801"),
        ("Converter: Hidden Photo Vault (App Store)", "https://apps.apple.com/us/app/id1536734125"),
        ("Photo Vault: Hide Pics Video (App Store)", "https://apps.apple.com/us/app/id1532670722"),
        ("CalcX Vault Secret Photo Lock (App Store)", "https://apps.apple.com/us/app/id1577144445"),
        ("Secret Calculator Vault Photo (App Store)", "https://apps.apple.com/us/app/id1479873340"),
        ("Is the iPhone Hidden album safe? (aisagalab.com)", "https://aisagalab.com/photo-vault/is-iphone-hidden-album-safe.html"),
    ],
}]
