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
}, {
    **COMMON, "lang": "ru", "path": "ru/kriptovaljuty-trampa-posle-vyborov-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-ru",
    "kicker": "Крипто-новости",
    "title": "Криптовалюты семьи Трампа после выборов: WLFI, TRUMP и USD1 (8 нояб. 2026)",
    "h1": "Криптовалюты семьи Трампа после промежуточных выборов: что собираются расследовать демократы и как двигались WLFI, TRUMP и USD1",
    "description": ("После того как 3 ноября 2026 года демократы получили большинство в Палате представителей, сообщается, что они "
                    "планируют расследовать World Liberty Financial (WLFI, USD1) и мем-монету TRUMP. Хронология, цены CoinGecko с 1 по "
                    "8 ноября, что отслеживать дальше и как следить за этими токенами на iPhone."),
    "llms": ("Новость, 8 ноября 2026 года: что сообщается о планах демократов расследовать World Liberty Financial (WLFI, USD1), "
             "World Liberty Trust и мем-монету TRUMP после промежуточных выборов 3 ноября, с хронологией, ценами CoinGecko с 1 по 8 ноября "
             "(TRUMP около −32 %, WLFI около −8 %, USD1 около 1 доллара), что отслеживать дальше и три приложения для iPhone, чтобы "
             "следить за токенами (CoinGecko, Crypton, CoinMarketCap). Это не финансовый совет."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Что сообщалось, с датами и источниками, и что делали цены в неделю после голосования.",
    "answer": [
        "<strong>После того как на промежуточных выборах 3 ноября 2026 года демократы получили большинство в Палате представителей, "
        "конгрессмен Роберт Гарсия, которому, вероятно, достанется председательство в комитете по надзору и расследованиям, дал понять, "
        "что будут расследования бизнеса семьи Трампа в сфере криптовалют; по данным " + a(CN, "crypto.news") + ", они могут начаться "
        "уже в феврале 2027 года.</strong> За неделю после голосования, по данным CoinGecko, мем-монета TRUMP упала примерно на 32 %, "
        "токен WLFI фонда World Liberty Financial — примерно на 8 %, а стейблкоин USD1 держался около 1 доллара.",
    ],
    "sections": [
        ("reported", "Что сообщалось",
         "<p>По данным " + a(CN, "crypto.news") + ", которое ссылается на прогнозы NBC News и MS NOW, демократы получили контроль "
         "над Палатой представителей. Издание пишет, что Гарсия ответил на итог двумя словами, «Lawyer up» («ищите адвоката»), и что "
         "комитеты смогут требовать документы и показания по повестке.</p>\n"
         "<p>Цели, которые назвало это издание:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, её токен WLFI и стейблкоин USD1, включая иностранное владение. crypto.news сообщает, "
             "что инвестиционная структура шейха Тахнуна бин Заида Аль Нахайяна из ОАЭ купила 49 % за, по сообщениям, 500 млн долларов "
             "незадолго до инаугурации в январе 2025 года.",
             "<strong>World Liberty Trust Company</strong>, планируемый траст-банк для USD1. Reuters сообщило, что Управление по контролю "
             "над денежным обращением (OCC) дало ему предварительное условное одобрение 14 августа 2026 года и что оно не окончательное ("
             + a(OCC, "Reuters, через The Star") + ").",
             "<strong>Мем-монета TRUMP.</strong> По данным crypto.news, Трамп сообщил о более чем 1 млрд долларов доходов, связанных с "
             "криптовалютой, за 2025 год, из них около 635 млн — роялти, связанные с монетой; Reuters оценило, что крипто-проекты семьи "
             "заработали не меньше 2,3 млрд долларов.",
             "<strong>Помилование основателя Binance Чанпэна Чжао.</strong> crypto.news сообщает, что Чжао отрицает деловые связи с семьёй "
             "и говорит, что никогда не обсуждал никаких договорённостей о помиловании.",
             "Деловые операции других членов семьи."]) +
         "<p>Пресс-секретарь Белого дома Лорен Бис сказала Newsweek, которую цитирует crypto.news, что планы демократов — продолжение того, "
         "что она назвала давней «охотой на ведьм» против президента. 8 ноября Financial Times вынесла эту историю на первую полосу под "
         "заголовком <em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "Хронология", ul([
            "<strong>До января 2025 года.</strong> Структура шейха Тахнуна бин Заида, по сообщениям, получает 49 % World Liberty Financial (crypto.news).",
            "<strong>14 августа 2026 года.</strong> OCC дает World Liberty Trust Company предварительное условное одобрение (Reuters).",
            "<strong>Сентябрь 2026 года.</strong> Закон CLARITY не проходит голосование о прекращении прений в Сенате (CNBC).",
            "<strong>3 ноября 2026 года.</strong> Промежуточные выборы; демократы получают большинство в Палате представителей по прогнозам NBC News и MS NOW.",
            "<strong>4 ноября 2026 года.</strong> TRUMP за неделю получает самое большое дневное падение на CoinGecko, с 1,59 до 1,27 доллара. crypto.news сообщает о планируемых расследованиях.",
            "<strong>5 ноября 2026 года.</strong> CNBC сообщает, что итог выборов ставит криптоиндустрию в оборону в Вашингтоне.",
            "<strong>8 ноября 2026 года.</strong> Financial Times выносит эту историю на первую полосу.",
            "<strong>С февраля 2027 года.</strong> Расследования могут начаться, по данным crypto.news."])),
        ("prices", "Как двигались токены с 1 по 8 ноября", table(
            ("Токен", "1 нояб. (дневное закрытие)", "8 нояб.", "Изменение", "Капитализация, 8 нояб."),
            [("TRUMP (Official Trump)", "$1,71", "$1,16", "&minus;32%", "~$328 млн"),
             ("WLFI (World Liberty Financial)", "$0,050", "$0,046", "&minus;8%", "~$1,47 млрд"),
             ("USD1 (стейблкоин)", "$0,998", "$0,998", "0%", "~$3,44 млрд (с ~$3,87 млрд)"),
             ("Bitcoin, для сравнения", "$78 294", "$75 806", "&minus;3%", "")],
            "Источник: CoinGecko, дневное закрытие в UTC за 1 ноября и цена утром 8 ноября (UTC). Округлено. USD1 сохранил цену, "
            "а его капитализация на CoinGecko за неделю упала примерно на 430 млн долларов. Bitcoin тоже падал в ту же неделю, "
            "поэтому не всё движение можно объяснить новостями.")),
        ("next", "Что отслеживать дальше", ul([
            "<strong>Когда начнут работать комитеты.</strong> crypto.news сообщает, что расследования могут начаться уже в феврале 2027 года, "
            "когда сформируется новая Палата.",
            "<strong>Закон CLARITY.</strong> " + a(CNBC, "CNBC") + " сообщает, что законопроект о структуре рынка уже провалился на "
            "голосовании о прекращении прений в Сенате в сентябре; аналитики, которых цитирует издание, ждут либо более жёсткой версии "
            "от демократов в следующем году, либо отсутствия движения до 2028 года.",
            "<strong>Траст-банк.</strong> Одобрение World Liberty Trust Company предварительное и условное; OCC ещё должно дать "
            "окончательное одобрение (Reuters)."])),
        ("track", "Как отслеживать WLFI, TRUMP и USD1 на iPhone",
         "<p>Любой крипто-трекер, который использует данные CoinGecko или CoinMarketCap, показывает все три. Три варианта:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), откуда взяты цены в этой статье, с оповещениями о цене и виджетами.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): ищите WLFI, TRUMP или USD1 по названию или тикеру, добавьте их "
             "в избранное и выберите для виджета списка монет на экране «Домой». Если они у вас есть, укажите количество и среднюю цену "
             "покупки, и увидите прибыль или убыток. Без аккаунта; в версии, которая сейчас в продаже, нет оповещений о цене.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), с оповещениями о цене и виджетами."]) +
         "<p>На reviewland есть сравнение большего числа приложений для этих трёх токенов по оповещениям, виджетам и ценам: "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (на английском).</p>\n"
         '<p class="note">Это не финансовый совет. Здесь говорится о том, что опубликовали другие, и о том, как двигались цены; '
         "мы не рекомендуем покупать или продавать что-либо.</p>\n"),
    ],
    "faq": [
        ("Расследуют ли демократы криптовалютные дела Трампа?", "По данным crypto.news, после победы в Палате представителей 3 ноября 2026 года демократы планируют изучить World Liberty Financial, USD1, мем-монету TRUMP и связанные сделки; расследования могут начаться уже в феврале 2027 года."),
        ("Как отреагировала монета TRUMP на выборы?", "На CoinGecko она упала с 1,71 доллара на закрытии 1 ноября примерно до 1,16 к 8 ноября, то есть на 32 %; самое большое дневное падение пришлось на 4 ноября."),
        ("Потеряла ли USD1 привязку к доллару?", "Нет. По данным CoinGecko, в неделю после голосования она держалась около 1 доллара и составляла примерно 0,998 доллара 8 ноября."),
        ("Как следить за WLFI и TRUMP на iPhone?", "Найдите их в трекере, который использует данные CoinGecko или CoinMarketCap, например в CoinGecko, Crypton или CoinMarketCap, добавьте в список наблюдения и выведите на виджет экрана «Домой»."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 ноября 2026 года.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 ноября 2026 года.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters через The Star, 15 августа 2026 года.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 ноября 2026 года (платно; только заголовок).",
        "Цены: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", данные на 8 ноября 2026 года.",
        "Приложения: их страницы в App Store США, 8 ноября 2026 года.",
    ],
    "fix": 'Если что-то здесь устарело, <a href="mailto:sagalabs@proton.me">напишите нам</a>, и мы исправим страницу.',
}, {
    **COMMON, "lang": "de", "path": "de/trumps-krypto-nach-der-wahl-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-de",
    "kicker": "Krypto-Nachrichten",
    "title": "Trumps Krypto-Geschäfte nach der Wahl: WLFI, TRUMP und USD1 (8. Nov. 2026)",
    "h1": "Trumps Krypto-Geschäfte nach den Midterms: was die Demokraten untersuchen wollen und wie sich WLFI, TRUMP und USD1 bewegt haben",
    "description": ("Nachdem die Demokraten am 3. November 2026 das Repräsentantenhaus gewonnen haben, heißt es, sie wollen World Liberty "
                    "Financial (WLFI, USD1) und die Memecoin TRUMP untersuchen. Chronologie, CoinGecko-Kurse vom 1. bis 8. November, was "
                    "als Nächstes zu beobachten ist und wie man diese Token auf dem iPhone verfolgt."),
    "llms": ("Nachricht, 8. November 2026: was über die geplanten Untersuchungen der Demokraten zu World Liberty Financial (WLFI, USD1), "
             "World Liberty Trust und der Memecoin TRUMP nach den Midterms am 3. November berichtet wird, mit datierter Chronologie, "
             "CoinGecko-Kursen vom 1. bis 8. November (TRUMP etwa −32 %, WLFI etwa −8 %, USD1 nahe 1 $), was als Nächstes zu beobachten "
             "ist und drei iPhone-Apps zum Verfolgen der Token (CoinGecko, Crypton, CoinMarketCap). Keine Finanzberatung."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Was berichtet wurde, mit Daten und Quellen, und was die Kurse in der Woche nach der Wahl getan haben.",
    "answer": [
        "<strong>Nachdem die Demokraten bei den Midterms am 3. November 2026 das Repräsentantenhaus gewonnen haben, hat der Abgeordnete "
        "Robert Garcia, der voraussichtlich den Aufsichtsausschuss leiten wird, Untersuchungen zu den Krypto-Geschäften der Familie "
        "Trump angekündigt; laut " + a(CN, "crypto.news") + " könnten sie schon im Februar 2027 beginnen.</strong> In der Woche nach der "
        "Wahl ist laut CoinGecko die Memecoin TRUMP um etwa 32 % gefallen, das WLFI-Token von World Liberty Financial um etwa 8 %, und "
        "der Stablecoin USD1 hält sich nahe 1 $.",
    ],
    "sections": [
        ("reported", "Was berichtet wurde",
         "<p>Laut " + a(CN, "crypto.news") + ", das sich auf Prognosen von NBC News und MS NOW beruft, haben die Demokraten die "
         "Kontrolle über das Repräsentantenhaus übernommen. Garcia habe auf das Ergebnis mit zwei Worten geantwortet, „Lawyer up“ "
         "(„Holt euch einen Anwalt“), und die Ausschüsse könnten per Vorladung Dokumente und Aussagen verlangen.</p>\n"
         "<p>Die Ziele, die diese Berichterstattung nennt:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, ihr Token WLFI und der Stablecoin USD1, einschließlich der ausländischen "
             "Eigentumsverhältnisse. crypto.news berichtet, dass eine Investmentgesellschaft von Scheich Tahnoon bin Zayed aus den VAE "
             "kurz vor der Amtseinführung im Januar 2025 einen Anteil von 49 % erworben hat, für berichtete 500 Mio. $.",
             "<strong>World Liberty Trust Company</strong>, die geplante Trust-Bank für USD1. Reuters berichtete, dass das Office of the "
             "Comptroller of the Currency ihr am 14. August 2026 eine vorläufige, bedingte Genehmigung erteilt hat und dass diese nicht "
             "endgültig ist (" + a(OCC, "Reuters, via The Star") + ").",
             "<strong>Die Memecoin TRUMP.</strong> Laut crypto.news meldete Trump für 2025 mehr als 1 Mrd. $ an krypto-bezogenen "
             "Einnahmen, davon etwa 635 Mio. $ an Lizenzgebühren für die Münze; Reuters schätzte, dass die Krypto-Projekte der Familie "
             "mindestens 2,3 Mrd. $ eingenommen haben.",
             "<strong>Die Begnadigung des Binance-Gründers Changpeng Zhao.</strong> crypto.news berichtet, dass Zhao geschäftliche "
             "Verbindungen zur Familie bestreitet und sagt, er habe nie über eine Begnadigung gesprochen.",
             "Geschäfte anderer Familienmitglieder."]) +
         "<p>Die Sprecherin des Weißen Hauses, Lauren Bis, sagte Newsweek, zitiert von crypto.news, die Pläne der Demokraten seien eine "
         "Fortsetzung dessen, was sie als langjährige Hexenjagd gegen den Präsidenten bezeichnete. Am 8. November brachte die Financial "
         "Times die Geschichte auf der Titelseite unter der Überschrift <em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "Chronologie", ul([
            "<strong>Vor Januar 2025.</strong> Eine Gesellschaft von Scheich Tahnoon bin Zayed soll 49 % von World Liberty Financial übernommen haben (crypto.news).",
            "<strong>14. August 2026.</strong> Das OCC erteilt World Liberty Trust Company eine vorläufige, bedingte Genehmigung (Reuters).",
            "<strong>September 2026.</strong> Das CLARITY Act scheitert bei der Abstimmung im Senat über den Antrag, die Debatte zu beenden (CNBC).",
            "<strong>3. November 2026.</strong> Midterm-Wahlen; die Demokraten gewinnen laut Prognosen von NBC News und MS NOW das Repräsentantenhaus.",
            "<strong>4. November 2026.</strong> TRUMP verzeichnet auf CoinGecko den größten Tagesverlust der Woche, von 1,59 $ auf 1,27 $. crypto.news berichtet über die geplanten Untersuchungen.",
            "<strong>5. November 2026.</strong> CNBC berichtet, dass das Ergebnis die Kryptobranche in Washington in die Defensive bringt.",
            "<strong>8. November 2026.</strong> Die Financial Times bringt die Geschichte auf der Titelseite.",
            "<strong>Ab Februar 2027.</strong> Untersuchungen könnten laut crypto.news beginnen."])),
        ("prices", "Wie sich die Token vom 1. bis 8. November bewegt haben", table(
            ("Token", "1. Nov. (Tagesschluss)", "8. Nov.", "Veränderung", "Marktkapitalisierung, 8. Nov."),
            [("TRUMP (Official Trump)", "$1,71", "$1,16", "&minus;32%", "~$328 Mio."),
             ("WLFI (World Liberty Financial)", "$0,050", "$0,046", "&minus;8%", "~$1,47 Mrd."),
             ("USD1 (Stablecoin)", "$0,998", "$0,998", "0%", "~$3,44 Mrd. (von ~$3,87 Mrd.)"),
             ("Bitcoin, zum Vergleich", "$78.294", "$75.806", "&minus;3%", "")],
            "Quelle: CoinGecko, Tagesschluss in UTC für den 1. November und Kurs am Morgen des 8. November (UTC). Gerundet. USD1 behielt "
            "seinen Kurs, während seine Marktkapitalisierung auf CoinGecko in der Woche um etwa 430 Mio. $ sank. Bitcoin fiel in derselben "
            "Woche ebenfalls, daher lässt sich nicht jede Bewegung auf die Nachrichten zurückführen.")),
        ("next", "Was als Nächstes zu beobachten ist", ul([
            "<strong>Wann die Ausschüsse beginnen.</strong> crypto.news berichtete, dass die Untersuchungen schon im Februar 2027 beginnen "
            "könnten, sobald das neue Repräsentantenhaus steht.",
            "<strong>Das CLARITY Act.</strong> " + a(CNBC, "CNBC") + " berichtete, dass das Gesetz zur Marktstruktur im September bereits bei "
            "einer Abstimmung im Senat über den Antrag zur Beendigung der Debatte gescheitert war; die zitierten Analysten erwarten entweder "
            "eine schärfere demokratische Fassung im nächsten Jahr oder bis 2028 keine Bewegung.",
            "<strong>Die Trust-Bank.</strong> Die Genehmigung für World Liberty Trust Company ist vorläufig und bedingt; das OCC muss "
            "noch die endgültige Genehmigung erteilen (Reuters)."])),
        ("track", "Wie man WLFI, TRUMP und USD1 auf dem iPhone verfolgt",
         "<p>Jeder Krypto-Tracker, der CoinGecko- oder CoinMarketCap-Daten nutzt, listet alle drei. Drei Optionen:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), die Quelle der Kurse in diesem Artikel, mit "
             "Kursalarmen und Widgets.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): Suche WLFI, TRUMP oder USD1 nach Name oder Symbol, füge sie den "
             "Favoriten hinzu und wähle sie für das Coin-Listen-Widget auf dem Home-Bildschirm. Wenn du welche besitzt, trage Menge und "
             "durchschnittlichen Kaufpreis ein, um Gewinn und Verlust zu sehen. Ohne Konto; die aktuell verkaufte Version hat keine Kursalarme.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), mit Kursalarmen und Widgets."]) +
         "<p>reviewland vergleicht weitere Apps für diese drei Token nach Alarmen, Widgets und Kurs in "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (auf Englisch).</p>\n"
         '<p class="note">Keine Finanzberatung. Dieser Artikel gibt wieder, was andere veröffentlicht haben, und was die Kurse getan haben; '
         "er empfiehlt nicht, etwas zu kaufen oder zu verkaufen.</p>\n"),
    ],
    "faq": [
        ("Untersuchen die Demokraten Trumps Krypto-Geschäfte?", "Laut crypto.news planen die Demokraten nach ihrem Sieg im Repräsentantenhaus am 3. November 2026, World Liberty Financial, USD1, die Memecoin TRUMP und verwandte Geschäfte zu prüfen; die Untersuchungen könnten schon im Februar 2027 beginnen."),
        ("Wie reagierte die TRUMP-Münze auf die Wahl?", "Auf CoinGecko fiel sie von 1,71 $ beim Schluss am 1. November auf etwa 1,16 $ am 8. November, also um etwa 32 %; der größte Tagesverlust war am 4. November."),
        ("Hat USD1 seine Bindung an den Dollar verloren?", "Nein. Laut CoinGecko blieb er in der Woche nach der Wahl nahe 1 $ und lag am 8. November bei etwa 0,998 $."),
        ("Wie verfolge ich WLFI und TRUMP auf dem iPhone?", "Suche sie in einem Tracker, der CoinGecko- oder CoinMarketCap-Daten nutzt, etwa CoinGecko, Crypton oder CoinMarketCap, füge sie einer Beobachtungsliste hinzu und lege sie als Widget auf den Home-Bildschirm."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4. November 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5. November 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15. August 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8. November 2026 (kostenpflichtig; nur die Überschrift).",
        "Kurse: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", abgerufen am 8. November 2026.",
        "Apps: ihre Seiten im US-App-Store, 8. November 2026.",
    ],
    "fix": 'Wenn hier etwas veraltet ist, <a href="mailto:sagalabs@proton.me">sag uns Bescheid</a>, dann korrigieren wir die Seite.',
}, {
    **COMMON, "lang": "ja", "path": "ja/chuukan-senkyo-ato-trump-kahei-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-ja",
    "kicker": "暗号資産ニュース",
    "title": "中間選挙後のトランプ家の暗号資産：WLFI、TRUMP、USD1（2026年11月8日）",
    "h1": "中間選挙後のトランプ家の暗号資産：民主党が調査を検討している内容と、WLFI・TRUMP・USD1の値動き",
    "description": ("2026年11月3日に民主党が下院で多数を獲得したのを受け、World Liberty Financial（WLFI、USD1）とミームコインTRUMPを"
                    "調査する計画が伝えられています。11月1日から8日までのCoinGecko価格、今後注目すべき点、iPhoneでこれらのトークンを追う方法をまとめました。"),
    "llms": ("ニュース、2026年11月8日：11月3日の中間選挙後に民主党が World Liberty Financial（WLFI、USD1）、World Liberty Trust、"
             "ミームコインTRUMPについて計画していると報じられている調査の内容。時系列、11月1日から8日までのCoinGecko価格"
             "（TRUMP約−32%、WLFI約−8%、USD1は約1ドル）、今後の注目点、トークンを追うためのiPhoneアプリ3つ（CoinGecko、Crypton、"
             "CoinMarketCap）。投資助言ではありません。"),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "報じられた内容を日付と出典つきで示し、選挙後の1週間の価格の動きも示します。",
    "answer": [
        "<strong>2026年11月3日の中間選挙で民主党が下院を制したのを受け、下院監視委員会の委員長に就任する見込みのロバート・ガルシア議員が、"
        "トランプ家の暗号資産事業に対する調査を示唆しました。" + a(CN, "crypto.news") + " によれば、調査は早ければ2027年2月にも始まる可能性があります。</strong> "
        "選挙後の1週間で、CoinGecko のデータでは、ミームコインTRUMPは約32%下落、World Liberty Financial のトークンWLFIは約8%下落、"
        "ステーブルコインUSD1は1ドル近くで推移しました。",
    ],
    "sections": [
        ("reported", "報じられた内容",
         "<p>" + a(CN, "crypto.news") + " によれば（NBC NewsとMS NOWの予測を引用）、民主党が下院の過半数を獲得しました。同紙は、"
         "ガルシア議員が結果に対して「Lawyer up」（弁護士を雇え）という2語で応じたと伝え、委員会は召喚状によって文書や証言を求めることができると報じています。</p>\n"
         "<p>同紙が挙げた調査対象は次のとおりです。</p>\n" + ul([
             "<strong>World Liberty Financial</strong>、そのトークンWLFI、ステーブルコインUSD1。外国資本による所有を含みます。"
             "crypto.news によれば、UAEのシェイク・タフヌーン・ビン・ザーイド関連の投資会社が、2025年1月の就任直前に、報道では5億ドルで49%の持ち分を取得したとされています。",
             "<strong>World Liberty Trust Company</strong>、USD1向けに計画されているトラスト銀行。Reuters によれば、通貨監督庁（OCC）は"
             "2026年8月14日に予備的な条件付き承認を与えたもので、最終承認ではありません（" + a(OCC, "Reuters、The Star経由") + "）。",
             "<strong>ミームコインTRUMP。</strong> crypto.news によれば、トランプ氏は2025年に暗号資産関連の収入として10億ドル超を申告し、"
             "そのうち約6億3500万ドルはこのコインに関連するロイヤルティでした。Reuters は、家族の暗号資産事業が少なくとも23億ドルを稼いだと推計しています。",
             "<strong>バイナンス創業者チャンポン・ジャオ（CZ）への恩赦。</strong> crypto.news によれば、ジャオ氏は家族との事業上の関係を否定し、"
             "恩赦に関する取り決めについて話し合ったことはないと述べています。",
             "家族のほかの成員の事業取引。"]) +
         "<p>ホワイトハウスの報道官ローレン・ビス氏は、crypto.news が引用した Newsweek の取材に対し、民主党の計画は、大統領に対する長年の"
         "「魔女狩り」の続きだと述べました。11月8日、Financial Times はこの話を「Crypto industry braces for reckoning over Trump ties」"
         "の見出しで一面に載せました。</p>\n"),
        ("timeline", "時系列", ul([
            "<strong>2025年1月以前。</strong> シェイク・タフヌーン・ビン・ザーイド関連の投資会社が World Liberty Financial の49%を取得したと報じられる（crypto.news）。",
            "<strong>2026年8月14日。</strong> OCC が World Liberty Trust Company に予備的な条件付き承認を与える（Reuters）。",
            "<strong>2026年9月。</strong> CLARITY法が、上院での討論終結（クローチャー）投票で否決される（CNBC）。",
            "<strong>2026年11月3日。</strong> 中間選挙。NBC NewsとMS NOWの予測で、民主党が下院を制する。",
            "<strong>2026年11月4日。</strong> CoinGecko でTRUMPが週内最大の1日下落、1.59ドルから1.27ドルへ。crypto.news が予定された調査を報じる。",
            "<strong>2026年11月5日。</strong> CNBC が、結果を受けて暗号資産業界がワシントンで守勢に立たされていると報じる。",
            "<strong>2026年11月8日。</strong> Financial Times が一面で報じる。",
            "<strong>2027年2月以降。</strong> crypto.news によれば、調査が始まる可能性がある。"])),
        ("prices", "11月1日から8日までのトークンの動き", table(
            ("トークン", "11月1日（日次終値）", "11月8日", "変化", "時価総額、11月8日"),
            [("TRUMP（Official Trump）", "$1.71", "$1.16", "&minus;32%", "約3億2800万ドル"),
             ("WLFI（World Liberty Financial）", "$0.050", "$0.046", "&minus;8%", "約14億7000万ドル"),
             ("USD1（ステーブルコイン）", "$0.998", "$0.998", "0%", "約34億4000万ドル（約38億7000万ドルから）"),
             ("ビットコイン（比較用）", "$78,294", "$75,806", "&minus;3%", "")],
            "出典：CoinGecko。11月1日のUTCでの日次終値と、11月8日午前（UTC）の価格。四捨五入。USD1は価格を維持しましたが、"
            "同週のCoinGecko上の時価総額は約4億3000万ドル減少しました。ビットコインも同じ週に下落したため、すべての値動きをニュースのせいにはできません。")),
        ("next", "今後の注目点", ul([
            "<strong>委員会の始動時期。</strong> crypto.news は、新しい下院が発足次第、調査は早ければ2027年2月にも始まる可能性があると報じています。",
            "<strong>CLARITY法。</strong> " + a(CNBC, "CNBC") + " は、この市場構造法案が9月にすでに上院の討論終結投票で否決されたと報じました。"
            "同紙が引用したアナリストは、来年により厳しい民主党版が出るか、2028年まで動きがないと見ています。",
            "<strong>トラスト銀行。</strong> World Liberty Trust Company の承認は予備的かつ条件付きで、OCCによる最終承認はまだです（Reuters）。"])),
        ("track", "iPhoneでWLFI、TRUMP、USD1を追う方法",
         "<p>CoinGecko または CoinMarketCap のデータを使う暗号資産トラッカーなら、3つすべてを扱っています。選択肢は3つです。</p>\n" + ul([
             "<strong>CoinGecko</strong>（" + a(COINGECKO_APP, "App Store") + "）：この記事の価格の出典で、価格アラートとウィジェットがあります。",
             "<strong>Crypton</strong>（" + a(CRYPTON, "App Store") + "）：WLFI、TRUMP、USD1を名前または記号で検索し、お気に入りに追加して、"
             "ホーム画面のコインリストウィジェットに表示できます。保有している場合は数量と平均購入価格を入力すると、損益が分かります。"
             "アカウントは不要で、現在販売中のバージョンには価格アラートはありません。",
             "<strong>CoinMarketCap</strong>（" + a(CMC_APP, "App Store") + "）：価格アラートとウィジェットがあります。"]) +
         "<p>reviewland では、この3つのトークンを対象に、アラート、ウィジェット、価格の観点でさらに多くのアプリを比較しています："
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + "（英語）。</p>\n"
         '<p class="note">投資助言ではありません。この記事は他者が発表した内容と価格の動きを伝えるもので、何かを売買することを勧めるものではありません。</p>\n'),
    ],
    "faq": [
        ("民主党はトランプ家の暗号資産を調査するのですか？", "crypto.news によれば、2026年11月3日に下院を制した後、民主党は World Liberty Financial、USD1、ミームコインTRUMP、関連する取引を調べることを計画しており、調査は早ければ2027年2月にも始まる可能性があります。"),
        ("選挙にTRUMPコインはどう反応しましたか？", "CoinGecko では、11月1日の終値の1.71ドルから、11月8日には約1.16ドルへ下落し、約32%の下げでした。最大の1日の下落は11月4日です。"),
        ("USD1はドルへの連動を失いましたか？", "いいえ。CoinGecko によれば、選挙後の1週間は1ドル近くにとどまり、11月8日には約0.998ドルでした。"),
        ("iPhoneでWLFIとTRUMPを追うにはどうすればいいですか？", "CoinGecko または CoinMarketCap のデータを使うトラッカー（CoinGecko、Crypton、CoinMarketCap など）で検索し、ウォッチリストに追加して、ホーム画面のウィジェットに表示してください。"),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + "、crypto.news、2026年11月4日。",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + "、CNBC、2026年11月5日。",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + "、Reuters（The Star経由）、2026年8月15日。",
        "<em>Crypto industry braces for reckoning over Trump ties</em>、Financial Times、2026年11月8日（有料記事。見出しのみ）。",
        "価格：CoinGecko、" + ", ".join(a(u, k) for k, u in CG.items()) + "、2026年11月8日時点で確認。",
        "アプリ：米国 App Store のページ、2026年11月8日時点。",
    ],
    "fix": '内容が古くなっている場合は、<a href="mailto:sagalabs@proton.me">ご連絡ください</a>。ページを修正します。',
}, {
    **COMMON, "lang": "pt-BR", "path": "pt-br/cripto-familia-trump-apos-eleicoes-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-pt-br",
    "kicker": "Notícias de cripto",
    "title": "Cripto da família Trump após as eleições: WLFI, TRUMP e USD1 (8 nov. 2026)",
    "h1": "Cripto da família Trump após as eleições de meio de mandato: o que os democratas querem investigar e como WLFI, TRUMP e USD1 se moveram",
    "description": ("Depois que os democratas conquistaram a Câmara dos Representantes em 3 de novembro de 2026, há relatos de que planejam "
                    "investigar a World Liberty Financial (WLFI, USD1) e a memecoin TRUMP. Cronologia, preços da CoinGecko de 1 a 8 de "
                    "novembro, o que observar a seguir e como acompanhar esses tokens no iPhone."),
    "llms": ("Notícia, 8 de novembro de 2026: o que foi relatado sobre as investigações que os democratas preparam contra a World Liberty "
             "Financial (WLFI, USD1), a World Liberty Trust e a memecoin TRUMP após as eleições de meio de mandato de 3 de novembro, com "
             "cronologia datada, preços da CoinGecko de 1 a 8 de novembro (TRUMP cerca de −32%, WLFI cerca de −8%, USD1 perto de US$ 1), "
             "o que observar a seguir e três apps para iPhone para acompanhar os tokens (CoinGecko, Crypton, CoinMarketCap). Não é "
             "aconselhamento financeiro."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "O que foi relatado, com datas e fontes, e o que os preços fizeram na semana após a votação.",
    "answer": [
        "<strong>Depois que os democratas conquistaram a Câmara nas eleições de meio de mandato de 3 de novembro de 2026, o deputado Robert "
        "Garcia, que deve presidir o Comitê de Supervisão da Câmara, sinalizou investigações sobre os negócios com cripto da família Trump; "
        "segundo o " + a(CN, "crypto.news") + ", elas poderiam começar já em fevereiro de 2027.</strong> Na semana após a votação, os dados "
        "da CoinGecko mostram a memecoin TRUMP em queda de cerca de 32%, o token WLFI da World Liberty Financial em queda de cerca de 8%, e a "
        "stablecoin USD1 perto de US$ 1.",
    ],
    "sections": [
        ("reported", "O que foi relatado",
         "<p>Segundo o " + a(CN, "crypto.news") + ", que citou projeções da NBC News e da MS NOW, os democratas assumiram o controle da "
         "Câmara. O site informa que Garcia respondeu ao resultado com duas palavras, «Lawyer up» («contratem um advogado»), e que os "
         "comitês poderão pedir documentos e depoimentos por intimação.</p>\n"
         "<p>Os alvos citados nessa reportagem são:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, seu token WLFI e sua stablecoin USD1, incluindo a propriedade estrangeira. O "
             "crypto.news informa que um veículo de investimento do xeque Tahnoon bin Zayed, dos Emirados Árabes Unidos, comprou 49% por "
             "US$ 500 milhões, segundo relatos, pouco antes da posse de janeiro de 2025.",
             "<strong>World Liberty Trust Company</strong>, o banco fiduciário planejado para o USD1. A Reuters informou que o Escritório do "
             "Controlador da Moeda (OCC) lhe deu aprovação preliminar condicional em 14 de agosto de 2026, e que ela não é final ("
             + a(OCC, "Reuters, via The Star") + ").",
             "<strong>A memecoin TRUMP.</strong> Segundo o crypto.news, Trump declarou mais de US$ 1 bilhão em renda ligada a cripto em 2025, "
             "cerca de US$ 635 milhões deles em royalties ligados à moeda; a Reuters estimou que os negócios cripto da família renderam pelo "
             "menos US$ 2,3 bilhões.",
             "<strong>O perdão ao fundador da Binance, Changpeng Zhao.</strong> O crypto.news informa que Zhao nega ligações de negócios com a "
             "família e diz que nunca discutiu qualquer acordo de clemência.",
             "Negócios de outros membros da família."]) +
         "<p>A porta-voz da Casa Branca, Lauren Bis, disse à Newsweek, citada pelo crypto.news, que os planos dos democratas são a "
         "continuação do que chamou de longa caça às bruxas contra o presidente. Em 8 de novembro, o Financial Times publicou a história na "
         "primeira página com o título <em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "Cronologia", ul([
            "<strong>Antes de janeiro de 2025.</strong> Um veículo de Tahnoon bin Zayed teria comprado 49% da World Liberty Financial (crypto.news).",
            "<strong>14 de agosto de 2026.</strong> O OCC concede à World Liberty Trust Company aprovação preliminar condicional (Reuters).",
            "<strong>Setembro de 2026.</strong> A lei CLARITY não passa na votação de encerramento de debate (cloture) no Senado (CNBC).",
            "<strong>3 de novembro de 2026.</strong> Eleições de meio de mandato; os democratas vencem a Câmara, segundo as projeções da NBC News e da MS NOW.",
            "<strong>4 de novembro de 2026.</strong> TRUMP tem a maior queda diária da semana na CoinGecko, de US$ 1,59 para US$ 1,27. O crypto.news informa as investigações planejadas.",
            "<strong>5 de novembro de 2026.</strong> A CNBC informa que o resultado põe a indústria cripto na defensiva em Washington.",
            "<strong>8 de novembro de 2026.</strong> O Financial Times publica a história na primeira página.",
            "<strong>A partir de fevereiro de 2027.</strong> As investigações poderiam começar, segundo o crypto.news."])),
        ("prices", "Como os tokens se moveram de 1 a 8 de novembro", table(
            ("Token", "1 nov. (fechamento diário)", "8 nov.", "Variação", "Valor de mercado, 8 nov."),
            [("TRUMP (Official Trump)", "US$ 1,71", "US$ 1,16", "&minus;32%", "~US$ 328 milhões"),
             ("WLFI (World Liberty Financial)", "US$ 0,050", "US$ 0,046", "&minus;8%", "~US$ 1,47 bilhão"),
             ("USD1 (stablecoin)", "US$ 0,998", "US$ 0,998", "0%", "~US$ 3,44 bilhões (de ~US$ 3,87 bilhões)"),
             ("Bitcoin, para comparação", "US$ 78.294", "US$ 75.806", "&minus;3%", "")],
            "Fonte: CoinGecko, fechamento diário em UTC de 1 de novembro e preço na manhã de 8 de novembro (UTC). Arredondado. O USD1 manteve "
            "o preço, enquanto o valor de mercado dele na CoinGecko caiu cerca de US$ 430 milhões na semana. O bitcoin também caiu na mesma "
            "semana, então nem todo movimento pode ser atribuído à notícia.")),
        ("next", "O que observar a seguir", ul([
            "<strong>Quando os comitês começam.</strong> O crypto.news informou que as investigações poderiam começar já em fevereiro de 2027, "
            "quando a nova Câmara estiver instalada.",
            "<strong>A lei CLARITY.</strong> A " + a(CNBC, "CNBC") + " informou que o projeto de estrutura de mercado já havia fracassado em "
            "uma votação de encerramento de debate no Senado em setembro; os analistas citados esperam uma versão democrata mais dura no ano "
            "que vem ou nenhum movimento até 2028.",
            "<strong>O banco fiduciário.</strong> A aprovação da World Liberty Trust Company é preliminar e condicional; o OCC ainda precisa dar "
            "a aprovação final (Reuters)."])),
        ("track", "Como acompanhar WLFI, TRUMP e USD1 no iPhone",
         "<p>Qualquer rastreador de cripto que use dados da CoinGecko ou da CoinMarketCap mostra os três. Três opções:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), de onde saem os preços deste artigo, com alertas de preço e widgets.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): procure WLFI, TRUMP ou USD1 pelo nome ou símbolo, adicione aos favoritos "
             "e escolha-os no widget de lista de moedas da tela inicial. Se você tiver algum, informe a quantidade e o preço médio de compra para "
             "ver lucro e prejuízo. Funciona sem conta, e a versão à venta não tem alertas de preço.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), com alertas de preço e widgets."]) +
         "<p>A reviewland compara mais apps para esses três tokens, por alertas, widgets e preço, em "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (em inglês).</p>\n"
         '<p class="note">Não é aconselhamento financeiro. Este artigo relata o que outros publicaram e o que os preços fizeram; não recomenda '
         "comprar nem vender nada.</p>\n"),
    ],
    "faq": [
        ("Os democratas estão investigando as cripto de Trump?", "Segundo o crypto.news, depois de vencerem a Câmara em 3 de novembro de 2026, os democratas planejam examinar a World Liberty Financial, o USD1, a memecoin TRUMP e negócios relacionados; as investigações poderiam começar já em fevereiro de 2027."),
        ("Como a moeda TRUMP reagiu às eleições?", "Na CoinGecko, ela caiu de US$ 1,71 no fechamento de 1 de novembro para cerca de US$ 1,16 em 8 de novembro, uma queda de cerca de 32%, com a maior queda diária em 4 de novembro."),
        ("O USD1 perdeu a paridade com o dólar?", "Não. Na CoinGecko, ele ficou perto de US$ 1 na semana após a votação, em cerca de US$ 0,998 em 8 de novembro."),
        ("Como acompanho WLFI e TRUMP no iPhone?", "Procure-os em um rastreador que use dados da CoinGecko ou da CoinMarketCap, como CoinGecko, Crypton ou CoinMarketCap, adicione à lista de observação e coloque-os em um widget da tela inicial."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 de novembro de 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 de novembro de 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15 de agosto de 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 de novembro de 2026 (pago; só a manchete).",
        "Preços: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", consultado em 8 de novembro de 2026.",
        "Apps: suas páginas na App Store dos EUA, 8 de novembro de 2026.",
    ],
    "fix": 'Se algo aqui estiver desatualizado, <a href="mailto:sagalabs@proton.me">avise-nos</a> e corrigiremos a página.',
}, {
    **COMMON, "lang": "fr", "path": "fr/cryptos-famille-trump-apres-elections-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-fr",
    "kicker": "Actualité crypto",
    "title": "Cryptos de la famille Trump après les élections : WLFI, TRUMP et USD1 (8 nov. 2026)",
    "h1": "Cryptos de la famille Trump après les élections de mi-mandat : ce que les démocrates veulent enquêter, et l’évolution de WLFI, TRUMP et USD1",
    "description": ("Après la victoire des démocrates à la Chambre des représentants le 3 novembre 2026, des informations indiquent qu’ils "
                    "prévoient d’enquêter sur World Liberty Financial (WLFI, USD1) et sur le mème coin TRUMP. Chronologie, cours CoinGecko du "
                    "1er au 8 novembre, ce qu’il faut suivre et comment suivre ces jetons sur iPhone."),
    "llms": ("Actualité, 8 novembre 2026 : ce qui a été rapporté sur les enquêtes que préparent les démocrates sur World Liberty Financial "
             "(WLFI, USD1), World Liberty Trust et le mème coin TRUMP après les élections de mi-mandat du 3 novembre, avec une chronologie datée, "
             "les cours CoinGecko du 1er au 8 novembre (TRUMP environ −32 %, WLFI environ −8 %, USD1 proche de 1 $), ce qu’il faut suivre et trois "
             "applications iPhone pour suivre les jetons (CoinGecko, Crypton, CoinMarketCap). Ce n’est pas un conseil financier."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Ce qui a été rapporté, avec dates et sources, et ce que les cours ont fait la semaine suivant le vote.",
    "answer": [
        "<strong>Après la victoire des démocrates à la Chambre lors des élections de mi-mandat du 3 novembre 2026, le représentant Robert Garcia, "
        "qui devrait présider la commission de surveillance de la Chambre, a laissé entendre des enquêtes sur les activités crypto de la famille "
        "Trump ; selon " + a(CN, "crypto.news") + ", elles pourraient commencer dès février 2027.</strong> La semaine suivant le vote, les "
        "données de CoinGecko montrent le mème coin TRUMP en baisse d’environ 32 %, le jeton WLFI de World Liberty Financial en baisse d’environ "
        "8 %, et le stablecoin USD1 proche de 1 $.",
    ],
    "sections": [
        ("reported", "Ce qui a été rapporté",
         "<p>Selon " + a(CN, "crypto.news") + ", qui cite les projections de NBC News et MS NOW, les démocrates ont pris le contrôle de la "
         "Chambre. Le site rapporte que Garcia a répondu au résultat par deux mots, « Lawyer up » (« prenez un avocat »), et que les commissions "
         "pourront demander des documents et des témoignages par citation à comparaître.</p>\n"
         "<p>Les cibles citées par ce reportage sont :</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, son jeton WLFI et son stablecoin USD1, y compris la propriété étrangère. crypto.news "
             "rapporte qu’un véhicule d’investissement du cheikh Tahnoon bin Zayed, des Émirats arabes unis, a pris 49 % pour, selon les "
             "informations, 500 millions de dollars, peu avant l’investiture de janvier 2025.",
             "<strong>World Liberty Trust Company</strong>, la banque fiduciaire prévue pour USD1. Reuters a rapporté que l’Office of the "
             "Comptroller of the Currency (OCC) lui a accordé une approbation préliminaire conditionnelle le 14 août 2026, et qu’elle n’est pas "
             "définitive (" + a(OCC, "Reuters, via The Star") + ").",
             "<strong>Le mème coin TRUMP.</strong> Selon crypto.news, Trump a déclaré plus d’un milliard de dollars de revenus liés aux cryptos pour "
             "2025, dont environ 635 millions de dollars de redevances liées à la monnaie ; Reuters a estimé que les activités crypto de la famille "
             "ont rapporté au moins 2,3 milliards de dollars.",
             "<strong>La grâce accordée au fondateur de Binance, Changpeng Zhao.</strong> crypto.news rapporte que Zhao nie tout lien d’affaires "
             "avec la famille et affirme n’avoir jamais discuté d’un accord de clémence.",
             "Les affaires d’autres membres de la famille."]) +
         "<p>La porte-parole de la Maison Blanche, Lauren Bis, a déclaré à Newsweek, cité par crypto.news, que les projets des démocrates "
         "prolongent ce qu’elle appelle une longue chasse aux sorcières contre le président. Le 8 novembre, le Financial Times a publié l’histoire "
         "en une, sous le titre <em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "Chronologie", ul([
            "<strong>Avant janvier 2025.</strong> Un véhicule du cheikh Tahnoon bin Zayed aurait pris 49 % de World Liberty Financial (crypto.news).",
            "<strong>14 août 2026.</strong> L’OCC accorde à World Liberty Trust Company une approbation préliminaire conditionnelle (Reuters).",
            "<strong>Septembre 2026.</strong> La loi CLARITY échoue au vote de clôture des débats au Sénat (CNBC).",
            "<strong>3 novembre 2026.</strong> Élections de mi-mandat ; les démocrates remportent la Chambre, selon les projections de NBC News et MS NOW.",
            "<strong>4 novembre 2026.</strong> TRUMP connaît sur CoinGecko la plus forte baisse quotidienne de la semaine, de 1,59 $ à 1,27 $. crypto.news rapporte les enquêtes prévues.",
            "<strong>5 novembre 2026.</strong> CNBC rapporte que le résultat met l’industrie crypto sur la défensive à Washington.",
            "<strong>8 novembre 2026.</strong> Le Financial Times met l’histoire en une.",
            "<strong>À partir de février 2027.</strong> Les enquêtes pourraient commencer, selon crypto.news."])),
        ("prices", "Évolution des jetons du 1er au 8 novembre", table(
            ("Jeton", "1er nov. (clôture quotidienne)", "8 nov.", "Variation", "Capitalisation, 8 nov."),
            [("TRUMP (Official Trump)", "1,71 $", "1,16 $", "&minus;32 %", "~328 millions $"),
             ("WLFI (World Liberty Financial)", "0,050 $", "0,046 $", "&minus;8 %", "~1,47 milliard $"),
             ("USD1 (stablecoin)", "0,998 $", "0,998 $", "0 %", "~3,44 milliards $ (contre ~3,87 milliards $)"),
             ("Bitcoin, pour comparaison", "78 294 $", "75 806 $", "&minus;3 %", "")],
            "Source : CoinGecko, clôture quotidienne en UTC le 1er novembre et cours du matin du 8 novembre (UTC). Arrondi. USD1 a conservé son "
            "cours, tandis que sa capitalisation sur CoinGecko a baissé d’environ 430 millions de dollars sur la semaine. Le bitcoin a aussi baissé "
            "la même semaine : tout mouvement ne peut donc pas être attribué à l’actualité.")),
        ("next", "Ce qu’il faut suivre", ul([
            "<strong>Quand les commissions commencent.</strong> crypto.news a rapporté que les enquêtes pourraient commencer dès février 2027, une "
            "fois la nouvelle Chambre en place.",
            "<strong>La loi CLARITY.</strong> " + a(CNBC, "CNBC") + " a rapporté que ce projet sur la structure du marché avait déjà échoué en "
            "septembre au vote de clôture des débats au Sénat ; les analystes cités attendent soit une version démocrate plus dure l’an prochain, "
            "soit aucun mouvement avant 2028.",
            "<strong>La banque fiduciaire.</strong> L’approbation de World Liberty Trust Company est préliminaire et conditionnelle ; l’OCC doit "
            "encore donner son approbation finale (Reuters)."])),
        ("track", "Comment suivre WLFI, TRUMP et USD1 sur iPhone",
         "<p>Tout traqueur de cryptos qui utilise les données de CoinGecko ou de CoinMarketCap les affiche tous les trois. Trois options :</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), la source des cours de cet article, avec alertes de prix et widgets.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + ") : recherchez WLFI, TRUMP ou USD1 par nom ou symbole, ajoutez-les aux favoris "
             "et choisissez-les pour le widget de liste de monnaies de l’écran d’accueil. Si vous en détenez, saisissez la quantité et votre prix "
             "d’achat moyen pour voir vos gains et pertes. Sans compte ; la version en vente n’a pas d’alertes de prix.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), avec alertes de prix et widgets."]) +
         "<p>reviewland compare davantage d’applications pour ces trois jetons, par alertes, widgets et prix, dans "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (en anglais).</p>\n"
         '<p class="note">Ce n’est pas un conseil financier. Cet article rapporte ce que d’autres ont publié et ce qu’ont fait les cours ; il ne '
         "recommande ni d’acheter ni de vendre quoi que ce soit.</p>\n"),
    ],
    "faq": [
        ("Les démocrates enquêtent-ils sur les cryptos de Trump ?", "Selon crypto.news, après leur victoire à la Chambre le 3 novembre 2026, les démocrates prévoient d’examiner World Liberty Financial, USD1, le mème coin TRUMP et les opérations liées ; les enquêtes pourraient commencer dès février 2027."),
        ("Comment le mème coin TRUMP a-t-il réagi aux élections ?", "Sur CoinGecko, il est passé de 1,71 $ à la clôture du 1er novembre à environ 1,16 $ le 8 novembre, soit une baisse d’environ 32 %, avec la plus forte baisse quotidienne le 4 novembre."),
        ("USD1 a-t-il perdu son ancrage au dollar ?", "Non. Sur CoinGecko, il est resté proche de 1 $ la semaine suivant le vote, à environ 0,998 $ le 8 novembre."),
        ("Comment suivre WLFI et TRUMP sur iPhone ?", "Recherchez-les dans un traqueur qui utilise les données de CoinGecko ou de CoinMarketCap, comme CoinGecko, Crypton ou CoinMarketCap, ajoutez-les à une liste de suivi et placez-les dans un widget de l’écran d’accueil."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 novembre 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 novembre 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15 août 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 novembre 2026 (payant ; titre seulement).",
        "Cours : CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", consultés le 8 novembre 2026.",
        "Applications : leurs pages de l’App Store américain, 8 novembre 2026.",
    ],
    "fix": 'Si quelque chose est périmé, <a href="mailto:sagalabs@proton.me">écrivez-nous</a> et nous corrigerons la page.',
}, {
    **COMMON, "lang": "ar", "path": "ar/kriptu-trump-baed-alintikhabat-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-ar",
    "kicker": "أخبار العملات الرقمية",
    "title": "عملات عائلة ترامب الرقمية بعد الانتخابات: WLFI وTRUMP وUSD1 (8 نوفمبر 2026)",
    "h1": "عملات عائلة ترامب الرقمية بعد انتخابات منتصف الولاية: ما يريد الديمقراطيون التحقيق فيه، وكيف تحركت WLFI وTRUMP وUSD1",
    "description": ("بعد فوز الديمقراطيين بمجلس النواب في 3 نوفمبر 2026، تُفيد تقارير بأنهم يخططون للتحقيق في World Liberty Financial "
                    "(WLFI وUSD1) وعملة الميم TRUMP. يتضمن المقال تسلسلًا زمنيًا، وأسعار CoinGecko من 1 إلى 8 نوفمبر، وما يجب متابعته لاحقًا، "
                    "وكيف تتابع هذه الرموز على آيفون."),
    "llms": ("خبر بتاريخ 8 نوفمبر 2026: ما أُفيد عن التحقيقات التي يعدّها الديمقراطيون بشأن World Liberty Financial (WLFI وUSD1) وWorld "
             "Liberty Trust وعملة الميم TRUMP بعد انتخابات منتصف الولاية في 3 نوفمبر، مع تسلسل زمني مؤرخ، وأسعار CoinGecko من 1 إلى 8 نوفمبر "
             "(TRUMP نحو −32%، وWLFI نحو −8%، وUSD1 قرب دولار واحد)، وما يُتابع لاحقًا، وثلاثة تطبيقات لآيفون لمتابعة الرموز (CoinGecko "
             "وCrypton وCoinMarketCap). ليست نصيحة مالية."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "ما أُفيد به، مع التواريخ والمصادر، وما فعلته الأسعار في الأسبوع بعد التصويت.",
    "answer": [
        "<strong>بعد فوز الديمقراطيين بمجلس النواب في انتخابات منتصف الولاية في 3 نوفمبر 2026، أشار النائب روبرت غارسيا، المتوقع أن يرأس لجنة "
        "الرقابة في المجلس، إلى تحقيقات في أعمال العائلة في العملات الرقمية؛ وبحسب " + a(CN, "crypto.news") + "، قد تبدأ في فبراير 2027.</strong> "
        "وفي الأسبوع التالي للتصويت، تُظهر بيانات CoinGecko انخفاض عملة الميم TRUMP بنحو 32%، وانخفاض رمز WLFI التابع لشركة World Liberty "
        "Financial بنحو 8%، وبقاء العملة المستقرة USD1 قرب دولار واحد.",
    ],
    "sections": [
        ("reported", "ما أُفيد به",
         "<p>بحسب " + a(CN, "crypto.news") + "، الذي استشهد بتوقعات NBC News وMS NOW، سيطر الديمقراطيون على مجلس النواب. وذكر الموقع أن "
         "غارسيا رد على النتيجة بكلمتين، «Lawyer up» («استعينوا بمحامٍ»)، وأن اللجان قد تطلب وثائق وشهادات عبر استدعاء قضائي.</p>\n"
         "<p>الأهداف التي يسمّيها هذا التقرير:</p>\n" + ul([
             "<strong>World Liberty Financial</strong> ورمزها WLFI وعملتها المستقرة USD1، بما في ذلك الملكية الأجنبية. ذكر crypto.news أن ذراعًا "
             "استثماريًا للشيخ طحنون بن زايد من الإمارات اشترى حصة 49% بنحو 500 مليون دولار، بحسب التقارير، قبيل تنصيب يناير 2025.",
             "<strong>World Liberty Trust Company</strong>، بنك الأمانة المخطط لـUSD1. ذكرت Reuters أن مكتب مراقب العملة (OCC) منحها موافقة "
             "مبدئية مشروطة في 14 أغسطس 2026، وأنها ليست نهائية (" + a(OCC, "Reuters، عبر The Star") + ").",
             "<strong>عملة الميم TRUMP.</strong> بحسب crypto.news، أعلن ترامب دخلًا مرتبطًا بالعملات الرقمية لعام 2025 يتجاوز مليار دولار، منها "
             "نحو 635 مليون دولار من أتاوات مرتبطة بالعملة؛ وقدّرت Reuters أن مشاريع العائلة في العملات الرقمية حققت ما لا يقل عن 2.3 مليار دولار.",
             "<strong>العفو عن مؤسس Binance تشانغبينغ تشاو.</strong> ذكر crypto.news أن تشاو ينفي وجود روابط عمل مع العائلة، ويقول إنه لم يناقش "
             "أي ترتيب للعفو قط.",
             "أعمال أفراد آخرين من العائلة."]) +
         "<p>قالت المتحدثة باسم البيت الأبيض، لورين بيس، لصحيفة Newsweek، كما نقل crypto.news، إن خطط الديمقراطيين امتداد لما وصفته بأنه «مطاردة "
         "ساحرات» طويلة ضد الرئيس. وفي 8 نوفمبر، نشرت Financial Times القصة على صفحتها الأولى تحت عنوان "
         "<em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "التسلسل الزمني", ul([
            "<strong>قبل يناير 2025.</strong> تشير التقارير إلى أن ذراعًا للشيخ طحنون بن زايد حصل على 49% من World Liberty Financial (crypto.news).",
            "<strong>14 أغسطس 2026.</strong> يمنح OCC شركة World Liberty Trust Company موافقة مبدئية مشروطة (Reuters).",
            "<strong>سبتمبر 2026.</strong> يفشل قانون CLARITY في تصويت إنهاء المناقشة في مجلس الشيوخ (CNBC).",
            "<strong>3 نوفمبر 2026.</strong> انتخابات منتصف الولاية؛ يفوز الديمقراطيون بمجلس النواب بحسب توقعات NBC News وMS NOW.",
            "<strong>4 نوفمبر 2026.</strong> تسجل TRUMP أكبر انخفاض يومي لها خلال الأسبوع على CoinGecko، من 1.59 إلى 1.27 دولار. ينقل crypto.news التحقيقات المخططة.",
            "<strong>5 نوفمبر 2026.</strong> تنقل CNBC أن النتيجة تضع صناعة العملات الرقمية في موقف دفاعي في واشنطن.",
            "<strong>8 نوفمبر 2026.</strong> تنشر Financial Times القصة على صفحتها الأولى.",
            "<strong>من فبراير 2027.</strong> قد تبدأ التحقيقات، بحسب crypto.news."])),
        ("prices", "كيف تحركت الرموز من 1 إلى 8 نوفمبر", table(
            ("الرمز", "1 نوفمبر (إغلاق يومي)", "8 نوفمبر", "التغير", "القيمة السوقية، 8 نوفمبر"),
            [("TRUMP (Official Trump)", "$1.71", "$1.16", "&minus;32%", "نحو 328 مليون $"),
             ("WLFI (World Liberty Financial)", "$0.050", "$0.046", "&minus;8%", "نحو 1.47 مليار $"),
             ("USD1 (عملة مستقرة)", "$0.998", "$0.998", "0%", "نحو 3.44 مليار $ (من نحو 3.87 مليار $)"),
             ("Bitcoin، للمقارنة", "$78,294", "$75,806", "&minus;3%", "")],
            "المصدر: CoinGecko، إغلاق يومي بتوقيت UTC لـ1 نوفمبر، وسعر صباح 8 نوفمبر (UTC). مقرّب. حافظت USD1 على سعرها، بينما انخفضت قيمتها "
            "السوقية على CoinGecko بنحو 430 مليون دولار خلال الأسبوع. وانخفض البيتكوين في الأسبوع نفسه أيضًا، لذا لا يمكن إرجاع كل حركة إلى الأخبار.")),
        ("next", "ما يجب متابعته", ul([
            "<strong>متى تبدأ اللجان.</strong> ذكر crypto.news أن التحقيقات قد تبدأ في فبراير 2027، بعد تشكيل المجلس الجديد.",
            "<strong>قانون CLARITY.</strong> ذكرت " + a(CNBC, "CNBC") + " أن مشروع قانون هيكل السوق فشل بالفعل في تصويت إنهاء المناقشة في مجلس الشيوخ "
            "في سبتمبر؛ ويتوقع المحللون الذين نقلت عنهم نسخة ديمقراطية أشد في العام المقبل، أو عدم أي تحرك حتى 2028.",
            "<strong>بنك الأمانة.</strong> موافقة World Liberty Trust Company مبدئية ومشروطة؛ ولا تزال OCC بحاجة إلى إعطاء الموافقة النهائية (Reuters)."])),
        ("track", "كيف تتابع WLFI وTRUMP وUSD1 على آيفون",
         "<p>أي متتبع للعملات الرقمية يستخدم بيانات CoinGecko أو CoinMarketCap يعرض الثلاثة. ثلاثة خيارات:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + ")، مصدر الأسعار في هذا المقال، مع تنبيهات سعرية وأدوات.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): ابحث عن WLFI أو TRUMP أو USD1 بالاسم أو الرمز، وأضفها إلى المفضلة، "
             "واختَرها لأداة قائمة العملات على الشاشة الرئيسية. إذا كنت تمتلك منها شيئًا، فأدخل الكمية ومتوسط سعر الشراء لترى الربح والخسارة. "
             "تعمل دون حساب، والنسخة المعروضة للبيع لا تحتوي على تنبيهات سعرية.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + ")، مع تنبيهات سعرية وأدوات."]) +
         "<p>تقارن reviewland المزيد من التطبيقات لهذه الرموز الثلاثة، بحسب التنبيهات والأدوات والسعر، في "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (بالإنجليزية).</p>\n"
         '<p class="note">ليست نصيحة مالية. يعرض هذا المقال ما نشره الآخرون وما فعلته الأسعار؛ ولا يوصي بشراء أو بيع أي شيء.</p>\n'),
    ],
    "faq": [
        ("هل يحقق الديمقراطيون في عملات ترامب الرقمية؟", "بحسب crypto.news، بعد فوزهم بمجلس النواب في 3 نوفمبر 2026، يخطط الديمقراطيون لدراسة World Liberty Financial وUSD1 وعملة الميم TRUMP والصفقات المرتبطة بها، وقد تبدأ التحقيقات في فبراير 2027."),
        ("كيف تفاعلت عملة TRUMP مع الانتخابات؟", "على CoinGecko انخفضت من 1.71 دولار عند إغلاق 1 نوفمبر إلى نحو 1.16 دولار في 8 نوفمبر، أي بنحو 32%، وكان أكبر انخفاض يومي في 4 نوفمبر."),
        ("هل فقدت USD1 ارتباطها بالدولار؟", "لا. بحسب CoinGecko بقيت قرب دولار واحد خلال الأسبوع بعد التصويت، عند نحو 0.998 دولار في 8 نوفمبر."),
        ("كيف أتابع WLFI وTRUMP على آيفون؟", "ابحث عنهما في متتبع يستخدم بيانات CoinGecko أو CoinMarketCap، مثل CoinGecko أو Crypton أو CoinMarketCap، وأضفهما إلى قائمة المراقبة وضعهما في أداة على الشاشة الرئيسية."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + "، crypto.news، 4 نوفمبر 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + "، CNBC، 5 نوفمبر 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + "، Reuters عبر The Star، 15 أغسطس 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>، Financial Times، 8 نوفمبر 2026 (مدفوع؛ العنوان فقط).",
        "الأسعار: CoinGecko، " + ", ".join(a(u, k) for k, u in CG.items()) + "، تم الاطلاع عليها في 8 نوفمبر 2026.",
        "التطبيقات: صفحاتها في App Store الأمريكي، 8 نوفمبر 2026.",
    ],
    "fix": 'إذا كان هناك شيء قديم هنا، <a href="mailto:sagalabs@proton.me">أخبرنا</a> وسنصحح الصفحة.',
}]
