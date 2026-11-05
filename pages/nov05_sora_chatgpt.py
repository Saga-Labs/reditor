"""Sora alternatives inside ChatGPT (video plugins), EN. Our app: Dora (its ChatGPT plugin).

Why this topic: Growth card ios-playbook#187 (5 Nov 2026), «Sora alternative in ChatGPT»; the Sora app is shutting down
(see pages/sora.py) and the best new Dora payers arrive through its ChatGPT plugin. Plugin listings and vendor pricing pages
were read on 2 Nov 2026 for reviewland.io/chatgpt-video-generator-plugins/; this page reuses those facts with its own order
and text, keeps that check date, and leaves out the two that do not generate scenes from a chat (Descript, an editor; Kling,
which needs a local Codex setup). Nothing installed, generated or paid for.
"""

D = "2026-11-05"
CHECKED = "2026-11-02"
OA = "https://openai.com/business/plugins/"
DORA = "https://chatgpt.com/plugins/plugin_asdk_app_6ac7e595853c8191baefac6a3a2b9c24"


def plugin(name, anchor, dev, url, best_for, facts, limits, row, ours=False, id_=None):
    a = {"name": name, "anchor": anchor, "developer": dev, "url": url, "best_for": best_for,
         "facts": facts, "limits": limits, "row": row}
    if ours:
        a["ours"] = True
        a["id"] = id_
    return a


