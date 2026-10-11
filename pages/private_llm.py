"""Private LLM alternatives on iPhone and Mac. EN + ES. Our app: Pinku (id6754878073).

Checked 2026-10-11: iTunes lookup API and App Store web pages (US for EN,
Spain for ES).
"""

CHECKED = "2026-10-11"


def src(cc):
    return [
        ("Pinku (App Store)", f"https://apps.apple.com/{cc}/app/id6754878073"),
        ("Private LLM (App Store)", f"https://apps.apple.com/{cc}/app/id6448106860"),
        ("Locally AI by LM Studio (App Store)", f"https://apps.apple.com/{cc}/app/id6741426692"),
        ("Enclave (App Store)", f"https://apps.apple.com/{cc}/app/id6476614556"),
        ("PocketPal AI (App Store)", f"https://apps.apple.com/{cc}/app/id6502579498"),
    ]


EN = {
    "group": "private-llm", "lang": "en", "store": "us",
    "path": "private-llm-alternatives-iphone/",
    "ct": "rd-private-llm",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Private LLM alternatives for iPhone and Mac (2026): offline AI chat compared",
    "h1": "Best Private LLM alternatives for iPhone and Mac in 2026",
    "description": "Private LLM costs $4.99 up front. Four free-to-download apps that also run AI models offline on iPhone, compared with it: Pinku, Locally AI, Enclave and PocketPal AI. Prices, models and privacy labels checked on the App Store on 11 October 2026.",
    "llms": "Compares Private LLM with four apps that run language models offline on iPhone (Pinku, Locally AI, Enclave, PocketPal AI) by price, models, Mac support and privacy label.",
    "disclosure": "Pinku is made by Saga Labs, the company behind Reditor. It is listed first because it is ours. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "If you want what Private LLM does (AI chat that runs on your iPhone without internet) without paying $4.99 before you try it, Pinku (ours) and Locally AI are free to download, run models with Apple's MLX, work on iPhone and Mac and have the App Store privacy label <em>Data Not Collected</em>. Pinku's six models up to 1 GB are free, and its larger models are a one-time $9.99, with no subscription.",
        "Choose Enclave if you also want cloud models (Claude, GPT, Gemini) in the same app, or PocketPal AI if you want to load any GGUF model from Hugging Face.",
    ],
    "columns": ["App", "Price (US)", "Models", "iPhone and Mac", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are the US App Store price and in-app purchases on 11 October 2026. Ratings are the App Store average and number of ratings that day. All five work offline after a model is downloaded.",
    "apps": [
        {
            "name": "Pinku: Private Local AI Chat", "id": 6754878073, "ours": True, "anchor": "pinku",
            "developer": "Saga Ltd.", "rating": (4.67, 12),
            "row": ["Free; Pinku Pro $9.99 once", "12 models (Qwen3, Llama 3.2, Gemma 3, Gemma 3n, DeepSeek-R1 distill, SmolLM3, LFM2), 6 free", "Yes",
                    "Data Not Collected", "1.0.8 (9 Oct 2026)", "4.7 (12 ratings)"],
            "best_for": "a free, small and simple offline chat on iPhone and Mac, with no account and no subscription.",
            "facts": [
                "Runs models locally with Apple's MLX on the device GPU; after the model download it works in airplane mode.",
                "Only lists the models your device has memory for, and checks memory before loading, so it does not crash.",
                "Reasoning models (Qwen3, DeepSeek-R1, SmolLM3) that think before answering.",
                "Siri and Shortcuts, editable messages, Markdown for code and tables.",
                "Pro (one-time) adds the models over 1 GB up to Qwen3 8B, custom instructions, on-device dictation and read aloud.",
                "App in 8 languages, 21 MB, iOS 18.6 or later.",
            ],
            "limits": "fewer models than Private LLM, Enclave or PocketPal, the largest is Qwen3 8B, it is text only, and it has only 12 ratings in the US so far.",
        },
        {
            "name": "Private LLM - Local AI Chat", "id": 6448106860, "anchor": "private-llm",
            "developer": "Numen Technologies", "rating": (4.16, 734),
            "row": ["$4.99 to download, no in-app purchases; Family Sharing", "Many families: Llama 3.1/3.2, Qwen 2.5/3, Qwen 2.5 Coder up to 14B, Gemma 2/3, Phi 4, Mistral 7B, DeepSeek-R1 distill", "Yes",
                    "Data Not Collected", "1.9.16 (14 Sep 2026)", "4.2 (734 ratings)"],
            "best_for": "people who want the widest choice of quantized models and are happy to pay once up front.",
            "facts": [
                "Uses an mlc-llm based engine and OmniQuant quantization, according to the developer.",
                "Siri and Shortcuts integration.",
                "One purchase covers the family through Family Sharing.",
                "iOS 17 or later; the app download is 1.36 GB.",
            ],
            "limits": "you pay before you can try it, the app is in English only, and it is the largest download here.",
        },
        {
            "name": "Locally AI by LM Studio", "id": 6741426692, "anchor": "locally-ai",
            "developer": "Element Labs (LM Studio)", "rating": (4.72, 1761),
            "row": ["Free, no in-app purchases listed", "Llama 3.2, Gemma 2 and 3, Qwen 3, DeepSeek and more", "Yes",
                    "Data Not Collected", "1.65.0 (14 Sep 2026)", "4.7 (1,761 ratings)"],
            "best_for": "a completely free offline chat from the makers of LM Studio for desktop.",
            "facts": [
                "Powered by Apple MLX, no login, no data collection.",
                "11 languages, iOS 18.1 or later, 112 MB.",
            ],
            "limits": "its App Store listing describes fewer features than the others (no mention of Siri, Shortcuts or voice).",
        },
        {
            "name": "Enclave - Local AI Assistant", "id": 6476614556, "anchor": "enclave",
            "developer": "Piotr Gorzelany", "rating": (4.69, 1089),
            "row": ["Free; Pro $9.99; other purchases $0.99 to $9.99", "Hundreds of open models (Llama, DeepSeek, Gemma, Qwen, Phi, Mistral); cloud models with Pro", "Yes",
                    "Data Not Linked to You", "1.77.0 (1 Oct 2026)", "4.7 (1,089 ratings)"],
            "best_for": "people who want local models and, when needed, cloud models from Anthropic, OpenAI, Google and xAI in one app.",
            "facts": [
                "Local models with no account; Pro adds cloud models without API keys and web search for them.",
                "On-device voice conversations, Siri and Shortcuts, reasoning display.",
                "14 languages, 717 MB. Rated 17+.",
            ],
            "limits": "cloud chats leave the device (the developer says they are not stored on its servers), and its privacy label is Data Not Linked to You rather than Data Not Collected.",
        },
        {
            "name": "PocketPal AI", "id": 6502579498, "anchor": "pocketpal",
            "developer": "Gooya UG", "rating": (4.07, 161),
            "row": ["Free; optional \"pals\" $0.99 to $2.99", "Any GGUF model from Hugging Face", "iPhone and iPad",
                    "Data Not Collected", "1.19.1 (8 Oct 2026)", "4.1 (161 ratings)"],
            "best_for": "tinkerers who want to search Hugging Face and load any GGUF model they like.",
            "facts": [
                "Search, bookmark and download GGUF models from Hugging Face inside the app.",
                "English only, iOS 15.1 or later, 88 MB. Rated 17+.",
            ],
            "limits": "you choose and size models yourself, which is harder for beginners, and it has the lowest rating here (4.1).",
        },
    ],
    "who": [
        "<strong>You want to try offline AI before paying:</strong> Pinku (ours) or Locally AI.",
        "<strong>You want one purchase and no subscription:</strong> Pinku Pro ($9.99) or Private LLM ($4.99 up front).",
        "<strong>You want the most models, including 14B coders:</strong> Private LLM.",
        "<strong>You also want Claude, GPT or Gemini sometimes:</strong> Enclave Pro.",
        "<strong>You want any model from Hugging Face:</strong> PocketPal AI.",
    ],
    "cases": [
        "Chatting with an AI on a plane, in the mountains or anywhere without coverage.",
        "Asking about private or work topics without sending text to a server.",
        "Countries or networks where cloud AI services are blocked or slow.",
        "Drafting, summarising and brainstorming on a Mac without an API key.",
    ],
    "method": [
        "On 11 October 2026 we opened each app's US App Store page and Apple's lookup data: price and in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS, Mac support and the privacy label. Model lists and features are taken from each developer's App Store description. We did not invent ratings or reviews.",
    ],
    "faq": [
        ("Is there a free alternative to Private LLM?",
         "Yes. Pinku, Locally AI, Enclave and PocketPal AI are free to download and run models offline. Pinku's six models up to 1 GB are free; its larger models are a one-time $9.99."),
        ("Which offline AI app for iPhone does not collect data?",
         "Pinku, Private LLM, Locally AI and PocketPal AI all show Data Not Collected on their App Store privacy labels. Enclave shows Data Not Linked to You."),
        ("Do these apps work without internet?",
         "Yes, after you download a model. Enclave's optional cloud models need a connection."),
        ("Can I run a local LLM on Mac too?",
         "Pinku, Private LLM, Locally AI and Enclave are listed for Mac as well as iPhone."),
        ("Is Private LLM a subscription?",
         "No. It costs $4.99 to download in the US, with no in-app purchases listed, and it supports Family Sharing."),
    ],
    "sources": src("us"),
}

