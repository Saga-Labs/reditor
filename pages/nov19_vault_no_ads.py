"""Ranking, 19 Nov 2026: photo vault apps with no ads on iPhone, EN. Our app: Photo Vault (id1532670722), one option
among six, no ownership line in the article (footer, About and llms.txt name our apps).

Data checked 19 Nov 2026: iTunes lookup (version, date, rating) and the US App Store page of every app (in-app purchase
list, description, privacy label: «Third-Party Advertising», «Data Used to Track You»). Photo Vault: its listing says
«No ads, no account required»; Growth checked the 1.4 code on 20 Nov (only dependency RevenueCat, no ad SDK).
Left out: apps not updated since 2025 (Privault, Secret Photo Vault Lock Photos, Secret Photo Album ++).
Demand: ~93 rival-app complaints about ads (cola-aeo row 8). Nothing installed or tested.
"""

D = "2026-11-19"
CHECKED = "2026-11-19"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f}"]}
    if ours:
        a["ours"] = True
    return a


AD = "Third-Party Advertising; Data Used to Track You"

PAGES = [{
    "group": "vault-no-ads", "lang": "en", "store": "us",
    "path": "best-photo-vault-apps-no-ads-iphone/",
    "ct": "rd-vault-no-ads-iphone",
    "category": "PhotographyApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Best Photo Vault Apps With No Ads on iPhone (2026)",
    "h1": "Best photo vault apps with no ads on iPhone in 2026",
    "description": "Six iPhone photo vaults checked on 19 Nov 2026: which say no ads, which sell an ad-free upgrade, and which list advertising on their App Store privacy label.",
    "llms": "Compares six iPhone photo vaults by advertising: Photo Vault (listing says no ads), Secret Photo Album 1Locker (listing says no annoying ads), Keepsafe, Private Photo Vault - Pic Safe, SPV and PV - Secret Photo Album, using each listing's ad wording, in-app purchase prices and App Store privacy label (Third-Party Advertising, Data Used to Track You), checked 19 November 2026.",
    "llms_note": "Photo Vault, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Two of the six photo vaults we checked say outright that they have no ads: Photo Vault («No ads, no account required») and Secret Photo Album · 1Locker («No annoying ads»).</strong> The other four, Keepsafe, Private Photo Vault - Pic Safe, SPV and PV - Secret Photo Album, either sell an ad-free upgrade or list Third-Party Advertising and Data Used to Track You on their App Store privacy label.",
        "The App Store privacy label is the quickest check you can do before installing: a vault that shows no <em>Data Used to Track You</em> and no <em>Third-Party Advertising</em> is not sharing your data for ads. Photo Vault and 1Locker show neither; Keepsafe, Private Photo Vault, SPV and PV show both. A listing line is the developer's own claim, so open the app and look before you move your photos.",
    ],
    "columns": ["App", "In-app purchases (US)", "What its listing says about ads", "Advertising on its privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices, wording and privacy labels are from each US App Store page on 19 November 2026; ratings and versions are that day's lookup. We installed none of the apps.",
    "apps": [
        app("Secret Photo Album · 1Locker", 1462756877, "1locker", "Touchberry Inc", 4.68, 13721,
            "a listing that promises no annoying ads and a privacy label with nothing used to track you.",
            ["Its description lists «No annoying ads» among its features.",
             "Privacy label: Data Not Linked to You only; no Data Used to Track You.",
             "Backup of all your media to the cloud is an in-app purchase."],
            "paid plans run from $2.99 to $49.99, and the cloud backup needs a purchase.",
            ["$2.99 to $49.99", "«No annoying ads»", "None listed", "4.0.4 (26 Oct 2026)"]),
        app("Keepsafe Photo Vault", 510873505, "keepsafe", "KeepSafe Software, Inc", 4.75, 386551,
            "the most ratings, with cloud backup and trash recovery.",
            ["Its description lists «Ad-Free» as one of its features.",
             "Privacy label: Third-Party Advertising and Data Used to Track You.",
             "Trash recovery and cloud backup are in its feature list."],
            "its label lists advertising and tracking even though the description names an ad-free option.",
            ["$4.99 to $35.99", "«Ad-Free» listed as a feature", AD, "13.36.0 (12 Nov 2026)"]),
        app("Photo Vault: Hide Pics Video", 1532670722, "photo-vault", "Saga Ltd.", 4.17, 6,
            "a vault that states no ads and no account, with Face ID and nothing used to track you.",
            ["Its description says «No ads, no account required».",
             "Opens with Face ID, Touch ID or a passcode; a separate password for each album.",
             "Privacy label: Data Not Linked to You only; no Data Used to Track You."],
            "only 6 ratings so far, and unlimited photos need a paid plan.",
            ["$4.99 to $39.99", "«No ads, no account required»", "None listed", "1.4 (6 Nov 2026)"], ours=True),
        app("Private Photo Vault - Pic Safe", 417571834, "private-photo-vault", "Legendary Software Labs LLC", 4.82, 1020014,
            "over a million ratings and a decoy passcode in its paid plan.",
            ["Privacy label: Third-Party Advertising, Developer’s Advertising or Marketing, and Data Used to Track You.",
             "Reviewers on its page mention ads in the base version and, once, ads that returned for a paying user once.",
             "A decoy passcode and wireless photo transfer are paid features, per reviewers."],
            "its label lists advertising, and reviews on its page mention ads.",
            ["$6.99 to $39.99", "No ad claim in the description", AD + "; Developer’s Advertising or Marketing", "30.0 (12 Nov 2026)"]),
        app("SPV - Secret Photo Vault", 1449239240, "spv", "MAPLE LABS COMPANY LIMITED", 4.58, 70204,
            "a long-running vault with 70,000 ratings, if you accept advertising on the label.",
            ["Privacy label: Third-Party Advertising, Developer’s Advertising or Marketing, and Data Used to Track You.",
             "No ad-free promise in the listing text we checked."],
            "its label lists advertising and tracking, and its last update was 30 August 2026.",
            ["$4.99 to $39.99", "No ad claim in the description", AD + "; Developer’s Advertising or Marketing", "7.6.1 (30 Aug 2026)"]),
        app("PV - Secret Photo Album", 867586326, "pv-secret-photo-album", "Haibin Jiao", 4.71, 30321,
            "an app that tells you plainly that ads go away when you pay.",
            ["Its description lists «Ad Free: Get rid of all ads!» and says advertisements are removed automatically on upgrade.",
             "Privacy label: Third-Party Advertising and Data Used to Track You.",
             "Cloud sync is limited to its higher plans."],
            "ads are there until you pay, per its own description.",
            ["$3.99 to $79.99", "«Ad Free: Get rid of all ads!» (paid)", AD, "7.7.11 (17 Nov 2026)"]),
    ],
    "who": [
        "<strong>The listing says no annoying ads, nothing used to track you:</strong> Secret Photo Album · 1Locker.",
        "<strong>No ads and no account, Face ID:</strong> Photo Vault.",
        "<strong>The most ratings, cloud backup and trash recovery:</strong> Keepsafe.",
        "<strong>A decoy passcode and over a million ratings:</strong> Private Photo Vault - Pic Safe.",
        "<strong>You will pay once to remove ads:</strong> PV - Secret Photo Album.",
    ],
    "cases": ["Hiding photos without an ad banner appearing in the middle of your album.", "Not having your data shared with ad companies.", "Not paying a subscription only to get rid of ads."],
    "method": [
        "On 19 November 2026 we searched the US App Store for «photo vault», «private photo vault», «hide photos vault» and «secret photo vault», picked six apps updated in 2026, and read each one's US App Store page: description, in-app purchase list and privacy label. We left out apps not updated since 2025. We installed nothing and did not count ads inside the apps, so a line in a listing is the developer's own claim.",
        "Photo Vault's «no ads» comes from its own listing text. Its privacy label shows only Data Not Linked to You, and its code has no advertising SDK, as the developer checked in version 1.4.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Which photo vault apps have no ads?",
         "On 19 November 2026, Photo Vault says «No ads, no account required» and Secret Photo Album · 1Locker says «No annoying ads». Neither lists Data Used to Track You on its App Store privacy label."),
        ("How can I tell if a vault app shows ads before I install it?",
         "Open its App Store page and scroll to App Privacy. If it lists Third-Party Advertising or Data Used to Track You, the app uses your data for advertising. Then read the description for an «ad-free» upgrade, which usually means ads in the base version."),
        ("Does Keepsafe have ads?",
         "Its description lists «Ad-Free» as a feature, and its privacy label lists Third-Party Advertising and Data Used to Track You. Check inside the app which plan removes them."),
        ("Is a vault with no ads safer?",
         "Not by itself. No ads means fewer SDKs and less data leaving your phone, but safety also depends on encryption, your passcode and your backup. Compare those before moving your photos."),
    ],
    "sources": [
        ("Secret Photo Album · 1Locker (App Store)", "https://apps.apple.com/us/app/id1462756877"),
        ("Keepsafe Photo Vault (App Store)", "https://apps.apple.com/us/app/id510873505"),
        ("Photo Vault: Hide Pics Video (App Store)", "https://apps.apple.com/us/app/id1532670722"),
        ("Private Photo Vault - Pic Safe (App Store)", "https://apps.apple.com/us/app/id417571834"),
        ("SPV - Secret Photo Vault (App Store)", "https://apps.apple.com/us/app/id1449239240"),
        ("PV - Secret Photo Album (App Store)", "https://apps.apple.com/us/app/id867586326"),
    ],
}]