PAGES = [{
    "group": "sora-chatgpt", "lang": "en", "store": "us",
    "path": "sora-alternatives-in-chatgpt/",
    "ct": "rd-sora-chatgpt",
    "category": "MultimediaApplication", "os": "ChatGPT", "link_label": "Plugin listing in ChatGPT",
    "checked_label": "Plugin listings and prices read on",
    "published": D, "updated": D, "checked": CHECKED,
    "title": "Sora Alternatives Inside ChatGPT (2026): 7 Video Plugins",
    "h1": "Sora alternatives you can use inside ChatGPT",
    "description": "With the Sora app shutting down, seven ChatGPT plugins that still make video from a chat, by what they make, free plan and cheapest price.",
    "llms": "Seven ChatGPT plugins that make video from a chat, as alternatives to Sora (whose app OpenAI is shutting down): Runway, OpenArt (Seedance, Wan, Minimax), Higgsfield, Dora AI Video, invideo, HeyGen and VEED, by what each makes, free plan and cheapest paid plan from each vendor's pricing page (read 2 Nov 2026). None was tested.",
    "llms_note": "Dora AI Video, one of the seven, is made by Saga Labs, which runs Reditor.",
    "answer": [
        "<strong>OpenAI is shutting down the Sora app, but you can still make videos without leaving ChatGPT</strong> by adding a video plugin: you connect the plugin's own account once, then ask for a clip in the chat and it comes back in the conversation. Each plugin bills through its own account, not through your ChatGPT plan.",
        "Closest to Sora's text-to-video: Runway (with a free 125-credit start) and OpenArt (pick a model such as Seedance or Wan). For an ad from a product photo, Higgsfield. For a short vertical clip from your own photo, paid per video, Dora AI Video. For a long video from one prompt, invideo. For a talking presenter, HeyGen or VEED. We read each listing and pricing page on 2 November 2026 and did not test the videos.",
    ],
    "columns": ["Plugin (as named in ChatGPT)", "Developer", "Makes", "Free plan (vendor site)", "Cheapest paid plan (vendor site)"],
    "table_note": "Listings and prices read on 2 November 2026 on each plugin's public listing and each vendor's pricing page, in US dollars. \"No free plan\" means the pricing page shows none.",
    "apps": [
        plugin("Runway", "runway", "Runway AI, Inc.", OA + "runway/",
               "the nearest thing to Sora's text to video, with editing in the same chat.",
               ["Its listing covers animating images, targeted edits to footage, new aspect ratios and multi-shot story videos.",
                "It also lists music, sound effects and voiceover.",
                "Pricing page: Free with 125 credits once; Standard $15 a month ($12 billed yearly); Pro $35, Max $95."],
               "the free credits are a one-off, and you need a Runway account.",
               ["Runway AI, Inc.", "Video, images, audio, multi-shot stories", "Yes: 125 credits once", "Standard $15 a month ($12 yearly)"]),
        plugin("OpenArt", "openart", "OpenArt Inc", OA + "openart/",
               "choosing the video model yourself.",
               ["The listing names Seedance 2.5 and 2.0, Minimax H3, Gemini Omni Flash and Wan 3.0, among others.",
                "Past work stays in projects; the result comes back into the chat.",
                "Pricing page: Starter $14 a month ($13 yearly) with 4,000 credits; Plus $34, Pro $56."],
               "no free plan on the pricing page, and no editing tools described.",
               ["OpenArt Inc", "Images and video from a choice of models", "No", "Starter $14 a month ($13 yearly)"]),
        plugin("Higgsfield", "higgsfield", "Higgsfield AI, Inc.", OA + "higgsfield/",
               "short ads made from a product photo.",
               ["Marketing Studio presets turn product photos into short video ads.",
                "Genjutsu copies the motion of a reference video or swaps the subject in a clip.",
                "Pricing page: Starter $19 a month with 270 credits; Plus $47, Ultra $99 billed yearly."],
               "built mostly around marketing.",
               ["Higgsfield AI, Inc.", "Images, videos, product ads, voiceovers", "Yes, limited", "Starter $19 a month"]),
        plugin("Dora AI Video", "dora", "Saga Labs", DORA,
               "a short vertical clip from your own photo, with the cost in coins shown before it generates.",
               ["Its listing says images arrive in about a minute and videos in about two.",
                "Vertical, horizontal or square, and the same character across a series of clips.",
                "The same account and coins work in the Dora iPhone app and on doravideo.com, and everything is saved to its gallery."],
               "short clips only, no free plan, and it does not post to social networks for you.",
               ["Saga Labs", "Short videos and images", "No", "Pro $2.99 the first week, then $4.99 a week; $119.99 a year"],
               ours=True, id_=6754180384),
        plugin("invideo", "invideo", "Invideo Inc", OA + "invideo/",
               "a longer video, with script, voiceover and music, from one prompt.",
               ["Its tagline is \"Create videos of any length\", and its sample prompt asks for a 5-minute video.",
                "Pricing page: Starter $20 a month ($10 yearly) with 400 credits; Plus $60, Max $250."],
               "no free plan on the pricing page, and no stated maximum length.",
               ["Invideo Inc", "Finished videos with script, voice and music", "No", "Starter $20 a month ($10 yearly)"]),
        plugin("HeyGen", "heygen", "HeyGen Technology Inc.", OA + "heygen/",
               "a talking avatar reading your script, or a translated video.",
               ["Videos, avatars, voices, translations and templates are managed from the chat.",
                "Pricing page: free with 3 watermarked videos a month up to 1 minute; Creator $29 a month ($24 yearly)."],
               "creating an avatar or a voice requires the rights and consent of the person, per its listing.",
               ["HeyGen Technology Inc.", "Talking-avatar videos", "Yes: 3 videos a month, watermarked", "Creator $29 a month ($24 yearly)"]),
        plugin("VEED Video Generator", "veed", "VEED", OA + "veed-video-generator/",
               "a presenter video with no camera, from a library of characters and voices.",
               ["You pick a character and a voice from VEED's library.",
                "Pricing page: Creator $20 a month ($10 yearly) with 6,000 credits and no watermark."],
               "the listing does not describe other video styles.",
               ["VEED", "Videos with a character and a voice", "Yes", "Creator $20 a month ($10 yearly)"]),
    ],
    "who": [
        "<strong>Text to video like Sora:</strong> Runway, or OpenArt to pick the model.",
        "<strong>An ad from a product photo:</strong> Higgsfield.",
        "<strong>A short clip from your photo, paid per video:</strong> Dora AI Video.",
        "<strong>A long video from one prompt:</strong> invideo.",
        "<strong>A presenter reading a script:</strong> HeyGen or VEED.",
    ],
    "cases": ["A vertical clip for Reels or TikTok from one photo.", "A product ad without a shoot.", "A narrated explainer from a written brief."],
    "method": [
        "On 2 November 2026 we read each plugin's public listing (on openai.com, and for Dora AI Video its ChatGPT directory listing) and each vendor's pricing page. We left out Descript, a video editor, and Kling AI, whose plugin needs a local Codex setup. We did not install a plugin, generate a video or pay for anything.",
        "The order follows how close each plugin is to Sora's \"describe it and get a clip\" use, not video quality. Prices change often: check inside each plugin before paying.",
    ],
    "faq": [
        ("Can I still make videos in ChatGPT without Sora?",
         "Yes. Add a video plugin such as Runway, OpenArt or Dora AI Video, connect its account, and ask for a video in the chat."),
        ("Which ChatGPT video plugin is free?",
         "On 2 November 2026 Runway (125 credits once), Higgsfield, HeyGen (3 watermarked videos a month) and VEED showed free plans. OpenArt, invideo and Dora AI Video did not."),
        ("Does a video plugin use my ChatGPT subscription?",
         "No. Each plugin bills through its own account; OpenAI says availability depends on the plugin, your plan and your workspace."),
        ("Which one makes the best videos?",
         "We did not test them. Try the same short prompt in two plugins on their free or smallest plan."),
    ],
    "sources": [
        ("Engadget, OpenAI is shutting down its Sora video generation app", "https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html"),
        ("OpenAI: plugins", OA),
        ("Runway pricing", "https://runway.com/pricing"),
        ("OpenArt pricing", "https://openart.ai/pricing"),
        ("Higgsfield pricing", "https://higgsfield.ai/pricing"),
        ("Dora AI Video in ChatGPT", DORA),
        ("Dora pricing", "https://doravideo.com/pricing"),
        ("invideo pricing", "https://invideo.io/pricing"),
        ("HeyGen pricing", "https://www.heygen.com/pricing"),
        ("VEED pricing", "https://www.veed.io/pricing"),
        ("Reviewland: all nine ChatGPT video plugins compared", "https://reviewland.io/chatgpt-video-generator-plugins/"),
    ],
}]
