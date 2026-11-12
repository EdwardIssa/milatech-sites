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
  gtag('config', GA_ID);

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);

  if (choice) return; /* already decided — no banner */

  function showBanner() {
    if (document.getElementById('mt-cookie-bar')) return;
    var style = document.createElement('style');
    style.textContent =
      '#mt-cookie-bar{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#171029;color:#EDE9FF;' +
      'border-top:2px solid #7A25F4;padding:12px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;' +
      'justify-content:center;font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;box-shadow:0 -2px 14px rgba(0,0,0,.45)}' +
      '#mt-cookie-bar a{color:#B79CFF;text-decoration:underline}' +
      '#mt-cookie-bar .mt-cookie-btns{display:flex;gap:8px}' +
      '#mt-cookie-bar button{cursor:pointer;border-radius:999px;padding:7px 18px;font:600 14px system-ui,-apple-system,"Segoe UI",sans-serif}' +
      '#mt-cookie-bar .mt-cookie-accept{background:#7A25F4;border:1px solid #7A25F4;color:#fff}' +
      '#mt-cookie-bar .mt-cookie-decline{background:transparent;border:1px solid #B79CFF;color:#B79CFF}';
    document.head.appendChild(style);

    var bar = document.createElement('div');
    bar.id = 'mt-cookie-bar';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookie notice');
    bar.innerHTML =
      '<span>We use analytics cookies to see how visitors use this site and make it better. ' +
      '<a href="/privacy">Privacy Policy</a></span>' +
      '<span class="mt-cookie-btns">' +
      '<button type="button" class="mt-cookie-accept">Accept</button>' +
      '<button type="button" class="mt-cookie-decline">Decline</button>' +
      '</span>';
    document.body.appendChild(bar);

    bar.querySelector('.mt-cookie-accept').addEventListener('click', function () {
      try { localStorage.setItem(KEY, 'granted'); } catch (e) { /* ignore */ }
      gtag('consent', 'update', { 'analytics_storage': 'granted' });
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
