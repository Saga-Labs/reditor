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
}]
