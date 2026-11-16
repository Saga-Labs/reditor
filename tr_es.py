"""Textos en español de las páginas hechas a partir de las inglesas (App Store de España).

La home y Acerca de en español están escritas a mano en build.py; este módulo solo aporta los textos de página
que i18n.py completa con datos de la tienda (ver tr_de.py para el formato).
"""

TEXT = {
    "car-video-complaints": {
        "path": "es/ver-videos-en-la-pantalla-del-coche-app-que-funciona-iphone/",
        "kicker": "Guía de la pantalla del coche",
        "title": "Cómo ver vídeos en la pantalla del coche sin pagar por una app que no funciona (2026)",
        "h1": "Cómo ver vídeos en la pantalla del coche sin pagar por una app que no funciona (2026)",
        "description": "Las apps de vídeo para el coche reciben reseñas de 1 y 2 estrellas con frases como «doesn't work in my car», «paid and nothing happened» y «scam». Cinco quejas de 863 reseñas y cómo evitar cada una antes de pagar.",
        "llms": "Guía, 14 de noviembre de 2026: las cinco quejas más repetidas en 863 reseñas de una y dos estrellas de apps de vídeo y widgets para el coche en el App Store de EE. UU. para iPhone (CarTV, CarDash, CarTube, APTV, myCar, Car Connect): «scam» y peticiones de reembolso, «doesn't work in my car», pago antes de probar, cargos inesperados y «stopped working after the iOS update», con una solución para cada una. El vídeo en la pantalla del coche solo se reproduce con el coche aparcado y solo en coches cuyo fabricante lo admite. Las cifras son aproximadas.",
        "llms_note": "CarScreen, una de las apps citadas, la hace Saga Labs, que gestiona Reditor.",
        "stand": "Quejas de reseñas del App Store de EE. UU. y una comprobación que puedes hacer con cada una antes de pagar.",
        "answer": [
            "<strong>Para ver vídeos en la pantalla del coche sin pagar por una app que no funciona, comprueba primero si tu coche admite vídeo, y paga solo por una app que te deje probarla gratis en tu propio coche.</strong> El vídeo en la pantalla del coche solo se reproduce con el coche aparcado y solo en coches cuyo fabricante lo admite, así que la misma app puede funcionar en un coche y no hacer nada en otro.",
            "<strong>Prueba gratis primero:</strong> {app:6833951195} (descarga gratuita, valoración: {rating:6833951195}) reproduce un clip de prueba de 5 segundos y te dice con claridad si el vídeo funciona en tu coche antes de que pagues. <a href=\"{CARSCREEN}\">Consigue CarScreen en el App Store</a>."
        ],
        "sections": [
            [
                "data",
                "Lo que revisamos",
                "<p>Descargamos 1.210 reseñas recientes del App Store de EE. UU. de ocho apps de vídeo y widgets para el coche y nos quedamos con las 863 de una o dos estrellas. Las cinco quejas de abajo son las que más se repiten. Los números salen de buscar palabras clave, así que son aproximados, y una reseña puede contar en más de un grupo.</p>\n<ul>\n<li>«Scam», «fraud», «want my money back»: unas 320 reseñas.</li>\n<li>«Doesn't work in my car» o «car not supported»: unas 170.</li>\n<li>«Paid and it didn't work», sin forma de probar antes: unas 120.</li>\n<li>«Charged again» o «can't cancel»: unas 100.</li>\n<li>«Stopped working after the iOS update»: unas 45.</li>\n</ul>\n<p>Las apps de las reseñas, con sus datos en el App Store de España a 14 de noviembre de 2026: {app:6800211040} (gratis, valoración {rating:6800211040}), {app:6797764175} (gratis, valoración {rating:6797764175}), {app:6756518125} (gratis, valoración {rating:6756518125}), {app:1665625393} (gratis, valoración {rating:1665625393}), {app:6755033589} (gratis, valoración {rating:6755033589}) y {app:6476621657} (gratis, valoración {rating:6476621657}). «Gratis» quiere decir descarga gratuita; la mayoría vende dentro una suscripción o un plan de por vida.</p>\n"
            ],
            [
                "scam",
                "«Scam» y «I want my money back»",
                "<p>Es la palabra que más se repite: «scam», «fraud» o «waste of money» aparece en unas 320 de las 863 reseñas, normalmente cuando la app no hizo nada en el coche de quien escribe. Frase típica: «Makes you pay and it did nothing» (CarTube, 1 estrella). Parte de la confusión viene del propio producto: la ficha de CarTube describe una extensión de Safari para reproducir vídeo en la web, mientras que las reseñas esperan vídeo en la pantalla de CarPlay.</p>\n<p><strong>Solución:</strong> antes de instalar, lee lo que promete la ficha de la app y no pagues hasta que la app haya mostrado algo en la pantalla de <em>tu</em> coche. Si ya has pagado, <a href=\"https://support.apple.com/es-es/118223\">Apple explica cómo pedir un reembolso</a>; la decisión es de Apple.</p>\n"
            ],
            [
                "notmycar",
                "«Doesn't work in my car»",
                "<p>Unas 170 reseñas hablan del coche: «Does not work on 2023 Hyundai Tucson with wireless CarPlay!» (CarTube, 1 estrella), «MY CAR WAS NOT EVEN SUPPORTED» (Car Connect, 1 estrella). Las propias fichas de las apps explican por qué. La de APTV dice que el vídeo solo se reproduce con el coche aparcado, necesita iOS 27 o posterior y un vehículo que admita vídeo en CarPlay, y que muchos vehículos todavía no lo admiten. La de CarDash dice que una conexión de audio de CarPlay no garantiza por sí sola el vídeo, y que el resultado depende de tu iPhone, de la versión de iOS, del vehículo y de la fuente del contenido.</p>\n<p><strong>Solución:</strong> trata el soporte del coche como una pregunta aparte de la app. Prueba en tu propio coche, aparcado. {app:6833951195} está pensada justamente para eso: según su ficha, reproduce un clip de prueba de 5 segundos y te dice con claridad si el vídeo funciona en tu coche. El vídeo solo funciona con el coche aparcado y en coches cuyo fabricante lo admite. Si la prueba dice que no, no has perdido nada y puedes seguir usando sus widgets gratuitos.</p>\n"
            ],
            [
                "paidfirst",
                "«Paid and it didn't work»",
                "<p>Unas 120 reseñas dicen que la app pidió dinero antes de que pudieran verla funcionar, y que después no funcionó: «just spent 5 bucks for it not to play anything on my car screen» (CarTV, 1 estrella); «No introductory trial to test app» (myCar, 1 estrella); «Charges me 31 dollar and it doesn't even work» (Car Connect, 1 estrella).</p>\n<p><strong>Solución:</strong> elige una app con una prueba gratis que funcione en el coche, no solo una descarga gratuita. Dos fichas lo dicen: el clip de prueba de 5 segundos de CarScreen, gratis y antes de cualquier pago, y en CarDash el «limited free car-playback allowance» y una fuente de listas antes de Pro. Decide cuando hayas visto el vídeo funcionar. La ficha de CarScreen dice que, tras la comprobación gratuita en el coche, un solo pago desbloquea el vídeo, las listas y el navegador, sin suscripción ni renovaciones.</p>\n"
            ],
            [
                "charged",
                "«Charged again» y «can't cancel»",
                "<p>Unas 100 reseñas hablan de dinero que sale tras el primer pago: «Click on free try, charges for full year subscriptions» (CarDash, 1 estrella). Varias fichas venden planes semanales, anuales o de por vida; la de APTV indica, a 14 de noviembre de 2026, un plan semanal de $9.99 y uno de por vida de $49.99.</p>\n<p><strong>Solución:</strong> lee el plan en la hoja de pago (el semanal es el más fácil de pasar por alto) y pon un recordatorio antes de que acabe una prueba. Para dejar de renovar, <a href=\"https://support.apple.com/es-es/118428\">cancela la suscripción desde Apple</a> en tu cuenta, no borrando la app. Una compra única evita las renovaciones por completo.</p>\n"
            ],
            [
                "iosupdate",
                "«Stopped working after the iOS update»",
                "<p>Unas 45 reseñas dicen que una actualización del iPhone rompió el vídeo: «Stopped working after iOS 27.2 update» (CarTV, 1 estrella), a menudo de personas que habían comprado un plan de por vida. No podemos confirmar la causa; solo recogemos lo que escribieron quienes reseñaron.</p>\n<p><strong>Solución:</strong> antes de comprar un plan de por vida, mira la fecha de la última actualización en la ficha de la app del App Store y lee las reseñas más recientes, no la media. El vídeo en la pantalla del coche depende a la vez del iPhone, de iOS y del coche (así lo dice la ficha de CarDash), así que un pago único es una apuesta mayor que una prueba gratuita. No instales una actualización grande de iOS justo antes de un viaje largo si dependes de ella.</p>\n"
            ],
            [
                "checklist",
                "Antes de pagar: una comprobación de cinco puntos",
                "<ul>\n<li>¿Tu coche es de los que su fabricante admite con vídeo en la pantalla? Si no lo encuentras, considéralo no compatible.</li>\n<li>¿La app lo prueba gratis en tu coche antes de la pantalla de pago?</li>\n<li>¿El plan es una suscripción o una compra única, y cuál es el precio en pantalla antes de confirmar?</li>\n<li>¿Sabes dónde cancelar (<a href=\"https://support.apple.com/es-es/118428\">Apple: cancelar una suscripción</a>) y dónde pedir un reembolso (<a href=\"https://support.apple.com/es-es/118223\">Apple: pedir un reembolso</a>)?</li>\n<li>¿Estás aparcado? Nunca mires mientras conduces.</li>\n</ul>\n"
            ]
        ],
        "faq": [
            [
                "¿Puedo ver vídeos de mi iPhone en la pantalla del coche?",
                "A veces. Según las fichas de CarScreen, CarDash y APTV, el vídeo llega a la pantalla del coche solo con el coche aparcado y solo en coches cuyo fabricante lo admite. Muchos coches no lo admiten."
            ],
            [
                "¿Por qué una app de vídeo para el coche funciona en un coche y en otro no?",
                "Porque depende del coche, no solo de la app. La ficha de APTV dice que muchos vehículos todavía no admiten vídeo en CarPlay, y la de CarDash, que una conexión de audio de CarPlay no garantiza por sí sola el vídeo."
            ],
            [
                "¿Cómo lo compruebo antes de pagar?",
                "Usa una app que pruebe primero tu coche. CarScreen reproduce un clip de prueba gratuito de 5 segundos y te dice si el vídeo funciona en tu coche; la ficha de CarDash ofrece una cuota limitada y gratuita de reproducción en el coche."
            ],
            [
                "¿Puedo pedir un reembolso al App Store?",
                "Puedes pedirlo. Apple explica cómo en su página sobre cómo pedir un reembolso por apps o contenido comprados a Apple; la aprobación depende de Apple."
            ],
            [
                "¿Es seguro ver vídeo en el coche?",
                "Solo con el coche aparcado. Todas las fichas de apps mencionadas aquí dicen que nunca se mire mientras se conduce."
            ]
        ],
        "sources_html": [
            "Reseñas: App Store de EE. UU., 1.210 descargadas de 8 apps, 863 con 1 o 2 estrellas, 14 de noviembre de 2026; recuento por palabra clave, aproximado.",
            "<a href=\"https://support.apple.com/es-es/118223\">Pedir un reembolso por apps o contenido comprados en Apple</a>, Soporte de Apple.",
            "<a href=\"https://support.apple.com/es-es/118428\">Cancelar una suscripción en Apple</a>, Soporte de Apple.",
            "Apps: sus fichas del App Store de España y datos de búsqueda de Apple, 14 de noviembre de 2026. CarScreen: su ficha en el App Store, {app:6833951195}."
        ],
        "fix": "Si algo de aquí está desactualizado, <a href=\"mailto:sagalabs@proton.me\">avísanos</a> y corregimos la página.",
        "decimal": ",",
        "no_rating": "nueva"
    },
}

