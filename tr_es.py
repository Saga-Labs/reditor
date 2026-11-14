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
