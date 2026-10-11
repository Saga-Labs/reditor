/* Umami analytics loader (self-hosted, cookieless, no banner).
   Dashboard: https://analytics.kilmaru.com  Site: reditor.cloud
   WEBSITE_ID is empty until the site is added in Umami; then paste it here. */
(function () {
  var WEBSITE_ID = '';
  var UMAMI_SRC = 'https://analytics.kilmaru.com/script.js';
  if (!WEBSITE_ID) return;
  var s = document.createElement('script');
  s.defer = true;
  s.src = UMAMI_SRC;
  s.setAttribute('data-website-id', WEBSITE_ID);
  s.setAttribute('data-domains', 'reditor.cloud');
  document.head.appendChild(s);
})();
