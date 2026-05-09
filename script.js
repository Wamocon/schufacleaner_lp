/* ═══════════════════════════════════════════════════════════════
   AWAY Landing Page V2 – Interactive Logic
   DE/EN Toggle | iPhone Screen Cycle | App Tabs | ROI | Reveal
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* ── 1. LANGUAGE TOGGLE (DE / EN) ──────────────────────────── */
  var currentLang = 'de';

  function initLangToggle() {
    var btnDe = $('#lang-de');
    var btnEn = $('#lang-en');
    if (!btnDe || !btnEn) return;

    function setLang(lang) {
      currentLang = lang;

      // Toggle button styles
      btnDe.classList.toggle('active-lang', lang === 'de');
      btnEn.classList.toggle('active-lang', lang === 'en');

      // Switch all labelled elements
      $$('[data-de]').forEach(function (el) {
        var newText = lang === 'de' ? el.getAttribute('data-de') : el.getAttribute('data-en');
        if (newText !== null) {
          // Preserve child elements (icons etc.) by checking first child type
          if (el.children.length === 0) {
            el.textContent = newText;
          } else {
            // Only update text nodes, leave icons intact
            var nodes = Array.prototype.slice.call(el.childNodes);
            nodes.forEach(function (node) {
              if (node.nodeType === 3 && node.textContent.trim().length > 0) {
                node.textContent = ' ' + newText + ' ';
              }
            });
          }
        }
      });

      // Switch placeholder attributes
      $$('[data-ph-de]').forEach(function (el) {
        el.placeholder = lang === 'de' ? el.getAttribute('data-ph-de') : el.getAttribute('data-ph-en');
      });

      // document lang attribute
      document.documentElement.lang = lang;
    }

    btnDe.addEventListener('click', function () { setLang('de'); });
    btnEn.addEventListener('click', function () { setLang('en'); });
  }

  /* ── 2. iPHONE SCREEN CYCLE ─────────────────────────────────── */
  function initIphoneScreenCycle() {
    var screens = $$('.app-screen');
    if (!screens.length) return;

    var current = 0;
    var interval = 4200; // ms per screen

    function showScreen(idx) {
      screens.forEach(function (s, i) {
        s.classList.toggle('active', i === idx);
      });
    }

    showScreen(0);

    setInterval(function () {
      current = (current + 1) % screens.length;
      showScreen(current);
    }, interval);
  }

  /* ── 3. APP SHOWCASE TABS ────────────────────────────────────── */
  function initShowcaseTabs() {
    var tabBtns = $$('.tab-btn');
    var tabPanels = $$('.tab-panel');
    if (!tabBtns.length) return;

    tabBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetTab = btn.getAttribute('data-tab');

        tabBtns.forEach(function (b) { b.classList.remove('active'); });
        tabPanels.forEach(function (p) { p.classList.remove('active'); });

        btn.classList.add('active');
        var targetPanel = $('#tab-' + targetTab);
        if (targetPanel) targetPanel.classList.add('active');
      });
    });
  }

  /* ── 4. ROI CALCULATOR ───────────────────────────────────────── */
  function initROICalculator() {
    var empSlider  = $('#employee-slider');
    var reqSlider  = $('#request-slider');
    var empLabel   = $('#employee-count-label');
    var reqLabel   = $('#request-count-label');
    var savingsVal = $('#savings-value');
    var hoursVal   = $('#hours-value');

    if (!empSlider || !reqSlider) return;

    function update() {
      var negativEintraege = parseInt(empSlider.value, 10);
      var investition      = parseInt(reqSlider.value, 10);

      empLabel.textContent = negativEintraege;
      reqLabel.textContent = investition.toLocaleString('de-DE');

      /*
       * Berechnung SCHUFA-Vorteil:
       *
       * 1. Anwaltskosten-Ersparnis:
       *    Ca. 70 % der angefochtenen Einträge werden erfolgreich bereinigt
       *    (konservative Schätzung). Durchschnittliche Anwaltskosten für eine
       *    Schufa-Löschung: 700 € (Mitte der BRAK-Spanne 500–1.000 €, BRAK 2025).
       *    Diese Kosten entfallen durch SchufaCleaner.
       *
       * 2. Zinsvorteil auf geplante Investition/Kredit:
       *    Ein bereinigter Schufa-Score ermöglicht erfahrungsgemäß bessere
       *    Kreditkonditionen. Konservative Annahme: 1,5 % p.a. Zinsvorteil
       *    über eine typische Laufzeit von 5 Jahren.
       *    Quelle: Schutzgemeinschaft für allgemeine Kreditsicherung (Schufa),
       *    Infomaterial "Wie wirkt der Score auf Kreditkonditionen?", 2024.
       *
       * Score-Punkte: ca. 10 Punkte Score-Verbesserung je bereinigtem Eintrag
       * (konservative Schätzung auf Basis des Schufa-Scoringsystems).
       */
      var erfolgreichBereinigt = Math.round(negativEintraege * 0.70);
      var anwaltKostenGespart  = erfolgreichBereinigt * 700;
      var zinsVorteil          = investition * 0.015 * 5;
      var moneySaved           = anwaltKostenGespart + zinsVorteil;
      var scorePunkte          = erfolgreichBereinigt * 10;

      var fmt = new Intl.NumberFormat('de-DE', {
        style: 'currency',
        currency: 'EUR',
        maximumFractionDigits: 0
      });

      savingsVal.textContent = fmt.format(moneySaved);
      hoursVal.textContent   = Math.round(scorePunkte).toLocaleString('de-DE') + ' Pkt.';

      // Subtle pulse animation
      savingsVal.style.transform = 'scale(1.04)';
      savingsVal.style.transition = 'transform 0.1s';
      setTimeout(function () {
        savingsVal.style.transform = 'scale(1)';
      }, 120);
    }

    empSlider.addEventListener('input', update);
    reqSlider.addEventListener('input', update);
    update();
  }

  /* ── 5. NAVIGATION SCROLL EFFECT ────────────────────────────── */
  function initNav() {
    var nav = $('#nav');
    if (!nav) return;

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          if (window.scrollY > 60) {
            nav.classList.add('nav-scrolled');
          } else {
            nav.classList.remove('nav-scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  /* ── 6. REVEAL ON SCROLL ─────────────────────────────────────── */
  function initReveal() {
    var els = $$('.reveal');
    if (!els.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal--visible');
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    els.forEach(function (el) { observer.observe(el); });
  }

  /* ── 7. SMOOTH SCROLLING ─────────────────────────────────────── */
  function initSmoothScroll() {
    $$('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var href = anchor.getAttribute('href');
        if (href === '#') return;
        e.preventDefault();
        var target = $(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  /* ── 8. FAQ ACCORDION ────────────────────────────────────────── */
  function initFAQ() {
    $$('.faq-item').forEach(function (item) {
      var btn = item.querySelector('.faq-question');
      if (!btn) return;
      btn.addEventListener('click', function () {
        var isOpen = item.classList.contains('open');
        // Close all
        $$('.faq-item').forEach(function (i) { i.classList.remove('open'); });
        // Toggle current
        if (!isOpen) item.classList.add('open');
      });
    });
  }

  /* ── 9. MOBILE MENU TOGGLE ───────────────────────────────────── */
  function initMobileMenu() {
    var menuBtn  = $('#mobile-menu-btn');
    var mobileNav = $('#mobile-nav');
    if (!menuBtn || !mobileNav) return;

    menuBtn.addEventListener('click', function () {
      var expanded = mobileNav.classList.toggle('hidden');
      menuBtn.setAttribute('aria-expanded', !expanded);
    });
  }

  /* ── 10. THEME TOGGLE (Hell / Dunkel) ────────────────────────── */
  function initThemeToggle() {
    var btn      = document.getElementById('theme-toggle');
    var iconMoon = document.getElementById('theme-icon-moon');
    var iconSun  = document.getElementById('theme-icon-sun');
    if (!btn) return;

    var html = document.documentElement;

    function applyTheme(theme) {
      html.setAttribute('data-theme', theme);
      localStorage.setItem('sc-theme', theme);
      if (theme === 'dark') {
        if (iconMoon) iconMoon.style.display = 'none';
        if (iconSun)  iconSun.style.display  = '';
      } else {
        if (iconMoon) iconMoon.style.display = '';
        if (iconSun)  iconSun.style.display  = 'none';
      }
    }

    // Initiales Icon auf gespeichertes Theme setzen
    var saved = localStorage.getItem('sc-theme') || 'light';
    applyTheme(saved);

    btn.addEventListener('click', function () {
      var current = html.getAttribute('data-theme') || 'light';
      applyTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  /* ── 11. CONTACT MODAL ───────────────────────────────────────── */
  function getModal() { return document.getElementById('contact-modal'); }

  window.openContactModal = function () {
    var modal = getModal();
    if (!modal) return;
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    // Close on backdrop click (once)
    modal.addEventListener('click', function backdropClose(e) {
      if (e.target === modal) {
        window.closeContactModal();
        modal.removeEventListener('click', backdropClose);
      }
    });
    // Close on Escape
    document.addEventListener('keydown', function escClose(e) {
      if (e.key === 'Escape') {
        window.closeContactModal();
        document.removeEventListener('keydown', escClose);
      }
    });
  };

  window.closeContactModal = function () {
    var modal = getModal();
    if (!modal) return;
    modal.style.display = 'none';
    document.body.style.overflow = '';
    var errEl = document.getElementById('cf-error');
    if (errEl) errEl.classList.add('hidden');
  };

  window.submitContactForm = function (e) {
    e.preventDefault();
    var name    = (document.getElementById('cf-name')    || {}).value || '';
    var email   = (document.getElementById('cf-email')   || {}).value || '';
    var company = (document.getElementById('cf-company') || {}).value || '';
    var subject = (document.getElementById('cf-subject') || {}).value || 'Allgemeine Anfrage';
    var message = (document.getElementById('cf-message') || {}).value || '';
    var errEl   = document.getElementById('cf-error');

    // Minimal validation
    if (!name.trim() || !email.trim() || !message.trim()) {
      if (errEl) errEl.classList.remove('hidden');
      return;
    }
    if (errEl) errEl.classList.add('hidden');

    var mailSubject = encodeURIComponent(
      'AWAY Anfrage' + (company.trim() ? ' \u2013 ' + company.trim() : '') + ': ' + subject
    );
    var mailBody = encodeURIComponent(
      'Beratungsanfrage \u00fcber AWAY Landing Page\n' +
      '\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n' +
      'Name:         ' + name.trim() + '\n' +
      'E-Mail:       ' + email.trim() + '\n' +
      (company.trim() ? 'Unternehmen:  ' + company.trim() + '\n' : '') +
      'Betreff:      ' + subject + '\n' +
      '\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n\n' +
      message.trim()
    );

    window.open('mailto:info@wamocon.de?subject=' + mailSubject + '&body=' + mailBody);
    window.closeContactModal();
  };

  /* ── INIT ────────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    initThemeToggle();
    initLangToggle();
    initIphoneScreenCycle();
    initShowcaseTabs();
    initROICalculator();
    initNav();
    initReveal();
    initSmoothScroll();
    initFAQ();
    initMobileMenu();
  });

})();
