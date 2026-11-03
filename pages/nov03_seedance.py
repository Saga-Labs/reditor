"""Seedance app alternatives for iPhone, EN. Our app: Dora (default model Seedance 2 Mini, per doravideo.com/models).
Checked 2026-11-02: US App Store search for «seedance», «seedance 2» and «seedance app» (saga-growth
data/aso-seedance-2026-11-02.json), iTunes lookup and US App Store pages for every app, seed.bytedance.com and
CapCut's newsroom. No quality test, nothing generated. Encargo de saga-growth, 2 nov, para el 3 nov."""

import pages.nov02_alts as _alts
from pages.nov02_alts import A as A2, FACTS as F2, LIMITS as L2, NOTE, METHOD, page, RELATED

D = "2026-11-03"
T3 = "Data Used to Track You; Data Linked to You; Data Not Linked to You"


def app(name, id_, anchor, dev, rating, count, price, langs, priv, ver):
    return {"name": name, "id": id_, "anchor": anchor, "developer": dev, "rating": (rating, count),
            "_row": (price, str(langs), priv, ver, f"{rating:.1f} ({count:,} ratings)")}


A = {
    "dora": A2["dora"], "runway": A2["runway"], "kling": A2["kling"],
    "capcut": app("CapCut: Photo & Video Editor", 1500855883, "capcut", "BYTEDANCE PTE. LTD.", 4.61, 1125712,
                  "Monthly plans listed from $7.99 to $19.99 (Standard $9.99, Pro $19.99), yearly $89.99",
                  20, "Data Used to Track You; Data Linked to You", "19.9.0 (27 Oct 2026)"),
    "sd2": app("SD2 AI Video Generator", 6748974690, "sd2", "PEPR AI Limited", 4.71, 188,
               "Weekly $8.99 or $17.99, monthly $23.99, yearly $39.99 to $199.99; credit packs $29.99 to $199.99",
               17, "Data Not Collected", "1.9.4 (22 Oct 2026)"),
    "dreamina": app("Dreamina AI: Image&Video Maker", 6749606485, "dreamina", "BYTEDANCE PTE. LTD.", 3.07, 44,
                    "Basic $15 a month, Standard $36, Advanced $79; credit packs $10 to $179.99",
                    1, T3, "2.1.3 (30 Oct 2026)"),
}

FACTS = {
    "dora": ["Its default video model is Seedance 2 Mini from ByteDance, with sound, up to 12 seconds and up to 720p, per doravideo.com/models. Seedance 2 and Seedance 2 Fast are also listed there, next to Kling 2.6, Gemini Omni and Grok.",
             "Starts from a photo or a written description. The coin cost shows before you generate, and failed generations refund the coins.",
             "The same account and coins work on doravideo.com and in AI assistants through its connector."],
    "capcut": ["Made by ByteDance, the company behind Seedance. CapCut's newsroom says Dreamina Seedance 2.0 reached CapCut users in the US on 7 April 2026, starting with paid users.",
               "That page gives clips up to 15 seconds in 6 aspect ratios, inside a full video editor with captions, keyframes and effects."],
    "runway": F2["runway"],
    "sd2": ["Its listing names Seedance 2.0 among its engines, next to Sora 2 Pro, Veo 3.1, Kling 3.0 and Runway.",
            "Text to video and image to video, with optional first and last frames to guide the shot."],
    "kling": F2["kling"],
    "dreamina": ["ByteDance's own image and video generator (its terms are on dreamina.capcut.com), with reference images, AI editing and a community feed.",
                 "CapCut's newsroom said in April 2026 that Seedance 2.0 would come to Dreamina AI; the App Store listing itself does not name the model."],
}

LIMITS = {
    "dora": "Seedance 2 Mini stops at 720p (higher resolutions need another model), no free video, and no timeline editing of long videos.",
    "capcut": "the App Store listing does not say which plan includes Seedance, and CapCut says it labels AI content with visible watermarks.",
    "runway": L2["runway"],
    "sd2": "a third-party app: its listing does not say how it reaches these models, and two weekly plans are listed ($8.99 and $17.99).",
    "kling": L2["kling"],
    "dreamina": "English only, the lowest average rating here (3.1), and its listing does not name Seedance.",
}

# page() reads the dicts of nov02_alts: add only the new apps there, then set Dora's Seedance text on this page alone.
NEW = ("capcut", "sd2", "dreamina")
_alts.A.update({k: A[k] for k in NEW})
_alts.FACTS.update({k: FACTS[k] for k in NEW})
_alts.LIMITS.update({k: LIMITS[k] for k in NEW})

