"""Ollama alternatives for Mac and iPhone (2026). EN only.

Checked 2026-10-20: GitHub API (licence, latest release, last commit) for Ollama,
llama.cpp, Jan and GPT4All; lmstudio.ai download, pricing and system
requirements; jan.ai Mac install docs; docs.ollama.com/macos and
ollama.com/pricing; iTunes lookup API (US) and App Store pages for the four
App Store apps. Pinku (ours) is one more option, not first and without the
"Our app" tag, per Marta (20 Oct 2026); transparency note in "method".
"""

CHECKED = "2026-10-20"
AISAGALAB = "https://aisagalab.com/blog/best-open-weight-ai-models.html"
REVIEWLAND = "https://reviewland.io/best-apps-run-open-source-ai-models-iphone/"

EN = {
    "group": "ollama-alternatives", "lang": "en", "store": "us",
    "path": "ollama-alternatives-mac-iphone/",
    "ct": "rd-ollama-alt",
    "category": "DeveloperApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Ollama alternatives for running open models on Mac and iPhone (2026)",
    "h1": "Best Ollama alternatives for Mac and iPhone in 2026",
    "description": "Eight Ollama alternatives compared: LM Studio, Jan, llama.cpp, GPT4All and the App Store apps Locally AI, Private LLM, Enclave and Pinku.",
    "llms": "Compares eight alternatives to Ollama for running open-weight models on Mac and iPhone (LM Studio, Jan, llama.cpp, GPT4All, Locally AI, Private LLM, Enclave, Pinku) by licence, macOS or iOS requirement, last update and whether they also run on iPhone. Notes that GPT4All has had no release since February 2025.",
    "llms_note": "Pinku, one of the eight, is made by Saga Labs, which runs Reditor.",
    "disclosure": "Pinku is made by Saga Labs, the company behind Reditor. It is listed on the same criteria as the others.",
    "answer": [
        "If Ollama feels too technical, LM Studio is the closest free alternative on a Mac: a desktop app with a model browser that runs models with llama.cpp and Apple's MLX. Jan is the open-source equivalent. If you want Ollama's engine without Ollama, use llama.cpp directly. GPT4All still works but has had no release since February 2025.",
        "Ollama has no iPhone app. To run the same open models on an iPhone, use an App Store app: Locally AI (from the LM Studio team), Private LLM, Enclave or Pinku, all of which also have a Mac version. For which model to choose, see <a href=\"" + AISAGALAB + "\">the guide to open-weight models</a>.",
    ],
    "columns": ["Tool", "Type", "Licence", "Mac requirement", "Also on iPhone", "Last update"],
    "table_note": "Licences and last updates from GitHub or the App Store on 20 October 2026; Mac requirements from each project's documentation or App Store page.",
    "apps": [
        {
            "name": "LM Studio", "anchor": "lmstudio", "developer": "Element Labs",
            "row": ["Desktop app with model browser", "Free; not open source", "Apple silicon, macOS 14, 16 GB recommended", "Yes, as Locally AI", "0.4.26"],
            "best_for": "the easiest switch from Ollama on a Mac, with a graphical model browser.",
            "facts": [
                "Runs models with llama.cpp and MLX; has a programmable API and a headless daemon (llmster) for servers.",
                "The free plan runs local models; optional Bionic+ ($20 a month) adds hosted open models.",
                "Intel Macs are not supported.",
            ],
            "limits": "closed source; the cloud plans are separate from local use.",
        },
        {
            "name": "Jan", "anchor": "jan", "developer": "Menlo Research",
            "row": ["Desktop chat app", "Open source, free", "macOS 13.6; Apple silicon for local models", "No", "0.8.6 (9 Oct 2026)"],
            "best_for": "an open-source app with a chat window and a local API server.",
            "facts": [
                "Its documentation sizes models by memory: 8 GB up to about 3B, 16 GB up to about 7B, 32 GB up to about 13B.",
                "Can also connect to cloud models from several providers.",
                "45,000 stars on GitHub.",
            ],
            "limits": "on Intel Macs its bundled engine does not load models; no iPhone version.",
        },
        {
            "name": "llama.cpp", "anchor": "llamacpp", "developer": "ggml-org",
            "row": ["Command line and server", "MIT", "Any Mac", "No (it powers several iPhone apps)", "Active (Oct 2026)"],
            "best_for": "people who want the engine itself, with the most control over quantisation and settings.",
            "facts": [
                "Runs GGUF files, the format most open models are shared in.",
                "The engine inside many of the apps on this page.",
                "131,827 stars on GitHub.",
            ],
            "limits": "terminal only; you choose and download models yourself.",
        },
        {
            "name": "GPT4All", "anchor": "gpt4all", "developer": "Nomic",
            "row": ["Desktop chat app", "MIT", "macOS download available", "No", "v3.10.0 (25 Feb 2025)"],
            "best_for": "existing users who rely on its LocalDocs feature for chatting with files.",
            "facts": [
                "Chat with local documents (LocalDocs).",
                "Last commit on GitHub on 27 May 2025.",
            ],
            "limits": "no release in about 20 months, so newer model families may not be supported.",
        },
        {
            "name": "Locally AI by LM Studio", "id": 6741426692, "anchor": "locally", "developer": "Element Labs", "rating": (4.71, 1804),
            "row": ["App Store app", "Free; not open source", "macOS 26", "Yes", "1.66.0 (15 Oct 2026)"],
            "best_for": "the same models on iPhone and Mac from one free app.",
            "facts": ["Apple MLX; no login; Data Not Collected.", "4.7 from 1,804 ratings in the US."],
            "limits": "on Mac it needs macOS 26; curated models only.",
        },
        {
            "name": "Private LLM - Local AI Chat", "id": 6448106860, "anchor": "privatellm", "developer": "Numen Technologies", "rating": (4.15, 736),
            "row": ["App Store app", "$4.99 once", "macOS 14", "Yes", "1.9.16 (14 Sep 2026)"],
            "best_for": "paying once for Mac and iPhone, with Siri and Shortcuts.",
            "facts": ["Models up to 14B on Mac; its own OmniQuant quantisation.", "Family Sharing; Data Not Collected."],
            "limits": "a fixed list of mostly older model families.",
        },
        {
            "name": "Enclave - Local AI Assistant", "id": 6476614556, "anchor": "enclave", "developer": "Piotr Gorzelany", "rating": (4.7, 1101),
            "row": ["App Store app", "Free; Pro $9.99", "macOS 27, M1 or later", "Yes (iOS 27)", "1.77.0 (1 Oct 2026)"],
            "best_for": "documents, voice and custom assistants, with optional cloud models.",
            "facts": ["\"Hundreds\" of open models, per its description.", "Pro adds cloud models."],
            "limits": "requires the newest macOS and iOS (27).",
        },
        {
            "name": "Pinku: Private Offline AI Chat", "id": 6754878073, "anchor": "pinku", "developer": "Saga Ltd.", "rating": (4.67, 12),
            "row": ["App Store app", "Free; Pinku Pro in-app purchase", "macOS 14, Apple silicon", "Yes (iPhone 12+)", "iPhone 1.0.9 (16 Oct 2026); Mac 1.0.7"],
            "best_for": "a short tested list that hides models your device cannot run, in 8 interface languages.",
            "facts": [
                "Chats never leave the device; Apple's privacy label lists only purchase history and an anonymous user ID, used for Pinku Pro purchases.",
                "Downloads from ModelScope where Hugging Face is blocked.",
            ],
            "limits": "12 curated models only (0.34 to 4.7 GB; no Gemma 4 or Qwen3.5 yet); the Mac version on sale is 1.0.7; few ratings.",
        },
    ],
    "who": [
        "You want Ollama, but with windows and menus: LM Studio.",
        "You want that, but open source: Jan.",
        "You want the engine and full control: llama.cpp.",
        "You want the same thing on your iPhone: Locally AI, Private LLM, Enclave or Pinku. Compared in detail on <a href=\"" + REVIEWLAND + "\">Reviewland</a>.",
    ],
    "cases": [
        "Run a coding model such as Devstral Small 2 or Qwen3.5 on a Mac with 32 GB or more.",
        "Keep sensitive documents off cloud services.",
        "Carry a small model on your iPhone for flights and places without signal.",
    ],
    "method": [
        "We checked each project's GitHub page (licence, latest release, last commit), documentation and, for App Store apps, the US App Store page on 20 October 2026.",
        "Ollama itself: MIT licence, latest release v0.40.6 on 16 October 2026, macOS 14 or later, Apple silicon or Intel (CPU only); its giant models run on Ollama's cloud with usage credits.",
        "From the team at Saga Labs: we make Pinku, one of the apps here. We built it because tools like Ollama and LM Studio expect some technical knowledge, such as picking a model file and a quantisation or using a terminal. Pinku is for everyone else: install it from the App Store, tap a model and chat privately, with no terminal and nothing to configure. The trade-off is a short list of small models chosen to fit each device, which is why it is not first here.",
    ],
    "faq": [
        ("What is the best Ollama alternative for Mac?", "LM Studio for a free desktop app with a model browser; Jan if you want it open source; llama.cpp if you are happy in a terminal."),
        ("Is there an Ollama app for iPhone?", "No. To run open models on iPhone use an App Store app such as Locally AI, Private LLM, Enclave or Pinku."),
        ("Is GPT4All still maintained?", "Its latest release on GitHub is v3.10.0 from 25 February 2025 and the last commit is from 27 May 2025."),
        ("Which open model should I run?", "It depends on memory. See the guide to open-weight models on aisagalab.com for sizes, licences and hardware."),
    ],
    "sources": [
        ("Ollama (GitHub)", "https://github.com/ollama/ollama"),
        ("Ollama macOS requirements", "https://docs.ollama.com/macos"),
        ("LM Studio system requirements", "https://lmstudio.ai/docs/app/system-requirements"),
        ("LM Studio pricing", "https://lmstudio.ai/pricing"),
        ("Jan Mac install", "https://www.jan.ai/docs/desktop/install/mac"),
        ("llama.cpp (GitHub)", "https://github.com/ggml-org/llama.cpp"),
        ("GPT4All (GitHub)", "https://github.com/nomic-ai/gpt4all"),
        ("Locally AI (App Store)", "https://apps.apple.com/us/app/id6741426692"),
        ("Private LLM (App Store)", "https://apps.apple.com/us/app/id6448106860"),
        ("Enclave (App Store)", "https://apps.apple.com/us/app/id6476614556"),
        ("Pinku (App Store)", "https://apps.apple.com/us/app/id6754878073"),
        ("Guide to open-weight models (aisagalab.com)", AISAGALAB),
    ],
}

PAGES = [EN]
