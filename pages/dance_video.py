"""Best AI apps to make a dancing video from a photo on iPhone. EN + ES. Our app: Dora (id6754180384).

Checked 2026-10-15: iTunes lookup API and App Store web pages (US for EN, Spain
for ES) for Dora, Viggle AI, Dance AI, Pose and PixVerse Lite. Dora's Motion
Control claims come from its App Store description and from the Dora repo
(models.ts: the model takes a reference video next to the photo; the app checks
on the phone that the photo has a person before generating). Privacy labels are
left out on purpose: they were not read for this page.
"""

CHECKED = "2026-10-15"


def src(cc):
    return [
        ("DORA (App Store)", f"https://apps.apple.com/{cc}/app/id6754180384"),
        ("Viggle AI (App Store)", f"https://apps.apple.com/{cc}/app/id6503272013"),
        ("Dance AI (App Store)", f"https://apps.apple.com/{cc}/app/id6758041184"),
        ("Pose (App Store)", f"https://apps.apple.com/{cc}/app/id6737417022"),
        ("PixVerse Lite (App Store)", f"https://apps.apple.com/{cc}/app/id6767802142"),
    ]


EN = {
    "group": "dance-video", "lang": "en", "store": "us",
    "path": "best-ai-apps-dancing-video-from-photo-iphone/",
    "ct": "rd-dance",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best AI dance video apps for iPhone photos (2026)",
    "h1": "Best AI apps to make a dancing video from a photo on iPhone in 2026",
    "description": "Five iPhone apps that make a person in a photo dance, compared by how they do it, price and languages: Dora, Viggle AI, Dance AI, Pose and more.",
    "llms": "Compares five iPhone apps that turn a photo into a dancing video (Dora, Viggle AI, Dance AI, Pose, PixVerse Lite) by how the dance is chosen (your own reference video or a template), price and languages.",
    "disclosure": "Dora is made by Saga Labs, the company behind Reditor. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "To make a person in a photo dance on iPhone, there are two ways: copy the moves of a video you choose, or pick a ready-made dance or trend. Dora (ours) and PixVerse Lite copy the moves of a reference video onto your photo (both call it Motion Control); Viggle AI does the same with one photo plus one video and also has more than 8,000 templates; Dance AI and Pose work from a library of dance styles and trends.",
        "All five are free to download and all five charge to make videos, by subscription, credits or both. If you only want one trending template, the template apps are quicker; if you want a specific dance you already have on video, use one of the three that take a reference video.",
    ],
    "columns": ["App", "Price (US)", "How the dance is chosen", "Languages", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the in-app purchases listed on each US App Store page on 15 October 2026; all five are free to download. Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "DORA · AI Video Generator", "id": 6754180384, "ours": True, "anchor": "dora",
            "developer": "Saga Ltd.", "rating": (4.27, 15),
            "row": ["Subscription: $4.99 or $9.99 a week, $119.99 a year; coin packs from $2.99 to $199.99",
                    "Motion Control copies the moves of a dance video onto the person in your photo",
                    "11", "1.4.1 (9 Oct 2026)", "4.3 (15 ratings)"],
            "best_for": "people who have a specific dance on video and want it on their own photo, in vertical format for TikTok and Reels.",
            "facts": [
                "Motion Control takes your photo plus a reference dance video and makes the person in the photo do those moves.",
                "Each generation shows its cost in coins before you tap, and failed generations refund the coins.",
                "A video takes about two minutes. Vertical 9:16, horizontal or square, up to 1080p, no watermark.",
                "The same account and coins work on doravideo.com and inside Claude and ChatGPT through the Dora connector.",
                "iOS 18.6 or later, 61 MB.",
            ],
            "limits": "it needs a paid plan or coins (there is no free video), Motion Control needs a person in the photo (the app checks this on the phone), a pet or a drawing is not a person for it, and it has only 15 ratings in the US so far. It does not have a large catalogue of dance templates to scroll through the way Viggle AI does.",
        },
        {
            "name": "Viggle AI: Meme Maker", "id": 6503272013, "anchor": "viggle",
            "developer": "WarpEngine Canada Inc.", "rating": (4.76, 28091),
            "row": ["Pro $4.99 a week, $9.99 a month or $95.90 a year; Live plans from $24.99 a month; extra credits $3 to $15",
                    "Mix: one photo plus one video, or one of 8,000+ templates (dances, memes, sports moments)",
                    "1 (English)", "2.0.7 (13 Oct 2026)", "4.8 (28,091 ratings)"],
            "best_for": "trend dances and meme videos, with the biggest template library of the five.",
            "facts": [
                "Its listing describes motion-controlled video generation: drop your photo into any video clip, or pick a template.",
                "Also lip-sync (Mic and Rap), a multi-character Editor, and a live webcam character swap in the Live plans.",
                "iOS 16 or later, 140 MB.",
            ],
            "limits": "the interface is English only, and the listing does not say how many credits one video costs.",
        },
        {
            "name": "Dance AI - Video Generator", "id": 6758041184, "anchor": "dance-ai",
            "developer": "Deepix AI Yazilim Teknolojileri Anonim Sirketi", "rating": (4.59, 17573),
            "row": ["Weekly premium $9.99 to $14.99, yearly $39.99 or $79.99; coin packs $9.99 to $34.99",
                    "A library of dance styles: upload a photo of a person, a child or a pet and pick a style",
                    "5", "1.1.0 (11 Sep 2026)", "4.6 (17,573 ratings)"],
            "best_for": "one-tap dances from a photo of a person, a child or a pet, without finding a reference video.",
            "facts": [
                "Pick a dance style from the library and generate; no choreography or editing.",
                "The listing says your photos are used only to generate the video and are not permanently stored afterwards.",
                "Also makes videos from a text prompt and applies filters and effects.",
                "iOS 15.1 or later, 105 MB.",
            ],
            "limits": "several recent reviews on its Spanish App Store page complain about paying for coins on top of the subscription, and you cannot bring your own dance video according to the listing.",
        },
        {
            "name": "Pose: AI Photo Video Generator", "id": 6737417022, "anchor": "pose",
            "developer": "SPARK DYNAMICS YAZILIM HIZMETLERI LIMITED SIRKETI", "rating": (4.66, 145673),
            "row": ["Several subscription tiers listed from $9.99 to $69.99",
                    "Trend effects: AI baby dancing video, sway dance, stadium cam, birthday photo shoot; no prompt needed",
                    "4", "1.4.7 (12 Oct 2026)", "4.7 (145,673 ratings)"],
            "best_for": "viral photo effects, such as a baby dancing video, from one uploaded photo.",
            "facts": [
                "Upload one photo and the effect is generated automatically, with no prompt.",
                "Besides dance effects it has photo styles, headshots and other trending filters.",
                "iOS 16 or later, 96 MB.",
            ],
            "limits": "it is built around trending effects rather than choosing a dance, and its listing does not say you can use your own reference video.",
        },
        {
            "name": "PixVerse Lite", "id": 6767802142, "anchor": "pixverse",
            "developer": "AIVORA PTE. LTD.", "rating": (4.31, 1659),
            "row": ["Elite $5.99 a week or $49.99 a year; credit packs $5 to $100",
                    "Motion Control: a character image plus a reference motion video; also dance templates",
                    "14", "0.8.1 (21 Sep 2026)", "4.3 (1,659 ratings)"],
            "best_for": "people who want a general AI video app that also has Motion Control and dance templates.",
            "facts": [
                "Its listing describes Motion Control as uploading a character image and a reference motion video to guide the movement.",
                "Also text to video, image to video, lip-sync, transitions and video upscaling up to 4K.",
                "iOS 15 or later, 121 MB.",
            ],
            "limits": "it is a broad video toolbox, so finding the dance feature takes more taps, and some recent reviews on its Spanish App Store page complain about charges and cancelling.",
        },
    ],
    "who": [
        "<strong>You have a specific dance on video and want it on your photo:</strong> Dora (ours), Viggle AI or PixVerse Lite.",
        "<strong>You want a trending dance in one tap:</strong> Viggle AI (8,000+ templates), Dance AI or Pose.",
        "<strong>You want your kid or pet to dance:</strong> Dance AI or Pose, whose listings mention children, pets or babies. Dora's Motion Control needs a person in the photo.",
        "<strong>You also want a general AI video app:</strong> Dora or PixVerse Lite.",
        "<strong>You also use Claude or ChatGPT:</strong> Dora, whose account and coins work in those assistants.",
    ],
    "cases": [
        "A friend or yourself doing a viral dance challenge from one photo.",
        "A vertical dance clip for TikTok, Instagram Reels or YouTube Shorts.",
        "A birthday or party video of someone dancing.",
        "Trying a choreography on a photo before filming it.",
    ],
    "method": [
        "On 15 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchase prices, version and release date, rating and number of ratings, languages, size and minimum iOS. What each app does is taken from its own App Store description; the way Dora's Motion Control works is also checked in our code. We did not run a quality test of the dances, so this page does not say which app makes the best-looking dance. We did not invent ratings or reviews.",
        "Subscriptions and credits change often. Check the price shown inside each app before paying.",
    ],
    "faq": [
        ("What is the best app to make a dancing video from a photo on iPhone?",
         "It depends on how you want to choose the dance. To copy a dance video you already have onto your photo, Dora (ours), Viggle AI and PixVerse Lite take a reference video. For one-tap trends, Viggle AI has more than 8,000 templates, and Dance AI and Pose work from a library of dance styles and effects."),
        ("Can I make a dancing video from a photo for free?",
         "All five apps are free to download, but each charges to make videos, by subscription, credits or both. None of them offers unlimited free videos according to their App Store listings."),
        ("How does an AI dance video work?",
         "You give the app a photo of a person and either pick a dance style or provide a reference video. The AI then generates a video where the person in the photo moves like the dance. With Motion Control, the moves are copied from the reference video."),
        ("Can I make my pet or my baby dance?",
         "Dance AI's listing mentions pets and children and Pose's mentions babies. Dora's Motion Control needs a person in the photo."),
        ("Which of these apps has no watermark?",
         "Dora's listing says there is no watermark on its videos. We did not verify watermarks in the other four, so check before you pay."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "dance-video", "lang": "es", "store": "es",
    "path": "es/mejores-apps-ia-video-baile-desde-foto-iphone/",
    "ct": "rd-dance-es",
    "category": "PhotoVideoApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores apps de IA para hacer bailar una foto en iPhone (2026)",
    "h1": "Mejores apps de IA para hacer un vídeo de baile desde una foto en iPhone en 2026",
    "description": "Cinco apps de iPhone que hacen bailar a una persona de una foto, comparadas por cómo lo hacen, precio e idiomas: Dora, Viggle AI, Dance AI y más.",
    "llms": "Compara cinco apps de iPhone que convierten una foto en un vídeo de baile (Dora, Viggle AI, Dance AI, Pose, PixVerse Lite) según cómo se elige el baile (tu propio vídeo de referencia o una plantilla), precio en euros e idiomas.",
    "disclosure": "Dora es de Saga Labs, la empresa que hace Reditor. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "Para hacer bailar a una persona de una foto en el iPhone hay dos caminos: copiar los movimientos de un vídeo que tú eliges, o escoger un baile o una tendencia ya hechos. Dora (nuestra) y PixVerse Lite copian los movimientos de un vídeo de referencia en tu foto (las dos lo llaman Motion Control); Viggle AI hace lo mismo con una foto y un vídeo y además tiene más de 8.000 plantillas; Dance AI y Pose parten de una biblioteca de estilos de baile y tendencias.",
        "Las cinco se descargan gratis y las cinco cobran por hacer vídeos, con suscripción, créditos o las dos cosas. Si solo quieres una plantilla de moda, las apps de plantillas son más rápidas; si quieres un baile concreto que ya tienes en vídeo, usa una de las tres que aceptan un vídeo de referencia.",
    ],
    "columns": ["App", "Precio (España)", "Cómo se elige el baile", "Idiomas", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precios: compras dentro de la app que muestra cada ficha del App Store de España el 15 de octubre de 2026; las cinco se descargan gratis. Valoración: media y número de valoraciones en España ese día.",
    "apps": [
        {
            "name": "DORA · Generador Vídeo IA", "id": 6754180384, "ours": True, "anchor": "dora",
            "developer": "Saga Ltd.",
            "row": ["Suscripción: 7,99 € a la semana o 129,99 € al año; packs de monedas de 2,99 € a 229,99 €",
                    "Motion Control copia los movimientos de un vídeo de baile en la persona de tu foto",
                    "11", "1.4.1 (9 oct 2026)", "Aún sin valoraciones en España"],
            "best_for": "quien tiene un baile concreto en vídeo y lo quiere en su propia foto, en vertical para TikTok y Reels.",
            "facts": [
                "Motion Control toma tu foto y un vídeo de baile de referencia y hace que la persona de la foto se mueva igual.",
                "Cada generación enseña su coste en monedas antes de pulsar, y si falla se devuelven.",
                "Un vídeo tarda unos dos minutos. Vertical 9:16, horizontal o cuadrado, hasta 1080p y sin marca de agua.",
                "La misma cuenta y las mismas monedas sirven en doravideo.com y dentro de Claude y ChatGPT con el conector de Dora.",
                "iOS 18.6 o posterior, 61 MB.",
            ],
            "limits": "hace falta plan de pago o monedas (no hay vídeo gratis), Motion Control necesita una persona en la foto (la app lo comprueba en el móvil), una mascota o un dibujo no cuentan como persona, y todavía no tiene valoraciones en España. No tiene un catálogo enorme de plantillas de baile para ir pasando como Viggle AI.",
        },
        {
            "name": "Viggle AI: Meme Maker", "id": 6503272013, "anchor": "viggle",
            "developer": "WarpEngine Canada Inc.", "rating": (4.73, 642),
            "row": ["Pro 5,99 € a la semana, 9,99 € al mes o 99,90 € al año; planes Live desde 29,99 € al mes; créditos extra de 3 € a 17 €",
                    "Mix: una foto y un vídeo, o una de más de 8.000 plantillas (bailes, memes, jugadas)",
                    "1 (inglés)", "2.0.7 (13 oct 2026)", "4,7 (642 valoraciones)"],
            "best_for": "bailes de moda y vídeos de memes, con la mayor biblioteca de plantillas de las cinco.",
            "facts": [
                "Su ficha habla de generación de vídeo con control de movimiento: mete tu foto en cualquier clip o elige una plantilla.",
                "También sincronización labial (Mic y Rap), un editor multipersonaje y un cambio de personaje en directo con la webcam en los planes Live.",
                "iOS 16 o posterior, 140 MB.",
            ],
            "limits": "la interfaz solo está en inglés y la ficha no dice cuántos créditos cuesta un vídeo.",
        },
        {
            "name": "Dance AI - Generador Vídeo", "id": 6758041184, "anchor": "dance-ai",
            "developer": "Deepix AI Yazilim Teknolojileri Anonim Sirketi", "rating": (4.15, 405),
            "row": ["Premium semanal de 9,99 € a 17,99 €, anual 44,99 € u 89,99 €; packs de monedas de 9,99 € a 39,99 €",
                    "Biblioteca de estilos de baile: sube la foto de una persona, un niño o una mascota y elige un estilo",
                    "5", "1.1.0 (11 sep 2026)", "4,2 (405 valoraciones)"],
            "best_for": "bailes con un toque desde la foto de una persona, un niño o una mascota, sin buscar un vídeo de referencia.",
            "facts": [
                "Eliges un estilo de baile de la biblioteca y generas; sin coreografía ni edición.",
                "La ficha dice que tus fotos se usan solo para generar el vídeo y no se guardan de forma permanente después.",
                "También hace vídeos desde un texto y aplica filtros y efectos.",
                "iOS 15.1 o posterior, 105 MB.",
            ],
            "limits": "varias reseñas recientes de su ficha en España se quejan de pagar monedas además de la suscripción, y según la ficha no puedes traer tu propio vídeo de baile.",
        },
        {
            "name": "Pose AI: Generador de imágenes", "id": 6737417022, "anchor": "pose",
            "developer": "SPARK DYNAMICS YAZILIM HIZMETLERI LIMITED SIRKETI", "rating": (4.34, 2501),
            "row": ["Varios niveles de suscripción, de 9,99 € a 34,99 €",
                    "Efectos de moda: vídeo de bebé bailando, baile con balanceo, cámara de estadio, sesión de cumpleaños; sin prompt",
                    "4", "1.4.7 (12 oct 2026)", "4,3 (2.501 valoraciones)"],
            "best_for": "efectos virales de foto, como un vídeo de bebé bailando, desde una sola foto.",
            "facts": [
                "Subes una foto y el efecto se genera solo, sin escribir nada.",
                "Además de bailes tiene estilos de foto, retratos y otros filtros de moda.",
                "iOS 16 o posterior, 96 MB.",
            ],
            "limits": "está pensada para efectos de moda, no para elegir un baile, y su ficha no dice que puedas usar tu propio vídeo de referencia.",
        },
        {
            "name": "PixVerse Lite", "id": 6767802142, "anchor": "pixverse",
            "developer": "AIVORA PTE. LTD.", "rating": (4.23, 119),
            "row": ["Elite 6,99 € a la semana o 59,99 € al año; packs de créditos de 6 € a 100 €",
                    "Motion Control: una imagen del personaje y un vídeo de movimiento de referencia; también plantillas de baile",
                    "14", "0.8.1 (21 sep 2026)", "4,2 (119 valoraciones)"],
            "best_for": "quien quiere una app de vídeo con IA general que además tenga Motion Control y plantillas de baile.",
            "facts": [
                "Su ficha describe Motion Control como subir una imagen de un personaje y un vídeo de movimiento de referencia para guiar el movimiento.",
                "También texto a vídeo, imagen a vídeo, sincronización labial, transiciones y mejora de vídeo hasta 4K.",
                "iOS 15 o posterior, 121 MB.",
            ],
            "limits": "es una caja de herramientas amplia, así que encontrar la función de baile lleva más toques, y algunas reseñas recientes de su ficha en España se quejan de cobros y de lo difícil que es cancelar.",
        },
    ],
    "who": [
        "<strong>Tienes un baile concreto en vídeo y lo quieres en tu foto:</strong> Dora (nuestra), Viggle AI o PixVerse Lite.",
        "<strong>Quieres un baile de moda con un toque:</strong> Viggle AI (más de 8.000 plantillas), Dance AI o Pose.",
        "<strong>Quieres que baile tu hijo o tu mascota:</strong> Dance AI o Pose, cuyas fichas mencionan niños, mascotas o bebés. El Motion Control de Dora necesita una persona en la foto.",
        "<strong>Quieres también una app de vídeo con IA general:</strong> Dora o PixVerse Lite.",
        "<strong>Usas también Claude o ChatGPT:</strong> Dora, cuya cuenta y monedas sirven en esos asistentes.",
    ],
    "cases": [
        "Tú o un amigo haciendo un baile viral desde una sola foto.",
        "Un clip de baile vertical para TikTok, Instagram Reels o YouTube Shorts.",
        "Un vídeo de cumpleaños o de fiesta con alguien bailando.",
        "Probar una coreografía en una foto antes de grabarla.",
    ],
    "method": [
        "El 15 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño e iOS mínimo. Lo que hace cada app sale de su propia descripción en el App Store; cómo funciona el Motion Control de Dora lo comprobamos además en nuestro código. No hicimos una prueba de calidad de los bailes, así que esta página no dice qué app hace el baile más bonito. No inventamos valoraciones ni reseñas.",
        "Las suscripciones y los créditos cambian a menudo. Mira el precio que enseña cada app antes de pagar.",
    ],
    "faq": [
        ("¿Cuál es la mejor app para hacer un vídeo de baile desde una foto en iPhone?",
         "Depende de cómo quieras elegir el baile. Para copiar en tu foto un baile que ya tienes en vídeo, Dora (nuestra), Viggle AI y PixVerse Lite aceptan un vídeo de referencia. Para tendencias con un toque, Viggle AI tiene más de 8.000 plantillas, y Dance AI y Pose parten de una biblioteca de estilos de baile y efectos."),
        ("¿Se puede hacer un vídeo de baile desde una foto gratis?",
         "Las cinco apps se descargan gratis, pero todas cobran por hacer vídeos, con suscripción, créditos o las dos cosas. Según sus fichas del App Store, ninguna ofrece vídeos gratis ilimitados."),
        ("¿Cómo funciona un vídeo de baile con IA?",
         "Das a la app una foto de una persona y eliges un estilo de baile o aportas un vídeo de referencia. La IA genera entonces un vídeo en el que la persona de la foto se mueve como el baile. Con Motion Control, los movimientos se copian del vídeo de referencia."),
        ("¿Puedo hacer bailar a mi mascota o a mi bebé?",
         "La ficha de Dance AI menciona mascotas y niños, y la de Pose, bebés. El Motion Control de Dora necesita una persona en la foto."),
        ("¿Cuál de estas apps no pone marca de agua?",
         "La ficha de Dora dice que sus vídeos no llevan marca de agua. No hemos comprobado la marca de agua en las otras cuatro: míralo antes de pagar."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]