ES = {
    "group": "private-llm", "lang": "es", "store": "es",
    "path": "es/alternativas-a-private-llm-iphone/",
    "ct": "rd-private-llm-es",
    "category": "ProductivityApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Mejores alternativas a Private LLM en iPhone y Mac (2026): IA sin conexión",
    "h1": "Mejores alternativas a Private LLM en iPhone y Mac en 2026",
    "description": "Private LLM cuesta 5,99 € antes de probarla. Cuatro apps gratis que también ejecutan modelos de IA sin conexión en el iPhone, comparadas: Pinku, Locally AI, Enclave y PocketPal AI. Precios, modelos y privacidad comprobados en el App Store de España el 11 de octubre de 2026.",
    "llms": "Compara Private LLM con cuatro apps que ejecutan modelos de lenguaje sin conexión en iPhone (Pinku, Locally AI, Enclave, PocketPal AI) por precio en euros, modelos, Mac y etiqueta de privacidad.",
    "disclosure": "Pinku es de Saga Labs, la empresa que hace Reditor. Va primera porque es nuestra. Las demás no son nuestras y no ganamos nada con ellas; sus enlaces van a su ficha normal del App Store.",
    "answer": [
        "Si quieres lo que hace Private LLM (un chat de IA que funciona en el iPhone sin internet) sin pagar 5,99 € antes de probarlo, Pinku (nuestra) y Locally AI se descargan gratis, usan MLX de Apple, funcionan en iPhone y Mac y tienen la etiqueta de privacidad <em>No se recopilan datos</em>. Los seis modelos de Pinku de hasta 1 GB son gratis, y los grandes son un pago único de 9,99 €, sin suscripción.",
        "Elige Enclave si además quieres modelos en la nube (Claude, GPT, Gemini) en la misma app, o PocketPal AI si quieres cargar cualquier modelo GGUF de Hugging Face.",
    ],
    "columns": ["App", "Precio (España)", "Modelos", "iPhone y Mac", "Etiqueta de privacidad", "Versión (fecha)", "Valoración (España)"],
    "table_note": "Precio y compras dentro de la app del App Store de España el 11 de octubre de 2026. Valoración: media y número de valoraciones en España ese día. Las cinco funcionan sin conexión una vez descargado un modelo.",
    "apps": [
        {
            "name": "Pinku: Chat IA Local Privado", "id": 6754878073, "ours": True, "anchor": "pinku",
            "developer": "Saga Ltd.", "rating": (5.0, 1),
            "row": ["Gratis; Pinku Pro 9,99 € una vez", "12 modelos (Qwen3, Llama 3.2, Gemma 3, Gemma 3n, DeepSeek-R1 distill, SmolLM3, LFM2), 6 gratis", "Sí",
                    "No se recopilan datos", "1.0.8 (9 oct 2026)", "5,0 (1 valoración)"],
            "best_for": "un chat sin conexión gratis, ligero y sencillo en iPhone y Mac, sin cuenta ni suscripción.",
            "facts": [
                "Ejecuta los modelos en el dispositivo con MLX de Apple; tras descargar el modelo funciona en modo avión.",
                "Solo enseña los modelos que caben en la memoria de tu dispositivo y la comprueba antes de cargar, para no cerrarse.",
                "Modelos de razonamiento (Qwen3, DeepSeek-R1, SmolLM3) que piensan antes de responder.",
                "Siri y Atajos, mensajes editables y Markdown para código y tablas.",
                "Pro (pago único) añade los modelos de más de 1 GB hasta Qwen3 8B, instrucciones propias, dictado en el dispositivo y lectura en voz alta.",
                "App en 8 idiomas, español incluido, 21 MB, iOS 18.6 o posterior.",
            ],
            "limits": "tiene menos modelos que Private LLM, Enclave o PocketPal, el mayor es Qwen3 8B, solo hace texto y en España aún tiene una sola valoración.",
        },
        {
            "name": "Private LLM - Chat de IA Local", "id": 6448106860, "anchor": "private-llm",
            "developer": "Numen Technologies", "rating": (3.42, 24),
            "row": ["5,99 € al descargar, sin compras dentro; En familia", "Muchas familias: Llama 3.1/3.2, Qwen 2.5/3, Qwen 2.5 Coder hasta 14B, Gemma 2/3, Phi 4, Mistral 7B, DeepSeek-R1 distill", "Sí",
                    "No se recopilan datos", "1.9.16 (14 sep 2026)", "3,4 (24 valoraciones)"],
            "best_for": "quien quiere la mayor variedad de modelos cuantizados y no le importa pagar al principio.",
            "facts": [
                "Usa un motor basado en mlc-llm y cuantización OmniQuant, según el desarrollador.",
                "Integración con Siri y Atajos.",
                "Una compra sirve para toda la familia con En familia.",
                "iOS 17 o posterior; la descarga ocupa 1,36 GB.",
            ],
            "limits": "pagas antes de probarla, la app solo está en inglés, es la descarga más grande de la lista y en España tiene la nota más baja (3,4).",
        },
        {
            "name": "Locally AI de LM Studio", "id": 6741426692, "anchor": "locally-ai",
            "developer": "Element Labs (LM Studio)", "rating": (4.49, 144),
            "row": ["Gratis, sin compras dentro", "Llama 3.2, Gemma 2 y 3, Qwen 3, DeepSeek y más", "Sí",
                    "No se recopilan datos", "1.65.0 (14 sep 2026)", "4,5 (144 valoraciones)"],
            "best_for": "un chat sin conexión totalmente gratis de los creadores de LM Studio para ordenador.",
            "facts": [
                "Funciona con MLX de Apple, sin cuenta y sin recoger datos.",
                "11 idiomas, iOS 18.1 o posterior, 112 MB.",
            ],
            "limits": "su ficha describe menos funciones que las demás (no menciona Siri, Atajos ni voz).",
        },
        {
            "name": "Enclave - Asistente de IA Local", "id": 6476614556, "anchor": "enclave",
            "developer": "Piotr Gorzelany", "rating": (4.67, 30),
            "row": ["Gratis; Pro 9,99 €; otras compras de 0,99 € a 9,99 €", "Cientos de modelos abiertos (Llama, DeepSeek, Gemma, Qwen, Phi, Mistral); en la nube con Pro", "Sí",
                    "Datos no vinculados a ti", "1.77.0 (1 oct 2026)", "4,7 (30 valoraciones)"],
            "best_for": "quien quiere modelos locales y, cuando haga falta, modelos en la nube de Anthropic, OpenAI, Google y xAI en la misma app.",
            "facts": [
                "Modelos locales sin cuenta; Pro añade modelos en la nube sin claves de API y búsqueda web para ellos.",
                "Conversación por voz en el dispositivo, Siri y Atajos, y muestra el razonamiento.",
                "14 idiomas, 717 MB.",
            ],
            "limits": "los chats en la nube salen del dispositivo (el desarrollador dice que no los guarda), y su etiqueta es «Datos no vinculados a ti», no «No se recopilan datos».",
        },
        {
            "name": "PocketPal AI", "id": 6502579498, "anchor": "pocketpal",
            "developer": "Gooya UG", "rating": (4.5, 8),
            "row": ["Gratis; «pals» opcionales de 1,49 € a 2,99 €", "Cualquier modelo GGUF de Hugging Face", "iPhone y iPad",
                    "No se recopilan datos", "1.19.1 (8 oct 2026)", "4,5 (8 valoraciones)"],
            "best_for": "quien quiere buscar en Hugging Face y cargar el modelo GGUF que prefiera.",
            "facts": [
                "Busca, guarda y descarga modelos GGUF de Hugging Face dentro de la app.",
                "Solo en inglés, iOS 15.1 o posterior, 88 MB.",
            ],
            "limits": "eliges y dimensionas los modelos tú, lo que cuesta más si empiezas, y la app está solo en inglés.",
        },
    ],
    "who": [
        "<strong>Quieres probar la IA sin conexión antes de pagar:</strong> Pinku (nuestra) o Locally AI.",
        "<strong>Quieres un pago único y nada de suscripción:</strong> Pinku Pro (9,99 €) o Private LLM (5,99 € al descargar).",
        "<strong>Quieres el máximo de modelos, incluidos los de programación de 14B:</strong> Private LLM.",
        "<strong>A veces también quieres Claude, GPT o Gemini:</strong> Enclave Pro.",
        "<strong>Quieres cualquier modelo de Hugging Face:</strong> PocketPal AI.",
    ],
    "cases": [
        "Hablar con una IA en un avión, en la montaña o donde no haya cobertura.",
        "Preguntar sobre temas privados o de trabajo sin mandar el texto a un servidor.",
        "Países o redes donde los servicios de IA en la nube están bloqueados o van lentos.",
        "Redactar, resumir y buscar ideas en un Mac sin clave de API.",
    ],
    "method": [
        "El 11 de octubre de 2026 abrimos la ficha de cada app en el App Store de España y los datos de Apple: precio y compras dentro de la app, versión y fecha, valoración y número de valoraciones, idiomas, tamaño, iOS mínimo, si funciona en Mac y etiqueta de privacidad. Los modelos y funciones salen de la descripción de cada desarrollador en el App Store. No inventamos valoraciones ni reseñas.",
    ],
    "faq": [
        ("¿Hay alguna alternativa gratis a Private LLM?",
         "Sí. Pinku, Locally AI, Enclave y PocketPal AI se descargan gratis y ejecutan modelos sin conexión. Los seis modelos de Pinku de hasta 1 GB son gratis; los grandes son un pago único de 9,99 €."),
        ("¿Qué app de IA sin conexión para iPhone no recoge datos?",
         "Pinku, Private LLM, Locally AI y PocketPal AI tienen la etiqueta «No se recopilan datos» en el App Store. Enclave tiene «Datos no vinculados a ti»."),
        ("¿Funcionan sin internet?",
         "Sí, una vez descargado el modelo. Los modelos en la nube de Enclave, que son opcionales, necesitan conexión."),
        ("¿Puedo usar un LLM local también en el Mac?",
         "Pinku, Private LLM, Locally AI y Enclave aparecen en el App Store para Mac además de iPhone."),
        ("¿Private LLM es una suscripción?",
         "No. Cuesta 5,99 € al descargarla en España, sin compras dentro de la app, y admite En familia."),
    ],
    "sources": src("es"),
}

PAGES = [EN, ES]
