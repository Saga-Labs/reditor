"""Apps to use Grok (xAI's chat assistant, not Grok Imagine) on iPhone, EN. Our app: Ask AI (id1662608035), whose listing names Grok.

Checked 2026-11-03: US App Store search for «grok», «grok ai», «grok chat», «ai chat multiple models», iTunes lookup
and the US App Store page of every app (price list, privacy label). Only apps whose own listing names Grok as a chat
model are in the list. Why this topic: Google suggests «grok app for iphone» (3 Nov); reviewland's
/grok-imagine-alternatives-iphone/ is about video, doravideo.com has Grok Imagine model pages, and no page on the 4
sites covers using Grok chat on iPhone. Registered in ios-playbook references/temas-webs.md. No quality test.
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


T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"
TN = "Data Used to Track You; Data Not Linked to You"

PAGES = [{
    "group": "grok-apps", "lang": "en", "store": "us",
    "path": "grok-apps-iphone/",
    "ct": "rd-grok-apps-iphone",
    "category": "ProductivityApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "How to Use Grok on iPhone (2026): the Grok App and 6 Other Apps",
    "h1": "Apps to use Grok on iPhone in 2026",
    "description": "Ways to use xAI's Grok on iPhone: the Grok app, Ask Grok in X, and chat apps that offer Grok next to Claude and Gemini, by price and privacy label.",
    "llms": "Explains how to use xAI's Grok chat assistant on an iPhone: the official Grok app (free, SuperGrok from $10 a month) and six other apps whose App Store listings name Grok (Chat AI, X with Ask Grok, ChatNow, Ask AI, Chat Smith, Nova), by price and App Store privacy label. Not about Grok Imagine video.",
    "answer": [
        "<strong>The direct way to use Grok on iPhone is the official <a href=\"https://apps.apple.com/us/app/id6670324846\">Grok</a> app from X Corp.</strong> It is free to download, with SuperGrok Lite at $10 a month, SuperGrok $30, Plus $100 and Heavy $300 listed on the US App Store on 3 November 2026, and a 4.9 rating from 1,567,769 ratings. Its listing covers chat, deep research, voice mode and real-time information from X.",
        "Six other apps also give you Grok. The X app has Ask Grok built in, for questions about posts and trending news. Chat AI, ChatNow, Ask AI, Chat Smith and Nova put a Grok model next to Claude, Gemini and others in one chat, so you can compare answers or switch without a second subscription. This page is about Grok as a chat assistant; for Grok Imagine video, see reviewland's <a href=\"https://reviewland.io/grok-imagine-alternatives-iphone/\">Grok Imagine alternatives</a>.",
    ],
    "columns": ["App", "Price (US)", "How it offers Grok, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Chat AI: Ask Agent Anything", 1668787639, "chat-ai", "DEEP FLOW SOFTWARE SERVICES - FZCO", 4.76, 329089,
            "the widest choice: Grok 4.7 next to GPT-6, Claude Opus 5, Gemini and DeepSeek, plus images and files.",
            ["Its listing names Grok 4.7 next to GPT-6, Claude Opus 5, Gemini 3.1 Pro, DeepSeek V4 Pro and Perplexity.",
             "Also makes images, reads PDF, TXT and DOCX files and searches the web with sources.",
             "Its in-app purchases are named «Ask AI Premium», but it is a different app from Ask AI below."],
            "weekly plans only, plus a lifetime option, and its privacy label includes Data Used to Track You.",
            ["Premium weekly $7.39 to $11.99; lifetime $39.99 or $69.99",
             "Grok 4.7 among several cloud models",
             "15", TN, "3.6.3 (28 Sep 2026)"]),
        app("X", 333903271, "x", "X Corp.", 4.58, 11160532,
            "people already on X who want Grok's take on a post, a video or the day's news.",
            ["Ask Grok is built into the app: it summarizes trending news, explains videos and adds context to posts, per its listing.",
             "Grok also powers X's photo and video editing tools.",
             "From the same company as the Grok app."],
            "it is a social network first, so Grok sits inside a feed rather than a clean chat app.",
            ["Premium Basic $4 a month, Premium $11, Premium Plus $50 (yearly $42 to $490)",
             "Ask Grok inside the X app",
             "41", T3, "12.39 (29 Oct 2026)"]),
        app("AI Chat Assistant – ChatNow", 1667518571, "chatnow", "Tappz GmbH", 4.80, 146222,
            "asking several models the same question, Grok included, and keeping the best answer.",
            ["Its listing names Grok 4.5 and Grok 4.3 among more than 30 models, with GPT-6 Astra, Claude Fable 5.1 and Gemini 3.1 Pro.",
             "You can ask several models the same question and compare the answers.",
             "Also makes images and video with models such as Nano Banana Pro, Veo 3.1 and Seedance 2.5."],
            "it needs iOS 26, and the plans range widely ($6.99 to $79.99 listed) without the listing saying which is which.",
            ["Plus from $6.99 to $79.99 listed, yearly $59.99; credits $9.99 or $19.99",
             "Grok 4.5 and 4.3 among 30+ models",
             "13", TN, "5.13 (24 Oct 2026)"]),
        app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3,
            "switching between Grok, Claude, Gemini and DeepSeek in the same conversation.",
            ["Its listing names models from several companies, including Gemini, Claude, Grok, DeepSeek and Perplexity Sonar, and you can switch model in the middle of a chat.",
             "With Pro, it searches the web by itself when a question needs current information.",
             "Reads photos you attach and can read any answer aloud."],
            "most models and web search need Pro (a few free messages a day without it), it does not read files or make images, and it has only 3 ratings.",
            ["A few free messages a day; Pro weekly $7.99, monthly $9.99, yearly listed from $39.99 to $69.99",
             "Grok among several cloud models, switchable mid-chat",
             "5", T3, "1.4.5 (2 Nov 2026)"], ours=True),
        app("Chat Smith: AI Chatbot & Agent", 1559479889, "chat-smith", "CHAT SMITH OPCO PTE. LTD", 4.58, 166659,
            "writing tools around the chat: a humanizer, an AI detector and a logo maker.",
            ["Its listing names Grok-4.5 next to GPT-6 Sol, Claude Sonnet 5, Gemini 3 and DeepSeek V4.",
             "Adds an AI Humanizer, an AI Detector, an AI logo maker and a calendar agent.",
             "A lifetime purchase is listed at $99.99."],
            "the download is large (725 MB), and its privacy label includes Data Used to Track You and Data Linked to You.",
            ["Pro weekly $4.99 or $6.99, monthly $6.99 or $9.99, yearly $39.99 or $69.99; lifetime $99.99",
             "Grok-4.5 among several cloud models",
             "10", T3, "9.261026.1 (29 Oct 2026)"]),
        app("AI Chatbot - Nova", 1669007652, "nova", "SCALEUP YAZILIM HIZMETLERI ANONIM SIRKETI", 4.64, 127366,
            "a simple chat app with Grok, Kimi and DeepSeek, plus voice mode and file work.",
            ["Its listing names xAI Grok 4.5 next to GPT-5.6, Gemini 3.6 Flash, Claude Opus 5, Kimi K3 and DeepSeek V4 Pro.",
             "Voice mode, web search, image generation, and work on Word and Excel files.",
             "Translates in 140+ languages, per its listing."],
            "its listing describes most features as built on OpenAI GPT-5.6, so check that Grok is selectable before paying.",
            ["Pro weekly $4.99 to $7.99, monthly $9.99, yearly $39.99 or $59.99",
             "Grok 4.5 among several cloud models",
             "9", TN, "4.5.6 (30 Oct 2026)"]),
    ],
    "who": [
        "<strong>Grok itself, with SuperGrok when you need more:</strong> the official Grok app.",
        "<strong>The most models, plus images and files:</strong> Chat AI.",
        "<strong>Grok on posts and news:</strong> X.",
        "<strong>Comparing several models' answers side by side:</strong> ChatNow.",
        "<strong>Grok, Claude, Gemini and DeepSeek in the same chat:</strong> Ask AI.",
        "<strong>Writing extras like a humanizer:</strong> Chat Smith.",
    ],
    "cases": ["Getting Grok's view on today's news.", "Comparing Grok's answer with Claude's or Gemini's.", "Using Grok without a SuperGrok subscription."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «grok», «grok ai», «grok chat» and «ai chat multiple models», and read each app's US App Store page and Apple's lookup data. We only included apps whose own listing names Grok as a chat model; what each app does comes from that listing. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there an official Grok app for iPhone?",
         "Yes: Grok, from X Corp. It is free to download; SuperGrok plans from $10 a month were listed on 3 November 2026."),
        ("Can I use Grok inside the X app?",
         "Yes. The X app's listing describes Ask Grok, which summarizes trending news, explains videos and adds context to posts."),
        ("Which apps let me use Grok and other models in one place?",
         "Chat AI, ChatNow, Ask AI, Chat Smith and Nova all name Grok in their listings, next to models such as Claude and Gemini. Ask AI lets you switch model in the middle of a conversation; ChatNow lets you compare answers."),
        ("Is this about Grok Imagine?",
         "No. Grok Imagine makes images and video; this page is about Grok as a chat assistant. Reviewland compares apps for Grok Imagine-style video."),
    ],
    "sources": [
        ("Grok (App Store)", "https://apps.apple.com/us/app/id6670324846"),
        ("Chat AI: Ask Agent Anything (App Store)", "https://apps.apple.com/us/app/id1668787639"),
        ("X (App Store)", "https://apps.apple.com/us/app/id333903271"),
        ("AI Chat Assistant – ChatNow (App Store)", "https://apps.apple.com/us/app/id1667518571"),
        ("All AI Models in One: Ask AI (App Store)", "https://apps.apple.com/us/app/id1662608035"),
        ("Chat Smith (App Store)", "https://apps.apple.com/us/app/id1559479889"),
        ("AI Chatbot - Nova (App Store)", "https://apps.apple.com/us/app/id1669007652"),
    ],
}]