TEXT["ai-companion-complaints"] = {
    "path": "es/companero-ia-sin-pago-sin-verificacion-iphone/",
    "kicker": "Guía de compañeros de IA",
    "title": "Cómo tener un compañero de IA sin muro de pago, sin verificación de identidad ni nube (2026)",
    "h1": "Cómo tener un compañero de IA sin muro de pago, sin verificación de identidad ni enviar tus chats a la nube (2026)",
    "description": "Las apps de compañeros de IA reciben reseñas de 1 y 2 estrellas que dicen «tienes que pagar para hablar», «verificación de edad» y «cero privacidad». Cinco quejas de 1.207 reseñas de Replika, Character AI, Nomi, Pi, Tolan y Kindroid, y cómo evitar cada una.",
    "llms": "Guía, 14 de noviembre de 2026: las cinco quejas más repetidas en 1.207 reseñas de 1 y 2 estrellas de la App Store de EE. UU. sobre seis apps de compañeros de IA para iPhone (Replika, Character AI, Nomi, Pi, Tolan, Kindroid): pagar para seguir hablando (unas 100 reseñas), anuncios (unas 127, sobre todo de Character AI), verificación de edad e identidad (unas 80), olvidos (unas 54) y chats o datos leídos, guardados o vendidos (unas 34), con una solución para cada una. Dos apps cuya ficha dice que funcionan en el iPhone sin cuenta y con la etiqueta de privacidad Data Not Collected: Talking Friday y Cora. Las cifras son aproximadas.",
    "stand": "Quejas de las reseñas de la App Store de EE. UU. y una comprobación que puedes hacer con cada app antes de pagar.",
    "answer": [
        "<strong>Para tener un compañero de IA sin muro de pago, sin verificación de identidad ni tus chats en el servidor de otro, usa una app que funcione en tu iPhone y no pida cuenta.</strong> Así no hay nada en lo que iniciar sesión, nada que verificar ni ningún servidor al que enviar los chats. El precio es un compañero más sencillo: voz o chat de texto normal, y un iPhone reciente.",
        "<strong>Nuestra recomendación para esto:</strong> {app:6786747271} (gratis, sin valoraciones todavía). Su ficha dice que la conversación funciona en el iPhone, sin cuenta, sin suscripción, sin compras dentro de la app y sin anuncios, y su etiqueta de privacidad en la App Store es Data Not Collected. <a class='cta' href='{href:6786747271}'>Descargar Talking Friday en la App Store</a>.",
    ],
    "sections": [
        ["data", "Lo que revisamos",
         "<p>Descargamos 2.606 reseñas recientes de la App Store de EE. UU. de seis apps de compañeros de IA y nos quedamos con las 1.207 de una o dos estrellas: {app:1158555867} (gratis, 4,4), {app:1671705818} (gratis, 4,3), {app:6477549878} (gratis, 4,8), {app:6451038161} (gratis, 4,7), {app:6445815935} (gratis, 4,4) y {app:6450270929} (gratis, 4,6, a 14 de noviembre de 2026). De Nomi solo había disponibles las 206 reseñas más recientes. Los recuentos salen de buscar palabras clave, así que son aproximados, y una reseña puede contar en más de un grupo.</p>\n<ul>\n<li>«Have to pay», muro de pago, límites de mensajes y «greedy»: unas 100 reseñas. Anuncios: unas 127, 115 de ellas de Character AI.</li>\n<li>«Age verification», comprobaciones con DNI o cara: unas 80, 54 de ellas de Character AI.</li>\n<li>Chats o datos leídos, guardados o vendidos, y «no way to delete my data»: unas 34, revisadas a mano.</li>\n<li>«Forgets» y «can't remember»: unas 54.</li>\n<li>Palabras más repetidas: «age verification» (47 reseñas), «have to pay» (39), «scam» (31), «greedy» (21), «too many ads» (17).</li>\n</ul>\n<p>Así que la nube no es la queja más frecuente; lo son el dinero y la identidad. Comparten una causa, por eso la solución es la misma: una app con cuenta y servidor puede pedirte que pagues, comprobar quién eres y leer tus datos. Una app en el iPhone sin cuenta tiene menos de las tres cosas.</p>\n"],
        ["paywall", "«Tienes que pagar para hablar» (y los anuncios)",
         "<p>Unas 100 reseñas hablan del dinero que se interpone entre tú y la conversación: «after a few messages it's gonna require you to pay to talk more» (Replika, 1 estrella); «You get a one time 30 minute trial then have to pay» (Replika, 1 estrella). La queja sobre Character AI es otra: unas 115 reseñas hablan de anuncios, por ejemplo «There are just too many ads» (Character AI, 2 estrellas).</p>\n<p><strong>Solución:</strong> antes de dedicar semanas a crear un personaje, averigua qué es gratis. Abre la página de la app en la App Store, lee la lista de compras dentro de la app y usa la versión gratuita unos días antes de pagar. Si te suscribes y te arrepientes, <a href='https://support.apple.com/en-us/118428'>cancela desde Apple</a> en lugar de borrar la app. Una app sin suscripción quita la pregunta: la ficha de {app:6786747271} dice que no tiene suscripción, ni compras dentro de la app, ni anuncios; el chat completo de {app:6738960374} es gratis y su Premium opcional añade búsqueda web.</p>\n"],
        ["idcheck", "«Verificación de edad»: enseñar el DNI o la cara para chatear",
         "<p>Es la queja de privacidad más grande de los datos, y no trata de los chats: unas 80 reseñas hablan de que te pidan verificar la edad con un documento o la cara. «I'm not showing my identification to an app that's invasion of my privacy» (Character AI, 1 estrella); «You don't need my selfie. Cancelling and deleting.» (Replika, 1 estrella).</p>\n<p><strong>Solución:</strong> antes de registrarte, comprueba si la app pide la cara o un documento y decide si una conversación vale la pena. La forma más sencilla de evitar la pregunta es una app sin cuenta. La ficha de {app:6786747271} dice que no hay cuenta ni inicio de sesión, y la de {app:6738960374} dice que no hay cuentas. No comprobamos por qué pide cada app en la nube; lee antes la explicación de la propia app.</p>\n"],
        ["cloud", "«Cero privacidad»: quién puede leer tus chats",
         "<p>Unas 34 reseñas hablan de quién ve los chats o los datos: «It trains on and reviews every thing you send it» (Pi, 1 estrella); «they keep every last conversation on file» (Nomi, 1 estrella); «all kindroid chats monitored» (Kindroid, 1 estrella); «their privacy policy is vague» (Tolan, 1 estrella). Son palabras de quienes reseñan; no hemos verificado ninguna.</p>\n<p>Lo que sí podemos comprobar es la etiqueta de privacidad de la App Store de cada app a 14 de noviembre de 2026:</p>\n<ul>\n<li>Replika: datos usados para seguirte (identificadores, datos de uso); vinculados a ti (ubicación, datos de contacto, identificadores, datos de uso).</li>\n<li>Character AI: usados para seguirte (ubicación, datos de contacto, identificadores, datos de uso); vinculados a ti (compras, información financiera, ubicación, datos de contacto, contenido del usuario, historial de búsqueda, identificadores, datos de uso, diagnóstico).</li>\n<li>Nomi: vinculados a ti (compras, datos de contacto, contenido del usuario, identificadores, datos de uso, diagnóstico).</li>\n<li>Pi: vinculados a ti (identificadores, datos de uso, diagnóstico).</li>\n<li>Tolan: usados para seguirte (compras, ubicación, datos de contacto, identificadores, datos de uso, otros datos); vinculados a ti (compras, datos de contacto, contenido del usuario, identificadores, datos de uso, diagnóstico, otros datos).</li>\n<li>Kindroid: usados para seguirte (identificadores, datos de uso); vinculados a ti (datos de contacto, identificadores).</li>\n<li>Talking Friday y Cora: Data Not Collected.</li>\n</ul>\n<p><strong>Solución:</strong> no le cuentes a un compañero en la nube nada que no quisieras tener en un servidor. Para lo que quieras decir en privado, usa una app que funcione en el iPhone. La ficha de {app:6786747271} dice que tu voz se procesa en el iPhone y nunca se sube, y que sigue funcionando en modo avión; la de {app:6738960374} dice que nunca envía tus conversaciones a servidores externos. Son afirmaciones de los desarrolladores, respaldadas por sus etiquetas; no las hemos probado. Puedes hacer la prueba tú: activa el modo avión a mitad de una conversación y mira si sigue.</p>\n"],
        ["memory", "«Se olvida de todo»",
         "<p>Unas 54 reseñas dicen que el compañero se olvida: «It forgets things within a few exchanges» (Replika, 1 estrella); «about every 4 to 5 days it loses access to its entire memory» (Replika, 1 estrella). Después de Replika, la app más citada aquí es Kindroid (15 reseñas), incluidas personas que pagaron por una memoria más larga.</p>\n<p><strong>Solución:</strong> ninguna app hace que esto desaparezca. Guarda una nota corta con los datos que quieres que sepa (tu nombre, pronombres, lo importante) y pégala cuando se olvide, o usa el campo de memoria o de historia de fondo si la app lo tiene. Para las apps en el dispositivo, <strong>no consta</strong>: ninguna ficha dice si la app recuerda chats anteriores, así que pruébala una semana antes de confiar en ella.</p>\n"],
        ["giveup", "Lo que cuesta quedarse en el iPhone",
         "<p>Quedarse en el iPhone tiene un coste. La ficha de {app:6786747271} dice que necesita un iPhone 15 Pro o más reciente y que es voz a voz, así que es un amigo con el que hablas, no un personaje que personalizas. {app:6738960374} funciona en Apple Intelligence en dispositivos compatibles o con modelos que descargas (de 400 MB a 3,5 GB, según su ficha), y su valoración es 3.0 con 2 valoraciones, así que está en una fase temprana. Ninguna ficha menciona fotos, avatares ni relaciones. Si quieres eso, está en las apps en la nube de arriba, con las compensaciones que describen las reseñas.</p>\n<ul>\n<li>Quieres hablar, gratis, sin que nada salga del teléfono: {app:6786747271} (iPhone 15 Pro o más reciente).</li>\n<li>Quieres chat de texto en el dispositivo, gratis: {app:6738960374}.</li>\n<li>Quieres un personaje con cara y pasado: una app en la nube, con el muro de pago y la etiqueta de arriba. Prueba antes la versión gratuita.</li>\n</ul>\n"],
    ],
    "faq": [
        ["¿Hay un compañero de IA que funcione sin internet?",
         "Algunas apps lo dicen. Las fichas de Talking Friday y Cora dicen que funcionan en el iPhone y sin internet. La mayoría de las apps de compañeros de las reseñas, como Replika y Character AI, son servicios en línea."],
        ["¿Las apps de compañeros de IA leen mis chats?",
         "Desde fuera no podemos saberlo. Algunas personas que reseñan dicen que sí, y que los chats se guardan. Lo que muestran las propias apps es su etiqueta de privacidad de la App Store: por ejemplo, el contenido del usuario de Nomi está vinculado a ti, igual que el de Character AI, mientras que Talking Friday y Cora tienen Data Not Collected."],
        ["¿Por qué las apps de compañeros de IA piden DNI o un selfi?",
         "Quienes reseñan Character AI, Replika y Kindroid describen pantallas de verificación de edad. No comprobamos por qué pide cada app; lee la explicación de la propia app antes de dar tu cara o un documento."],
        ["¿Qué compañero de IA es gratis y sin anuncios?",
         "Según su ficha, Talking Friday no tiene suscripción, ni compras dentro de la app, ni anuncios. El chat de Cora es gratis, y su Premium opcional añade búsqueda web. Quienes reseñan describen los anuncios sobre todo en Character AI."],
        ["¿Un compañero de IA en el dispositivo puede recordarme?",
         "No consta. Ni la ficha de Talking Friday ni la de Cora dicen si recuerdan chats anteriores, así que pruébalo antes de confiar en ello."],
    ],
    "sources_html": [
        "Reseñas: App Store de EE. UU., 2.606 descargadas de 6 apps, 1.207 con 1 o 2 estrellas, 14 de noviembre de 2026; recuentos por palabras clave, aproximados.",
        "Apps y etiquetas de privacidad: sus páginas de la App Store de EE. UU. y los datos de búsqueda de Apple, 14 de noviembre de 2026: {app:1158555867}, {app:1671705818}, {app:6450270929}, {app:6445815935}, {app:6477549878}, {app:6451038161}, {app:6786747271}, {app:6738960374}.",
        "<a href='https://support.apple.com/en-us/118428'>Cancelar una suscripción desde Apple</a>, Soporte de Apple.",
    ],
    "fix": "Si algo de esta página está desactualizado, <a href='mailto:sagalabs@proton.me'>avísanos</a> y lo corregiremos.",
    "not_on_sale": "{names} no está a la venta en la App Store de España: su nombre va sin enlace y los datos son los de la ficha de EE. UU.",
}

