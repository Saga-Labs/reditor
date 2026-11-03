"""Blockfolio alternatives on iPhone, EN. Our app: Crypton (id1143691286).

Checked 2026-11-03: US App Store search for «blockfolio», «crypto portfolio tracker», «crypto tracker», iTunes lookup and
the US App Store page of every app (price list, privacy label); Wikipedia's FTX article for Blockfolio's history (FTX
bought it in August 2020; FTX has been in Chapter 11 since 11 November 2022). A paid app called «Blockfolio Pro: Crypto
Tracker» (Roxwin Vietnam Technologies, $1.99, 1 rating) is not the original and is named only as a warning. Why this
topic: Google suggests «blockfolio alternative», «blockfolio replacement», «blockfolio alternative reddit» (3 Nov); no
page on the 4 sites covers it. To avoid repeating reviewland's crypto pages (CoinStats alternatives, free trackers,
tracking without a wallet), only CoinStats and Crypton overlap with them. Registered in ios-playbook
references/temas-webs.md (23429dd). Nothing installed or tested.
"""

D = "2026-11-03"
CHECKED = "2026-11-03"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f} ({count:,} ratings)"]}
    if ours:
        a["ours"] = True
    return a


NL = "Data Not Linked to You"

PAGES = [{
    "group": "blockfolio-alt", "lang": "en", "store": "us",
    "path": "blockfolio-alternatives-iphone/",
    "ct": "rd-blockfolio-alt-iphone",
    "category": "FinanceApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Blockfolio Alternatives for iPhone (2026): 6 Crypto Trackers",
    "h1": "Best Blockfolio alternatives for iPhone in 2026",
    "description": "Blockfolio became part of FTX, which went bankrupt in 2022. Six iPhone crypto portfolio trackers to use instead, by price, account and privacy label.",
    "llms": "Explains what happened to Blockfolio (bought by FTX in August 2020; FTX in Chapter 11 bankruptcy since November 2022) and compares six iPhone crypto portfolio trackers to use instead: CoinStats, Crypto Tracker by BitScreener, Bitfolio, Crypton, BitWorth and AssetDash, by price, how you add holdings, whether an account is needed and App Store privacy label. Warns that a paid App Store app named «Blockfolio Pro» is from a different developer.",
    "llms_note": "Crypton, one of the six, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>Blockfolio, the crypto portfolio tracker, is no longer on the App Store:</strong> on 3 November 2026 we found no Blockfolio or FTX app from the original company in the US store. FTX bought it in August 2020 for $150 million, and FTX has been in Chapter 11 bankruptcy since 11 November 2022, per <a href=\"https://en.wikipedia.org/wiki/FTX\">Wikipedia</a>. A paid App Store app called «Blockfolio Pro: Crypto Tracker» ($1.99) comes from a different developer, Roxwin Vietnam Technologies, and had one rating on 3 November 2026; it is not the original.",
        "To track your coins the way Blockfolio did, by typing in what you hold, Bitfolio, Crypton and BitWorth need no account and list no exchange connection; BitWorth and Crypton list no purchases at all. To sync wallets and exchanges automatically, CoinStats connects 300+ of them, and AssetDash syncs up to 3 Solana wallets for free. reviewland compares more trackers in <a href=\"https://reviewland.io/coinstats-alternatives-iphone/\">CoinStats alternatives</a>.",
    ],
    "columns": ["App", "Price (US)", "How you add holdings, per its listing", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("CoinStats: Crypto Portfolio", 1247849330, "coinstats", "COINSTATSAPP LLC", 4.76, 86089,
            "syncing every wallet and exchange automatically, with P&L and tax export.",
            ["Connects 300+ wallets and exchanges (MetaMask, Phantom, Binance, Coinbase…) or a pasted wallet address.",
             "Realized and unrealized profit and loss, cost basis, price alerts and perpetual futures history.",
             "Prices for 20,000+ coins; exports transaction history for taxes."],
            "the full price list is long and high (up to $164.99 a year), and the listing does not say what stays free.",
            ["Pro $4.99 a month or $39.99 a year; Premium $15.99 to $19.99 a month, $119.99 to $164.99 a year",
             "Wallets, exchanges or a wallet address", "Not stated", NL, "5.31.1 (30 Oct 2026)"]),
        app("Crypto Tracker by BitScreener", 1240849311, "bitscreener", "BITSCREENER PTE. LTD.", 4.74, 20152,
            "manual entry like Blockfolio, plus exchange API and CSV import, with a cheap lifetime option.",
            ["Portfolio by manual entry, exchange API or CSV import and export, with 1H to 1M performance.",
             "Prices from 200+ markets, a screener with 100+ criteria, alerts and news.",
             "Lifetime premium is listed at $9.99."],
            "its privacy label includes Data Used to Track You and Data Linked to You, and its last update was 29 May 2026.",
            ["Unlimited access $4.99 or $41.99; lifetime $9.99",
             "Manual, exchange API or CSV", "Not stated", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "4.6.7 (29 May 2026)"]),
        app("Bitfolio - Crypto portfolio", 1264391689, "bitfolio", "Timelabs Ltd", 4.34, 523,
            "a private tracker with no account, several portfolios, and other assets next to crypto.",
            ["No account; portfolio data stays on the device, per its listing.",
             "10,000+ coins, tokens and perpetual markets; multiple portfolios and watchlists.",
             "Can also track real estate, collectibles and other personal assets."],
            "it needs iOS 26, and some features are in Pro.",
            ["Pro $1.99 a month, $9.99 a year, lifetime $29.99",
             "Manual", "None", NL, "7.1.1 (14 Oct 2026)"]),
        app("Crypto Tracker: Crypton", 1143691286, "crypton", "Saga Ltd.", 4.72, 185,
            "a fast, free tracker with P&L per coin and Home Screen widgets, no account needed.",
            ["Live prices for the top 250 coins, plus any coin listed on CoinGecko; charts from 1 day to 1 year.",
             "Portfolio with profit and loss per coin from your average buy price; Home Screen widgets for prices and portfolio.",
             "No purchases listed; an optional account only syncs the portfolio."],
            "English only, no exchange or wallet sync, no price alerts in its listing, and it needs iOS 18.",
            ["No purchases listed",
             "Manual (amount and average buy price)", "Optional, to sync", NL, "2.0.8 (24 Oct 2026)"], ours=True),
        app("BitWorth - Crypto Tracker", 1239107714, "bitworth", "Andy Feng", 4.75, 1658,
            "the simplest answer to «what is my crypto worth right now», free.",
            ["No account, no sign-up and no exchange connections; add the coins you hold.",
             "Everything stays on the device unless you choose to back it up, per its listing.",
             "A live global chat and news feed; free, made by one developer."],
            "English only, it needs iOS 26, and it is deliberately simple: no P&L or alerts named in its listing.",
            ["No purchases listed",
             "Manual", "None", NL, "3.02.09 (13 Oct 2026)"]),
        app("AssetDash: Portfolio Tracker", 1541886930, "assetdash", "Asset Dash Corporation", 4.72, 1082,
            "Solana holders who want wallets, tokens and NFTs synced for free.",
            ["Free tier syncs up to 3 Solana wallets, with net worth and allocation.",
             "Premium ($4.99 a month) adds other chains, exchanges and brokerages such as Coinbase, Binance and Robinhood.",
             "Also trades Solana tokens inside the app."],
            "anything beyond Solana needs Premium, its privacy label lists Data Linked to You, and its last update was 18 November 2025.",
            ["Premium $4.99 a month",
             "Synced wallets (Solana free)", "Not stated", "Data Linked to You", "3.0.104 (18 Nov 2025)"]),
    ],
    "who": [
        "<strong>Every wallet and exchange synced:</strong> CoinStats.",
        "<strong>Manual entry plus CSV, cheap lifetime:</strong> BitScreener.",
        "<strong>No account, several portfolios:</strong> Bitfolio.",
        "<strong>Free, P&L per coin and widgets:</strong> Crypton.",
        "<strong>Just the total, free:</strong> BitWorth.",
        "<strong>Solana wallets:</strong> AssetDash.",
    ],
    "cases": ["Moving a Blockfolio-style manual portfolio to a new app.", "Checking your total on a Home Screen widget.", "Tracking coins without linking an exchange."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «blockfolio», «crypto portfolio tracker» and «crypto tracker», and read each app's US App Store page and Apple's lookup data. Blockfolio's history comes from Wikipedia's article on FTX. We installed nothing.",
        "None of these apps buys or sells for you except AssetDash's Solana trading; they show prices and what your holdings are worth. This page is not investment advice.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("What happened to Blockfolio?",
         "FTX bought it in August 2020 for $150 million. FTX filed for Chapter 11 bankruptcy on 11 November 2022, per Wikipedia."),
        ("Is «Blockfolio Pro» on the App Store the original Blockfolio?",
         "No. «Blockfolio Pro: Crypto Tracker» is a $1.99 app from Roxwin Vietnam Technologies, with one US rating on 3 November 2026."),
        ("Which Blockfolio alternative is free?",
         "Crypton and BitWorth list no purchases. Bitfolio, BitScreener and AssetDash have free versions with paid upgrades."),
        ("Which ones work without an account or exchange connection?",
         "Bitfolio and BitWorth need no account; Crypton's account is optional and only syncs your portfolio. All three let you type in what you hold."),
    ],
    "sources": [
        ("FTX (Wikipedia)", "https://en.wikipedia.org/wiki/FTX"),
        ("CoinStats (App Store)", "https://apps.apple.com/us/app/id1247849330"),
        ("Crypto Tracker by BitScreener (App Store)", "https://apps.apple.com/us/app/id1240849311"),
        ("Bitfolio (App Store)", "https://apps.apple.com/us/app/id1264391689"),
        ("Crypto Tracker: Crypton (App Store)", "https://apps.apple.com/us/app/id1143691286"),
        ("BitWorth (App Store)", "https://apps.apple.com/us/app/id1239107714"),
        ("AssetDash (App Store)", "https://apps.apple.com/us/app/id1541886930"),
        ("Blockfolio Pro: Crypto Tracker (App Store)", "https://apps.apple.com/us/app/id6751293115"),
    ],
}]
