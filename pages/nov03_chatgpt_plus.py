"""ChatGPT Plus alternatives on iPhone, EN. Our app: Ask AI (id1662608035).

Checked 2026-11-03: US App Store page of ChatGPT and of every app (price list, privacy label) plus iTunes lookup. Gemini's
price list did not load that day; its prices are from its US App Store page read earlier the same day for
/chatgpt-image-alternatives-iphone/. Why this topic: Google suggests «chatgpt plus alternative», «... free», «best
chatgpt plus alternative», «is there a cheaper alternative to chatgpt plus» (3 Nov); no page on the 4 sites compares paid
plans against ChatGPT Plus (reviewland has Poe alternatives; reditor has Perplexity, ChatOn, DeepSeek, Grok pages).
Registered in ios-playbook references/temas-webs.md. No quality test.
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


LK = "Data Linked to You"
T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"

PAGES = [{
    "group": "chatgpt-plus-alt", "lang": "en", "store": "us",
    "path": "chatgpt-plus-alternatives-iphone/",
    "ct": "rd-chatgpt-plus-alt-iphone",
    "category": "ProductivityApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "ChatGPT Plus Alternatives for iPhone (2026): 7 Plans Compared",
    "h1": "Best ChatGPT Plus alternatives for iPhone in 2026",
    "description": "ChatGPT Plus is $19.99 a month on the iPhone. Seven AI chat plans compared by monthly price, models and privacy label, from $4.99 to $30.",
    "llms": "Compares seven iPhone alternatives to ChatGPT Plus ($19.99 a month on the US App Store; ChatGPT Go is $8): Google Gemini (AI Plus $4.99, Pro $19.99), Poe (Basic $4.99), Ask AI ($9.99 a month, several companies' models), Vibe by Mistral ($14.99), Claude (Pro $20), Perplexity (Pro $20) and Grok (SuperGrok Lite $10, SuperGrok $30), by monthly price, what the plan gives and App Store privacy label.",
    "llms_note": "Ask AI, one of the seven, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>ChatGPT Plus costs $19.99 a month in the iPhone app</strong> (US App Store, 3 November 2026). OpenAI's own cheaper plan is ChatGPT Go at $8, and Pro starts at $100. Most rivals price their main plan the same: Claude Pro and Perplexity Pro are $20 and Gemini's Google AI Pro is $19.99.",
        "To pay less, Google AI Plus ($4.99) and Poe Basic ($4.99) are the cheapest monthly plans listed, then Ask AI ($9.99 a month, with Gemini, Claude, Grok, DeepSeek and Perplexity Sonar models in one chat), SuperGrok Lite ($10) and Vibe Pro by Mistral ($14.99). Every app here is free to download with a free tier. For more on single assistants, see our <a href=\"/perplexity-alternatives-iphone/\">Perplexity alternatives</a> and <a href=\"/grok-apps-iphone/\">Grok apps</a>.",
    ],
    "columns": ["App", "Cheapest monthly plan (US)", "Other plans listed", "Models, per its listing", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. ChatGPT for comparison: Go $8, Plus $19.99, Pro from $100. Ratings are that day's App Store average and count.",
    "apps": [
        app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2393415,
            "the cheapest plan from a big lab, with Gmail, Calendar and Photos built in.",
            ["Google AI Plus at $4.99 a month; Pro at $19.99 matches ChatGPT Plus.",
             "Connects Gmail, Calendar, Google Photos and YouTube; makes and edits photos with Nano Banana 2.",
             "In 70 languages."],
            "the listing does not say which features each plan adds, and the plans bundle cloud storage you may not need.",
            ["Google AI Plus $4.99", "Pro $19.99, Ultra $199.99 a month",
             "Gemini", LK, "1.2026.4262206 (29 Oct 2026)"]),
        app("Poe – Fast AI Chat", 1640745955, "poe", "Quora, Inc", 4.72, 53844,
            "many companies' models, plus image and video generators, for $4.99 a month.",
            ["Models from OpenAI, Anthropic and Google, and image and video generators such as FLUX, Ideogram and Runway, per its listing.",
             "Ask several bots in one thread and compare answers; over 1 million custom bots.",
             "Basic is $4.99 a month or $49.99 a year; Plus is $19.99."],
            "the model names in its listing are old (GPT-4.5, Claude 3.7 Sonnet, Gemini 2.0), so check what each plan includes in the app.",
            ["Basic $4.99", "Plus $19.99 a month; $49.99 or $199.99 a year",
             "OpenAI, Anthropic, Google and others", LK, "6.1.0 (5 Oct 2026)"]),
        app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1570441,
            "a $10 plan with image and video generation in the same app.",
            ["SuperGrok Lite at $10 a month; SuperGrok at $30.",
             "Deep research on the web, document and photo analysis, and Grok Imagine for images and short videos with sound.",
             "Extra usage credits from $5."],
            "its privacy label includes Data Used to Track You, and the top plans reach $100 and $300 a month.",
            ["SuperGrok Lite $10", "SuperGrok $30, Plus $100, Heavy $300",
             "Grok", T3, "1.4.61 (1 Nov 2026)"]),
        app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3,
            "half the price of Plus for models from several companies, switching mid-chat.",
            ["Models from Gemini, Claude, Grok, DeepSeek and Perplexity Sonar in one chat; switch at any time and keep the conversation.",
             "A few free messages every day; Pro adds every model, web search and a higher limit.",
             "Reads photos and reads answers aloud."],
            "only 3 US ratings, no ChatGPT models, it does not make images or read files, and its privacy label includes Data Used to Track You.",
            ["Monthly $9.99", "Weekly $7.99; yearly $69.99",
             "Gemini, Claude, Grok, DeepSeek, Perplexity Sonar", T3, "1.4.5 (2 Nov 2026)"], ours=True),
        app("Vibe by Mistral (ex-Le Chat)", 6740410176, "mistral", "MISTRAL AI", 4.76, 1346,
            "a European alternative at $14.99, built for research and long tasks.",
            ["Formerly Le Chat; Vibe Pro is $14.99 a month or $149.99 a year.",
             "Deep research with sources across the web and connected tools; drafts reports from your email, calendar and documents.",
             "A free plan for quick answers."],
            "far fewer ratings than the big apps (1,346), and the listing does not say which models Pro uses.",
            ["Vibe Pro $14.99", "$149.99 a year",
             "Mistral", "Data Linked to You; Data Not Linked to You", "2.16.0 (23 Oct 2026)"]),
        app("Claude by Anthropic", 6473753684, "claude", "Anthropic PBC", 4.72, 293855,
            "writing and coding help at the same price as Plus, or a little less paid yearly.",
            ["Claude Pro is $20 a month, or $214.99 a year (about $17.92 a month).",
             "Writing, research and coding help that plans multi-step tasks, per its listing.",
             "Max ($124.99) and Ultra ($249.99) for heavy use; usage credits from $20."],
            "not cheaper than Plus month to month, and the listing names no image generator.",
            ["Pro $20", "Pro $214.99 a year; Max $124.99, Ultra $249.99 a month",
             "Claude", LK, "1.261030.19 (1 Nov 2026)"]),
        app("Perplexity: AI Agent & Search", 1668000334, "perplexity", "Perplexity AI Inc.", 4.82, 521431,
            "answers with cited sources, using several labs' models, for the price of Plus.",
            ["Every answer cites its sources; Pro Search and Deep Research.",
             "Uses top models from OpenAI, Anthropic, Meta and more, per its listing.",
             "Pro is $20 a month or $200 a year; credits from $5."],
            "the same price as Plus, and Max is $200 a month.",
            ["Pro $20", "Pro $200 a year; Max $200 a month",
             "OpenAI, Anthropic, Meta and others", LK, "26.43.0 (31 Oct 2026)"]),
    ],
    "who": [
        "<strong>Cheapest plan from a big lab:</strong> Gemini (Google AI Plus, $4.99).",
        "<strong>Many models for $4.99:</strong> Poe Basic.",
        "<strong>Several companies' models, switch mid-chat, $9.99:</strong> Ask AI.",
        "<strong>Images and video in a $10 plan:</strong> Grok.",
        "<strong>Writing and coding, paid yearly:</strong> Claude.",
        "<strong>Answers with sources:</strong> Perplexity.",
    ],
    "cases": ["Cutting a $19.99 subscription to under $10.", "Trying Claude, Gemini and Grok without three subscriptions.", "Research with cited sources."],
    "method": [
        "On 3 November 2026 we read ChatGPT's and each app's US App Store page (price list and privacy label) and Apple's lookup data. «Cheapest monthly plan» is the lowest monthly subscription in each price list; usage credits are not counted. We ran no quality test.",
        "Prices bought inside the iPhone app can differ from prices on each company's website.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there a cheaper alternative to ChatGPT Plus?",
         "Yes. In the iPhone app, ChatGPT Go is $8. Elsewhere, Google AI Plus and Poe Basic are $4.99 a month, Ask AI is $9.99 and SuperGrok Lite is $10."),
        ("Which alternative costs the same as ChatGPT Plus?",
         "Claude Pro and Perplexity Pro are $20 a month and Google AI Pro is $19.99. Claude Pro is $214.99 paid yearly, a little under $18 a month."),
        ("Is there a free alternative to ChatGPT Plus?",
         "Every app here has a free tier. The free versions limit messages or models; Ask AI, for example, allows a few free messages a day."),
        ("Can I use Claude, Gemini and Grok with one subscription?",
         "Ask AI and Poe put several companies' models in one app. Ask AI lists Gemini, Claude, Grok, DeepSeek and Perplexity Sonar; Poe lists OpenAI, Anthropic and Google models among others."),
    ],
    "sources": [
        ("ChatGPT (App Store)", "https://apps.apple.com/us/app/id6448311069"),
        ("Google Gemini (App Store)", "https://apps.apple.com/us/app/id6477489729"),
        ("Poe (App Store)", "https://apps.apple.com/us/app/id1640745955"),
        ("Grok (App Store)", "https://apps.apple.com/us/app/id6670324846"),
        ("Ask AI (App Store)", "https://apps.apple.com/us/app/id1662608035"),
        ("Vibe by Mistral (App Store)", "https://apps.apple.com/us/app/id6740410176"),
        ("Claude by Anthropic (App Store)", "https://apps.apple.com/us/app/id6473753684"),
        ("Perplexity (App Store)", "https://apps.apple.com/us/app/id1668000334"),
    ],
}]