# ---- 16 Nov 2026: guías del 15 nov (traducción diaria). Enlaces a la tienda de España; datos de la búsqueda de hoy.
_ES_TN = "https://apps.apple.com/es/app/id1348028646"
_ES_GT = "https://apps.apple.com/es/app/id414706506"
_ES_MT = "https://apps.apple.com/es/app/id1018949559"
_ES_IT = "https://apps.apple.com/es/app/id288113403"
_ES_CANCEL = "https://support.apple.com/en-us/118428"
_ES_REFUND = "https://support.apple.com/en-us/118223"

TEXT["translator-complaints"] = {
    "path": "es/aplicaciones-traduccion-suscripcion-sin-sorpresas-iphone/",
    "kicker": "Guía de traductores",
    "title": "Alternativas a Translate Now sin una suscripción sorpresa (2026)",
    "h1": "Alternativas a Translate Now sin una suscripción sorpresa (2026)",
    "description": "Las apps de traducción reciben reseñas de 1 y 2 estrellas por suscripciones y cobros, por el modo sin conexión que falla y por los errores de red. Lo que dicen 157 reseñas recientes de cuatro apps de traducción y cómo comprobar cada una antes de pagar.",
    "llms": "Guía, 15 de noviembre de 2026: las tres quejas que más se repiten en 157 reseñas recientes de 1 y 2 estrellas de la App Store de Translate Now, Google Translate, Microsoft Translator e iTranslate: suscripciones y cobros tras cancelar (cerca de la mitad de las reseñas de Translate Now), el modo sin conexión que no funciona como se anuncia y los errores de red. Cada una tiene una comprobación que hacer antes de descargar o viajar. Los números son aproximados.",
    "stand": "Quejas de 157 reseñas recientes de la App Store de cuatro apps de traducción y una comprobación que hacer antes de pagar o viajar.",
    "answer": [
        "<strong>Para elegir un traductor sin una suscripción sorpresa, lee las condiciones de prueba y de renovación en su página de la App Store antes de descargarlo, pon un recordatorio para el día en que termine la prueba y sabe dónde cancelar: Ajustes, tu nombre, Suscripciones.</strong> Prueba el modo sin conexión en casa antes de un viaje, porque varias apps fallan ahí.",
        "En 157 reseñas de 1 y 2 estrellas de Translate Now, Google Translate, Microsoft Translator e iTranslate, las quejas más comunes fueron las suscripciones y los cobros (sobre todo en Translate Now), el modo sin conexión que no funciona como se esperaba y los errores de red. Cada una tiene una comprobación más abajo.",
    ],
    "sections": [
        ["data", "Qué miramos",
         "<p>Descargamos las reseñas más recientes de 1 y 2 estrellas de cuatro apps de traducción de la App Store de EE. UU.: <a href='" + _ES_TN + "'>Translate Now - AI Translator</a> (30 reseñas), <a href='" + _ES_GT + "'>Google Translate</a> (55), <a href='" + _ES_MT + "'>Microsoft Translator</a> (57) e <a href='" + _ES_IT + "'>iTranslate Translator</a> (15). Son 157 reseñas en total, las más recientes de cada app (hasta 100 por app), descargadas el 15 de noviembre de 2026. Tres grupos se repiten una y otra vez: el dinero (suscripciones, muros de pago, cobros tras cancelar), el modo sin conexión que no funciona como se espera y los errores de red.</p>\n<ul>\n<li>Suscripciones, muros de pago y cobros: cerca de la mitad de las reseñas de Translate Now (14 de 30) y 4 de 15 en iTranslate.</li>\n<li>Problemas sin conexión o «sin internet»: 5 de 55 en Google Translate y 6 de 57 en Microsoft Translator.</li>\n<li>Traducciones erróneas o malas: 10 de 55 en Google Translate.</li>\n</ul>\n<p>Las reseñas son opiniones de personas descontentas. No son una prueba de las apps.</p>\n"],
        ["money", "«Me cobraron después de cancelar» y la prueba (el grupo más grande)",
         "<p>Es el grupo más grande en Translate Now. Un reseñador: «I canceled the subscription and it still charged me» (Translate Now, 1 estrella). Otro: «Did not realize they were taking $10.98 a WEEK on a subscription fee» (Translate Now, 1 estrella). En iTranslate, la queja es la prueba: «Be sure to cancel after trial or pay $40 per month every month!» (iTranslate, 1 estrella). Algunos dicen que la parte gratuita es demasiado pequeña: «You have to pay for common languages» (Translate Now, 1 estrella). Son palabras de los reseñadores, no datos que hayamos comprobado en cada app.</p>\n<p>Las páginas de la App Store dicen lo que vende cada app. La página de Translate Now promociona una suscripción llamada Air Apps One. La de iTranslate dice que una prueba gratuita se convierte en suscripción de pago salvo que la renovación automática se desactive al menos 24 horas antes de que termine la prueba.</p>\n<p><strong>Solución, antes de descargar y antes de cualquier prueba:</strong></p>\n<ol>\n<li>Baja hasta el final de la página de la App Store y lee las condiciones de suscripción: el precio, con qué frecuencia se renueva y cuándo termina la prueba gratuita.</li>\n<li>Pon un recordatorio en el calendario para el día antes de que termine la prueba.</li>\n<li>Para revisar o parar una suscripción: abre Ajustes, toca tu nombre, toca Suscripciones, toca la suscripción y luego Cancelar suscripción. Los pasos de Apple están en <a href='" + _ES_CANCEL + "'>Cancelar una suscripción en Apple</a>. Borrar la app no cancela la suscripción.</li>\n<li>Si te cobraron después de cancelar, puedes pedir a Apple un reembolso: <a href='" + _ES_REFUND + "'>Solicitar un reembolso de apps o contenido comprado en Apple</a>. Apple decide.</li>\n</ol>\n"],
        ["offline", "«No funciona sin conexión» (Google Translate, Microsoft Translator)",
         "<p>Un traductor es más útil cuando no hay señal: en un avión o en el metro de una ciudad extranjera. Las reseñas dicen que ahí es donde fallan varias apps. Un reseñador de Google Translate: «It DOES NOT work offline as advertised…» (1 estrella). Otro, desde Japón: «This app was unusable if /when I wasn't connected to the internet» (2 estrellas). Un reseñador de Microsoft Translator dice que la app «removed the ability to download languages for offline use» (1 estrella).</p>\n<p>La página de iTranslate en la App Store dice lo mismo desde su lado: para usar el modo sin conexión hay que descargar antes los paquetes de idiomas.</p>\n<p><strong>Solución:</strong> prueba el modo sin conexión en casa, con Wi-Fi, antes de viajar. Apaga el Wi-Fi y los datos móviles, abre la app y traduce una frase. Si falla, falta el paquete de idioma o la app no ofrece el modo sin conexión para ese idioma. Busca en los ajustes de la app los idiomas descargables y, si no los encuentras, consulta antes la página de la App Store.</p>\n"],
        ["network", "«Error de red» (Microsoft Translator)",
         "<p>Microsoft Translator tiene las quejas de red más numerosas de este grupo, sobre todo por su modo de conversación en directo: «Keeps getting network error when trying to use live translation» (2 estrellas), de un reseñador que estaba en Wi-Fi. Otro reseñador dice que la app le pedía revisar la red mientras estaba en Wi-Fi.</p>\n<p><strong>Solución:</strong> cierra la app del todo, apaga y enciende el Wi-Fi y prueba con datos móviles. Si sigue fallando, usa el modo de texto, que es más lento pero a menudo funciona. Si necesitas un modo sin conexión fiable, decídelo antes de viajar, no en mitad de una conversación.</p>\n"],
        ["checklist", "Antes de descargar o viajar: una comprobación de 5 puntos",
         "<ul>\n<li>¿Leí las condiciones de suscripción y la duración de la prueba en la página de la App Store antes de descargar?</li>\n<li>¿Puse un recordatorio para el día antes de que termine la prueba?</li>\n<li>¿Probé el modo sin conexión en casa, con el Wi-Fi y los datos móviles apagados?</li>\n<li>¿Comprobé qué idiomas puedo descargar y si los necesito antes de salir?</li>\n<li>¿Sé dónde cancelar (<a href='" + _ES_CANCEL + "'>Apple: cancelar una suscripción</a>) y cómo pedir un reembolso (<a href='" + _ES_REFUND + "'>Apple: solicitar un reembolso</a>)?</li>\n</ul>\n"],
    ],
    "faq": [
        ["¿Qué app de traducción tiene menos quejas por suscripciones?",
         "Las reseñas no señalan un ganador. En este conjunto, Translate Now tuvo más quejas por suscripciones y cobros (14 de 30 reseñas recientes de 1 y 2 estrellas). Lee las condiciones de suscripción de cada app en la App Store antes de descargar."],
        ["¿Funciona Google Translate sin conexión en el iPhone?",
         "Algunos reseñadores dicen que no funciona sin conexión como se anuncia. Pruébalo en casa, con el Wi-Fi y los datos móviles apagados, antes de un viaje, y comprueba qué idiomas puedes descargar."],
        ["¿Cómo cancelo la suscripción de una app de traducción?",
         "En el iPhone, abre Ajustes, toca tu nombre, toca Suscripciones, toca la suscripción y luego Cancelar suscripción. Apple lo explica en su página sobre cómo cancelar una suscripción."],
        ["¿Puedo recuperar un cobro hecho después de cancelar?",
         "Puedes pedírselo a Apple. Su página sobre cómo solicitar un reembolso de apps o contenido comprado en Apple explica el proceso; la decisión es de Apple."],
    ],
    "sources_html": [
        "Reseñas: feed de reseñas de la App Store de EE. UU., la página más reciente de cada app, 157 reseñas de 1 o 2 estrellas, descargadas el 15 de noviembre de 2026; recuentos por palabras clave, aproximados.",
        "Apps: páginas de la App Store de EE. UU. y datos de búsqueda de Apple de Translate Now, Google Translate, Microsoft Translator e iTranslate, a 15 de noviembre de 2026.",
        "<a href='" + _ES_CANCEL + "'>Cancelar una suscripción en Apple</a>, Soporte de Apple.",
        "<a href='" + _ES_REFUND + "'>Solicitar un reembolso de apps o contenido comprado en Apple</a>, Soporte de Apple.",
    ],
    "fix": "Si algo de esta página está desactualizado, <a href='mailto:sagalabs@proton.me'>avísanos</a> y lo corregiremos.",
    "not_on_sale": "{names} no está a la venta en la App Store de España: su nombre va sin enlace y los datos son los de la ficha de EE. UU.",
}

