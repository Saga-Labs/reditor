/* Umami analytics loader (self-hosted, cookieless, no banner) + fuente IA en el ct (abajo).
   Dashboard: https://analytics.kilmaru.com  Site: reditor.cloud
   WEBSITE_ID is empty until the site is added in Umami; then paste it here. */
(function () {
  var WEBSITE_ID = 'e476834d-fc72-4a80-a37a-61e07c9a26c8';
  var UMAMI_SRC = 'https://analytics.kilmaru.com/script.js';
  if (!WEBSITE_ID) return;
  var s = document.createElement('script');
  s.defer = true;
  s.src = UMAMI_SRC;
  s.setAttribute('data-website-id', WEBSITE_ID);
  s.setAttribute('data-domains', 'reditor.cloud');
  document.head.appendChild(s);
})();

/* De qué IA o buscador llega la visita, en el ct de la App Store (Growth, 25 oct 2026).
   Si la visita llega desde ChatGPT, Perplexity, Claude, Gemini, Copilot... (por
   utm_source o por el referrer), al pulsar un enlace a una app nuestra el ct de
   la pagina pasa a llevar delante la fuente: "rl-ai-chat" -> "gpt-rl-ai-chat".
   Asi App Analytics -> Sources -> Campaigns separa las descargas por IA.
   Sin cookies: la fuente se guarda solo en sessionStorage, para las paginas
   siguientes de la misma visita. Apple deja 40 caracteres en ct. */
(function () {
  var SOURCES = [
    [/(^|\.)(chatgpt\.com|chat\.openai\.com|openai\.com)$/, 'gpt'],
    [/(^|\.)perplexity\.ai$/, 'pplx'],
    [/(^|\.)claude\.ai$/, 'cld'],
    [/(^|\.)gemini\.google\.com$|(^|\.)bard\.google\.com$/, 'gem'],
    [/(^|\.)copilot\.microsoft\.com$|(^|\.)copilot\.cloud\.microsoft$/, 'cop'],
    [/(^|\.)chat\.deepseek\.com$|(^|\.)deepseek\.com$/, 'dsk'],
    [/(^|\.)grok\.com$|(^|\.)x\.ai$/, 'grok'],
    [/(^|\.)meta\.ai$/, 'meta'],
    [/(^|\.)chat\.mistral\.ai$/, 'mis'],
    [/(^|\.)you\.com$/, 'you'],
    [/(^|\.)phind\.com$/, 'phind'],
    [/(^|\.)google\.[a-z.]+$/, 'ggl'],
    [/(^|\.)bing\.com$/, 'bing'],
    [/(^|\.)duckduckgo\.com$/, 'ddg']
  ];
  var KEY = 'saga_ai_src';

  function host(s) {
    s = String(s || '').toLowerCase().trim();
    if (!s) return '';
    if (s.indexOf('://') < 0) s = 'https://' + s;
    try { return new URL(s).hostname.replace(/^www\./, ''); } catch (e) { return ''; }
  }

  function code(h) {
    for (var i = 0; i < SOURCES.length; i++) if (SOURCES[i][0].test(h)) return SOURCES[i][1];
    return '';
  }

  var src = '';
  try {
    var q = new URLSearchParams(location.search);
    src = code(host(q.get('utm_source'))) || code(host(document.referrer));
    if (src) sessionStorage.setItem(KEY, src);
    else src = sessionStorage.getItem(KEY) || '';
  } catch (e) {}
  if (!src) return;

  function retag(a) {
    var href = a.getAttribute('href') || '';
    if (href.indexOf('apps.apple.com') < 0 || a.getAttribute('data-ai-src')) return;
    var m = href.match(/([?&](?:amp;)?ct=)([^&#]*)/);
    if (!m) return;
    var ct = decodeURIComponent(m[2]).replace(/^aisagalab-/, 'as-');
    var tagged = src + '-' + ct;
    if (tagged.length > 40) {
      // Cortado, con 4 letras de un hash para que dos paginas no compartan campana.
      var h = 5381;
      for (var i = 0; i < ct.length; i++) h = ((h * 33) ^ ct.charCodeAt(i)) >>> 0;
      tagged = tagged.slice(0, 35).replace(/-+$/, '') + '-' + ('000' + h.toString(36)).slice(-4);
    }
    a.setAttribute('href', href.replace(m[0], m[1] + encodeURIComponent(tagged)));
    a.setAttribute('data-ai-src', src);
  }

  function onPress(e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (a) retag(a);
  }
  document.addEventListener('pointerdown', onPress, true);
  document.addEventListener('click', onPress, true);
  document.addEventListener('auxclick', onPress, true);
})();