SEEDANCE = page("seedance-app-alternatives-iphone", "rd-seedance-app-alternatives-iphone",
    "Seedance App for iPhone: Real Options and Alternatives (2026)", "Seedance app alternatives for iPhone in 2026",
    "There is no app called Seedance from ByteDance on the US App Store. Six iPhone apps that use Seedance or do the same job: CapCut, Runway, SD2, Dora, Kling, Dreamina.",
    "Notes that on 2 November 2026 no app called Seedance from ByteDance appeared on the US App Store, names apps that use the Seedance name and are not from ByteDance, and compares six iPhone options (CapCut, Runway, SD2 AI Video Generator, Dora, Kling AI, Dreamina AI) by price, model and App Store privacy label.",
    ["<strong>There is no app called Seedance from ByteDance on the US App Store.</strong> Seedance is a video model made by ByteDance Seed (<a href=\"https://seed.bytedance.com/en/seedance\">seed.bytedance.com</a>). On 2 November 2026, a US App Store search for «seedance app» showed apps that use the Seedance name and are not from ByteDance, going by the developer shown on each App Store page: <a href=\"https://apps.apple.com/us/app/id6776995890\">速影AI-seedance 2.5</a> (Nanjing Yanmao Information Technology), <a href=\"https://apps.apple.com/us/app/id6758517479\">Seadance-AI特效视频生成2.0极速版</a> (individual developer), <a href=\"https://apps.apple.com/us/app/id6754003115\">纳米P视频 - Seedance2.0版</a> (Beijing Qihoo Technology) and, searching «seedance», <a href=\"https://apps.apple.com/us/app/id6770917609\">Seedenca AI</a> (individual developer). We cannot confirm what model any of them runs. Their listings are in Chinese, except Seedenca AI, whose listing does not mention Seedance at all.",
     "ByteDance's own route on iPhone is CapCut: <a href=\"https://www.capcut.com/newsroom/dreamina-seedance-2\">CapCut's newsroom</a> says Dreamina Seedance 2.0 reached the US on 7 April 2026. Runway lists Seedance 2.5 among its models, and SD2 lists Seedance 2.0. Dora uses Seedance 2 Mini by default. Kling AI is a rival model family, in its own app."],
    ["capcut", "runway", "sd2", "kling", "dreamina"],
    dict(dora="Short clips on Seedance 2 Mini by default, cost shown first", capcut="Seedance from ByteDance inside a full editor", runway="Seedance 2.5 next to Kling 3 Pro and Gen-4.5", sd2="Seedance 2.0 next to Sora 2 Pro and Veo 3.1", kling="A rival model family, up to 4K", dreamina="ByteDance's generator app; listing does not name Seedance"),
    dict(dora="someone who wants a short clip with sound on a Seedance model and to see the coin cost before tapping.",
         capcut="people who want ByteDance's own route to Seedance and to keep editing the clip afterwards.",
         runway="people who want Seedance 2.5 and other models in the same app.",
         sd2="people who want to switch between Seedance, Sora and Veo in one app.",
         kling="people open to a different model with stated length and 4K.",
         dreamina="people who want ByteDance's generator and can check inside the app which model it offers."),
    ["<strong>From ByteDance itself:</strong> CapCut.", "<strong>Seedance 2.5:</strong> Runway, whose listing names it.", "<strong>Seedance plus Sora and Veo in one app:</strong> SD2.", "<strong>A short clip on Seedance 2 Mini, cost first:</strong> Dora.", "<strong>A different model, up to 4K:</strong> Kling AI."],
    ["A short clip with sound from a written idea.", "Animating a photo.", "Telling apps from ByteDance apart from apps that only use the name."],
    [("Is there an official Seedance app for iPhone?", "Not under that name. On 2 November 2026 we found no app called Seedance from ByteDance on the US App Store. ByteDance offers the model in CapCut, according to CapCut's newsroom, and through BytePlus for developers, according to seed.bytedance.com."),
     ("Is 速影AI-seedance 2.5 or 纳米P视频 an official Seedance app?", "Their developers are Nanjing Yanmao Information Technology and Beijing Qihoo Technology, not ByteDance. We cannot tell which model they run. Check the developer name before paying."),
     ("Which iPhone apps name Seedance 2.5 or 2.0?", "Of the listings we read on 2 November 2026, Runway names Seedance 2.5 and SD2 names Seedance 2.0. CapCut's newsroom describes Dreamina Seedance 2.0. Models change often, so check inside the app."),
     ("What is Seedance 2 Mini?", "A lighter Seedance 2 model from ByteDance. Dora's model page lists it with sound, up to 12 seconds and up to 720p, as Dora's default.")],
    [("Seedance, ByteDance Seed", "https://seed.bytedance.com/en/seedance"),
     ("Dreamina Seedance 2.0, CapCut newsroom", "https://www.capcut.com/newsroom/dreamina-seedance-2"),
     ("Dora models", "https://doravideo.com/models"),
     ("速影AI-seedance 2.5 (App Store)", "https://apps.apple.com/us/app/id6776995890"),
     ("纳米P视频 - Seedance2.0版 (App Store)", "https://apps.apple.com/us/app/id6754003115"),
     ("Seadance-AI特效视频生成2.0极速版 (App Store)", "https://apps.apple.com/us/app/id6758517479"),
     ("Seedenca AI: Video Creator (App Store)", "https://apps.apple.com/us/app/id6770917609")])
SEEDANCE.update(group="seedance-alt", published=D, updated=D, checked="2026-11-02",
                related=list(RELATED))
_dora = next(a for a in SEEDANCE["apps"] if a.get("ours"))
_dora.update(facts=FACTS["dora"], limits=LIMITS["dora"])

PAGES = [SEEDANCE]
