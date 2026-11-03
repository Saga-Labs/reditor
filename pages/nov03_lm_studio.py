"""LM Studio on iPhone, EN. Our app: Pinku (id6754878073), which runs models on the iPhone or Mac and does NOT connect to LM Studio.

Checked 2026-11-03: US App Store search for «lm studio», «lm studio client», «local llm server», «pocketpal», «ollama
client», iTunes lookup and the US App Store page of every app (price list, privacy label, Mac availability). LM Studio
itself has no iPhone app; Locally AI is from the same team (Element Labs) and goes in the intro. Why this topic: Google
suggests «lm studio iphone app», «lm studio iphone client», «lm studio ios app», «lm studio ios client» (3 Nov); no
page on the 4 sites covers it (/ollama-alternatives-mac-iphone/ compares desktop tools; this one is the iPhone side).
Registered in ios-playbook references/temas-webs.md (37cca5f). No speed test, nothing installed.
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


NC = "Data Not Collected"

PAGES = [{
    "group": "lm-studio-iphone", "lang": "en", "store": "us",
    "path": "lm-studio-apps-iphone/",
    "ct": "rd-lm-studio-apps-iphone",
    "category": "DeveloperApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "LM Studio on iPhone (2026): 7 Apps to Connect or Run Models",
    "h1": "How to use LM Studio on iPhone in 2026",
    "description": "LM Studio has no iPhone app. Seven apps that either connect to LM Studio on your computer or run open models on the iPhone itself, by price and privacy.",
    "llms": "Explains how to use LM Studio from an iPhone: LM Studio has no iPhone app; its team makes Locally AI, which runs models on the phone. Compares seven iPhone apps: three that connect to an LM Studio server on your computer and also run models on the phone (LM Mini, Reins, LocalMind), one more client (Chapper), and three that only run models on the device (Pinku, Noema, PocketPal AI), by price, LM Studio connection, Mac version and App Store privacy label.",
    "llms_note": "Pinku, one of the seven, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>LM Studio has no iPhone app.</strong> Its team, Element Labs, makes <a href=\"https://apps.apple.com/us/app/id6741426692\">Locally AI by LM Studio</a> for iPhone, iPad and Mac: free, no login, privacy label <em>Data Not Collected</em>, and it runs models such as Llama, Gemma and Qwen on the phone with Apple's MLX. Its listing does not say it connects to LM Studio on your computer.",
        "So there are two ways in. To chat with the models already loaded in LM Studio on your Mac or PC, use a client: LM Mini, Reins and LocalMind name LM Studio in their listings and also run smaller models on the phone, and Chapper is a client with an optional on-device add-on. To skip the computer and run open models on the iPhone itself, Pinku, Noema and PocketPal AI do that offline. For desktop tools, see our <a href=\"/ollama-alternatives-mac-iphone/\">Ollama alternatives</a>.",
    ],
    "columns": ["App", "Price (US)", "Connects to LM Studio, per its listing", "Runs models on the iPhone", "Mac app", "App Store privacy label", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. «Mac app» means a Mac version on the App Store. Ratings are that day's App Store average and count.",
    "apps": [
        app("LM Mini", 6751125309, "lm-mini", "Sultan Haider", 4.45, 158,
            "people already running LM Studio who want to manage it from the phone, at home or away.",
            ["Connects to LM Studio, Ollama, Jan AI and oMLX over Wi-Fi or USB, and from anywhere through LM Mini Connect, encrypted with your key.",
             "Lets you manage and download models on LM Studio from your phone, and imports chats from LM Studio.",
             "Also downloads models to run on the phone with no internet; version 1.10.8 came out on 2 November 2026."],
            "English only, and the lifetime price ($119.99) is the highest here.",
            ["Monthly $4.99, yearly $29.99, lifetime $119.99",
             "Yes: LM Studio, Ollama, Jan AI, oMLX", "Yes", "Yes", NC]),
        app("Reins: for Ollama & LM Studio", 6739738501, "reins", "Ibrahim Cetin", 4.56, 317,
            "one app for your LM Studio or Ollama server and MLX models on the phone, with web search.",
            ["Connects to Ollama, LM Studio or any OpenAI-compatible server, with several servers you can switch between.",
             "Runs MLX models on the iPhone, including any MLX model not in its library, and Apple's on-device Foundation Models.",
             "Web search without an API key, file attachments (images, PDFs, CSVs) and branching chats."],
            "English only; keeps generating in the background only on iOS 26.",
            ["Monthly $6.99, yearly $39.99, lifetime $99.99",
             "Yes: LM Studio, Ollama, OpenAI-compatible", "Yes (MLX)", "Yes", NC]),
        app("LocalMind: Ollama & LM Studio", 6777025480, "localmind", "Abdul Momin Sakib", 4.47, 15,
            "an open-source client with no purchases listed.",
            ["Connects to an Ollama or LM Studio server, OpenRouter, Requesty or any OpenAI-compatible endpoint.",
             "Downloads supported models to run on the phone, offline after the download.",
             "Open source on GitHub, per its listing, with optional end-to-end encrypted sync to your own S3 storage."],
            "only 15 ratings, English only, and no Mac version.",
            ["No purchases listed",
             "Yes: LM Studio, Ollama, OpenAI-compatible", "Yes", "No", NC]),
        app("Private Offline AI Chat: Pinku", 6754878073, "pinku", "Saga Ltd.", 4.67, 12,
            "running open models on the iPhone or Mac with no LM Studio and no computer at all.",
            ["Runs 11 open models on the device with Apple's MLX, from Qwen3 0.6B (0.4 GB) to Qwen3 8B (4.7 GB), and only lists the ones your device has the memory for.",
             "Works in airplane mode after the download; no account, and chats are saved only on the device.",
             "Chatting with the default model, Llama 3.2 1B, is free; Pinku Pro, to choose any model, is yearly ($16.99) or one-time (from $9.99)."],
            "it does not connect to LM Studio or any server, and its privacy label lists Data Linked to You (purchase history and a user ID, for Pinku Pro purchases).",
            ["Free; Pinku Pro $16.99 a year or one-time from $9.99",
             "No", "Yes (MLX, 11 models)", "Yes", "Data Linked to You"], ours=True),
        app("Noema: Local AI & Offline LLM", 6751169935, "noema", "Alexandru Stamate", 4.61, 36,
            "chatting with your own PDFs and books on the device.",
            ["Runs local models on iPhone, iPad, Mac and Apple Vision, in GGUF, MLX, ExecuTorch and Core ML.",
             "Indexes PDFs, EPUBs and textbooks and answers from them; shows whether a model fits your device before you download it.",
             "Can act as a private local API for other apps on your network, and Noema Relay lets one Apple device use a model hosted on another."],
            "its listing does not name LM Studio, and it is a large download (409 MB).",
            ["No purchases listed",
             "Not named (other remote providers optional)", "Yes", "Yes", NC]),
        app("Chapper: AI & LM Studio Client", 6760984679, "chapper", "Prevolut Ltd", 3.11, 9,
            "detailed control of LM Studio models from an iPhone, with no subscription.",
            ["Connects to LM Studio, Ollama, llama.cpp and other OpenAI-compatible endpoints; loads and unloads models and shows quantization and context length.",
             "One purchase (Chapper Pro, $9.99) and an optional on-device add-on ($4.99); no subscription, per its listing.",
             "MCP tools, a sandboxed terminal and export to TXT, PDF, Markdown, JSON and more."],
            "the lowest rating here (3.1 from 9 ratings), no Mac version, and its last update was 6 August 2026.",
            ["Chapper Pro $9.99; on-device add-on $4.99",
             "Yes: LM Studio, Ollama, llama.cpp", "With the $4.99 add-on", "No", NC]),
        app("PocketPal AI", 6502579498, "pocketpal", "Gooya UG (haftungsbeschraenkt)", 4.04, 165,
            "finding GGUF models on Hugging Face and running them offline on the phone.",
            ["Searches Hugging Face for GGUF models inside the app, to bookmark or download.",
             "Chats offline once a model is downloaded; runs on iOS 15.1 and later, the oldest here.",
             "Version 1.22.0 came out on 1 November 2026."],
            "it does not connect to LM Studio, there is no Mac version, and its listing is short on detail.",
            ["PocketPal Plus $3.99 to $44.99; add-ons from $0.99",
             "No", "Yes (GGUF)", "No", NC]),
    ],
    "who": [
        "<strong>Managing LM Studio on your Mac from the phone:</strong> LM Mini.",
        "<strong>LM Studio or Ollama plus MLX models on the phone:</strong> Reins.",
        "<strong>Open source, nothing to buy:</strong> LocalMind.",
        "<strong>No computer, offline on iPhone and Mac:</strong> Pinku.",
        "<strong>Asking questions about your own documents:</strong> Noema.",
        "<strong>Same team as LM Studio:</strong> Locally AI (free).",
    ],
    "cases": ["Using the bigger model on your Mac from the sofa.", "Chatting with AI on a plane with no Wi-Fi.", "Keeping work notes off cloud chat servers."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «lm studio», «lm studio client», «local llm server», «pocketpal» and «ollama client», and read each app's US App Store page and Apple's lookup data. «Connects to LM Studio» means its listing names LM Studio. We installed nothing and ran no speed test.",
        "To reach LM Studio from a phone, LM Studio's server has to be running on your computer and reachable on your network (or through the app's own relay, where it has one).",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Is there an LM Studio app for iPhone?",
         "No. LM Studio runs on Mac, Windows and Linux. Its team makes Locally AI for iPhone, which runs models on the phone; its listing does not mention connecting to LM Studio."),
        ("How do I connect my iPhone to LM Studio on my Mac?",
         "Start LM Studio's local server on the Mac, then add its address in a client such as LM Mini, Reins, LocalMind or Chapper. LM Mini also lists USB and a remote relay, LM Mini Connect."),
        ("Can I run the same models on the iPhone without a computer?",
         "Smaller versions, yes. Locally AI, Pinku, Noema and PocketPal AI run open models such as Llama, Qwen and Gemma on the phone, offline after the download. Models that need a Mac's memory will not fit."),
        ("Which of these collect no data?",
         "All except Pinku have the App Store label Data Not Collected. Pinku's label lists purchase history and a user ID, used for Pinku Pro purchases, not chats."),
    ],
    "sources": [
        ("Locally AI by LM Studio (App Store)", "https://apps.apple.com/us/app/id6741426692"),
        ("LM Mini (App Store)", "https://apps.apple.com/us/app/id6751125309"),
        ("Reins (App Store)", "https://apps.apple.com/us/app/id6739738501"),
        ("LocalMind (App Store)", "https://apps.apple.com/us/app/id6777025480"),
        ("Pinku (App Store)", "https://apps.apple.com/us/app/id6754878073"),
        ("Noema (App Store)", "https://apps.apple.com/us/app/id6751169935"),
        ("Chapper (App Store)", "https://apps.apple.com/us/app/id6760984679"),
        ("PocketPal AI (App Store)", "https://apps.apple.com/us/app/id6502579498"),
        ("LM Studio", "https://lmstudio.ai/"),
    ],
}]
