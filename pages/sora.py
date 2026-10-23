"""Sora app alternatives on iPhone. EN + ES. Our app: Dora (id6754180384).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES). The Sora app page (id6744034028) returns 404 and the lookup
API returns nothing. Shutdown announced by OpenAI on 24 March 2026 (Engadget).
"""

CHECKED = "2026-10-11"
ENGADGET = "https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html"


def src(cc):
    return [
        ("Engadget, OpenAI is shutting down its Sora video generation app", ENGADGET),
        ("Sora by OpenAI, App Store page (returns 404)", f"https://apps.apple.com/{cc}/app/id6744034028"),
        ("DORA (App Store)", f"https://apps.apple.com/{cc}/app/id6754180384"),
        ("Kling AI (App Store)", f"https://apps.apple.com/{cc}/app/id6738049229"),
        ("Grok (App Store)", f"https://apps.apple.com/{cc}/app/id6670324846"),
        ("Google Gemini (App Store)", f"https://apps.apple.com/{cc}/app/id6477489729"),
        ("CapCut (App Store)", f"https://apps.apple.com/{cc}/app/id1500855883"),
    ]


EN = {
    "group": "sora", "lang": "en", "store": "us",
    "path": "sora-app-alternatives-iphone/",
    "ct": "rd-sora",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Sora app alternatives for iPhone video makers (2026)",
    "h1": "Best Sora app alternatives for iPhone in 2026",
    "description": "The Sora app is gone. Five iPhone apps that still make AI videos from a photo or text, compared: Dora, Kling AI, Grok and more. Prices checked.",
    "llms": "OpenAI's Sora app is no longer on the App Store; compares five iPhone apps for AI video (Dora, Kling AI, Grok Imagine, Gemini, CapCut) by price, length and resolution, and privacy label.",
    "disclosure": "Dora is made by Saga Labs, the company behind Reditor. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "The Sora app is gone: OpenAI announced on 24 March 2026 that it was shutting it down, and on 11 October 2026 its App Store page no longer opens. To make AI videos from a photo or a prompt on iPhone now, Dora (ours) gives you several video models in one app with the coin cost shown before you generate, and Kling AI is the strongest single-model option, with clips up to 15 seconds that can be extended to 3 minutes.",
        "If you already pay for an AI assistant, Grok (Grok Imagine) and Google Gemini (Gemini Omni, on paid Google AI plans) also make short videos inside the chat app.",
    ],
    "columns": ["App", "Price (US)", "What it makes", "Account", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the in-app purchases listed on each US App Store page on 11 October 2026; all five are free to download. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "DORA · AI Video Generator", "id": 6754180384, "ours": True, "anchor": "dora",
            "developer": "Saga Ltd.", "rating": (4.27, 15),
            "row": ["Subscription: $4.99 or $9.99 a week, $119.99 a year; coin packs from $2.99", "Video from a photo or text, dance copy (Motion Control), product ads, images up to 4K",
                    "Yes; same account on doravideo.com and in Claude and ChatGPT", "Data Used to Track You; Data Not Linked to You", "1.4.1 (9 Oct 2026)", "4.3 (15 ratings)"],
            "best_for": "people who want Sora-style clips from a photo or a sentence, ready for TikTok and Reels, without picking a model provider.",
            "facts": [
                "Several video models in one app; each generation shows its coin cost before you tap, and failed generations refund the coins.",
                "Vertical 9:16, horizontal or square, up to 1080p, no watermark. Some models add sound.",
                "Motion Control copies the moves of a dance video onto the person in your photo.",
                "A video takes about two minutes, an image about one.",
                "11 languages, iOS 18.6 or later, 61 MB.",
            ],
            "limits": "it is a paid subscription, it has only 15 ratings in the US so far, and its privacy label includes data used to track you. It does not edit long videos on a timeline.",
        },
        {
            "name": "Kling AI: AI Image & Video Maker", "id": 6738049229, "anchor": "kling",
            "developer": "KLING AI PTE. LTD.", "rating": (4.68, 31607),
            "row": ["Credits from $5 (330); plans $10, $37 or $92 a month", "Video from text or images, up to 15 s in 1080p or 4K, extendable to 3 min",
                    "Yes", "Data Used to Track You; Data Linked to You; Data Not Linked to You", "3.8.20 (11 Sep 2026)", "4.7 (31,607 ratings)"],
            "best_for": "longer or higher-resolution clips from one top video model.",
            "facts": [
                "Native 1080p or 4K clips up to 15 seconds; Video Extension takes them to 3 minutes.",
                "Image generation in 4K with several reference images.",
                "Clone & Try: reuse a prompt from another creator's video.",
                "5 languages, iOS 14 or later, 237 MB.",
            ],
            "limits": "credits run out quickly on long or 4K clips, and the privacy label includes data used to track you.",
        },
        {
            "name": "Grok (Grok Imagine)", "id": 6670324846, "anchor": "grok",
            "developer": "X Corp.", "rating": (4.87, 1497069),
            "row": ["SuperGrok Lite $10, SuperGrok $30, Plus $100, Heavy $300; extra credits from $5", "Images, short videos with sound, photo to video, inside a chat assistant",
                    "Yes", "Data Linked to You", "1.4.51 (9 Oct 2026)", "4.9 (1,497,069 ratings)"],
            "best_for": "people who already use Grok and want quick clips without another app.",
            "facts": [
                "Grok Imagine makes images from text or voice and short videos with sound, or animates a photo.",
                "Also a general AI assistant for chat, research and coding.",
                "38 languages, iOS 17 or later, 186 MB. Rated 17+.",
            ],
            "limits": "video is one feature of a chat app, without templates for social formats, and the listing does not say how many videos each plan includes.",
        },
        {
            "name": "Google Gemini (Gemini Omni)", "id": 6477489729, "anchor": "gemini",
            "developer": "Google LLC", "rating": (4.72, 2330532),
            "row": ["Video needs Google AI Plus ($4.99), Pro ($19.99) or Ultra ($199.99), or Workspace", "Cinematic videos from your ideas with Gemini Omni, inside the Gemini assistant",
                    "Google account", "Data Linked to You", "1.2026.3970207 (7 Oct 2026)", "4.7 (2,330,532 ratings)"],
            "best_for": "people who already pay for a Google AI plan.",
            "facts": [
                "The listing says Gemini Omni turns ideas into cinematic videos for Google AI Plus, Pro, Ultra and Workspace users.",
                "The same plans include Google storage (400 GB to 30 TB).",
                "70 languages, iOS 17.4 or later, 391 MB.",
            ],
            "limits": "video is not available on the free plan, and it is one feature of a general assistant.",
        },
        {
            "name": "CapCut: Photo & Video Editor", "id": 1500855883, "anchor": "capcut",
            "developer": "BYTEDANCE PTE. LTD.", "rating": (4.61, 1123502),
            "row": ["Standard $9.99 a month, Pro $19.99 a month, yearly $89.99", "Video editing: keyframes, auto captions, effects, 4K 60fps export",
                    "Optional", "Data Used to Track You; Data Linked to You", "19.7.0 (8 Oct 2026)", "4.6 (1,123,502 ratings)"],
            "best_for": "finishing an AI clip: cutting, captions, music and effects before you post.",
            "facts": [
                "Trim, split and merge clips, speed curves, chroma key and stabilisation.",
                "Auto captions, text-to-speech, motion tracking and background removal.",
                "20 languages, iOS 15 or later, 824 MB. Also on Mac.",
            ],
            "limits": "its App Store listing describes editing tools, not generating a video from a prompt the way Sora did, so it complements the apps above rather than replacing them.",
        },
    ],
    "who": [
        "<strong>You used Sora to animate photos or write prompts for short clips:</strong> Dora (ours) or Kling AI.",
        "<strong>You want 4K or clips longer than 15 seconds:</strong> Kling AI.",
        "<strong>You already pay for an assistant:</strong> Grok (SuperGrok) or Gemini (Google AI Plus or higher).",
        "<strong>You also use the web or Claude and ChatGPT:</strong> Dora, whose account and coins work on doravideo.com and in those assistants.",
        "<strong>You need to edit and caption the result:</strong> CapCut, after any of the above.",
    ],
    "cases": [
        "Bringing an old photo to life as a short video.",
        "A vertical clip for TikTok, Instagram Reels or YouTube Shorts from one sentence.",
        "A product video or ad for a shop or an app.",
        "Copying a trending dance onto your own photo (Dora's Motion Control).",
    ],
    "method": [
        "On 11 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchase prices, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. What each app makes is taken from its own App Store description. We did not invent ratings or reviews.",
        "The Sora app's App Store page (id6744034028) returned \"not found\" that day. The shutdown date comes from Engadget's report of OpenAI's announcement.",
    ],
    "faq": [
        ("Is the Sora app still available on iPhone?",
         "No. OpenAI announced on 24 March 2026 that it was shutting down the Sora app, and on 11 October 2026 its App Store page no longer opens."),
        ("What is the best Sora alternative on iPhone?",
         "For short videos from a photo or a prompt, Dora (ours, several models in one app) and Kling AI (up to 15 seconds in 1080p or 4K, extendable to 3 minutes). Grok and Gemini also make videos if you pay for their plans."),
        ("Is there a free Sora alternative?",
         "All five apps are free to download, but video generation is paid in each: Dora by subscription and coins, Kling AI by credits or plans, Gemini only on Google AI Plus or higher, Grok through SuperGrok plans and credits."),
        ("Can I turn a photo into a video on iPhone without Sora?",
         "Yes. Dora, Kling AI and Grok Imagine all animate a photo into a short video."),
        ("Which Sora alternative works for TikTok and Reels?",
         "Dora exports vertical 9:16 up to 1080p with no watermark. CapCut is useful afterwards to add captions and music."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "sora", "lang": "es", "store": "es",
    "path": "es/alternativas-a-sora-iphone/",
    "ct": "rd-sora-es",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores alternativas a Sora para hacer vídeos con IA en iPhone (2026)",
    "h1": "Mejores alternativas a la app de Sora en iPhone en 2026",
    "description": "La app de Sora ya no existe. Cinco apps de iPhone que hacen vídeos con IA desde una foto o un texto: Dora, Kling AI, Grok y más. Precios comprobados.",
    "llms": "La app de Sora ya no está en el App Store; compara cinco apps de iPhone para vídeo con IA (Dora, Kling AI, Grok Imagine, Gemini, CapCut) por precio en euros, duración y resolución, y privacidad.",
    "disclosure": "Dora es de Saga Labs, la empresa que hace Reditor. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "La app de Sora ya no existe: OpenAI anunció el 24 de marzo de 2026 que la cerraba, y el 11 de octubre de 2026 su ficha del App Store ya no abre. Para hacer vídeos con IA desde una foto o un texto en el iPhone, Dora (nuestra) junta varios modelos de vídeo en una app y enseña el coste en monedas antes de generar, y Kling AI es la mejor opción de un solo modelo, con clips de hasta 15 segundos que se pueden alargar a 3 minutos.",
        "Si ya pagas un asistente de IA, Grok (Grok Imagine) y Google Gemini (Gemini Omni, con los planes de pago de Google AI) también hacen vídeos cortos dentro del chat.",
    ],
    "columns": ["App", "Precio (España)", "Qué hace", "Cuenta", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app que muestra cada ficha del App Store de España el 11 de octubre de 2026; las cinco se descargan gratis. Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "DORA · Generador Vídeo IA", "id": 6754180384, "ours": True, "anchor": "dora",
            "developer": "Saga Ltd.",
            "row": ["Suscripción: 7,99 € a la semana o 129,99 € al año; packs de monedas desde 2,99 €", "Vídeo desde una foto o un texto, copiar un baile (Motion Control), anuncios de producto, imágenes hasta 4K",
                    "Sí; la misma cuenta sirve en doravideo.com y en Claude y ChatGPT", "Datos utilizados para rastrearte; datos no vinculados a ti", "1.4.1 (9 oct 2026)", "Aún sin valoraciones en España"],
            "best_for": "quien quiere clips al estilo de Sora desde una foto o una frase, listos para TikTok y Reels, sin elegir proveedor de modelos.",
            "facts": [
                "Varios modelos de vídeo en una app; cada generación enseña su coste en monedas antes de pulsar, y si falla se devuelven.",
                "Vertical 9:16, horizontal o cuadrado, hasta 1080p y sin marca de agua. Algunos modelos añaden sonido.",
                "Motion Control copia los movimientos de un vídeo de baile en la persona de tu foto.",
                "Un vídeo tarda unos dos minutos y una imagen, uno.",
                "11 idiomas, iOS 18.6 o posterior, 61 MB.",
            ],
            "limits": "es una suscripción de pago, todavía no tiene valoraciones en España y su etiqueta de privacidad incluye datos para rastrearte. No edita vídeos largos en una línea de tiempo.",
        },
        {
            "name": "Kling AI: AI Image&Video Maker", "id": 6738049229, "anchor": "kling",
            "developer": "KLING AI PTE. LTD.", "rating": (4.62, 1687),
            "row": ["Créditos desde 6 € (330); planes de 10 €, 39 €, 99 € o 199,99 € al mes", "Vídeo desde texto o imágenes, hasta 15 s en 1080p o 4K, ampliable a 3 min",
                    "Sí", "Datos utilizados para rastrearte; datos vinculados a ti; datos no vinculados a ti", "3.8.20 (11 sep 2026)", "4,6 (1.687 valoraciones)"],
            "best_for": "clips más largos o con más resolución con un único modelo puntero.",
            "facts": [
                "Clips de hasta 15 segundos en 1080p o 4K; con Video Extension llegan a 3 minutos.",
                "Imágenes en 4K con varias imágenes de referencia.",
                "Clone & Try: reutilizar la idea del vídeo de otro creador.",
                "5 idiomas, iOS 14 o posterior, 237 MB.",
            ],
            "limits": "los créditos se gastan rápido con clips largos o en 4K, y su etiqueta incluye datos para rastrearte.",
        },
        {
            "name": "Grok (Grok Imagine)", "id": 6670324846, "anchor": "grok",
            "developer": "X Corp.", "rating": (4.81, 72312),
            "row": ["SuperGrok Lite 10 €, SuperGrok 35 €, Plus 100 €, Heavy 349 €; créditos extra desde 6 €", "Imágenes, vídeos cortos con sonido y foto a vídeo, dentro de un asistente",
                    "Sí", "Datos vinculados a ti", "1.4.51 (9 oct 2026)", "4,8 (72.312 valoraciones)"],
            "best_for": "quien ya usa Grok y quiere clips rápidos sin otra app.",
            "facts": [
                "Grok Imagine hace imágenes desde texto o voz y vídeos cortos con sonido, o anima una foto.",
                "Es además un asistente de IA para chatear, buscar y programar.",
                "38 idiomas, iOS 17 o posterior, 186 MB.",
            ],
            "limits": "el vídeo es una función más de un chat, sin plantillas para redes, y la ficha no dice cuántos vídeos entran en cada plan.",
        },
        {
            "name": "Google Gemini (Gemini Omni)", "id": 6477489729, "anchor": "gemini",
            "developer": "Google LLC", "rating": (4.68, 207849),
            "row": ["El vídeo pide Google AI Plus (4,99 €), Pro (21,99 €) o Ultra, o Workspace", "Vídeos cinematográficos con Gemini Omni dentro del asistente Gemini",
                    "Cuenta de Google", "Datos vinculados a ti", "1.2026.3970207 (7 oct 2026)", "4,7 (207.849 valoraciones)"],
            "best_for": "quien ya paga un plan de Google AI.",
            "facts": [
                "Según la ficha, Gemini Omni convierte ideas en vídeos cinematográficos para usuarios de Google AI Plus, Pro, Ultra y Workspace.",
                "Los mismos planes incluyen almacenamiento de Google.",
                "70 idiomas, iOS 17.4 o posterior, 391 MB.",
            ],
            "limits": "el vídeo no está en el plan gratis y es una función más de un asistente general.",
        },
        {
            "name": "CapCut - Editor de vídeo", "id": 1500855883, "anchor": "capcut",
            "developer": "BYTEDANCE PTE. LTD.", "rating": (4.54, 41985),
            "row": ["Standard 11,99 € al mes, Pro 23,99 € al mes", "Edición: fotogramas clave, subtítulos automáticos, efectos, exportación 4K 60 fps",
                    "Opcional", "Datos utilizados para rastrearte; datos vinculados a ti", "19.7.0 (8 oct 2026)", "4,5 (41.985 valoraciones)"],
            "best_for": "terminar un clip hecho con IA: cortar, subtitular, poner música y efectos antes de publicar.",
            "facts": [
                "Recortar, dividir y unir clips, curvas de velocidad, croma y estabilización.",
                "Subtítulos automáticos, texto a voz, seguimiento de movimiento y quitar el fondo.",
                "20 idiomas, iOS 15 o posterior, 824 MB. También en Mac.",
            ],
            "limits": "su ficha describe herramientas de edición, no generar un vídeo desde un texto como hacía Sora, así que complementa a las de arriba más que sustituirlas.",
        },
    ],
    "who": [
        "<strong>Usabas Sora para animar fotos o hacer clips desde un texto:</strong> Dora (nuestra) o Kling AI.",
        "<strong>Quieres 4K o clips de más de 15 segundos:</strong> Kling AI.",
        "<strong>Ya pagas un asistente:</strong> Grok (SuperGrok) o Gemini (Google AI Plus o superior).",
        "<strong>También usas la web o Claude y ChatGPT:</strong> Dora, cuya cuenta y monedas sirven en doravideo.com y en esos asistentes.",
        "<strong>Necesitas editar y subtitular el resultado:</strong> CapCut, después de cualquiera de las anteriores.",
    ],
    "cases": [
        "Dar vida a una foto antigua con un vídeo corto.",
        "Un clip vertical para TikTok, Reels o Shorts a partir de una frase.",
        "Un vídeo de producto o un anuncio para una tienda o una app.",
        "Copiar un baile de moda en tu propia foto (Motion Control de Dora).",
    ],
    "method": [
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo y etiqueta de privacidad. Lo que hace cada app sale de su propia descripción en el App Store. No inventamos valoraciones ni reseñas.",
        "La ficha de la app de Sora (id6744034028) daba «no encontrada» ese día. La fecha del cierre sale de la noticia de Engadget sobre el anuncio de OpenAI.",
    ],
    "faq": [
        ("¿Sigue existiendo la app de Sora en iPhone?",
         "No. OpenAI anunció el 24 de marzo de 2026 que cerraba la app de Sora, y el 11 de octubre de 2026 su ficha del App Store ya no abre."),
        ("¿Cuál es la mejor alternativa a Sora en iPhone?",
         "Para vídeos cortos desde una foto o un texto, Dora (nuestra, varios modelos en una app) y Kling AI (hasta 15 segundos en 1080p o 4K, ampliables a 3 minutos). Grok y Gemini también hacen vídeos si pagas sus planes."),
        ("¿Hay alguna alternativa gratis a Sora?",
         "Las cinco se descargan gratis, pero generar vídeo es de pago en todas: Dora con suscripción y monedas, Kling AI con créditos o planes, Gemini solo con Google AI Plus o superior y Grok con los planes SuperGrok y créditos."),
        ("¿Se puede convertir una foto en vídeo en el iPhone sin Sora?",
         "Sí. Dora, Kling AI y Grok Imagine animan una foto y la convierten en un vídeo corto."),
        ("¿Qué alternativa a Sora sirve para TikTok y Reels?",
         "Dora exporta en vertical 9:16 hasta 1080p y sin marca de agua. CapCut sirve después para poner subtítulos y música."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]
