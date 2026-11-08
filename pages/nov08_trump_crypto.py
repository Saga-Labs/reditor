"""News (8 Nov 2026): Democrats' planned investigations into the Trump family's crypto after the midterms, and how
WLFI, TRUMP and USD1 moved from 1 to 8 November (EN + ES). Moved here from aisagalab.com on 8 Nov 2026 (Marta: "Estos
artículos no pegan en aisagalab. Pegan en reditor o en reviewland").

Checked 8 Nov 2026 (same data as the aisagalab original, SagaLab commit 7a6278d):
- crypto.news, 4 Nov 2026 (Rony Roy): House to Democrats per NBC News and MS NOW; Robert Garcia, «Lawyer up.»;
  investigations from February 2027; WLFI, USD1, World Liberty Trust, TRUMP, Changpeng Zhao pardon (he denies it);
  49 % and $500M from Tahnoon; Reuters, $2.3B; more than $1B and ~$635M from TRUMP; Lauren Bis to Newsweek.
- Reuters in The Star, 15 Aug 2026: OCC preliminary conditional approval on 14 Aug 2026, not final.
- CNBC, 5 Nov 2026 (Tanaya Macheel): CLARITY failed Senate cloture in September.
- FT, 8 Nov 2026: headline only (paywalled).
- Prices: CoinGecko API, daily UTC close of 1 Nov and value of 8 Nov ~10:20 UTC.
- Crypton 2.0.8 (search any CoinGecko coin), no price alerts in the version on sale.
Reditor rules: Crypton is one option among three, in the middle; no ownership line in the article (footer, About and
llms.txt name our apps); Crypton links carry pt+ct, competitors plain App Store links. No political opinion, no predictions.
"""

D = "2026-11-08"
CRYPTON_ID = 1143691286
COINGECKO_APP = "https://apps.apple.com/us/app/id1390323960"
CMC_APP = "https://apps.apple.com/us/app/id1282107098"
CN = "https://crypto.news/democrats-prepare-to-investigate-world-liberty-financial-after-house-win/"
CNBC = "https://www.cnbc.com/2026/11/05/crypto-midterms-democrats-clarity-act.html"
OCC = "https://www.thestar.com.my/tech/tech-news/2026/08/15/us-regulator-approves-bank-charter-for-trump-backed-crypto-company-world-liberty-financial"
RL = "https://reviewland.io/best-apps-to-track-wlfi-trump-coin-iphone/"
CG = {"TRUMP": "https://www.coingecko.com/en/coins/official-trump",
      "WLFI": "https://www.coingecko.com/en/coins/world-liberty-financial",
      "USD1": "https://www.coingecko.com/en/coins/usd1-wlfi",
      "BTC": "https://www.coingecko.com/en/coins/bitcoin"}
# Crypton link: build.py replaces {CRYPTON} with store_link(id, ct) of each page.
CRYPTON = "{CRYPTON}"


def a(u, t):
    return f'<a href="{u}">{t}</a>'


def ul(items):
    return "<ul>\n" + "".join(f"<li>{x}</li>\n" for x in items) + "</ul>\n"


def table(th, rows, note):
    return ('<div class="scroll"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in th) + "</tr></thead>\n<tbody>\n"
            + "".join("<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>\n" for r in rows)
            + f'</tbody></table></div>\n<p class="note">{note}</p>\n')


EN_PATH = "trump-crypto-midterms-investigation-wlfi-trump-usd1/"
ES_PATH = "es/criptos-de-trump-tras-las-elecciones-investigacion-wlfi-trump-usd1/"

COMMON = {"group": "trump-crypto-news", "kind": "news", "store": "us", "category": "FinanceApplication",
          "published": D, "updated": D, "checked": D, "apps": []}

