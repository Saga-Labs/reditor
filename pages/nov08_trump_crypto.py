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
}, {
    **COMMON, "lang": "zh-Hant", "path": "zh-hant/川普家族加密貨幣-期中選舉後-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-zh-hant",
    "kicker": "加密貨幣新聞",
    "title": "期中選舉後的川普家族加密貨幣：WLFI、TRUMP 與 USD1（2026 年 11 月 8 日）",
    "h1": "期中選舉後的川普家族加密貨幣：民主黨想調查什麼，以及 WLFI、TRUMP 與 USD1 如何變動",
    "description": ("民主黨在 2026 年 11 月 3 日贏得眾議院後，有報導指他們計畫調查 World Liberty Financial（WLFI、USD1）與迷因幣 TRUMP。"
                    "本文提供時間表、11 月 1 日至 8 日的 CoinGecko 價格、接下來要觀察的重點，以及如何在 iPhone 上追蹤這些代幣。"),
    "llms": ("新聞，2026 年 11 月 8 日：關於民主黨在 11 月 3 日期中選舉後，計畫調查 World Liberty Financial（WLFI、USD1）、World Liberty Trust "
             "與迷因幣 TRUMP 的報導整理，包括有日期的時間表、11 月 1 日至 8 日的 CoinGecko 價格（TRUMP 約 −32%、WLFI 約 −8%、USD1 接近 1 美元）、"
             "接下來要觀察的重點，以及三款用來追蹤代幣的 iPhone App（CoinGecko、Crypton、CoinMarketCap）。非投資建議。"),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "報導內容附日期與來源，以及選後一週價格的變化。",
    "answer": [
        "<strong>民主黨在 2026 年 11 月 3 日期中選舉贏得眾議院後，預計將主持眾議院監督委員會的眾議員 Robert Garcia 表示，將針對川普家族的加密貨幣業務展開調查；"
        "據 " + a(CN, "crypto.news") + " 報導，最早可能在 2027 年 2 月開始。</strong> 投票後一週，CoinGecko 數據顯示，迷因幣 TRUMP 下跌約 32%，"
        "World Liberty Financial 的 WLFI 代幣下跌約 8%，穩定幣 USD1 則維持在 1 美元附近。",
    ],
    "sections": [
        ("reported", "報導內容",
         "<p>據 " + a(CN, "crypto.news") + "（引述 NBC News 與 MS NOW 的預測），民主黨已取得眾議院控制權。該媒體報導，Garcia 對結果的回應只有兩個字："
         "「Lawyer up」（「去找律師」），而委員會可以透過傳票要求文件與證詞。</p>\n"
         "<p>該報導點名的調查對象包括：</p>\n" + ul([
             "<strong>World Liberty Financial</strong>、其代幣 WLFI 與穩定幣 USD1，包括外國持股。crypto.news 報導，阿拉伯聯合大公國 Tahnoon bin Zayed 酋長相關的投資機構，"
             "在 2025 年 1 月就職前不久，據報以約 5 億美元取得 49% 股權。",
             "<strong>World Liberty Trust Company</strong>，即規劃中用於 USD1 的信託銀行。Reuters 報導，美國貨幣監理署（OCC）於 2026 年 8 月 14 日給予初步有條件核准，"
             "且尚非最終核准（" + a(OCC, "Reuters，經 The Star 刊載") + "）。",
             "<strong>迷因幣 TRUMP。</strong>據 crypto.news，川普申報 2025 年加密貨幣相關收入超過 10 億美元，其中約 6.35 億美元來自與該幣相關的權利金；"
             "Reuters 估計，家族加密貨幣事業至少賺得 23 億美元。",
             "<strong>幣安創辦人趙長鵬獲赦免。</strong>crypto.news 報導，趙長鵬否認與川普家族有業務往來，並表示從未討論過任何赦免安排。",
             "家族其他成員的業務往來。"]) +
         "<p>白宮發言人 Lauren Bis 對 Newsweek 表示（經 crypto.news 引述），民主黨的計畫是她所稱針對總統長期「獵巫」的延續。11 月 8 日，《金融時報》"
         "以 <em>Crypto industry braces for reckoning over Trump ties</em> 為標題，將此事登上頭版。</p>\n"),
        ("timeline", "時間表", ul([
            "<strong>2025 年 1 月之前。</strong>據報，Tahnoon bin Zayed 酋長相關機構取得 World Liberty Financial 49% 股權（crypto.news）。",
            "<strong>2026 年 8 月 14 日。</strong>OCC 給予 World Liberty Trust Company 初步有條件核准（Reuters）。",
            "<strong>2026 年 9 月。</strong>CLARITY 法案在參議院的終結辯論（cloture）表決中未通過（CNBC）。",
            "<strong>2026 年 11 月 3 日。</strong>期中選舉；據 NBC News 與 MS NOW 預測，民主黨贏得眾議院。",
            "<strong>2026 年 11 月 4 日。</strong>TRUMP 在 CoinGecko 上出現當週單日最大跌幅，從 1.59 美元跌至 1.27 美元。crypto.news 報導計畫中的調查。",
            "<strong>2026 年 11 月 5 日。</strong>CNBC 報導，此結果使加密貨幣產業在華盛頓陷入守勢。",
            "<strong>2026 年 11 月 8 日。</strong>《金融時報》將此事登上頭版。",
            "<strong>2027 年 2 月起。</strong>據 crypto.news，調查可能開始。"])),
        ("prices", "11 月 1 日至 8 日代幣走勢", table(
            ("代幣", "11 月 1 日（每日收盤）", "11 月 8 日", "變動", "市值，11 月 8 日"),
            [("TRUMP（Official Trump）", "1.71 美元", "1.16 美元", "&minus;32%", "約 3.28 億美元"),
             ("WLFI（World Liberty Financial）", "0.050 美元", "0.046 美元", "&minus;8%", "約 14.7 億美元"),
             ("USD1（穩定幣）", "0.998 美元", "0.998 美元", "0%", "約 34.4 億美元（原約 38.7 億美元）"),
             ("比特幣，作為比較", "78,294 美元", "75,806 美元", "&minus;3%", "")],
            "來源：CoinGecko，UTC 時間 11 月 1 日每日收盤價，以及 11 月 8 日上午（UTC）價格。已四捨五入。USD1 價格維持不變，但其在 CoinGecko 上的市值"
            "於該週減少約 4.3 億美元。比特幣同週也下跌，因此並非所有波動都能歸因於新聞。")),
        ("next", "接下來要觀察的重點", ul([
            "<strong>委員會何時開始運作。</strong>crypto.news 報導，新眾議院就位後，調查最早可能在 2027 年 2 月開始。",
            "<strong>CLARITY 法案。</strong>" + a(CNBC, "CNBC") + " 報導，該市場結構法案已在 9 月的參議院終結辯論表決中失敗；所引述的分析師預期明年會出現更嚴格的民主黨版本，"
            "或要到 2028 年才會有進展。",
            "<strong>信託銀行。</strong>World Liberty Trust Company 的核准為初步且有條件；OCC 仍需給予最終核准（Reuters）。"])),
        ("track", "如何在 iPhone 上追蹤 WLFI、TRUMP 與 USD1",
         "<p>任何使用 CoinGecko 或 CoinMarketCap 資料的加密貨幣追蹤 App 都能查到這三者。三個選擇：</p>\n" + ul([
             "<strong>CoinGecko</strong>（" + a(COINGECKO_APP, "App Store") + "）：本文價格的來源，提供價格提醒與小工具。",
             "<strong>Crypton</strong>（" + a(CRYPTON, "App Store") + "）：可依名稱或代號搜尋 WLFI、TRUMP 或 USD1，加入最愛，並選擇在主畫面的幣種清單小工具中顯示。"
             "若您持有這些代幣，可輸入數量與平均買入價，查看損益。無需帳號；目前販售的版本沒有價格提醒。",
             "<strong>CoinMarketCap</strong>（" + a(CMC_APP, "App Store") + "）：提供價格提醒與小工具。"]) +
         "<p>reviewland 在 " + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + "（英文）中，依提醒、小工具與價格比較了更多適用於這三種代幣的 App。</p>\n"
         '<p class="note">非投資建議。本文只是轉述他人已發布的內容與價格走勢，並不建議買進或賣出任何資產。</p>\n'),
    ],
    "faq": [
        ("民主黨會調查川普的加密貨幣嗎？", "據 crypto.news 報導，民主黨在 2026 年 11 月 3 日贏得眾議院後，計畫審視 World Liberty Financial、USD1、迷因幣 TRUMP 及相關交易；調查最早可能在 2027 年 2 月開始。"),
        ("選舉後 TRUMP 幣有何反應？", "在 CoinGecko 上，它從 11 月 1 日收盤的 1.71 美元，在 11 月 8 日降至約 1.16 美元，跌幅約 32%；單日最大跌幅出現在 11 月 4 日。"),
        ("USD1 有沒有失去與美元的錨定？", "沒有。據 CoinGecko，選後一週它維持在 1 美元附近，11 月 8 日約為 0.998 美元。"),
        ("如何在 iPhone 上追蹤 WLFI 與 TRUMP？", "在使用 CoinGecko 或 CoinMarketCap 資料的追蹤 App 中搜尋，例如 CoinGecko、Crypton 或 CoinMarketCap，加入觀察清單，並放到主畫面小工具中。"),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + "，crypto.news，2026 年 11 月 4 日。",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + "，CNBC，2026 年 11 月 5 日。",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + "，Reuters 經 The Star 刊載，2026 年 8 月 15 日。",
        "<em>Crypto industry braces for reckoning over Trump ties</em>，Financial Times，2026 年 11 月 8 日（付費；僅標題）。",
        "價格：CoinGecko，" + "、".join(a(u, k) for k, u in CG.items()) + "，查詢日期為 2026 年 11 月 8 日。",
        "App：其美國 App Store 頁面，2026 年 11 月 8 日。",
    ],
    "fix": '如果本頁有過時內容，請<a href="mailto:sagalabs@proton.me">告訴我們</a>，我們會修正。',
}, {
    **COMMON, "lang": "th", "path": "th/kripto-ครอบครัวทรัมป์-หลังเลือกตั้ง-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-th",
    "kicker": "ข่าวคริปโต",
    "title": "คริปโตของครอบครัวทรัมป์หลังการเลือกตั้ง: WLFI, TRUMP และ USD1 (8 พ.ย. 2026)",
    "h1": "คริปโตของครอบครัวทรัมป์หลังการเลือกตั้งกลางเทอม: พรรคเดโมแครตวางแผนจะสอบสวนอะไร และ WLFI, TRUMP และ USD1 เคลื่อนไหวอย่างไร",
    "description": ("หลังพรรคเดโมแครตชนะสภาผู้แทนราษฎรเมื่อวันที่ 3 พ.ย. 2026 มีรายงานว่าพวกเขาวางแผนสอบสวน World Liberty Financial (WLFI, USD1) "
                    "และเหรียญมีม TRUMP บทความนี้มีลำดับเหตุการณ์ ราคา CoinGecko ตั้งแต่วันที่ 1 ถึง 8 พ.ย. สิ่งที่ควรติดตามต่อ และวิธีติดตามโทเคนเหล่านี้บน iPhone"),
    "llms": ("ข่าว 8 พ.ย. 2026: สรุปสิ่งที่มีรายงานเกี่ยวกับการสอบสวนที่พรรคเดโมแครตวางแผนไว้กับ World Liberty Financial (WLFI, USD1), World Liberty Trust "
             "และเหรียญมีม TRUMP หลังการเลือกตั้งกลางเทอมวันที่ 3 พ.ย. พร้อมลำดับเหตุการณ์ที่ระบุวันที่ ราคา CoinGecko ตั้งแต่วันที่ 1 ถึง 8 พ.ย. "
             "(TRUMP ประมาณ −32%, WLFI ประมาณ −8%, USD1 ใกล้ 1 ดอลลาร์) สิ่งที่ควรติดตามต่อ และแอป iPhone สามตัวสำหรับติดตามโทเคน "
             "(CoinGecko, Crypton, CoinMarketCap) ไม่ใช่คำแนะนำทางการเงิน"),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "สิ่งที่มีรายงาน พร้อมวันที่และแหล่งที่มา และราคาเคลื่อนไหวอย่างไรในสัปดาห์หลังการลงคะแนน",
    "answer": [
        "<strong>หลังพรรคเดโมแครตชนะสภาผู้แทนราษฎรในการเลือกตั้งกลางเทอมวันที่ 3 พ.ย. 2026 โรเบิร์ต การ์เซีย สมาชิกสภาที่คาดว่าจะเป็นประธานคณะกรรมาธิการกำกับดูแล "
        "ส่งสัญญาณว่าจะมีการสอบสวนธุรกิจคริปโตของครอบครัวทรัมป์ และตามรายงานของ " + a(CN, "crypto.news") + " อาจเริ่มได้ตั้งแต่กุมภาพันธ์ 2027</strong> "
        "ในสัปดาห์หลังการลงคะแนน ข้อมูลของ CoinGecko แสดงว่าเหรียญมีม TRUMP ลดลงประมาณ 32% โทเคน WLFI ของ World Liberty Financial ลดลงประมาณ 8% "
        "และสเตเบิลคอยน์ USD1 ยังอยู่ใกล้ 1 ดอลลาร์",
    ],
    "sections": [
        ("reported", "สิ่งที่มีรายงาน",
         "<p>ตาม " + a(CN, "crypto.news") + " ซึ่งอ้างการคาดการณ์ของ NBC News และ MS NOW พรรคเดโมแครตได้เสียงข้างมากในสภา บทความรายงานว่าการ์เซียตอบต่อผลลัพธ์"
         "ด้วยคำสองคำว่า «Lawyer up» («ไปหาทนายมา») และคณะกรรมาธิการสามารถขอเอกสารและคำให้การผ่านหมายเรียกได้</p>\n"
         "<p>เป้าหมายที่รายงานนี้ระบุ ได้แก่:</p>\n" + ul([
             "<strong>World Liberty Financial</strong> โทเคน WLFI และสเตเบิลคอยน์ USD1 รวมถึงความเป็นเจ้าของจากต่างชาติ crypto.news รายงานว่าบริษัทลงทุนที่เกี่ยวข้องกับ"
             "เชค Tahnoon bin Zayed แห่งสหรัฐอาหรับเอมิเรตส์ ซื้อหุ้น 49% ในราคาที่รายงานว่า 500 ล้านดอลลาร์ ไม่นานก่อนพิธีสาบานตนเดือนมกราคม 2025",
             "<strong>World Liberty Trust Company</strong> ธนาคารทรัสต์ที่วางแผนไว้สำหรับ USD1 Reuters รายงานว่า Office of the Comptroller of the Currency (OCC) "
             "ให้การอนุมัติเบื้องต้นแบบมีเงื่อนไขเมื่อวันที่ 14 ส.ค. 2026 และยังไม่ใช่การอนุมัติขั้นสุดท้าย (" + a(OCC, "Reuters ผ่าน The Star") + ")",
             "<strong>เหรียญมีม TRUMP</strong> ตาม crypto.news ทรัมป์แจ้งรายได้ที่เกี่ยวข้องกับคริปโตมากกว่า 1 พันล้านดอลลาร์สำหรับปี 2025 ในนั้นประมาณ 635 ล้านดอลลาร์"
             "เป็นค่าลิขสิทธิ์ที่เกี่ยวกับเหรียญ และ Reuters ประมาณการว่ากิจการคริปโตของครอบครัวทำรายได้อย่างน้อย 2.3 พันล้านดอลลาร์",
             "<strong>การอภัยโทษให้ Changpeng Zhao ผู้ก่อตั้ง Binance</strong> crypto.news รายงานว่า Zhao ปฏิเสธว่ามีความเกี่ยวข้องทางธุรกิจกับครอบครัว "
             "และบอกว่าไม่เคยหารือเรื่องการอภัยโทษ",
             "ธุรกรรมทางธุรกิจของสมาชิกครอบครัวคนอื่น"]) +
         "<p>โฆษกทำเนียบขาว Lauren Bis บอกกับ Newsweek ซึ่ง crypto.news อ้างถึง ว่าแผนของพรรคเดโมแครตเป็นความต่อเนื่องของสิ่งที่เธอเรียกว่าการล่าแม่มด"
         "ต่อประธานาธิบดีมาอย่างยาวนาน เมื่อวันที่ 8 พ.ย. Financial Times นำเรื่องนี้ขึ้นหน้าแรกภายใต้หัวข้อ <em>Crypto industry braces for reckoning over Trump ties</em></p>\n"),
        ("timeline", "ลำดับเหตุการณ์", ul([
            "<strong>ก่อนมกราคม 2025</strong> บริษัทที่เกี่ยวข้องกับ Tahnoon bin Zayed รายงานว่าถือหุ้น 49% ของ World Liberty Financial (crypto.news)",
            "<strong>14 ส.ค. 2026</strong> OCC ให้การอนุมัติเบื้องต้นแบบมีเงื่อนไขแก่ World Liberty Trust Company (Reuters)",
            "<strong>ก.ย. 2026</strong> กฎหมาย CLARITY ไม่ผ่านการลงมติยุติการอภิปรายในวุฒิสภา (CNBC)",
            "<strong>3 พ.ย. 2026</strong> การเลือกตั้งกลางเทอม; พรรคเดโมแครตได้สภาผู้แทนราษฎรตามการคาดการณ์ของ NBC News และ MS NOW",
            "<strong>4 พ.ย. 2026</strong> TRUMP มีการลดลงรายวันมากที่สุดของสัปดาห์บน CoinGecko จาก 1.59 ดอลลาร์เป็น 1.27 ดอลลาร์ crypto.news รายงานการสอบสวนที่วางแผนไว้",
            "<strong>5 พ.ย. 2026</strong> CNBC รายงานว่าผลลัพธ์ทำให้อุตสาหกรรมคริปโตต้องตั้งรับในวอชิงตัน",
            "<strong>8 พ.ย. 2026</strong> Financial Times นำเรื่องขึ้นหน้าแรก",
            "<strong>ตั้งแต่ ก.พ. 2027</strong> การสอบสวนอาจเริ่มขึ้นตาม crypto.news"])),
        ("prices", "ความเคลื่อนไหวของโทเคนระหว่างวันที่ 1 ถึง 8 พ.ย.", table(
            ("โทเคน", "1 พ.ย. (ราคาปิดรายวัน)", "8 พ.ย.", "การเปลี่ยนแปลง", "มูลค่าตลาด 8 พ.ย."),
            [("TRUMP (Official Trump)", "1.71 ดอลลาร์", "1.16 ดอลลาร์", "&minus;32%", "ประมาณ 328 ล้านดอลลาร์"),
             ("WLFI (World Liberty Financial)", "0.050 ดอลลาร์", "0.046 ดอลลาร์", "&minus;8%", "ประมาณ 1.47 พันล้านดอลลาร์"),
             ("USD1 (สเตเบิลคอยน์)", "0.998 ดอลลาร์", "0.998 ดอลลาร์", "0%", "ประมาณ 3.44 พันล้านดอลลาร์ (จากประมาณ 3.87 พันล้านดอลลาร์)"),
             ("Bitcoin เปรียบเทียบ", "78,294 ดอลลาร์", "75,806 ดอลลาร์", "&minus;3%", "")],
            "แหล่งที่มา: CoinGecko ราคาปิดรายวันตามเวลา UTC ของวันที่ 1 พ.ย. และราคาช่วงเช้าของวันที่ 8 พ.ย. (UTC) ปัดเศษแล้ว USD1 รักษาราคาไว้ได้ "
            "ขณะที่มูลค่าตลาดบน CoinGecko ลดลงประมาณ 430 ล้านดอลลาร์ในสัปดาห์นั้น Bitcoin ก็ลดลงในสัปดาห์เดียวกัน จึงไม่สามารถยกทุกการเคลื่อนไหวให้เป็นผลจากข่าวได้")),
        ("next", "สิ่งที่ควรติดตามต่อ", ul([
            "<strong>เมื่อคณะกรรมาธิการเริ่มทำงาน</strong> crypto.news รายงานว่าการสอบสวนอาจเริ่มได้เร็วที่สุดในกุมภาพันธ์ 2027 เมื่อสภาชุดใหม่เข้าที่แล้ว",
            "<strong>กฎหมาย CLARITY</strong> " + a(CNBC, "CNBC") + " รายงานว่าร่างกฎหมายโครงสร้างตลาดนี้ไม่ผ่านการลงมติยุติการอภิปรายในวุฒิสภาไปแล้วเมื่อเดือนกันยายน "
            "นักวิเคราะห์ที่อ้างในรายงานคาดว่าจะมีฉบับพรรคเดโมแครตที่เข้มกว่าในปีหน้า หรือไม่มีความเคลื่อนไหวจนถึงปี 2028",
            "<strong>ธนาคารทรัสต์</strong> การอนุมัติของ World Liberty Trust Company เป็นแบบเบื้องต้นและมีเงื่อนไข OCC ยังต้องให้การอนุมัติขั้นสุดท้าย (Reuters)"])),
        ("track", "วิธีติดตาม WLFI, TRUMP และ USD1 บน iPhone",
         "<p>แอปติดตามคริปโตที่ใช้ข้อมูลของ CoinGecko หรือ CoinMarketCap จะแสดงทั้งสามตัว มีสามทางเลือก:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + ") แหล่งที่มาของราคาในบทความนี้ พร้อมการแจ้งเตือนราคาและวิดเจ็ต",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): ค้นหา WLFI, TRUMP หรือ USD1 ด้วยชื่อหรือสัญลักษณ์ เพิ่มในรายการโปรด แล้วเลือกให้แสดง"
             "ในวิดเจ็ตรายการเหรียญบนหน้าจอหลัก หากคุณถืออยู่ ให้ใส่จำนวนและราคาซื้อเฉลี่ยเพื่อดูกำไรขาดทุน ใช้งานได้โดยไม่ต้องมีบัญชี และเวอร์ชันที่วางขายอยู่ไม่มีการแจ้งเตือนราคา",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + ") พร้อมการแจ้งเตือนราคาและวิดเจ็ต"]) +
         "<p>reviewland เปรียบเทียบแอปเพิ่มเติมสำหรับโทเคนทั้งสามนี้ตามการแจ้งเตือน วิดเจ็ต และราคาใน "
         + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + " (เป็นภาษาอังกฤษ)</p>\n"
         '<p class="note">ไม่ใช่คำแนะนำทางการเงิน บทความนี้รายงานสิ่งที่คนอื่นเผยแพร่และการเคลื่อนไหวของราคา ไม่ได้แนะนำให้ซื้อหรือขายสิ่งใด</p>\n'),
    ],
    "faq": [
        ("พรรคเดโมแครตกำลังสอบสวนคริปโตของทรัมป์อยู่หรือไม่", "ตาม crypto.news หลังชนะสภาผู้แทนราษฎรเมื่อวันที่ 3 พ.ย. 2026 พรรคเดโมแครตวางแผนจะตรวจสอบ World Liberty Financial, USD1, เหรียญมีม TRUMP และดีลที่เกี่ยวข้อง การสอบสวนอาจเริ่มได้เร็วที่สุดในกุมภาพันธ์ 2027"),
        ("เหรียญ TRUMP ตอบสนองต่อการเลือกตั้งอย่างไร", "บน CoinGecko เหรียญลดจาก 1.71 ดอลลาร์ ณ ราคาปิดวันที่ 1 พ.ย. เหลือประมาณ 1.16 ดอลลาร์ในวันที่ 8 พ.ย. คิดเป็นการลดลงประมาณ 32% โดยวันที่ลดลงมากที่สุดในหนึ่งวันคือวันที่ 4 พ.ย."),
        ("USD1 เสียการผูกกับดอลลาร์หรือไม่", "ไม่ ตาม CoinGecko มันอยู่ใกล้ 1 ดอลลาร์ตลอดสัปดาห์หลังการลงคะแนน โดยอยู่ที่ประมาณ 0.998 ดอลลาร์ในวันที่ 8 พ.ย."),
        ("จะติดตาม WLFI และ TRUMP บน iPhone ได้อย่างไร", "ค้นหาในแอปติดตามที่ใช้ข้อมูลของ CoinGecko หรือ CoinMarketCap เช่น CoinGecko, Crypton หรือ CoinMarketCap เพิ่มในรายการที่จะติดตาม และวางไว้ในวิดเจ็ตบนหน้าจอหลัก"),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 พ.ย. 2026",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 พ.ย. 2026",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters ผ่าน The Star, 15 ส.ค. 2026",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 พ.ย. 2026 (แบบเสียเงิน; เฉพาะพาดหัว)",
        "ราคา: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", ตรวจสอบเมื่อ 8 พ.ย. 2026",
        "แอป: หน้า App Store ของสหรัฐฯ ของแต่ละแอป 8 พ.ย. 2026",
    ],
    "fix": 'หากมีข้อมูลในหน้านี้ที่ล้าสมัย <a href="mailto:sagalabs@proton.me">แจ้งเราได้</a> แล้วเราจะแก้ไขหน้านี้',
}, {
    **COMMON, "lang": "tr", "path": "tr/trump-ailesinin-kriptolari-ara-secim-sonrasi-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-tr",
    "kicker": "Kripto haberleri",
    "title": "Seçim sonrası Trump ailesinin kripto paraları: WLFI, TRUMP ve USD1 (8 Kas 2026)",
    "h1": "Ara seçim sonrası Trump ailesinin kripto paraları: Demokratların neyi araştırmayı planladığı ve WLFI, TRUMP ve USD1'in nasıl hareket ettiği",
    "description": ("Demokratlar 3 Kasım 2026'da Temsilciler Meclisi'ni kazandıktan sonra, World Liberty Financial (WLFI, USD1) ve TRUMP meme coin'ini "
                    "araştırmayı planladıkları bildiriliyor. Bu yazıda zaman çizelgesi, 1-8 Kasım CoinGecko fiyatları, bundan sonra izlenecekler ve "
                    "bu token'ları iPhone'da nasıl takip edeceğiniz var."),
    "llms": ("Haber, 8 Kasım 2026: 3 Kasım ara seçiminden sonra Demokratların World Liberty Financial (WLFI, USD1), World Liberty Trust ve TRUMP meme coin "
             "hakkında planladığı soruşturmalara dair bildirilenler; tarihli zaman çizelgesi, 1-8 Kasım CoinGecko fiyatları (TRUMP yaklaşık −%32, WLFI "
             "yaklaşık −%8, USD1 1 dolara yakın), bundan sonra izlenecekler ve token'ları takip etmek için üç iPhone uygulaması (CoinGecko, Crypton, "
             "CoinMarketCap). Yatırım tavsiyesi değildir."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Bildirilenler, tarih ve kaynaklarıyla; oylamadan sonraki haftada fiyatların ne yaptığı.",
    "answer": [
        "<strong>Demokratlar 3 Kasım 2026 ara seçimlerinde Temsilciler Meclisi'ni kazandıktan sonra, meclisin Denetim Komitesi'ni yönetmesi beklenen Temsilci Robert Garcia, "
        "Trump ailesinin kripto işlerine yönelik soruşturmalara işaret etti; " + a(CN, "crypto.news") + "'e göre bunlar en erken Şubat 2027'de başlayabilir.</strong> "
        "Oylamadan sonraki hafta CoinGecko verileri, TRUMP meme coin'in yaklaşık %32, World Liberty Financial'ın WLFI token'ının yaklaşık %8 düştüğünü, "
        "USD1 stablecoin'in ise 1 dolara yakın kaldığını gösteriyor.",
    ],
    "sections": [
        ("reported", "Bildirilenler",
         "<p>" + a(CN, "crypto.news") + "'e göre, NBC News ve MS NOW tahminlerine atıfta bulunan haber, Demokratların Temsilciler Meclisi'nin kontrolünü ele geçirdiğini "
         "bildirdi. Haberde Garcia'nın sonuca «Lawyer up» («avukat tutun») diyerek karşılık verdiği, komitelerin de celp yoluyla belge ve ifade talep edebileceği yer alıyor.</p>\n"
         "<p>Bu haberde adı geçen hedefler şunlar:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, WLFI token'ı ve USD1 stablecoin'i, yabancı sahiplik dahil. crypto.news, BAE'li Şeyh Tahnoon bin Zayed'e bağlı bir "
             "yatırım aracının, Ocak 2025 göreve başlamasından kısa süre önce, bildirildiğine göre 500 milyon dolara %49 hisse aldığını yazdı.",
             "<strong>World Liberty Trust Company</strong>, USD1 için planlanan trust bankası. Reuters, Para Birimi Denetleyicisi Ofisi'nin (OCC) 14 Ağustos 2026'da ona "
             "ön koşullu onay verdiğini ve bunun kesin olmadığını bildirdi (" + a(OCC, "Reuters, The Star aracılığıyla") + ").",
             "<strong>TRUMP meme coin.</strong> crypto.news'e göre Trump, 2025 için kriptoyla ilgili 1 milyar doların üzerinde gelir bildirdi; bunun yaklaşık 635 milyon doları "
             "coin ile bağlantılı telif ücretlerinden geliyordu. Reuters, ailenin kripto girişimlerinin en az 2,3 milyar dolar kazandığını tahmin etti.",
             "<strong>Binance kurucusu Changpeng Zhao'nun affı.</strong> crypto.news, Zhao'nun aileyle iş bağlantısını reddettiğini ve hiçbir af düzenlemesini görüşmediğini bildirdi.",
             "Ailenin diğer üyelerinin iş işlemleri."]) +
         "<p>Beyaz Saray sözcüsü Lauren Bis, crypto.news'in aktardığı Newsweek'e, Demokratların planlarının, onun başkana karşı uzun süredir süren «cadı avı» dediği şeyin "
         "devamı olduğunu söyledi. 8 Kasım'da Financial Times, konuyu <em>Crypto industry braces for reckoning over Trump ties</em> başlığıyla birinci sayfasına taşıdı.</p>\n"),
        ("timeline", "Zaman çizelgesi", ul([
            "<strong>Ocak 2025'ten önce.</strong> Tahnoon bin Zayed'e bağlı bir araç World Liberty Financial'ın %49'unu aldığı bildirildi (crypto.news).",
            "<strong>14 Ağustos 2026.</strong> OCC, World Liberty Trust Company'ye ön koşullu onay verir (Reuters).",
            "<strong>Eylül 2026.</strong> CLARITY Yasası, Senato'da tartışmayı sonlandırma (cloture) oylamasında başarısız olur (CNBC).",
            "<strong>3 Kasım 2026.</strong> Ara seçimler; NBC News ve MS NOW tahminlerine göre Demokratlar Temsilciler Meclisi'ni kazanır.",
            "<strong>4 Kasım 2026.</strong> TRUMP, CoinGecko'da haftanın en büyük günlük düşüşünü yaşar: 1,59 dolardan 1,27 dolara. crypto.news planlanan soruşturmaları bildirir.",
            "<strong>5 Kasım 2026.</strong> CNBC, sonucun kripto sektörünü Washington'da savunmaya ittiğini bildirir.",
            "<strong>8 Kasım 2026.</strong> Financial Times haberi birinci sayfaya taşır.",
            "<strong>Şubat 2027'den itibaren.</strong> crypto.news'e göre soruşturmalar başlayabilir."])),
        ("prices", "1-8 Kasım arasında token'ların hareketi", table(
            ("Token", "1 Kas. (günlük kapanış)", "8 Kas.", "Değişim", "Piyasa değeri, 8 Kas."),
            [("TRUMP (Official Trump)", "1,71 $", "1,16 $", "&minus;%32", "~328 milyon $"),
             ("WLFI (World Liberty Financial)", "0,050 $", "0,046 $", "&minus;%8", "~1,47 milyar $"),
             ("USD1 (stablecoin)", "0,998 $", "0,998 $", "%0", "~3,44 milyar $ (~3,87 milyar $'dan)"),
             ("Bitcoin, karşılaştırma için", "78.294 $", "75.806 $", "&minus;%3", "")],
            "Kaynak: CoinGecko, 1 Kasım için UTC'de günlük kapanış ve 8 Kasım sabahı (UTC) fiyatı. Yuvarlanmıştır. USD1 fiyatını korudu; CoinGecko'daki piyasa değeri "
            "ise o hafta yaklaşık 430 milyon dolar düştü. Bitcoin de aynı hafta düştü, bu yüzden her hareket habere bağlanamaz.")),
        ("next", "Bundan sonra izlenecekler", ul([
            "<strong>Komitelerin ne zaman başlayacağı.</strong> crypto.news, yeni Meclis oluşunca soruşturmaların en erken Şubat 2027'de başlayabileceğini bildirdi.",
            "<strong>CLARITY Yasası.</strong> " + a(CNBC, "CNBC") + ", bu piyasa yapısı tasarısının Eylül'de Senato'da tartışmayı sonlandırma oylamasında zaten başarısız olduğunu bildirdi; "
            "haberde alıntılanan analistler, gelecek yıl daha sert bir Demokrat sürüm ya da 2028'e kadar hareketsizlik bekliyor.",
            "<strong>Trust bankası.</strong> World Liberty Trust Company'nin onayı ön koşullu ve geçici; OCC'nin nihai onayı hâlâ gerekiyor (Reuters)."])),
        ("track", "WLFI, TRUMP ve USD1'i iPhone'da nasıl takip edersiniz",
         "<p>CoinGecko veya CoinMarketCap verilerini kullanan her kripto takip uygulaması üçünü de listeler. Üç seçenek:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "): bu yazıdaki fiyatların kaynağı; fiyat uyarıları ve widget'lar var.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): WLFI, TRUMP veya USD1'i ad ya da sembolle arayın, favorilere ekleyin ve ana ekrandaki coin listesi "
             "widget'ında gösterin. Bu token'lardan elinizde varsa miktarı ve ortalama alış fiyatını girerek kâr ve zararı görebilirsiniz. Hesap gerektirmez; "
             "satıştaki sürümde fiyat uyarısı yoktur.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "): fiyat uyarıları ve widget'lar var."]) +
         "<p>reviewland, bu üç token için uyarılar, widget'lar ve fiyat açısından daha fazla uygulamayı " + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone")
         + " başlıklı yazısında karşılaştırıyor (İngilizce).</p>\n"
         '<p class="note">Yatırım tavsiyesi değildir. Bu yazı, başkalarının yayımladıklarını ve fiyatların ne yaptığını aktarır; hiçbir şeyi almayı ya da satmayı önermez.</p>\n'),
    ],
    "faq": [
        ("Demokratlar Trump'ın kripto işlerini araştırıyor mu?", "crypto.news'e göre Demokratlar 3 Kasım 2026'da Temsilciler Meclisi'ni kazandıktan sonra World Liberty Financial, USD1, TRUMP meme coin'i ve ilgili işlemleri incelemeyi planlıyor; soruşturmalar en erken Şubat 2027'de başlayabilir."),
        ("TRUMP coin seçimlere nasıl tepki verdi?", "CoinGecko'da 1 Kasım kapanışındaki 1,71 dolardan 8 Kasım'da yaklaşık 1,16 dolara düştü; yani yaklaşık %32 geriledi. En büyük günlük düşüş 4 Kasım'daydı."),
        ("USD1 dolara bağlılığını kaybetti mi?", "Hayır. CoinGecko'ya göre oylamadan sonraki hafta 1 dolara yakın kaldı; 8 Kasım'da yaklaşık 0,998 dolardaydı."),
        ("WLFI ve TRUMP'ı iPhone'da nasıl takip ederim?", "CoinGecko veya CoinMarketCap verilerini kullanan bir takip uygulamasında, örneğin CoinGecko, Crypton veya CoinMarketCap'te arayın, izleme listenize ekleyin ve ana ekrana widget olarak koyun."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 Kasım 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 Kasım 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters, The Star aracılığıyla, 15 Ağustos 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 Kasım 2026 (ücretli; yalnızca başlık).",
        "Fiyatlar: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", 8 Kasım 2026 tarihinde alındı.",
        "Uygulamalar: ABD App Store sayfaları, 8 Kasım 2026.",
    ],
    "fix": 'Buradaki bir bilgi güncel değilse <a href="mailto:sagalabs@proton.me">bize yazın</a>, sayfayı düzeltelim.',
}, {
    **COMMON, "lang": "it", "path": "it/criptovalute-famiglia-trump-dopo-elezioni-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-it",
    "kicker": "Notizie crypto",
    "title": "Criptovalute della famiglia Trump dopo le elezioni: WLFI, TRUMP e USD1 (8 nov 2026)",
    "h1": "Criptovalute della famiglia Trump dopo le elezioni di metà mandato: cosa vogliono indagare i democratici e come si sono mossi WLFI, TRUMP e USD1",
    "description": ("Dopo la vittoria dei democratici alla Camera dei rappresentanti il 3 novembre 2026, si riferisce che intendono indagare su World Liberty "
                    "Financial (WLFI, USD1) e sulla memecoin TRUMP. Cronologia, prezzi CoinGecko dall'1 all'8 novembre, cosa osservare in seguito e come "
                    "seguire questi token su iPhone."),
    "llms": ("Notizia, 8 novembre 2026: cosa è stato riferito sulle indagini che i democratici preparano su World Liberty Financial (WLFI, USD1), World Liberty "
             "Trust e la memecoin TRUMP dopo le elezioni di metà mandato del 3 novembre, con cronologia datata, prezzi CoinGecko dall'1 all'8 novembre (TRUMP "
             "circa −32%, WLFI circa −8%, USD1 vicino a 1 $), cosa osservare in seguito e tre app per iPhone per seguire i token (CoinGecko, Crypton, "
             "CoinMarketCap). Non è consulenza finanziaria."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "Cosa è stato riferito, con date e fonti, e cosa hanno fatto i prezzi nella settimana dopo il voto.",
    "answer": [
        "<strong>Dopo la vittoria dei democratici alla Camera nelle elezioni di metà mandato del 3 novembre 2026, il deputato Robert Garcia, che dovrebbe presiedere "
        "la commissione di vigilanza della Camera, ha lasciato intendere indagini sulle attività crypto della famiglia Trump; secondo " + a(CN, "crypto.news") + ", "
        "potrebbero iniziare già a febbraio 2027.</strong> Nella settimana successiva al voto, i dati di CoinGecko mostrano la memecoin TRUMP in calo di circa il 32%, "
        "il token WLFI di World Liberty Financial in calo di circa l'8% e lo stablecoin USD1 vicino a 1 $.",
    ],
    "sections": [
        ("reported", "Cosa è stato riferito",
         "<p>Secondo " + a(CN, "crypto.news") + ", che cita le proiezioni di NBC News e MS NOW, i democratici hanno conquistato il controllo della Camera. Il sito riferisce "
         "che Garcia ha risposto al risultato con due parole, «Lawyer up» («prendete un avvocato»), e che le commissioni potranno chiedere documenti e testimonianze tramite citazione.</p>\n"
         "<p>I bersagli citati in quel servizio sono:</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, il suo token WLFI e lo stablecoin USD1, compresa la proprietà estera. crypto.news riferisce che un veicolo d'investimento "
             "dello sceicco Tahnoon bin Zayed, degli Emirati Arabi Uniti, avrebbe acquisito il 49% per una cifra riportata di 500 milioni di dollari, poco prima dell'insediamento del gennaio 2025.",
             "<strong>World Liberty Trust Company</strong>, la trust bank prevista per USD1. Reuters ha riferito che l'Office of the Comptroller of the Currency (OCC) le ha concesso "
             "un'approvazione preliminare condizionata il 14 agosto 2026, e che non è definitiva (" + a(OCC, "Reuters, via The Star") + ").",
             "<strong>La memecoin TRUMP.</strong> Secondo crypto.news, Trump ha dichiarato oltre 1 miliardo di dollari di redditi legati alle cripto per il 2025, di cui circa "
             "635 milioni di dollari in royalties legate alla moneta; Reuters ha stimato che le attività crypto della famiglia abbiano fruttato almeno 2,3 miliardi di dollari.",
             "<strong>La grazia al fondatore di Binance, Changpeng Zhao.</strong> crypto.news riferisce che Zhao nega legami d'affari con la famiglia e dice di non aver mai "
             "discusso alcun accordo di clemenza.",
             "Affari di altri membri della famiglia."]) +
         "<p>La portavoce della Casa Bianca Lauren Bis ha detto a Newsweek, citata da crypto.news, che i piani dei democratici sono la continuazione di quella che ha definito "
         "una lunga caccia alle streghe contro il presidente. L'8 novembre il Financial Times ha messo la storia in prima pagina con il titolo "
         "<em>Crypto industry braces for reckoning over Trump ties</em>.</p>\n"),
        ("timeline", "Cronologia", ul([
            "<strong>Prima di gennaio 2025.</strong> Un veicolo legato allo sceicco Tahnoon bin Zayed avrebbe preso il 49% di World Liberty Financial (crypto.news).",
            "<strong>14 agosto 2026.</strong> L'OCC concede a World Liberty Trust Company un'approvazione preliminare condizionata (Reuters).",
            "<strong>Settembre 2026.</strong> La legge CLARITY non supera il voto di chiusura del dibattito (cloture) al Senato (CNBC).",
            "<strong>3 novembre 2026.</strong> Elezioni di metà mandato; i democratici vincono la Camera, secondo le proiezioni di NBC News e MS NOW.",
            "<strong>4 novembre 2026.</strong> TRUMP registra su CoinGecko il calo giornaliero più forte della settimana, da 1,59 $ a 1,27 $. crypto.news riferisce delle indagini previste.",
            "<strong>5 novembre 2026.</strong> CNBC riferisce che il risultato mette l'industria crypto sulla difensiva a Washington.",
            "<strong>8 novembre 2026.</strong> Il Financial Times pubblica la storia in prima pagina.",
            "<strong>Da febbraio 2027.</strong> Le indagini potrebbero iniziare, secondo crypto.news."])),
        ("prices", "Come si sono mossi i token dall'1 all'8 novembre", table(
            ("Token", "1 nov. (chiusura giornaliera)", "8 nov.", "Variazione", "Capitalizzazione, 8 nov."),
            [("TRUMP (Official Trump)", "1,71 $", "1,16 $", "&minus;32%", "~328 milioni $"),
             ("WLFI (World Liberty Financial)", "0,050 $", "0,046 $", "&minus;8%", "~1,47 miliardi $"),
             ("USD1 (stablecoin)", "0,998 $", "0,998 $", "0%", "~3,44 miliardi $ (da ~3,87 miliardi $)"),
             ("Bitcoin, per confronto", "78.294 $", "75.806 $", "&minus;3%", "")],
            "Fonte: CoinGecko, chiusura giornaliera in UTC dell'1 novembre e prezzo della mattina dell'8 novembre (UTC). Arrotondato. USD1 ha mantenuto il prezzo, mentre la sua "
            "capitalizzazione su CoinGecko è scesa di circa 430 milioni di dollari nella settimana. Anche il bitcoin è sceso nella stessa settimana, quindi non tutto il movimento si può attribuire alla notizia.")),
        ("next", "Cosa osservare in seguito", ul([
            "<strong>Quando partono le commissioni.</strong> crypto.news ha riferito che le indagini potrebbero iniziare già a febbraio 2027, una volta insediata la nuova Camera.",
            "<strong>La legge CLARITY.</strong> La " + a(CNBC, "CNBC") + " ha riferito che il progetto sulla struttura del mercato era già fallito a settembre nel voto di chiusura del dibattito al Senato; "
            "gli analisti citati prevedono una versione democratica più dura l'anno prossimo, oppure nessun movimento fino al 2028.",
            "<strong>La trust bank.</strong> L'approvazione di World Liberty Trust Company è preliminare e condizionata; l'OCC deve ancora concedere l'approvazione definitiva (Reuters)."])),
        ("track", "Come seguire WLFI, TRUMP e USD1 su iPhone",
         "<p>Qualsiasi tracker crypto che usa i dati di CoinGecko o CoinMarketCap li elenca tutti e tre. Tre opzioni:</p>\n" + ul([
             "<strong>CoinGecko</strong> (" + a(COINGECKO_APP, "App Store") + "), da cui vengono i prezzi di questo articolo, con avvisi di prezzo e widget.",
             "<strong>Crypton</strong> (" + a(CRYPTON, "App Store") + "): cerca WLFI, TRUMP o USD1 per nome o simbolo, aggiungili ai preferiti e scegli di mostrarli nel widget "
             "dell'elenco monete della schermata Home. Se ne possiedi, inserisci la quantità e il prezzo medio d'acquisto per vedere guadagni e perdite. Funziona senza account; "
             "la versione in vendita non ha avvisi di prezzo.",
             "<strong>CoinMarketCap</strong> (" + a(CMC_APP, "App Store") + "), con avvisi di prezzo e widget."]) +
         "<p>reviewland confronta altre app per questi tre token, per avvisi, widget e prezzo, in " + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone")
         + " (in inglese).</p>\n"
         '<p class="note">Non è consulenza finanziaria. Questo articolo riporta ciò che altri hanno pubblicato e ciò che hanno fatto i prezzi; non consiglia di comprare o vendere nulla.</p>\n'),
    ],
    "faq": [
        ("I democratici indagano sulle cripto di Trump?", "Secondo crypto.news, dopo la vittoria alla Camera del 3 novembre 2026, i democratici prevedono di esaminare World Liberty Financial, USD1, la memecoin TRUMP e operazioni collegate; le indagini potrebbero iniziare già a febbraio 2027."),
        ("Come ha reagito la moneta TRUMP alle elezioni?", "Su CoinGecko è scesa da 1,71 $ alla chiusura dell'1 novembre a circa 1,16 $ l'8 novembre, cioè circa il 32% in meno; il calo giornaliero più forte è stato il 4 novembre."),
        ("USD1 ha perso l'aggancio al dollaro?", "No. Su CoinGecko è rimasto vicino a 1 $ nella settimana dopo il voto, a circa 0,998 $ l'8 novembre."),
        ("Come seguo WLFI e TRUMP su iPhone?", "Cercali in un tracker che usa i dati di CoinGecko o CoinMarketCap, come CoinGecko, Crypton o CoinMarketCap, aggiungili a una lista di controllo e mettili in un widget della schermata Home."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 4 novembre 2026.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 5 novembre 2026.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters via The Star, 15 agosto 2026.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 8 novembre 2026 (a pagamento; solo il titolo).",
        "Prezzi: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", consultati l'8 novembre 2026.",
        "App: le loro pagine dell'App Store statunitense, 8 novembre 2026.",
    ],
    "fix": 'Se qualcosa qui è superato, <a href="mailto:sagalabs@proton.me">scrivici</a> e correggeremo la pagina.',
}, {
    **COMMON, "lang": "ko", "path": "ko/trump-gamun-kripto-jungandeon-yihu-wlfi-trump-usd1/", "ct": "rd-trump-crypto-midterms-ko",
    "kicker": "암호화폐 뉴스",
    "title": "중간선거 이후 트럼프 일가의 암호화폐: WLFI, TRUMP, USD1 (2026년 11월 8일)",
    "h1": "중간선거 이후 트럼프 일가의 암호화폐: 민주당이 조사하려는 내용과 WLFI, TRUMP, USD1의 움직임",
    "description": ("민주당이 2026년 11월 3일 하원을 차지한 뒤, World Liberty Financial(WLFI, USD1)과 밈코인 TRUMP를 조사할 계획이라는 보도가 나왔습니다. "
                    "11월 1일부터 8일까지의 CoinGecko 가격, 앞으로 지켜볼 점, iPhone에서 이 토큰을 추적하는 방법을 정리했습니다."),
    "llms": ("뉴스, 2026년 11월 8일: 11월 3일 중간선거 이후 민주당이 World Liberty Financial(WLFI, USD1), World Liberty Trust, 밈코인 TRUMP를 두고 준비 중인 "
             "조사에 대해 보도된 내용. 날짜가 적힌 연표, 11월 1일부터 8일까지의 CoinGecko 가격(TRUMP 약 −32%, WLFI 약 −8%, USD1은 1달러 근처), 앞으로 지켜볼 점, "
             "토큰을 추적할 iPhone 앱 세 가지(CoinGecko, Crypton, CoinMarketCap). 투자 조언이 아닙니다."),
    "llms_note": "Crypton, one of the three apps named, is made by Saga Labs, which runs Reditor.",
    "stand": "보도된 내용을 날짜와 출처와 함께 정리하고, 투표 이후 한 주 동안 가격이 어떻게 움직였는지 보여줍니다.",
    "answer": [
        "<strong>민주당이 2026년 11월 3일 중간선거에서 하원을 차지한 뒤, 하원 감독위원장을 맡을 것으로 예상되는 로버트 가르시아 의원은 트럼프 일가의 암호화폐 사업에 대한 "
        "조사를 시사했습니다. " + a(CN, "crypto.news") + "에 따르면 조사는 이르면 2027년 2월에 시작될 수 있습니다.</strong> 투표 후 한 주 동안 CoinGecko 데이터에 따르면 "
        "밈코인 TRUMP는 약 32%, World Liberty Financial의 WLFI 토큰은 약 8% 떨어졌고, 스테이블코인 USD1은 1달러 근처를 유지했습니다.",
    ],
    "sections": [
        ("reported", "보도된 내용",
         "<p>NBC News와 MS NOW의 예측을 인용한 " + a(CN, "crypto.news") + "에 따르면 민주당이 하원을 장악했습니다. 이 매체는 가르시아 의원이 결과에 «Lawyer up»(«변호사를 구하라»)이라는 "
         "두 단어로 답했다고 전했으며, 위원회는 소환장을 통해 문서와 증언을 요구할 수 있다고 보도했습니다.</p>\n"
         "<p>이 보도에서 거론된 대상은 다음과 같습니다.</p>\n" + ul([
             "<strong>World Liberty Financial</strong>, 토큰 WLFI, 스테이블코인 USD1, 외국인 지분을 포함합니다. crypto.news는 아랍에미리트의 타후난 빈 자이드 셰이크와 "
             "관련된 투자 기관이 2025년 1월 취임 직전 보도된 5억 달러에 49% 지분을 취득했다고 전했습니다.",
             "<strong>World Liberty Trust Company</strong>, USD1을 위해 계획된 신탁은행입니다. Reuters는 통화감독청(OCC)이 2026년 8월 14일 예비적 조건부 승인을 내렸으며 "
             "최종 승인이 아니라고 보도했습니다(" + a(OCC, "Reuters, The Star 경유") + ").",
             "<strong>밈코인 TRUMP.</strong> crypto.news에 따르면 트럼프는 2025년 암호화폐 관련 소득을 10억 달러 넘게 신고했으며, 그중 약 6억 3500만 달러는 이 코인과 "
             "연결된 로열티였습니다. Reuters는 일가의 암호화폐 사업이 최소 23억 달러를 벌었다고 추산했습니다.",
             "<strong>바이낸스 창업자 자오창펑(CZ)의 사면.</strong> crypto.news는 자오창펑이 일가와의 사업 관계를 부인하며, 사면 협상을 논의한 적이 없다고 말했다고 보도했습니다.",
             "일가의 다른 구성원들의 사업 거래."]) +
         "<p>백악관 대변인 로렌 비스는 crypto.news가 인용한 Newsweek에 민주당의 계획은 대통령에 대한 오랜 «마녀사냥»의 연장이라고 말했습니다. 11월 8일 Financial Times는 "
         "이 이야기를 <em>Crypto industry braces for reckoning over Trump ties</em>라는 제목으로 1면에 실었습니다.</p>\n"),
        ("timeline", "연표", ul([
            "<strong>2025년 1월 이전.</strong> 타후난 빈 자이드 셰이크 관련 기관이 World Liberty Financial 지분 49%를 취득한 것으로 보도됨(crypto.news).",
            "<strong>2026년 8월 14일.</strong> OCC가 World Liberty Trust Company에 예비적 조건부 승인을 내림(Reuters).",
            "<strong>2026년 9월.</strong> CLARITY 법안이 상원 토론 종결(cloture) 표결에서 부결됨(CNBC).",
            "<strong>2026년 11월 3일.</strong> 중간선거; NBC News와 MS NOW 예측에 따르면 민주당이 하원을 차지함.",
            "<strong>2026년 11월 4일.</strong> TRUMP가 CoinGecko에서 그 주 가장 큰 하루 하락을 기록, 1.59달러에서 1.27달러로. crypto.news가 예정된 조사를 보도함.",
            "<strong>2026년 11월 5일.</strong> CNBC가 이번 결과로 암호화폐 업계가 워싱턴에서 수세에 몰렸다고 보도함.",
            "<strong>2026년 11월 8일.</strong> Financial Times가 1면에 이 이야기를 실음.",
            "<strong>2027년 2월 이후.</strong> crypto.news에 따르면 조사가 시작될 수 있음."])),
        ("prices", "11월 1일부터 8일까지 토큰의 움직임", table(
            ("토큰", "11월 1일 (일일 종가)", "11월 8일", "변동", "시가총액, 11월 8일"),
            [("TRUMP (Official Trump)", "$1.71", "$1.16", "&minus;32%", "약 3억 2800만 달러"),
             ("WLFI (World Liberty Financial)", "$0.050", "$0.046", "&minus;8%", "약 14억 7000만 달러"),
             ("USD1 (스테이블코인)", "$0.998", "$0.998", "0%", "약 34억 4000만 달러 (약 38억 7000만 달러에서)"),
             ("비트코인, 비교용", "$78,294", "$75,806", "&minus;3%", "")],
            "출처: CoinGecko, 11월 1일 UTC 기준 일일 종가와 11월 8일 오전(UTC) 가격. 반올림. USD1은 가격을 유지했지만 CoinGecko 기준 시가총액은 그 주에 약 4억 3000만 달러 줄었습니다. "
            "비트코인도 같은 주에 하락했으므로 모든 움직임을 뉴스 탓으로 돌릴 수는 없습니다.")),
        ("next", "앞으로 지켜볼 점", ul([
            "<strong>위원회가 언제 시작하는지.</strong> crypto.news는 새 하원이 구성되면 조사가 이르면 2027년 2월에 시작될 수 있다고 보도했습니다.",
            "<strong>CLARITY 법안.</strong> " + a(CNBC, "CNBC") + "는 이 시장 구조 법안이 9월 상원 토론 종결 표결에서 이미 부결됐다고 보도했습니다. 인용된 애널리스트들은 "
            "내년에 더 강경한 민주당 버전이 나오거나, 2028년까지 움직임이 없을 것으로 예상했습니다.",
            "<strong>신탁은행.</strong> World Liberty Trust Company의 승인은 예비적이고 조건부입니다. OCC의 최종 승인은 아직 남아 있습니다(Reuters)."])),
        ("track", "iPhone에서 WLFI, TRUMP, USD1을 추적하는 방법",
         "<p>CoinGecko 또는 CoinMarketCap 데이터를 쓰는 암호화폐 추적 앱은 이 세 가지를 모두 보여줍니다. 세 가지 선택지:</p>\n" + ul([
             "<strong>CoinGecko</strong>(" + a(COINGECKO_APP, "App Store") + "): 이 글의 가격 출처이며, 가격 알림과 위젯이 있습니다.",
             "<strong>Crypton</strong>(" + a(CRYPTON, "App Store") + "): WLFI, TRUMP, USD1을 이름이나 기호로 검색해 즐겨찾기에 추가하고, 홈 화면의 코인 목록 위젯에 표시하도록 고를 수 있습니다. "
             "보유 중이라면 수량과 평균 매수가를 입력해 손익을 볼 수 있습니다. 계정 없이 쓸 수 있으며, 판매 중인 버전에는 가격 알림이 없습니다.",
             "<strong>CoinMarketCap</strong>(" + a(CMC_APP, "App Store") + "): 가격 알림과 위젯이 있습니다."]) +
         "<p>reviewland에서는 이 세 토큰을 알림, 위젯, 가격 기준으로 더 많은 앱과 비교합니다: " + a(RL, "the best apps to track WLFI and the TRUMP coin on iPhone") + "(영어).</p>\n"
         '<p class="note">투자 조언이 아닙니다. 이 글은 다른 곳에서 발표된 내용과 가격 움직임을 전할 뿐이며, 무엇을 사거나 팔라고 권하지 않습니다.</p>\n'),
    ],
    "faq": [
        ("민주당이 트럼프의 암호화폐를 조사하나요?", "crypto.news에 따르면, 민주당은 2026년 11월 3일 하원을 차지한 뒤 World Liberty Financial, USD1, 밈코인 TRUMP 및 관련 거래를 살펴볼 계획이며, 조사는 이르면 2027년 2월에 시작될 수 있습니다."),
        ("TRUMP 코인은 선거에 어떻게 반응했나요?", "CoinGecko에서 11월 1일 종가 1.71달러에서 11월 8일 약 1.16달러로 떨어져, 약 32% 하락했습니다. 하루 최대 하락은 11월 4일이었습니다."),
        ("USD1은 달러 페그를 잃었나요?", "아니요. CoinGecko에 따르면 투표 후 한 주 동안 1달러 근처에 머물렀고, 11월 8일 약 0.998달러였습니다."),
        ("iPhone에서 WLFI와 TRUMP는 어떻게 추적하나요?", "CoinGecko 또는 CoinMarketCap 데이터를 쓰는 추적 앱, 예를 들어 CoinGecko, Crypton, CoinMarketCap에서 검색해 관심 목록에 추가하고 홈 화면 위젯에 올려 두세요."),
    ],
    "sources_html": [
        a(CN, "Democrats prepare to investigate World Liberty Financial after House win") + ", crypto.news, 2026년 11월 4일.",
        a(CNBC, "Democratic sweep puts crypto on defensive in Washington") + ", CNBC, 2026년 11월 5일.",
        a(OCC, "US regulator approves bank charter for Trump-backed crypto company World Liberty Financial") + ", Reuters(The Star 경유), 2026년 8월 15일.",
        "<em>Crypto industry braces for reckoning over Trump ties</em>, Financial Times, 2026년 11월 8일(유료; 제목만).",
        "가격: CoinGecko, " + ", ".join(a(u, k) for k, u in CG.items()) + ", 2026년 11월 8일 조회.",
        "앱: 미국 App Store 페이지, 2026년 11월 8일.",
    ],
    "fix": '내용이 오래되었다면 <a href="mailto:sagalabs@proton.me">알려 주세요</a>. 페이지를 고치겠습니다.',
}]
