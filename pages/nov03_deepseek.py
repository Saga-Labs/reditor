"""Apps to use DeepSeek on iPhone, EN (was /deepseek-alternatives-iphone/ for a few minutes on 3 Nov; that URL is reviewland's, see ios-playbook references/temas-webs.md). Our app: Ask AI (id1662608035), whose listing names DeepSeek among its models.

Checked 2026-11-03: US App Store search for «deepseek», «deepseek ai», «deepseek chat» and «deepseek offline»,
iTunes lookup and the US App Store page of every app (price list, privacy label). Only apps whose own listing names
DeepSeek are in the list (Poe, ChatOn, Genie, Claude, Grok and Perplexity are left out because theirs do not).
Why this topic: Google suggests «deepseek app», «deepseek app store» and «deepseek apple» (3 Nov), our AI-answer
tracking asks «AI chatbot app with DeepSeek iPhone» (saga-growth aeo-preguntas.md, Ask AI 5), and no DeepSeek page
exists on reditor, reviewland, aisagalab or doravideo.com (sitemaps read 3 Nov). No quality test.
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


PAGES = [{
    "group": "deepseek-alt", "lang": "en", "store": "us",
    "path": "deepseek-apps-iphone/",
    "ct": "rd-deepseek-apps-iphone",
    "category": "ProductivityApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "How to Use DeepSeek on iPhone (2026): 7 Apps That Offer It",
    "h1": "Apps to use DeepSeek on iPhone in 2026",
    "description": "Seven ways to use DeepSeek on iPhone: the free official app, three chat apps that offer it next to other models, and three that run it offline.",
    "llms": "Explains how to use DeepSeek on an iPhone: describes the official DeepSeek app (free, Hangzhou DeepSeek, Data Linked to You) and compares six iPhone apps whose App Store listings name DeepSeek: three cloud chat apps with several models (Chat AI by Deep Flow, AI Chat by AppStation, Ask AI) and three that run smaller DeepSeek-based models offline on the phone (Locally AI, Private LLM, Enclave), by price and App Store privacy label.",
    "answer": [
        "<strong>The simplest way to use DeepSeek on iPhone is its official app.</strong> It is <a href=\"https://apps.apple.com/us/app/id6737597349\">DeepSeek - AI Assistant</a> from Hangzhou DeepSeek Artificial Intelligence Co., Ltd: free, with no in-app purchases listed, in 71 languages. On 3 November 2026 its US App Store rating was 3.9 from 12,484 ratings, and its privacy label lists Data Linked to You.",
        "Six other apps also give you DeepSeek. To use it next to other models in one chat, Chat AI, AI Chat and Ask AI name DeepSeek in their listings, beside Claude and Gemini. To keep everything on the phone, Locally AI, Private LLM and Enclave run DeepSeek-based models offline; these are small distilled versions (Private LLM names DeepSeek R1 Distill), not the full model the official app uses.",
    ],
    "columns": ["App", "Price (US)", "How it offers DeepSeek, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download except Private LLM. Ratings are that day's App Store average and count.",
    "apps": [
        app("Chat AI: Ask Agent Anything", 1668787639, "chat-ai", "DEEP FLOW SOFTWARE SERVICES - FZCO", 4.76, 329089,
            "people who want DeepSeek V4 Pro and many other models, plus images and files, in one big app.",
            ["Its listing names DeepSeek V4 Pro next to GPT-6, Claude Opus 5, Gemini 3.1 Pro, Grok 4.7 and Perplexity.",
             "Also makes images, reads PDF, TXT and DOCX files, searches the web with sources and has hands-free voice.",
             "The most ratings of any app here (329,089)."],
            "weekly plans only, plus a lifetime option, and its privacy label includes Data Used to Track You.",
            ["Premium weekly $7.39 to $11.99; lifetime $39.99 or $69.99",
             "DeepSeek V4 Pro among several cloud models",
             "15", "Data Used to Track You; Data Not Linked to You", "3.6.3 (28 Sep 2026)"]),
        app("Locally AI by LM Studio", 6741426692, "locally-ai", "Element Labs Inc", 4.70, 1897,
            "running a DeepSeek-based model offline, for free, with nothing collected.",
            ["Runs models such as Llama, Gemma, Qwen and DeepSeek on the iPhone and iPad, offline, with Apple MLX, per its listing.",
             "No login and no data collection: its privacy label is Data Not Collected.",
             "Made by the team behind LM Studio for the Mac and PC."],
            "on-device models are much smaller than the DeepSeek in the official app, and answers depend on your iPhone's memory.",
            ["Free; no in-app purchases listed",
             "Smaller DeepSeek-based models, offline on the phone",
             "11", "Data Not Collected", "1.66.0 (15 Oct 2026)"]),
        app("AI Chat - Smart AI Assistant", 6468878395, "ai-chat", "AppStation Studio Pte. Ltd.", 4.82, 551,
            "a chat app in many languages that offers DeepSeek for coding and technical questions.",
            ["Its listing names Claude, DeepSeek and Gemini, and suggests DeepSeek for coding and technical tasks.",
             "Searches the web, makes and edits images, and reads PDFs and other files.",
             "In 38 languages."],
            "it has not been updated since 14 August 2026, and the plans are pricier than Ask AI's.",
            ["Pro weekly $7.99, monthly $19.99, yearly $99.99",
             "DeepSeek among several cloud models",
             "38", "Data Linked to You; Data Not Linked to You", "3.3.1 (14 Aug 2026)"]),
        app("All AI Models in One: Ask AI", 1662608035, "ask-ai", "Saga Ltd.", 5.0, 3,
            "switching between DeepSeek, Claude, Gemini and Grok in the same conversation.",
            ["Its listing names models from several companies, including Gemini, Claude, Grok, DeepSeek and Perplexity Sonar, and you can switch model in the middle of a chat.",
             "With Pro, it searches the web by itself when a question needs current information.",
             "Reads photos you attach and can read any answer aloud."],
            "most models and web search need Pro (a few free messages a day without it), it does not read files or make images, and it has only 3 ratings.",
            ["A few free messages a day; Pro weekly $7.99, monthly $9.99, yearly listed from $39.99 to $69.99",
             "DeepSeek among several cloud models, switchable mid-chat",
             "5", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "1.4.5 (2 Nov 2026)"], ours=True),
        app("Private LLM - Local AI Chat", 6448106860, "private-llm", "Numen Technologies Limited", 4.15, 741,
            "paying once, with no subscription, for offline models that include DeepSeek R1 Distill.",
            ["Its listing names DeepSeek R1 Distill based models next to Llama, Gemma, Qwen and Mistral, all running on the device.",
             "Works with Siri and Shortcuts, and lets you set your own system prompt.",
             "Its privacy label is Data Not Collected."],
            "it costs $4.99 up front, is in English only, the download is 1.36 GB, and it has the lowest rating here (4.2).",
            ["$4.99 once; no in-app purchases listed",
             "DeepSeek R1 Distill models, offline on the phone",
             "1", "Data Not Collected", "1.9.18 (28 Oct 2026)"]),
        app("Enclave - Local AI Assistant", 6476614556, "enclave", "Piotr Gorzelany", 4.70, 1115,
            "an offline app that shows DeepSeek R1's reasoning, with optional cloud models later.",
            ["Runs open models on the iPhone, DeepSeek among them, and displays the reasoning of thinking models such as DeepSeek R1, per its listing.",
             "Chats with PDFs, text files and images locally; voice chat works offline.",
             "Pro adds cloud models from Anthropic, OpenAI, Google and xAI, and web search."],
            "it needs iOS 27, and offline models are small versions, not the full DeepSeek.",
            ["Free; Pro $9.99; three other purchases $0.99 to $9.99",
             "DeepSeek-based models offline; cloud models with Pro",
             "14", "Data Not Linked to You", "1.77.0 (1 Oct 2026)"]),
    ],
    "who": [
        "<strong>The full DeepSeek model, free:</strong> the official DeepSeek app.",
        "<strong>DeepSeek plus many other models, images and files:</strong> Chat AI.",
        "<strong>DeepSeek offline, free, nothing collected:</strong> Locally AI.",
        "<strong>DeepSeek, Claude, Gemini and Grok in the same chat:</strong> Ask AI.",
        "<strong>Offline with a one-time price:</strong> Private LLM.",
        "<strong>Offline now, cloud models later:</strong> Enclave.",
    ],
    "cases": ["Asking DeepSeek a coding question.", "Comparing DeepSeek's answer with Claude's or Gemini's.", "Using a DeepSeek model with no internet."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «deepseek», «deepseek ai», «deepseek chat» and «deepseek offline», and read each app's US App Store page and Apple's lookup data. We only included apps whose own listing names DeepSeek; what each app does comes from that listing. We ran no quality test.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there an official DeepSeek app for iPhone?",
         "Yes: DeepSeek - AI Assistant, from Hangzhou DeepSeek Artificial Intelligence Co., Ltd. It is free, with no in-app purchases listed on 3 November 2026."),
        ("Can I use DeepSeek on iPhone without internet?",
         "Not with the official app. Locally AI, Private LLM and Enclave run smaller DeepSeek-based models on the phone with no connection; they are distilled versions, so answers are simpler than the full model's."),
        ("Which app lets me use DeepSeek and other models in one place?",
         "Chat AI, AI Chat and Ask AI all name DeepSeek in their listings, next to Claude and Gemini. Ask AI lets you switch model in the middle of a conversation."),
        ("Is Chat AI the same app as Ask AI?",
         "No. Chat AI: Ask Agent Anything is from DEEP FLOW SOFTWARE SERVICES (Codeway); its in-app purchases are named «Ask AI Premium». All AI Models in One: Ask AI is a different app, from Saga Ltd."),
    ],
    "sources": [
        ("DeepSeek - AI Assistant (App Store)", "https://apps.apple.com/us/app/id6737597349"),
        ("Chat AI: Ask Agent Anything (App Store)", "https://apps.apple.com/us/app/id1668787639"),
        ("Locally AI by LM Studio (App Store)", "https://apps.apple.com/us/app/id6741426692"),
        ("AI Chat - Smart AI Assistant (App Store)", "https://apps.apple.com/us/app/id6468878395"),
        ("All AI Models in One: Ask AI (App Store)", "https://apps.apple.com/us/app/id1662608035"),
        ("Private LLM - Local AI Chat (App Store)", "https://apps.apple.com/us/app/id6448106860"),
        ("Enclave - Local AI Assistant (App Store)", "https://apps.apple.com/us/app/id6476614556"),
    ],
}]