PAGES = [{
    **COMMON, "lang": "en", "path": EN_PATH, "ct": "rd-trump-crypto-midterms",
    "kicker": "Crypto news",
    "title": "Trump Family Crypto After the Midterms: WLFI, TRUMP and USD1 (8 Nov 2026)",
    "h1": "Trump family crypto after the midterms: what Democrats plan to investigate, and how WLFI, TRUMP and USD1 moved",
    "description": ("After Democrats won the House on 3 November 2026, reports say they plan to investigate World Liberty "
                    "Financial (WLFI, USD1) and the TRUMP meme coin. A dated timeline, CoinGecko prices from 1 to 8 November, "
                    "what to watch next and how to follow these tokens on iPhone."),
    "llms": ("News, 8 November 2026: what has been reported about Democrats' planned investigations into World Liberty Financial "
             "(WLFI, USD1), World Liberty Trust and the TRUMP meme coin after the 3 November midterms, with a dated timeline, "
             "CoinGecko prices from 1 to 8 November (TRUMP about -32%, WLFI about -8%, USD1 near $1), what to watch next and three "
             "iPhone apps to follow the tokens (CoinGecko, Crypton, CoinMarketCap). Not financial advice."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "What has been reported, with dates and sources, and what the prices did in the week after the vote.",
    "answer": [
        "<strong>After Democrats won the House in the 3 November 2026 midterms, Rep. Robert Garcia, expected to chair "
        "the House Oversight Committee, signalled investigations into the Trump family's crypto businesses, which "
        "according to " + a(CN, "crypto.news") + " could begin as early as February 2027.</strong> In the week after "
        "the vote, CoinGecko data show the TRUMP meme coin down about 32%, World Liberty Financial's WLFI token down "
        "about 8%, and the USD1 stablecoin holding close to $1.",
    ],
    "sections": [
        ("reported", "What has been reported",
         "<p>According to " + a(CN, "crypto.news") + ", which cited NBC News and MS NOW projections, Democrats won "
         "control of the House. It reported that Garcia answered the result with two words, &ldquo;Lawyer up,&rdquo; "
         "and that committees could seek documents and testimony by subpoena.</p>\n"
         "<p>The targets named in that reporting are:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, its WLFI token and its USD1 stablecoin, including its foreign "
             "ownership. crypto.news reported that an investment vehicle of the UAE's Sheikh Tahnoon bin Zayed took a 49% "
             "stake, for a reported $500 million, shortly before the January 2025 inauguration.",
             "<strong>World Liberty Trust Company</strong>, the planned trust bank for USD1. Reuters reported that the "
             "Office of the Comptroller of the Currency gave it preliminary conditional approval on 14 August 2026, and that "
             "it is not final (" + a(OCC, "Reuters, via The Star") + ").",
             "<strong>The TRUMP meme coin.</strong> According to crypto.news, Trump reported more than $1 billion of "
             "crypto-related income for 2025, about $635 million of it in royalties tied to the coin, and Reuters estimated "
             "that the family's crypto ventures earned at least $2.3 billion.",
             "<strong>The pardon of Binance founder Changpeng Zhao.</strong> crypto.news reported that Zhao denies business "
             "ties to the family and says he never discussed any clemency arrangement.",
             "Business dealings of other family members."]) +
         "<p>White House spokeswoman Lauren Bis told Newsweek, as cited by crypto.news, that the Democrats' plans are a "
         "continuation of what she described as a long-running witch hunt against the president. On 8 November the "
         "Financial Times carried the story on its front page under the headline <em>Crypto industry braces for reckoning "
         "over Trump ties</em>.</p>\n"),
        ("timeline", "Timeline", ul([
            "<strong>Before January 2025.</strong> A vehicle of Sheikh Tahnoon bin Zayed reportedly takes 49% of World Liberty Financial (crypto.news).",
            "<strong>14 August 2026.</strong> The OCC gives World Liberty Trust Company preliminary conditional approval (Reuters).",
            "<strong>September 2026.</strong> The CLARITY Act fails a Senate cloture vote (CNBC).",
            "<strong>3 November 2026.</strong> Midterm elections; Democrats win the House, according to NBC News and MS NOW projections.",
            "<strong>4 November 2026.</strong> TRUMP has its largest daily fall of the week on CoinGecko, from $1.59 to $1.27. crypto.news reports the planned investigations.",
            "<strong>5 November 2026.</strong> CNBC reports that the result puts the crypto industry on the defensive in Washington.",
            "<strong>8 November 2026.</strong> The Financial Times runs the story on its front page.",
            "<strong>From February 2027.</strong> Investigations could begin, according to crypto.news."])),
        ("prices", "How the tokens moved, 1 to 8 November", table(
            ("Token", "1 Nov (daily close)", "8 Nov", "Change", "Market cap, 8 Nov"),
            [("TRUMP (Official Trump)", "$1.71", "$1.16", "&minus;32%", "~$328 million"),
             ("WLFI (World Liberty Financial)", "$0.050", "$0.046", "&minus;8%", "~$1.47 billion"),
             ("USD1 (stablecoin)", "$0.998", "$0.998", "0%", "~$3.44 billion (from ~$3.87 billion)"),
             ("Bitcoin, for comparison", "$78,294", "$75,806", "&minus;3%", "")],
            "Source: CoinGecko, daily close in UTC for 1 November and the price on the morning of 8 November (UTC). Rounded. "
            "USD1 kept its price, while its market cap on CoinGecko fell by about $430 million over the week. Bitcoin also fell "
            "over the same week, so not every move can be put down to the news.")),
        ("next", "What to watch next", ul([
            "<strong>When the committees start.</strong> crypto.news reported that investigations could begin as early as "
            "February 2027, once the new House is in place.",
            "<strong>The CLARITY Act.</strong> " + a(CNBC, "CNBC") + " reported that the market-structure bill had already failed "
            "a Senate cloture vote in September; analysts it quoted expect either a tougher Democratic version next year or no "
            "movement until 2028.",
            "<strong>The trust bank.</strong> World Liberty Trust Company's approval is preliminary and conditional; the OCC "
            "still has to give final approval (Reuters)."])),
        ("track", "How to track WLFI, TRUMP and USD1 on iPhone",
         "<p>Any crypto tracker that uses CoinGecko or CoinMarketCap data lists all three. Three options:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), the source of the prices in this article, "
             "with price alerts and widgets.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): search for WLFI, TRUMP or USD1 by name or symbol, add "
             "them to your favourites and pick them for the Coin List widget on your Home Screen. If you hold any, add the amount "
             "and your average buy price to see profit and loss. It works without an account, and it has no price alerts in the "
             "version on sale.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), with price alerts and widgets."]) +
         "<p>reviewland compares more apps for these three tokens, by alerts, widgets and price, in "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + ". If you used Blockfolio, see "
         '<a href="/blockfolio-alternatives-iphone/">Blockfolio alternatives for iPhone</a>.</p>\n'
         '<p class="note">Not financial advice. This article reports what others have published and what prices did; it does '
         "not recommend buying or selling anything.</p>\n"),
    ],
    "faq": [
        ("Are Democrats investigating Trump's crypto?", "According to crypto.news, after winning the House on 3 November 2026, Democrats plan to look at World Liberty Financial, USD1, the TRUMP meme coin and related deals, and investigations could begin as early as February 2027."),
        ("How did the TRUMP coin react to the midterms?", "On CoinGecko it went from $1.71 at the 1 November close to about $1.16 on 8 November, a fall of about 32%, with the largest daily drop on 4 November."),
        ("Did USD1 lose its peg?", "No. On CoinGecko it stayed close to $1 in the week after the vote, at about $0.998 on 8 November."),
        ("How can I follow WLFI and TRUMP on iPhone?", "Search for them in a tracker that uses CoinGecko or CoinMarketCap data, such as CoinGecko, Crypton or CoinMarketCap, add them to a watchlist and put them on a Home Screen widget."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 November 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 November 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15 August 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 November 2026 (paywalled; headline only).",
        "Prices: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", read on 8 November 2026.",
        "Apps: their US App Store pages, 8 November 2026.",
    ],
    "fix": 'If something here is out of date, <a href="mailto:sagalabs@proton.me">tell us</a> and we will fix the page.',
}, {
    **COMMON, "lang": "es", "path": ES_PATH, "ct": "rd-trump-crypto-midterms-es",
    "kicker": "Noticias cripto",
    "title": "Las criptos de Trump tras las elecciones: WLFI, TRUMP y USD1 (8 nov 2026)",
    "h1": "Las criptos de la familia Trump tras las elecciones: qué quieren investigar los demócratas y cómo se han movido WLFI, TRUMP y USD1",
    "description": ("Tras ganar los demócratas la Cámara de Representantes el 3 de noviembre de 2026, varios medios cuentan que "
                    "investigarán World Liberty Financial (WLFI, USD1) y la memecoin TRUMP. Cronología, precios de CoinGecko del 1 "
                    "al 8 de noviembre, qué vigilar y cómo seguir estos tokens en el iPhone."),
    "llms": ("Noticia, 8 de noviembre de 2026: lo publicado sobre las investigaciones que preparan los demócratas a World Liberty "
             "Financial (WLFI, USD1), World Liberty Trust y la memecoin TRUMP tras las elecciones del 3 de noviembre, con cronología, "
             "precios de CoinGecko del 1 al 8 de noviembre, qué vigilar y tres apps de iPhone para seguir los tokens (CoinGecko, "
             "Crypton, CoinMarketCap). No es asesoramiento financiero."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Lo publicado hasta ahora, con fecha y fuente, y qué hicieron los precios la semana siguiente a la votación.",
    "answer": [
        "<strong>Los demócratas ganaron la Cámara de Representantes en las elecciones del 3 de noviembre de 2026, y "
        "el congresista Robert Garcia, que previsiblemente presidirá el Comité de Supervisión, ha dado a entender que "
        "habrá investigaciones sobre los negocios cripto de la familia Trump; según " + a(CN, "crypto.news") + ", "
        "podrían empezar en febrero de 2027.</strong> En la semana posterior, según CoinGecko, la memecoin TRUMP bajó "
        "un 32 %, el token WLFI de World Liberty Financial un 8 % y la stablecoin USD1 se mantuvo cerca de 1 dólar.",
    ],
    "sections": [
        ("publicado", "Qué se ha publicado",
         "<p>Según " + a(CN, "crypto.news") + ", que cita las proyecciones de NBC News y MS NOW, los demócratas se quedan "
         "con la Cámara. El medio cuenta que Garcia respondió al resultado con un aviso de dos palabras, «Lawyer up» "
         "(«búsquense abogado»), y que los comités podrán pedir documentos y declaraciones por citación.</p>\n"
         "<p>Lo que esa información señala como objetivo:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, con su token WLFI y su stablecoin USD1, y quién es dueño de qué. "
             "crypto.news publica que un vehículo de inversión del jeque emiratí Tahnoon bin Zayed se quedó con el 49 %, por "
             "unos 500 millones de dólares, poco antes de la toma de posesión de enero de 2025.",
             "<strong>World Liberty Trust Company</strong>, el banco fiduciario previsto para USD1. Según Reuters, la "
             "Oficina del Contralor de la Moneda (OCC) le dio una aprobación preliminar y condicional el 14 de agosto de 2026, "
             "que todavía no es definitiva (" + a(OCC, "Reuters, en The Star") + ").",
             "<strong>La memecoin TRUMP.</strong> Según crypto.news, Trump declaró más de 1.000 millones de dólares de "
             "ingresos ligados a las cripto en 2025, unos 635 millones por derechos vinculados a esta moneda; Reuters calcula "
             "que los negocios cripto de la familia han ganado al menos 2.300 millones.",
             "<strong>El indulto a Changpeng Zhao</strong>, fundador de Binance. crypto.news recoge que Zhao niega tener "
             "negocios con la familia y haber hablado nunca de un indulto.",
             "Negocios de otros miembros de la familia."]) +
         "<p>La portavoz de la Casa Blanca Lauren Bis dijo a Newsweek, según crypto.news, que lo que buscan los demócratas "
         "es seguir con lo que ella llama una caza de brujas contra el presidente que dura ya años. El 8 de noviembre el "
         "Financial Times lo llevó a portada con el titular <em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("cronologia", "Cronología", ul([
            "<strong>Antes de enero de 2025.</strong> Un vehículo del jeque Tahnoon bin Zayed se queda, según la prensa, con el 49 % de World Liberty Financial (crypto.news).",
            "<strong>14 de agosto de 2026.</strong> La OCC da a World Liberty Trust Company una aprobación preliminar y condicional (Reuters).",
            "<strong>Septiembre de 2026.</strong> La ley CLARITY no supera una votación de cloture en el Senado (CNBC).",
            "<strong>3 de noviembre de 2026.</strong> Elecciones de mitad de mandato; los demócratas ganan la Cámara, según las proyecciones de NBC News y MS NOW.",
            "<strong>4 de noviembre de 2026.</strong> TRUMP tiene en CoinGecko su mayor caída diaria de la semana, de 1,59 a 1,27 dólares. crypto.news informa de las investigaciones.",
            "<strong>5 de noviembre de 2026.</strong> CNBC publica que el resultado deja al sector cripto a la defensiva en Washington.",
            "<strong>8 de noviembre de 2026.</strong> El Financial Times lo lleva a portada.",
            "<strong>Desde febrero de 2027.</strong> Podrían empezar las investigaciones, según crypto.news."])),
        ("precios", "Cómo se movieron los tokens del 1 al 8 de noviembre", table(
            ("Token", "1 nov (cierre)", "8 nov", "Cambio", "Capitalización, 8 nov"),
            [("TRUMP (Official Trump)", "1,71 $", "1,16 $", "&minus;32 %", "~328 millones $"),
             ("WLFI (World Liberty Financial)", "0,050 $", "0,046 $", "&minus;8 %", "~1.470 millones $"),
             ("USD1 (stablecoin)", "0,998 $", "0,998 $", "0 %", "~3.440 millones $ (desde ~3.870 millones)"),
             ("Bitcoin, para comparar", "78.294 $", "75.806 $", "&minus;3 %", "")],
            "Fuente: CoinGecko, cierre diario en UTC del 1 de noviembre y precio de la mañana del 8 de noviembre (UTC), redondeado. "
            "USD1 mantuvo el precio, pero su capitalización en CoinGecko bajó unos 430 millones de dólares en la semana. El bitcoin "
            "también bajó esa semana, así que no todo movimiento se puede atribuir a la noticia.")),
        ("vigilar", "Qué vigilar a partir de ahora", ul([
            "<strong>Cuándo arrancan los comités.</strong> crypto.news apunta a febrero de 2027 como pronto, ya con la nueva Cámara.",
            "<strong>La ley CLARITY.</strong> Según " + a(CNBC, "CNBC") + ", la ley sobre la estructura del mercado cripto ya se "
            "atascó en el Senado en septiembre; los analistas que cita esperan o una versión más dura de los demócratas el año que "
            "viene o nada hasta 2028.",
            "<strong>El banco fiduciario.</strong> La aprobación de World Liberty Trust Company es preliminar y condicional: la OCC "
            "aún tiene que dar la definitiva (Reuters)."])),
        ("seguir", "Cómo seguir WLFI, TRUMP y USD1 en el iPhone",
         "<p>Cualquier app que use datos de CoinGecko o CoinMarketCap tiene los tres. Tres opciones:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), de donde salen los precios de este artículo, "
             "con alertas de precio y widgets.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): busca WLFI, TRUMP o USD1 por nombre o símbolo, añádelos "
             "a favoritos y elígelos en el widget de lista de monedas de la pantalla de inicio. Si tienes alguno, pon la cantidad y "
             "tu precio medio de compra y verás cuánto ganas o pierdes. No hace falta cuenta, y la versión a la venta no tiene "
             "alertas de precio.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), con alertas de precio y widgets."]) +
         "<p>En reviewland hay una comparativa de más apps para estos tres tokens, por alertas, widgets y precio: "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (en inglés).</p>\n"
         '<p class="note">Esto no es asesoramiento financiero. Contamos lo que otros han publicado y lo que hicieron los precios; '
         "no recomendamos comprar ni vender nada.</p>\n"),
    ],
    "faq": [
        ("¿Van a investigar los demócratas las criptos de Trump?", "Según crypto.news, tras ganar la Cámara el 3 de noviembre de 2026 quieren examinar World Liberty Financial, USD1, la memecoin TRUMP y otros negocios, y las investigaciones podrían empezar en febrero de 2027."),
        ("¿Cómo reaccionó la moneda TRUMP a las elecciones?", "En CoinGecko pasó de 1,71 dólares al cierre del 1 de noviembre a unos 1,16 el 8 de noviembre, un 32 % menos, con la mayor caída diaria el 4 de noviembre."),
        ("¿Ha perdido USD1 su paridad con el dólar?", "No. En CoinGecko se mantuvo cerca de 1 dólar la semana siguiente a la votación, en unos 0,998 el 8 de noviembre."),
        ("¿Cómo sigo WLFI y TRUMP en el iPhone?", "Búscalos en una app que use datos de CoinGecko o CoinMarketCap, como CoinGecko, Crypton o CoinMarketCap, añádelos a favoritos y ponlos en un widget de la pantalla de inicio."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 de noviembre de 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 de noviembre de 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters en The Star, 15 de agosto de 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 de noviembre de 2026 (de pago; solo el titular).",
        "Precios: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", consultado el 8 de noviembre de 2026.",
        "Apps: sus fichas del App Store de EE. UU., 8 de noviembre de 2026.",
    ],
    "fix": 'Si algo está desactualizado, <a href="mailto:sagalabs@proton.me">avísanos</a> y lo corregimos.',
}]
