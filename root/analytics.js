/* Mila Tech fleet analytics — Google Analytics 4 with Consent Mode.
   Consent default (all denied) is set BEFORE the gtag library loads.
   No analytics storage happens unless the visitor accepts the cookie
   notice (choice remembered in localStorage). Advertising storage is
   always denied. */
(function () {
  var GA_ID = 'G-ZY5T7WBELR';
  var KEY = 'mt-cookie-consent';

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;

  gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied'
  });
  gtag('js', new Date());

  var choice = null;
  try { choice = localStorage.getItem(KEY); } catch (e) { /* storage unavailable */ }
  if (choice === 'granted') {
    gtag('consent', 'update', { 'analytics_storage': 'granted' });
  }
  /* send_page_view is disabled on config: config's automatic page_view is
     dispatched under the denied consent default as a cookieless ping, which
     GA4 does not record as a page_view, and it is never re-sent after a
     consent grant. Exactly one explicit page_view is sent instead -- here,
     after the stored-consent update above, and in the Accept handler after
     its consent update. Denied / no choice: no page_view, no storage. */
  gtag('config', GA_ID, { 'send_page_view': false });

  function sendPageView() {
    gtag('event', 'page_view', {
      'page_title': document.title,
      'page_location': window.location.href,
      'page_path': window.location.pathname
    });
  }
  if (choice === 'granted') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', sendPageView);
    } else {
      sendPageView();
    }
  }

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);

  if (choice) return; /* already decided — no banner */

  function showBanner() {
    if (document.getElementById('mt-cookie-bar')) return;
    var style = document.createElement('style');
    style.textContent =
      '#mt-cookie-bar{position:static;z-index:1;width:100%;box-sizing:border-box;background:#0A0614;color:#EDE9FF;' +
      'border-bottom:2px solid #7A25F4;padding:6px 12px;display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;' +
      'justify-content:center;font:13px/1.3 system-ui,-apple-system,"Segoe UI",sans-serif;box-shadow:none}' +
      '#mt-cookie-bar a{color:#B79CFF;text-decoration:underline}' +
      '#mt-cookie-bar .mt-cookie-btns{display:flex;gap:8px;flex:0 0 auto}' +
      '#mt-cookie-bar button{cursor:pointer;border-radius:999px;padding:4px 12px;font:600 13px system-ui,-apple-system,"Segoe UI",sans-serif}' +
      '#mt-cookie-bar .mt-cookie-accept{background:#7A25F4;border:1px solid #7A25F4;color:#fff}' +
      '#mt-cookie-bar .mt-cookie-decline{background:transparent;border:1px solid #B79CFF;color:#B79CFF}';
    document.head.appendChild(style);

    var bar = document.createElement('div');
    bar.id = 'mt-cookie-bar';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookie notice');
    bar.innerHTML =
      '<span>Analytics cookies. <a href="/privacy">Privacy Policy</a></span>' +
      '<span class="mt-cookie-btns">' +
      '<button type="button" class="mt-cookie-accept">Accept</button>' +
      '<button type="button" class="mt-cookie-decline">Decline</button>' +
      '</span>';
    document.body.insertBefore(bar, document.body.firstChild);

    bar.querySelector('.mt-cookie-accept').addEventListener('click', function () {
      try { localStorage.setItem(KEY, 'granted'); } catch (e) { /* ignore */ }
      gtag('consent', 'update', { 'analytics_storage': 'granted' });
      sendPageView();
      bar.remove();
    });
    bar.querySelector('.mt-cookie-decline').addEventListener('click', function () {
      try { localStorage.setItem(KEY, 'denied'); } catch (e) { /* ignore */ }
      bar.remove();
    });
  }

  if (document.body) { showBanner(); }
  else { document.addEventListener('DOMContentLoaded', showBanner); }
})();