_ES_FS = "https://apps.apple.com/es/app/id6752642525"
_ES_HD = "https://apps.apple.com/es/app/id6747442689"
_ES_CO = "https://apps.apple.com/es/app/id1603892248"
_ES_TCGP = "https://www.tcgplayer.com/categories/trading-and-collectible-card-games/pokemon"
_ES_CM = "https://www.cardmarket.com/en/Pokemon"
_ES_EBAY = "https://www.ebay.com/help/buying/search-tips/advanced-search?id=4044"
_ES_RANK = "https://reviewland.io/best-pokemon-card-scanner-apps-iphone/"

TEXT["tcg-price-complaints"] = {
    "path": "es/como-comprobar-precio-cartas-pokemon-sin-valores-erroneos-iphone/",
    "kicker": "Guía de precios de cartas",
    "title": "Cómo comprobar el precio de las cartas Pokémon sin valores erróneos ni muro de pago para escanear (2026)",
    "h1": "Cómo comprobar el precio de las cartas Pokémon sin valores erróneos ni muro de pago al escanear (2026)",
    "description": "Las apps de escaneo de cartas reciben reseñas de 1 a 3 estrellas por precios erróneos o cambiantes (21 %), muros de pago y límites de escaneo (21 %), cartas no reconocidas (12 %) y cargos sorpresa (8 %). Lo que dicen 895 reseñas y cómo comprobar un precio tú mismo.",
    "llms": "Guía, 15 de noviembre de 2026: las cuatro quejas que más se repiten en 895 reseñas de 1 a 3 estrellas de la App Store de las apps de escaneo de cartas FoilSnap, HoloDex y Collectr: precio erróneo o cambiante (21 %), muro de pago o límite de escaneos (cerca del 21 %), carta no reconocida (12 %) y cargos sorpresa (8 %). Cada una tiene una solución: comparar TCGplayer y Cardmarket, revisar los anuncios vendidos en eBay, buscar el número y la edición impresos, y leer antes las condiciones de prueba y los pasos de Apple para cancelar. Los números son aproximados.",
    "stand": "Quejas de 895 reseñas de la App Store y una comprobación que puedes hacer para cada una sin ninguna app.",
    "answer": [
        "<strong>Para comprobar el precio de una carta Pokémon sin un valor erróneo, trata el precio de un escáner como una primera estimación: confirma la carta exacta en TCGplayer y Cardmarket y luego mira por cuánto se vendió la misma carta en los anuncios vendidos de eBay.</strong> Para evitar un muro de pago al escanear, lee los límites gratuitos y las condiciones de prueba en la página de la app en la App Store antes de escanear, y sabe dónde cancelar en Ajustes: tu nombre, luego Suscripciones.",
        "En 895 reseñas de 1 a 3 estrellas de FoilSnap, HoloDex y Collectr, las quejas principales fueron un precio erróneo o cambiante (21 %), un muro de pago o límite de escaneos (cerca del 21 %), una carta no reconocida (12 %) y un cargo sorpresa (8 %). Cada una tiene abajo una solución que funciona hoy.",
    ],
    "sections": [
        ["data", "Qué miramos",
         "<p>Descargamos las reseñas recientes de 1 a 3 estrellas de las tres apps de escaneo de Pokémon y TCG con más reseñas: <a href='" + _ES_FS + "'>TCG Card Scanner - FoilSnap</a> (283 reseñas, gratis, 4,8), <a href='" + _ES_HD + "'>HoloDex - TCG Scan &amp; Collect</a> (284, gratis, 4,8) y <a href='" + _ES_CO + "'>Collectr - TCG Collector App</a> (328, gratis, 4,9), todas a 15 de noviembre de 2026, de siete tiendas de la App Store: 895 reseñas de 1 a 3 estrellas. Los recuentos salen de buscar palabras clave, así que son aproximados y una reseña puede contar en más de un grupo. Las cuatro quejas más importantes para comprobar precios:</p>\n<ul>\n<li>Precio erróneo, anticuado o cambiante: <strong>21 %</strong> (191 reseñas).</li>\n<li>Carta no reconocida o identificada mal: <strong>12 %</strong> (110).</li>\n<li>Muro de pago demasiado pronto o una app «gratuita» que no es gratis: <strong>11,5 %</strong> (103), más un límite de escaneos gratuitos: <strong>9,7 %</strong> (87).</li>\n<li>Cargo sorpresa, no se puede cancelar, cobro tras cancelar: <strong>8 %</strong> (75).</li>\n</ul>\n<p>Las reseñas son opiniones de personas descontentas, no una prueba de las apps. Para una clasificación de siete apps de escaneo según lo que dice cada ficha, mira <a href='" + _ES_RANK + "'>Las mejores apps para escanear cartas Pokémon en iPhone (2026)</a>.</p>\n"],
        ["wrongprice", "«Precio erróneo» y «un valor distinto en cada escaneo» (21 %)",
         "<p>Es la queja más frecuente, en las tres apps. Un reseñador de FoilSnap: «Results were all different values ranging from cents to $25.» (reseña de 1 a 3 estrellas, EE. UU.). Duele sobre todo cuando usas el precio para vender o cambiar cartas.</p>\n<p><strong>Solución, en cinco pasos que puedes hacer hoy sin ninguna app extra:</strong></p>\n<ol>\n<li>Localiza los datos de la carta: su nombre, el número impreso (normalmente cerca del borde inferior) y el símbolo o código de la edición. Dos cartas con el mismo nombre pueden valer cantidades muy distintas.</li>\n<li>Busca ese nombre y número en <a href='" + _ES_TCGP + "'>TCGplayer</a> y abre la versión exacta (holo, holo inverso, primera edición, idioma). Lee el precio de mercado y los anuncios más baratos, no un solo número.</li>\n<li>Compara la misma carta en <a href='" + _ES_CM + "'>Cardmarket</a>, que muestra precios europeos en euros. Si los dos sitios están muy lejos, una de las dos cifras es otra versión o otro estado. (Cardmarket puede no cargar para herramientas automáticas, pero se abre en un navegador normal.)</li>\n<li>Mira por cuánto se vendió de verdad: en eBay, busca la carta y filtra por artículos vendidos (<a href='" + _ES_EBAY + "'>eBay: cómo funciona la búsqueda avanzada</a>). Los precios vendidos son lo que la gente pagó; los precios pedidos son solo esperanzas.</li>\n<li>Compara el mismo estado. Una carta en casi perfecto estado y una copia usada de la misma carta se venden a precios distintos, y un escáner no ve una esquina doblada en una foto.</li>\n</ol>\n<p>Haz la misma comprobación si el escáner da un precio muy bajo, como en la reseña «Most of my cards prices of 50p 30p or 10p» (FoilSnap, Reino Unido): un precio que parece demasiado bajo o demasiado alto es una señal para comparar, no para fiarse.</p>\n"],
        ["notrecognised", "«No reconoce mi carta» (12 %)",
         "<p>Cerca del 12 % de las reseñas dicen que la app dio el nombre equivocado de la carta o de la edición: «Every time you scan it gives you the wrong name of the card» (FoilSnap, EE. UU.). Casi una cuarta parte (23 %) de las reseñas de 1 a 3 estrellas de FoilSnap trata de esto. La propia ficha de FoilSnap reconoce el problema de fondo: dice que los escáneres normales a menudo identifican mal las cartas por el reflejo de los hologramas.</p>\n<p><strong>Solución:</strong> no te fíes de un nombre que no has leído. Compara el nombre, el número y el símbolo de edición que muestra la app con lo que está impreso en la carta. Si no coinciden, busca el número y la edición a mano en <a href='" + _ES_TCGP + "'>TCGplayer</a>. Para el escaneo en sí, pon la carta plana sobre un fondo liso, oscuro o claro, e inclínala lejos de las lámparas para que el brillo no refleje. Otro 8 % de las reseñas dice que falta un idioma («No support for German cards. Only English, Japanese and Chinese.», Collectr, Alemania), así que si tus cartas no están en inglés, revisa la ficha y la lista de cartas antes de pagar.</p>\n"],
        ["paywall", "«Muro de pago» y «solo 10 escaneos» (cerca del 21 %)",
         "<p>Otro 21 % de las reseñas trata del dinero antes que del valor: muros de pago que llegan demasiado pronto (11,5 %) y un límite de escaneos gratuitos (9,7 %). «Immediate pay wall for core app functionality» (HoloDex, Canadá). «After you scan 35 cards they make you pay» (Collectr, EE. UU.). Las fichas coinciden: la de HoloDex dice que las compras dentro de la app desbloquean escaneos ilimitados, filtros exclusivos y valoración con IA, y la de Collectr dice que el escaneo ilimitado necesita una compra dentro de la app. Las tres apps se descargan gratis, lo que no es lo mismo que usarlas gratis.</p>\n<p><strong>Solución:</strong> antes de escanear una colección, lee la página de la app en la App Store, la descripción y la lista de compras dentro de la app. Busca las palabras «ilimitado», «premium» o «compra dentro de la app» junto a lo que quieres. Dos fichas dicen que los precios son gratis: la de Dex dice que sus precios de TCGplayer, Cardmarket, eBay y CardTrader son gratis para todos, y la de PriceCharting dice que la app es completamente gratuita. Para una o dos cartas, quizá no necesites ninguna app: los pasos de arriba, hechos en una web, no cuestan nada. Hemos puesto los límites gratuitos que pudimos leer, uno al lado del otro, en <a href='" + _ES_RANK + "'>nuestra clasificación de siete apps de escaneo de cartas</a>.</p>\n"],
        ["charged", "«Me cobraron» y «no me dejaba cancelar» (8 %)",
         "<p>Cerca del 8 % trata de cobros: «Tried to cancel and it wouldn't let me and it auto renewed.» (FoilSnap, EE. UU.). Es la queja principal de FoilSnap después de los precios (15 % de sus reseñas de 1 a 3 estrellas). La ficha de FoilSnap dice, como muchas apps, que una suscripción se renueva sola salvo que canceles al menos 24 horas antes de que termine el periodo actual.</p>\n<p><strong>Solución, en tu iPhone, en menos de un minuto:</strong></p>\n<ol>\n<li>Antes de empezar una prueba gratuita, lee la hoja de pago: muestra el precio, con qué frecuencia se renueva y la fecha en que termina la prueba.</li>\n<li>Pon un recordatorio en el calendario para el día antes de que termine la prueba.</li>\n<li>Para revisarlo o pararlo: abre Ajustes, toca tu nombre, toca Suscripciones, toca la suscripción y luego Cancelar suscripción. Los pasos de Apple están en <a href='" + _ES_CANCEL + "'>Cancelar una suscripción en Apple</a>. Borrar la app no cancela la suscripción.</li>\n<li>Si te cobraron sin querer, puedes pedir un reembolso: <a href='" + _ES_REFUND + "'>Solicitar un reembolso de apps o contenido comprado en Apple</a>. Apple decide.</li>\n</ol>\n"],
        ["checklist", "Antes de confiar en un precio o empezar una prueba: una comprobación de 5 puntos",
         "<ul>\n<li>¿Leí el nombre, el número y la edición de la carta, y coinciden con lo que dice la app?</li>\n<li>¿Comparé el precio en TCGplayer y Cardmarket para la misma versión y el mismo estado?</li>\n<li>¿Miré los anuncios vendidos en eBay antes de vender o cambiar?</li>\n<li>¿Leí la lista de compras dentro de la app y las condiciones de la prueba antes de escanear?</li>\n<li>¿Sé la fecha en que termina la prueba y dónde cancelar (<a href='" + _ES_CANCEL + "'>Apple: cancelar una suscripción</a>)?</li>\n</ul>\n"],
    ],
    "faq": [
        ["¿Qué precisión tienen las apps de escaneo de cartas Pokémon?",
         "Varía. En 895 reseñas de 1 a 3 estrellas de FoilSnap, HoloDex y Collectr, el 21 % menciona un precio erróneo, anticuado o cambiante, y el 12 %, una carta no reconocida. Usa el valor de la app como primera estimación y comprueba la carta exacta en TCGplayer y Cardmarket."],
        ["¿Por qué un escáner muestra un precio distinto cada vez?",
         "Las reseñas no dicen por qué. Una reseñadora de FoilSnap obtuvo valores desde céntimos hasta 25 $ para la misma carta en diez escaneos. Otra versión, otro estado u otra fuente pueden cambiar la cifra, así que confírmala en un mercado."],
        ["¿Dónde puedo comprobar precios de cartas Pokémon gratis?",
         "TCGplayer y Cardmarket muestran precios de cartas Pokémon en sus webs, y los anuncios vendidos de eBay muestran por cuánto se vendieron. La ficha de Dex en la App Store dice que sus precios son gratis para todos."],
        ["¿Cómo cancelo la suscripción de una app de escaneo de cartas?",
         "En el iPhone, abre Ajustes, toca tu nombre, toca Suscripciones, toca la suscripción y luego Cancelar suscripción. Apple lo explica en su página sobre cómo cancelar una suscripción."],
        ["¿Puedo pedir un reembolso a la App Store?",
         "Puedes pedirlo. Apple explica cómo en su página sobre cómo solicitar un reembolso de apps o contenido comprado en Apple; la aprobación depende de Apple."],
    ],
    "sources_html": [
        "Reseñas: App Store de EE. UU., CA, Reino Unido, DE, AU, FR y JP; 895 reseñas de 1 a 3 estrellas de tres apps, descargadas el 15 de noviembre de 2026; recuentos por palabras clave, aproximados.",
        "<a href='" + _ES_CANCEL + "'>Cancelar una suscripción en Apple</a>, Soporte de Apple.",
        "<a href='" + _ES_REFUND + "'>Solicitar un reembolso de apps o contenido comprado en Apple</a>, Soporte de Apple.",
        "<a href='" + _ES_TCGP + "'>TCGplayer: Pokémon</a>; <a href='" + _ES_CM + "'>Cardmarket: Pokémon</a>; <a href='" + _ES_EBAY + "'>eBay: búsqueda avanzada</a>.",
        "Apps: sus páginas de la App Store de EE. UU. y datos de búsqueda de Apple, 15 de noviembre de 2026. <a href='" + _ES_RANK + "'>Las mejores apps para escanear cartas Pokémon en iPhone (2026)</a>, Reviewland.",
    ],
    "fix": "Si algo de esta página está desactualizado, <a href='mailto:sagalabs@proton.me'>avísanos</a> y lo corregiremos.",
    "not_on_sale": "{names} no está a la venta en la App Store de España: su nombre va sin enlace y los datos son los de la ficha de EE. UU.",
}
