"""Perplexity alternatives for iPhone, EN. Our app: Ask AI (id1662608035), which lists Perplexity Sonar among its models.

Checked 2026-11-02: iTunes lookup API (country us) and the US App Store page of every app (price list, privacy
label). Only apps whose own listing says they search the web or give AI answers from the web are in the list
(ChatGPT and Gemini are left out because their listings do not say so). Why this topic: our AI-answer tracking
asks «AI chat app with web search iPhone» (saga-growth data/aeo/2026-W43.csv), and no Perplexity page exists on
reditor, reviewland, aisagalab or doravideo.com (checked 2 Nov). No quality test.
"""

D = "2026-11-03"
CHECKED = "2026-11-02"


def app(name, id_, anchor, dev, rating, count, best_for, facts, limits, row, ours=False):
    a = {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
         "best_for": best_for, "facts": facts, "limits": limits,
         "row": row + [f"{rating:.1f}"]}
    if ours:
        a["ours"] = True
    return a


PAGES = [{
    "group": "perplexity-alt", "lang": "en", "store": "us",
    "path": "perplexity-alternatives-iphone/",
    "ct": "rd-perplexity-alternatives-iphone",
    "category": "ReferenceApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Perplexity Alternatives for iPhone (2026): 6 AI Search Apps Compared",
    "h1": "Best Perplexity alternatives for iPhone in 2026",
    "description": "Six iPhone apps that answer questions from the web like Perplexity: Claude, Bing, Brave, Ask AI, Arc Search and DuckDuckGo, by price and privacy label.",
    "llms": "Compares six iPhone alternatives to Perplexity whose App Store listings say they search the web or give AI answers from it (Claude, Microsoft Bing Search, Brave, Ask AI, Arc Search, DuckDuckGo), by price, how the answer is built and App Store privacy label.",
    "answer": [
        "<strong>Perplexity answers a question with sources and citations, and its app is free with Pro at $20 a month and Max at $200</strong> (US App Store, 2 November 2026). The six alternatives below fall into two kinds. Claude and Ask AI are chat assistants that search the web when a question needs it; Claude's listing says it gives citations, and Ask AI does it with Pro. Microsoft Bing, Brave, Arc Search and DuckDuckGo are search apps or browsers that put an AI answer on top of normal results, free to use.",
        "If privacy is why you are leaving: Perplexity's App Store label lists Data Linked to You. Brave and DuckDuckGo list only Data Not Linked to You, and both say their AI features do not use your chats to train models. Bing's label is the broadest here, with Data Used to Track You.",
    ],
    "columns": ["App", "Price (US)", "How it answers, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 2 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Claude by Anthropic", 6473753684, "claude", "Anthropic PBC", 4.72, 292674,
            "long, careful answers you want to keep discussing, with citations.",
            ["Its listing says Claude searches the web, compiles findings with accurate citations and surfaces what is useful.",
             "Reads photos, PDFs and screenshots, and can connect Google Drive, Gmail and Calendar.",
             "Voice conversations in several languages."],
            "it is an assistant first, not a search page: you ask and wait for a written answer rather than scanning results.",
            ["Pro $20 a month or $214.99 a year, Max $124.99, Ultra $249.99 a month",
             "Chat that searches the web and cites sources",
             "32", "Data Linked to You", "1.261030.19 (1 Nov 2026)"]),
        app("Microsoft Bing Search", 345323231, "bing", "Microsoft Corporation", 4.75, 299077,
            "people who want a normal search page with an AI summary on top, for free.",
            ["Copilot Search in Bing puts a curated answer or summary at the top of the results, per its listing.",
             "Each answer comes with web links and suggested follow-up topics.",
             "In 41 languages."],
            "its privacy label is the broadest here (Data Used to Track You and Data Linked to You).",
            ["Free; no in-app purchases listed",
             "Search results with an AI answer on top",
             "41", "Data Used to Track You; Data Linked to You", "34.4.441029001 (2 Nov 2026)"]),
        app("Brave Browser & Search Engine", 1052879175, "brave", "Brave Software, Inc.", 4.78, 671838,
            "private search with AI answers inside a full browser.",
            ["Brave Search runs on its own index, not resold Google or Bing results, and Ask Brave puts results and AI answers in one place, per its listing.",
             "Leo, a free AI assistant, summarizes or translates the page you are on; Brave says it does not record or train on your chats.",
             "Blocks ads and trackers on every site."],
            "more capable AI models need Leo Premium, and it is a browser to switch to, not a single answer app.",
            ["Free; Leo Premium $14.99 a month or $149.99 a year; Firewall + VPN $9.99 a month",
             "Own search index with AI answers; Leo assistant",
             "37", "Data Not Linked to You", "1.97 (21 Oct 2026)"]),
        app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3,
            "people who want Perplexity's own Sonar model next to Gemini, Claude and Grok in one chat.",
            ["Its listing names models from several companies, including Gemini, Claude, Grok, DeepSeek and Perplexity Sonar, and you can switch model in the middle of a chat.",
             "With Pro, it searches the web by itself when a question needs current information.",
             "Reads photos you attach and can read any answer aloud."],
            "web search and most models need Pro (a few free messages a day without it), and it does not read files or make images.",
            ["A few free messages a day; Pro yearly, listed from $39.99 to $69.99",
             "Chat with several models; web search with Pro",
             "5", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "1.4.5 (2 Nov 2026)"], ours=True),
        app("Arc Search — Find it, Faster", 6472513080, "arc-search", "The Browser Company of New York Inc.", 4.88, 25104,
            "getting one clean page of answers instead of a list of links.",
            ["Browse for Me reads pages for you and builds a summary, and Pinch to Summarize condenses the page you are on, per its listing.",
             "Voice search and Call Arc for hands-free questions.",
             "Blocks ads, trackers and cookie pop-ups."],
            "English only, and it summarizes web pages rather than holding a long conversation.",
            ["Free; no in-app purchases listed",
             "Browser that summarizes pages into an answer",
             "1", "Data Linked to You; Data Not Linked to You", "1.49.0 (19 Oct 2026)"]),
        app("DuckDuckGo, optional Duck.ai", 663592361, "duckduckgo", "Duck Duck Go, Inc.", 4.84, 2417376,
            "the most private option: search that is not tracked, with optional AI answers and chat.",
            ["Search Assist and Duck.ai are optional and never use your data to train AI, per its listing.",
             "Duck.ai lets you chat with third-party AI models, anonymized by DuckDuckGo.",
             "The browser blocks trackers, ads and cookie pop-ups for free."],
            "the subscriptions mainly add VPN and identity services; the AI answers are simpler than Perplexity's research mode.",
            ["Free; Plus $9.99 a month or $99.99 a year, Pro $19.99 a month or $199.99 a year",
             "Private search with optional AI answers and Duck.ai chat",
             "26", "Data Not Linked to You", "7.243.0 (26 Oct 2026)"]),
    ],
    "who": [
        "<strong>Long answers with citations, in a chat:</strong> Claude.",
        "<strong>A free search page with an AI summary:</strong> Microsoft Bing.",
        "<strong>Private search inside a full browser:</strong> Brave.",
        "<strong>Perplexity's Sonar model plus other models in one chat:</strong> Ask AI.",
        "<strong>One summary page instead of links:</strong> Arc Search.",
        "<strong>The least data collected:</strong> DuckDuckGo.",
    ],
    "cases": ["Checking a fact with sources.", "Researching a purchase.", "Getting a quick summary of a news story."],
    "method": [
        "On 2 November 2026 we read Perplexity's and each app's US App Store page and Apple's lookup data. We only included apps whose own listing says they search the web or answer from it; what each app does comes from that listing. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("What is the best free alternative to Perplexity on iPhone?",
         "Microsoft Bing, Brave, Arc Search and DuckDuckGo give AI answers from the web for free."),
        ("Which alternative is the most private?",
         "By App Store label, DuckDuckGo and Brave: both list only Data Not Linked to You, and both say their AI features do not train on your conversations."),
        ("Can I use Perplexity's model in another app?",
         "Ask AI lists Perplexity Sonar among its models, next to Gemini, Claude, Grok and DeepSeek; you need Pro for most models and for web search."),
        ("Why are ChatGPT and Gemini not on this list?",
         "Their App Store listings, as of 2 November 2026, do not say that they search the web, and we only list what each listing states."),
    ],
    "sources": [
        ("Perplexity: AI Agent & Search (App Store)", "https://apps.apple.com/us/app/id1668000334"),
        ("Claude by Anthropic (App Store)", "https://apps.apple.com/us/app/id6473753684"),
        ("Microsoft Bing Search (App Store)", "https://apps.apple.com/us/app/id345323231"),
        ("Brave Browser & Search Engine (App Store)", "https://apps.apple.com/us/app/id1052879175"),
        ("All AI Models in One: Ask AI (App Store)", "https://apps.apple.com/us/app/id1662608035"),
        ("Arc Search (App Store)", "https://apps.apple.com/us/app/id6472513080"),
        ("DuckDuckGo (App Store)", "https://apps.apple.com/us/app/id663592361"),
    ],
}]
