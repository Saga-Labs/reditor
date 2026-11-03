"""ChatGPT image generator alternatives for iPhone, EN. Our app: Dora (id6754180384), which lists OpenAI's GPT-4o Image and ChatGPT 2 (GPT-Image-2) and Google's Nano Banana models on doravideo.com/models.

Checked 2026-11-03: US App Store search for «gpt image», «chatgpt image», «microsoft copilot», iTunes lookup and the US
App Store page of every app (price list, privacy label), and doravideo.com/models for Dora. Only apps whose listing
says they make or edit images (Microsoft Copilot is left out: its listing talks about reading images, not making
them). Ask AI is not listed: it reads photos but does not make images. Why this topic: Google suggests «chatgpt image
alternative», «... free», «chatgpt alternative image generator», «chatgpt alternative image editor» (3 Nov); no page
on the 4 sites covers it. Overlaps partly with /midjourney-alternatives-iphone/ and /nano-banana-apps-iphone/ (same
apps for different questions; each page links the others). Registered in ios-playbook references/temas-webs.md.
No quality test, nothing generated.
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
LN = "Data Linked to You; Data Not Linked to You"

PAGES = [{
    "group": "chatgpt-image", "lang": "en", "store": "us",
    "path": "chatgpt-image-alternatives-iphone/",
    "ct": "rd-chatgpt-image-alt-iphone",
    "category": "GraphicsDesignApplication",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "ChatGPT Image Generator Alternatives for iPhone (2026): 6 Apps",
    "h1": "Best ChatGPT image generator alternatives for iPhone in 2026",
    "description": "Six iPhone apps that make and edit images from a description like ChatGPT: Gemini, Ideogram, Adobe Firefly, Dora, Chat Smith and ChatNow, by price and model.",
    "llms": "Compares six iPhone alternatives to ChatGPT's image generator, apps whose listings say they make or edit images from a description: Google Gemini (Nano Banana 2), Ideogram (text in images), Adobe Firefly (licensed Adobe models plus OpenAI and Google partner models), Dora (GPT Image and Nano Banana per coin), Chat Smith (GPT-Image 2.5) and ChatNow (GPT Image 2 and Nano Banana Pro), by price, image model and App Store privacy label.",
    "answer": [
        "<strong>ChatGPT makes images from a description and changes uploaded ones «with a few simple words», per its App Store listing</strong>; its plans are Go at $8 a month, Plus at $19.99 and Pro from $100 (US App Store, 3 November 2026). If you want another app for that, the six below do the same job in different ways.",
        "Google Gemini edits and makes photos with Nano Banana 2. Ideogram is built for readable text in images, such as logos and posters. Adobe Firefly offers Adobe's own models, trained on licensed content per Adobe, plus partner models from OpenAI and Google. Dora, Chat Smith and ChatNow let you use OpenAI's image models outside ChatGPT: Dora's model page lists GPT-4o Image and ChatGPT 2 (GPT-Image-2) at 6 coins an image, next to Nano Banana. For more image apps by style, see our <a href=\"/midjourney-alternatives-iphone/\">Midjourney alternatives</a> and <a href=\"/nano-banana-apps-iphone/\">Nano Banana apps</a>.",
    ],
    "columns": ["App", "Price (US)", "Image model, per its listing", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are in-app purchases listed on each US App Store page on 3 November 2026; pages list only some. All are free to download. Ratings are that day's App Store average and count.",
    "apps": [
        app("Google Gemini", 6477489729, "gemini", "Google LLC", 4.73, 2393415,
            "editing a photo by describing the change, with Google's Nano Banana 2.",
            ["Its listing names Nano Banana 2 for making and editing photos: camera and lighting controls, mockups that blend several images, posters with sharp text and diagrams.",
             "Also an assistant that connects Gmail, Calendar, Google Photos and YouTube.",
             "In 70 languages."],
            "the listing does not say which plan includes image generation, and the paid plans bundle cloud storage you may not need.",
            ["Google AI Plus $4.99, Pro $19.99, Ultra $199.99 a month; storage from $1.99",
             "Nano Banana 2",
             "70", "Data Linked to You", "1.2026.4262206 (29 Oct 2026)"]),
        app("Ideogram AI - Image Generator", 6476790495, "ideogram", "Ideogram AI Inc", 4.78, 2690,
            "logos, posters and any image whose words must be spelled right.",
            ["Stylized text and precise composition, per its listing, plus a logo maker.",
             "An editor with generative fill, new aspect ratios and background removal; AI headshots and face swap from one photo.",
             "Free weekly credits to start, per its listing."],
            "English only, images only (no video), and paid plans start at $11.99 a month.",
            ["Basic $11.99, Plus $28.99, Pro $85.99 a month (yearly $119.99 to $829.99)",
             "Ideogram's own models",
             "1", LN, "2026.41 (24 Oct 2026)"]),
        app("Adobe Firefly AI Video & Photo", 6742595426, "firefly", "Adobe Inc.", 4.69, 11210,
            "commercial work, with Adobe's licensed models and OpenAI's and Google's in one app.",
            ["Adobe says its own Firefly models are trained on licensed content.",
             "Its listing names partner models from Adobe, Google, OpenAI, Luma and Runway.",
             "Also video, sound and background removal, in 27 languages."],
            "credits are bought on top of the plan, and partner models use more of them.",
            ["Firefly Mobile $4.99 a month or $49.99 a year; credits $4.99 to $499.99",
             "Adobe Firefly models plus OpenAI and Google partner models",
             "27", LN, "26.19.0 (28 Oct 2026)"]),
        app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16,
            "OpenAI's and Google's image models side by side, paying per image in coins, with video from the same coins.",
            ["doravideo.com/models lists GPT-4o Image (6 coins, best for readable text) and ChatGPT 2, which it describes as GPT-Image-2 (6 coins), next to Nano Banana (4), Nano Banana 2 (10) and Nano Banana Pro (18).",
             "Images from a description or a reference photo, back in about a minute, per its App Store listing.",
             "The coin cost shows before you generate, failed generations refund the coins, and the same coins work on doravideo.com and in Claude and ChatGPT."],
            "its App Store listing does not name these models (the list is on its website), OpenAI's models there are standard resolution, and there are no free images: coins need the Pro plan.",
            ["Pro weekly $4.99 or $6.99, yearly $119.99; coin packs $3.99 to $224.99",
             "GPT-4o Image, GPT-Image-2 and Nano Banana, per doravideo.com/models",
             "11", "Data Used to Track You; Data Not Linked to You", "1.4.2 (26 Oct 2026)"], ours=True),
        app("Chat Smith: AI Chatbot & Agent", 1559479889, "chat-smith", "CHAT SMITH OPCO PTE. LTD", 4.58, 166659,
            "OpenAI's newest image model named in a listing, GPT-Image 2.5, inside a chat app.",
            ["Its listing says its image generator is powered by OpenAI GPT-Image 2.5 and Gemini Nano Banana Pro, from text or from a photo.",
             "Also a chat app with GPT, Claude, Gemini, DeepSeek and Grok, an AI logo maker and an AI detector.",
             "A lifetime purchase is listed at $99.99."],
            "a large download (725 MB), and its privacy label includes Data Used to Track You and Data Linked to You.",
            ["Pro weekly $4.99 or $6.99, monthly $6.99 or $9.99, yearly $39.99 or $69.99; lifetime $99.99",
             "GPT-Image 2.5 and Nano Banana Pro",
             "10", T3, "9.261026.1 (29 Oct 2026)"]),
        app("AI Chat Assistant – ChatNow", 1667518571, "chatnow", "Tappz GmbH", 4.80, 146222,
            "images and video next to 30+ chat models under one subscription.",
            ["Its listing names GPT Image 2, Nano Banana Pro, Nano Banana 2 and Flux for images, and says you can edit photos too.",
             "Also short videos with Veo 3.1, Sora 2 and Kling 2.1.",
             "Ask several chat models the same question and compare answers."],
            "it needs iOS 26, and the plans range widely ($6.99 to $79.99 listed).",
            ["Plus from $6.99 to $79.99 listed, yearly $59.99; credits $9.99 or $19.99",
             "GPT Image 2, Nano Banana Pro and 2, Flux",
             "13", "Data Used to Track You; Data Not Linked to You", "5.13 (24 Oct 2026)"]),
    ],
    "who": [
        "<strong>Editing photos by describing the change:</strong> Google Gemini.",
        "<strong>Readable words in the image:</strong> Ideogram.",
        "<strong>Commercial work with licensed models:</strong> Adobe Firefly.",
        "<strong>OpenAI and Google models per image, cost shown first:</strong> Dora.",
        "<strong>GPT-Image 2.5 inside a chat app:</strong> Chat Smith.",
        "<strong>Images, video and chat in one subscription:</strong> ChatNow.",
    ],
    "cases": ["A poster or social image with text.", "Changing the background or style of your own photo.", "Making images when you have hit ChatGPT's limit."],
    "method": [
        "On 3 November 2026 we searched the US App Store for «gpt image», «chatgpt image» and «microsoft copilot», and read ChatGPT's and each app's US App Store page and Apple's lookup data. We only included apps whose listing says they make or edit images; for Dora, whose listing does not name its models, we used its own model page. We ran no quality test.",
        "Microsoft Copilot is not listed because its App Store listing talks about reading images, not making them.",
        "Prices change often. Check inside each app before paying.",
    ],
    "faq": [
        ("Which apps use OpenAI's image models outside ChatGPT?",
         "Of the listings we read, Chat Smith names GPT-Image 2.5, ChatNow names GPT Image 2, and Adobe Firefly names OpenAI among its partner models. Dora lists GPT-4o Image and GPT-Image-2 on its model page."),
        ("Which alternative is best for text inside images?",
         "Ideogram, whose listing is built around stylized, readable text. Dora's model page also recommends its GPT-4o Image model for signs, posters and other images with words."),
        ("Is there a free alternative?",
         "Ideogram's listing mentions free weekly credits. The others list paid plans or credits; check each app for a free tier."),
        ("Can these apps edit a photo I upload?",
         "Yes: Gemini, Ideogram, Firefly, Chat Smith and ChatNow describe photo editing in their listings, and Dora accepts a reference photo."),
    ],
    "sources": [
        ("ChatGPT (App Store)", "https://apps.apple.com/us/app/id6448311069"),
        ("Google Gemini (App Store)", "https://apps.apple.com/us/app/id6477489729"),
        ("Ideogram (App Store)", "https://apps.apple.com/us/app/id6476790495"),
        ("Adobe Firefly (App Store)", "https://apps.apple.com/us/app/id6742595426"),
        ("DORA · AI Video Generator (App Store)", "https://apps.apple.com/us/app/id6754180384"),
        ("Dora models and costs", "https://doravideo.com/models"),
        ("Chat Smith (App Store)", "https://apps.apple.com/us/app/id1559479889"),
        ("AI Chat Assistant – ChatNow (App Store)", "https://apps.apple.com/us/app/id1667518571"),
    ],
}]
