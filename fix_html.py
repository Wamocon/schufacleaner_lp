# Patch script - completed, safe to delete


with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = []

# ── 1. Feature card: AWAY connection paragraph (line 474) ──────────────────
replacements.append((
    'data-de="AWAY verbindet sich direkt mit deinem Google- oder Microsoft-Konto (echter OAuth2-Flow) und versendet den fertigen Antrag inkl. AcroForm-PDF-Anhang." data-en="AWAY connects directly to your Google or Microsoft account (real OAuth2 flow) and sends the completed request including AcroForm PDF attachment.">AWAY verbindet sich direkt mit deinem Google- oder Microsoft-Konto und versendet den fertigen Antrag inkl. AcroForm-PDF-Anhang.</p>',
    'data-de="SchufaCleaner versendet das fertige Widerspruchsschreiben direkt per E-Mail an die SCHUFA oder die jeweilige Auskunftei – optional als PDF-Anhang." data-en="SchufaCleaner sends the finished dispute letter directly by email to the SCHUFA or the relevant credit bureau – optionally as a PDF attachment.">SchufaCleaner versendet das fertige Widerspruchsschreiben direkt per E-Mail an die SCHUFA oder die jeweilige Auskunftei – optional als PDF-Anhang.</p>'
))

# ── 2. Duplicate leftover paragraph (line 523) ────────────────────────────
replacements.append((
    '          <p class="text-slate-500 text-sm mb-5" data-de="Lade deine bestehenden AcroForm-PDF Vorlagen hoch. AWAY befüllt die Formularfelder direkt per Feldzuweisung – kein Platzhalter-Parsing, stabiler Export ohne Formatverlust." data-en="Upload your existing AcroForm PDF templates. AWAY fills the form fields directly via field assignment – no placeholder parsing, stable export without formatting loss.">Lade deine AcroForm-PDF Vorlagen hoch. AWAY befüllt die Formularfelder direkt per Feldzuweisung – stabiler Export ohne Formatverlust.</p>',
    ''
))

# ── 3. Feature card: TeamRadar integration → rename ───────────────────────
replacements.append((
    '          <h3 class="font-bold text-slate-900 mb-2" data-de="TeamRadar-Integration" data-en="TeamRadar integration">TeamRadar-Integration</h3>\n          <p class="text-slate-500 text-sm" data-de="AWAY ist als Micro-Frontend in TeamRadar eingebettet – direkter Absprung oder InApp-Nutzung über das App-Portal." data-en="AWAY is embedded as a micro-frontend in TeamRadar – direct jump-out or in-app use via the app portal.">AWAY ist als Micro-Frontend in TeamRadar eingebettet – InApp-Nutzung oder direkter Absprung möglich.</p>',
    '          <h3 class="font-bold text-slate-900 mb-2" data-de="API &amp; Integrationen" data-en="API &amp; integrations">API &amp; Integrationen</h3>\n          <p class="text-slate-500 text-sm" data-de="REST-API für Unternehmensintegrationen: Buchhaltungssoftware, CRM oder eigene Portale können Dispute-Status und Ergebnisse automatisiert abrufen." data-en="REST API for enterprise integrations: accounting software, CRM or custom portals can retrieve dispute status and results automatically.">REST-API für Unternehmensintegrationen: Buchhaltungssoftware, CRM oder eigene Portale können Dispute-Status automatisiert abrufen.</p>'
))

# ── 4. ROI heading description (line 877) ────────────────────────────────
replacements.append((
    '        <p class="text-white/45 text-lg max-w-xl mx-auto" data-de="Berechnet die mögliche Ersparnis durch AWAY – transparent, ohne erfundene Zahlen." data-en="Calculate your potential savings with AWAY – transparent, no made-up numbers.">Berechnet die mögliche Ersparnis durch AWAY – transparent, ohne erfundene Zahlen.</p>',
    '        <p class="text-white/45 text-lg max-w-xl mx-auto" data-de="Berechnen Sie die mögliche Zinsersparnis durch eine verbesserte Bonität – transparent, ohne erfundene Zahlen." data-en="Calculate your potential interest savings through an improved credit score – transparent, no made-up numbers.">Berechnen Sie die mögliche Zinsersparnis durch eine verbesserte Bonität – transparent, ohne erfundene Zahlen.</p>'
))

# ── 5. ROI slider 1 label + range ─────────────────────────────────────────
replacements.append((
    '                <label class="text-sm font-bold uppercase tracking-widest text-indigo-400" data-de="Negative Einträge" data-en="Negative entries">Negative Einträge</label>\n                <span id="employee-count-label" class="text-2xl font-black text-white font-display">50</span>\n              </div>\n              <input type="range" id="employee-slider" min="10" max="500" value="50">',
    '                <label class="text-sm font-bold uppercase tracking-widest text-indigo-400" data-de="Anzahl negativer Einträge" data-en="Number of negative entries">Anzahl negativer Einträge</label>\n                <span id="employee-count-label" class="text-2xl font-black text-white font-display">3</span>\n              </div>\n              <input type="range" id="employee-slider" min="1" max="20" value="3">'
))

# ── 6. ROI slider 2 label + range ─────────────────────────────────────────
replacements.append((
    '                <label class="text-sm font-bold uppercase tracking-widest text-indigo-400" data-de="Anträge / Mitarbeiter / Jahr (Ø)" data-en="Requests / employee / year (avg)">Anträge / Mitarbeiter / Jahr (Ø)</label>\n                <span id="request-count-label" class="text-2xl font-black text-white font-display">5</span>\n              </div>\n              <input type="range" id="request-slider" min="1" max="15" value="5">',
    '                <label class="text-sm font-bold uppercase tracking-widest text-indigo-400" data-de="Geplante Investition / Kredit (€)" data-en="Planned investment / loan (€)">Geplante Investition / Kredit (€)</label>\n                <span id="request-count-label" class="text-2xl font-black text-white font-display">30.000</span>\n              </div>\n              <input type="range" id="request-slider" min="5000" max="100000" value="30000" step="1000">'
))

# ── 7. ROI disclaimer ─────────────────────────────────────────────────────
replacements.append((
    '            <p class="text-white/35 text-xs leading-relaxed" data-de="Schätzung: Basis ist ein durchschnittlicher manueller Verwaltungsaufwand von ~20 Min. pro Antrag (Antrag erstellen, E-Mail versenden, Kalender manuell pflegen) und ein interner Stundensatz von 50 €/h. Eigene Werte können abweichen." data-en="Estimate: Based on an average manual effort of ~20 min. per request (creating request, sending email, manually updating calendar) and an internal hourly rate of €50/h. Your actual values may differ.">Schätzung: Basis ist ein durchschnittlicher manueller Aufwand von ~20 Min. pro Antrag und ein interner Stundensatz von 50 €/h. Eigene Werte können abweichen.</p>',
    '            <p class="text-white/35 text-xs leading-relaxed" data-de="Schätzung: Basis ist eine angenommene Zinsdifferenz von 2,5 % p.a. zwischen einem negativen und einem bereinigten SCHUFA-Score. Eigene Konditionen können abweichen." data-en="Estimate: Based on an assumed interest rate difference of 2.5% p.a. between a negative and a cleansed SCHUFA score. Your actual terms may differ.">Schätzung: Basis ist eine angenommene Zinsdifferenz von 2,5 % p.a. zwischen negativem und bereinigtem SCHUFA-Score. Eigene Konditionen können abweichen.</p>'
))

# ── 8. ROI result card ────────────────────────────────────────────────────
replacements.append((
    '            <div class="text-indigo-400 text-xs font-bold uppercase tracking-widest mb-4" data-de="Geschätzte jährliche Zeitersparnis" data-en="Estimated annual time saving">Geschätzte jährliche Zeitersparnis</div>\n            <div id="savings-value" class="text-6xl font-black text-white mb-3 font-display transition-transform">2.125 €</div>\n            <div class="text-white/40 mb-8 text-sm">≈ <span id="hours-value" class="text-white font-bold">43 Std.</span> <span data-de="weniger manuelle Arbeit pro Jahr" data-en="less manual work per year">weniger manuelle Arbeit pro Jahr</span></div>\n            <a href="#pricing" class="block w-full bg-indigo-600 hover:bg-indigo-500 text-white py-4 rounded-2xl font-bold transition-all shadow-lg shadow-indigo-900/40" data-de="Jetzt Zeit sparen" data-en="Save time now">Jetzt Zeit sparen</a>',
    '            <div class="text-indigo-400 text-xs font-bold uppercase tracking-widest mb-4" data-de="Mögliche Zinsersparnis p.a." data-en="Potential interest saving p.a.">Mögliche Zinsersparnis p.a.</div>\n            <div id="savings-value" class="text-6xl font-black text-white mb-3 font-display transition-transform">750 €</div>\n            <div class="text-white/40 mb-8 text-sm">≈ <span id="hours-value" class="text-white font-bold">3 Einträge</span> <span data-de="bestreitbar – SCHUFA-Score verbessern" data-en="contestable – improve your SCHUFA score">bestreitbar – SCHUFA-Score verbessern</span></div>\n            <a href="#pricing" class="block w-full bg-indigo-600 hover:bg-indigo-500 text-white py-4 rounded-2xl font-bold transition-all shadow-lg shadow-indigo-900/40" data-de="Jetzt Score verbessern" data-en="Improve score now">Jetzt Score verbessern</a>'
))

# ── 9. LITE pricing card content ──────────────────────────────────────────
replacements.append((
    '          <div class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-3" data-de="LITE" data-en="LITE">LITE</div>\n          <div class="flex items-end gap-1 mb-1">\n            <div class="text-4xl font-black text-slate-900 font-display">2 €</div>\n            <div class="text-slate-400 text-sm mb-1.5" data-de="/ Nutzer / Monat" data-en="/ user / month">/ Nutzer / Monat</div>\n          </div>\n          <div class="text-slate-400 text-sm mb-6" data-de="Bis 50 Nutzer · 1 Organisation" data-en="Up to 50 users · 1 organisation">Bis 50 Nutzer · 1 Organisation</div>\n          <a href="https://away-alpha.vercel.app/" target="_blank" rel="noopener" class="block w-full text-center border border-slate-200 hover:border-indigo-400 text-slate-700 hover:text-indigo-600 py-3 rounded-xl font-semibold text-sm transition-all mb-6" data-de="Lite testen" data-en="Try Lite">Lite testen</a>\n          <div class="space-y-1">\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Bis 50 Nutzer" data-en="Up to 50 users">Bis 50 Nutzer</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="1 Organisation" data-en="1 organisation">1 Organisation</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Integrierter Kalender" data-en="Embedded calendar">Integrierter Kalender</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Antragstellung (Wizard)" data-en="Request wizard">Antragstellung (Wizard)</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Standard-Support" data-en="Standard support">Standard-Support</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="AcroForm-PDF Vorlagen" data-en="AcroForm PDF templates">AcroForm-PDF Vorlagen</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="OAuth2 E-Mail-Versand" data-en="OAuth2 email dispatch">OAuth2 E-Mail-Versand</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="Kalender-Sync (Outlook/Google)" data-en="Calendar sync (Outlook/Google)">Kalender-Sync (Outlook/Google)</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="Admin-Panel &amp; Berichte" data-en="Admin panel &amp; reports">Admin-Panel &amp; Berichte</span></div>\n          </div>',
    '          <div class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-3" data-de="FREE" data-en="FREE">FREE</div>\n          <div class="flex items-end gap-1 mb-1">\n            <div class="text-4xl font-black text-slate-900 font-display">0 €</div>\n          </div>\n          <div class="text-slate-400 text-sm mb-6" data-de="Dauerhaft kostenlos" data-en="Forever free">Dauerhaft kostenlos</div>\n          <a href="https://schufacleaner.vercel.app/" target="_blank" rel="noopener" class="block w-full text-center border border-slate-200 hover:border-indigo-400 text-slate-700 hover:text-indigo-600 py-3 rounded-xl font-semibold text-sm transition-all mb-6" data-de="Kostenlos starten" data-en="Start free">Kostenlos starten</a>\n          <div class="space-y-1">\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="1 SCHUFA-Analyse" data-en="1 SCHUFA analysis">1 SCHUFA-Analyse</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="1 Widerspruchsschreiben" data-en="1 dispute letter">1 Widerspruchsschreiben</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Basis-Auswertung" data-en="Basic evaluation">Basis-Auswertung</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Standard-Support" data-en="Standard support">Standard-Support</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="Unbegrenzte Analysen" data-en="Unlimited analyses">Unbegrenzte Analysen</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="KI-Prioritätserkennung" data-en="AI priority detection">KI-Prioritätserkennung</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="Fristenverfolgung" data-en="Deadline tracking">Fristenverfolgung</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="E-Mail-Versand" data-en="Email dispatch">E-Mail-Versand</span></div>\n            <div class="pf-row"><svg class="cross-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg><span class="text-slate-400" data-de="Verlaufsberichte" data-en="History reports">Verlaufsberichte</span></div>\n          </div>'
))

# ── 10. PRO pricing card content ──────────────────────────────────────────
replacements.append((
    '          <div class="text-xs font-bold uppercase tracking-widest text-indigo-600 mb-3">PRO</div>\n          <div class="flex items-end gap-1 mb-1">\n            <div class="text-4xl font-black text-slate-900 font-display">6 €</div>\n            <div class="text-slate-400 text-sm mb-1.5" data-de="/ Nutzer / Monat" data-en="/ user / month">/ Nutzer / Monat</div>\n          </div>\n          <div class="text-slate-400 text-sm mb-6" data-de="Unbegrenzte Nutzer &amp; Organisationen" data-en="Unlimited users &amp; organisations">Unbegrenzte Nutzer &amp; Organisationen</div>\n          <a href="https://away-alpha.vercel.app/" target="_blank" rel="noopener" class="block w-full text-center bg-indigo-600 hover:bg-indigo-500 text-white py-3 rounded-xl font-semibold text-sm transition-all mb-6 shadow-lg shadow-indigo-100" data-de="Pro testen" data-en="Try Pro">Pro testen</a>\n          <div class="space-y-1">\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Alles aus Lite" data-en="Everything in Lite">Alles aus Lite</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Unbegrenzte Nutzer" data-en="Unlimited users">Unbegrenzte Nutzer</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Unbegrenzte Organisationen" data-en="Unlimited organisations">Unbegrenzte Organisationen</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="AcroForm-PDF Vorlagen" data-en="AcroForm PDF templates">AcroForm-PDF Vorlagen</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="OAuth2 E-Mail (Google &amp; Microsoft)" data-en="OAuth2 email (Google &amp; Microsoft)">OAuth2 E-Mail (Google &amp; Microsoft)</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Kalender-Sync + Team-Einladung" data-en="Calendar sync + team invitation">Kalender-Sync + Team-Einladung</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Admin-Panel &amp; Benutzerverwaltung" data-en="Admin panel &amp; user management">Admin-Panel &amp; Benutzerverwaltung</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Berichte &amp; Auslastungsübersichten" data-en="Reports &amp; capacity views">Berichte &amp; Auslastungsübersichten</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Prioritäts-Support" data-en="Priority support">Prioritäts-Support</span></div>\n          </div>',
    '          <div class="text-xs font-bold uppercase tracking-widest text-indigo-600 mb-3">PRO</div>\n          <div class="flex items-end gap-1 mb-1">\n            <div class="text-4xl font-black text-slate-900 font-display">9 €</div>\n            <div class="text-slate-400 text-sm mb-1.5" data-de="/ Nutzer / Monat" data-en="/ user / month">/ Nutzer / Monat</div>\n          </div>\n          <div class="text-slate-400 text-sm mb-6" data-de="Unbegrenzte Analysen &amp; Widersprüche" data-en="Unlimited analyses &amp; disputes">Unbegrenzte Analysen &amp; Widersprüche</div>\n          <a href="https://schufacleaner.vercel.app/" target="_blank" rel="noopener" class="block w-full text-center bg-indigo-600 hover:bg-indigo-500 text-white py-3 rounded-xl font-semibold text-sm transition-all mb-6 shadow-lg shadow-indigo-100" data-de="Pro testen" data-en="Try Pro">Pro testen</a>\n          <div class="space-y-1">\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Alles aus Free" data-en="Everything in Free">Alles aus Free</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Unbegrenzte SCHUFA-Analysen" data-en="Unlimited SCHUFA analyses">Unbegrenzte SCHUFA-Analysen</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Unbegrenzte Widerspruchsschreiben" data-en="Unlimited dispute letters">Unbegrenzte Widerspruchsschreiben</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="KI-Prioritätserkennung" data-en="AI priority detection">KI-Prioritätserkennung</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Fristenverfolgung &amp; Erinnerungen" data-en="Deadline tracking &amp; reminders">Fristenverfolgung &amp; Erinnerungen</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="E-Mail-Versand (direkt an Auskunftei)" data-en="Email dispatch (direct to bureau)">E-Mail-Versand (direkt an Auskunftei)</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Verlaufsberichte" data-en="History reports">Verlaufsberichte</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Mehrere Auskunfteien (SCHUFA, Creditreform, Bürgel)" data-en="Multiple bureaus (SCHUFA, Creditreform, Bürgel)">Mehrere Auskunfteien</span></div>\n            <div class="pf-row"><svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg><span data-de="Prioritäts-Support" data-en="Priority support">Prioritäts-Support</span></div>\n          </div>'
))

# ── 11. Innovation Package / Enterprise ───────────────────────────────────
replacements.append((
    '            <div class="text-xs font-bold uppercase tracking-widest text-indigo-400 mb-3">INNOVATION PACKAGE</div>\n            <div class="text-3xl font-black text-white font-display mb-1" data-de="Auf Anfrage" data-en="On request">Auf Anfrage</div>\n            <div class="text-white/40 text-sm mb-6" data-de="AWAY + TRACE + TeamRadar im Bundle" data-en="AWAY + TRACE + TeamRadar bundle">AWAY + TRACE + TeamRadar im Bundle</div>',
    '            <div class="text-xs font-bold uppercase tracking-widest text-indigo-400 mb-3">LEGAL EXPERT PACKAGE</div>\n            <div class="text-3xl font-black text-white font-display mb-1" data-de="Auf Anfrage" data-en="On request">Auf Anfrage</div>\n            <div class="text-white/40 text-sm mb-6" data-de="Pro + Rechtsberatung + Fachsupport" data-en="Pro + legal advice + specialist support">Pro + Rechtsberatung + Fachsupport</div>'
))

replacements.append((
    '              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span><strong class="text-white">AWAY</strong> <span data-de="– Urlaubsplaner" data-en="– Leave planner">– Urlaubsplaner</span></span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span><strong class="text-white">TRACE</strong> <span data-de="– Zeiterfassung (intern &amp; extern)" data-en="– Time tracking (internal &amp; external)">– Zeiterfassung (intern &amp; extern)</span></span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span><strong class="text-white">TeamRadar</strong> <span data-de="– Verwaltung" data-en="– Management">– Verwaltung</span></span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Zentrales App-Portal (InApp oder Direktlink)" data-en="Central app portal (in-app or direct link)">Zentrales App-Portal (InApp oder Direktlink)</span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Dediziertes Onboarding" data-en="Dedicated onboarding">Dediziertes Onboarding</span>\n              </div>',
    '              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Alles aus Pro" data-en="Everything in Pro">Alles aus Pro</span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Rechtsberatung durch Fachanwalt" data-en="Legal advice by specialist lawyer">Rechtsberatung durch Fachanwalt</span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Persönlicher Fallmanager" data-en="Personal case manager">Persönlicher Fallmanager</span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="White-Label-Option" data-en="White-label option">White-Label-Option</span>\n              </div>\n              <div class="pf-row" style="border-color:rgba(255,255,255,0.05);color:rgba(255,255,255,0.65);">\n                <svg class="check-ico w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>\n                <span data-de="Dediziertes Onboarding" data-en="Dedicated onboarding">Dediziertes Onboarding</span>\n              </div>'
))

# ── 12. FAQ items (entire block) ──────────────────────────────────────────
old_faq = '''      <div class="space-y-3 reveal">

        <div class="faq-item">
          <button class="faq-question" data-de="Wo werden meine Daten gespeichert?" data-en="Where is my data stored?">Wo werden meine Daten gespeichert?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="AWAY nutzt Supabase als Backend (Auth &amp; Datenbank). Die Datenspeicherung erfolgt ausschließlich auf EU-Servern. Die App ist vollständig DSGVO-konform entwickelt." data-en="AWAY uses Supabase as backend (auth &amp; database). Data is stored exclusively on EU servers. The app is fully GDPR-compliant.">AWAY nutzt Supabase als Backend (Auth &amp; Datenbank). Die Datenspeicherung erfolgt ausschließlich auf EU-Servern. Die App ist vollständig DSGVO-konform entwickelt.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Wie verbinde ich Outlook oder Google Kalender?" data-en="How do I connect Outlook or Google Calendar?">Wie verbinde ich Outlook oder Google Kalender?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="In den App-Einstellungen können Nutzer ihr Google- oder Microsoft-Konto per OAuth2 verbinden. Danach werden Urlaubseinträge nach Genehmigung automatisch synchronisiert und Team-Einladungen versendet. Der OAuth2-Flow ist in der App vollständig implementiert." data-en="In the app settings, users can connect their Google or Microsoft account via OAuth2. After that, approved leave is automatically synced and team invitations are sent. The OAuth2 flow is fully implemented in the app.">In den Einstellungen können Nutzer ihr Google- oder Microsoft-Konto per OAuth2 verbinden. Nach Genehmigung werden Einträge automatisch synchronisiert und Team-Einladungen versendet.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Welche Vorlagen-Formate werden unterstützt?" data-en="Which template formats are supported?">Welche Vorlagen-Formate werden unterstützt?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="AWAY verwendet ausschließlich AcroForm-PDF als Vorlagenformat. Eigene AcroForm-PDF Vorlagen hochladen – AWAY befüllt die Felder direkt per Feldzuweisung ohne Platzhalter-Parsing (Name, Zeitraum, Personalnummer, Belegnummer etc.)." data-en="AWAY exclusively uses AcroForm PDF as the template format. Upload your own AcroForm PDF templates – AWAY fills the fields directly via field assignment without placeholder parsing.">AWAY verwendet ausschließlich AcroForm-PDF. Vorlagen hochladen – AWAY befüllt die Felder direkt per Feldzuweisung ohne Platzhalter-Parsing.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Was unterscheidet Lite von Pro?" data-en="What's the difference between Lite and Pro?">Was unterscheidet Lite von Pro?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Lite ist für Teams bis 50 Nutzer mit 1 Organisation – inklusive Wizard und Basis-Kalender, jedoch ohne AcroForm-PDF Vorlagen, automatischen E-Mail- oder Kalender-Sync. Pro hebt alle Grenzen auf: unbegrenzte Nutzer und Organisationen, AcroForm-PDF Vorlagen, OAuth2 E-Mail-Versand, Outlook- &amp; Google-Kalender-Sync, Admin-Panel, Berichte und Prioritäts-Support." data-en="Lite is for teams up to 50 users with 1 organisation – including wizard and basic calendar, but without AcroForm PDF templates, automatic email or calendar sync. Pro removes all limits: unlimited users and organisations, AcroForm PDF templates, OAuth2 email dispatch, Outlook &amp; Google calendar sync, admin panel, reports and priority support.">Lite: bis 50 Nutzer, 1 Org, Basis-Kalender, kein AcroForm-PDF, kein Auto-Sync. Pro: unbegrenzte Nutzer, AcroForm-PDF, OAuth2 E-Mail, Kalender-Sync, Admin, Berichte, Prioritäts-Support.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Was ist das Innovation Package?" data-en="What is the Innovation Package?">Was ist das Innovation Package?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Das Innovation Package bündelt drei Apps: AWAY (Urlaubsplanung), TRACE (Zeiterfassung intern &amp; extern) und TeamRadar (Echtzeit-Verfügbarkeit &amp; Auslastung). TeamRadar dient als zentrale Plattform, in der AWAY und TRACE per App-Portal eingebettet sind oder direkt geöffnet werden können. Konditionen auf Anfrage." data-en="The Innovation Package bundles three apps: AWAY (leave management), TRACE (time tracking internal &amp; external) and TeamRadar (real-time availability &amp; capacity). TeamRadar serves as the central platform with AWAY and TRACE embedded via app portal or opened directly. Pricing on request.">Bundle aus AWAY (Urlaubsplanung), TRACE (Zeiterfassung) und TeamRadar (Verfügbarkeit &amp; Auslastung). TeamRadar ist die zentrale Plattform mit eingebettetem App-Portal.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Wie lange dauert die Einrichtung?" data-en="How long does setup take?">Wie lange dauert die Einrichtung?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Für die Grundeinrichtung (Konto anlegen, Organisation erstellen, erste Vorlage hochladen) werden typischerweise unter 5 Minuten benötigt. Die Anbindung von Outlook oder Google Kalender per OAuth2 ist ein einmaliger Vorgang und dauert weitere 2–3 Minuten." data-en="Basic setup (create account, create organisation, upload first template) typically takes under 5 minutes. Connecting Outlook or Google Calendar via OAuth2 is a one-time step that takes another 2–3 minutes.">Grundeinrichtung unter 5 Minuten. OAuth2-Anbindung (Outlook/Google) einmalig 2–3 Minuten zusätzlich.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Kann ich das Abo jederzeit kündigen?" data-en="Can I cancel the subscription anytime?">Kann ich das Abo jederzeit kündigen?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Ja. Pro-Abos können monatlich gekündigt werden – keine Mindestlaufzeit. Nach der Kündigung wird dein Account automatisch auf Free zurückgestuft." data-en="Yes. Pro subscriptions can be cancelled monthly – no minimum term. After cancellation, your account is automatically downgraded to Free.">Ja, monatlich kündbar ohne Mindestlaufzeit. Nach Kündigung automatische Rückstufung auf Free.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Wird AWAY mobil unterstützt?" data-en="Is AWAY supported on mobile?">Wird AWAY mobil unterstützt?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="AWAY ist als responsive Web-App (Next.js) gebaut und auf Desktop, Tablet und Smartphone nutzbar. Eine native App ist in der Roadmap. Über das TeamRadar App-Portal ist AWAY auch direkt in der TeamRadar-App verfügbar." data-en="AWAY is built as a responsive web app (Next.js) and usable on desktop, tablet and smartphone. A native app is on the roadmap. Via the TeamRadar app portal, AWAY is also available directly in the TeamRadar app.">AWAY ist eine responsive Web-App (Next.js) – nutzbar auf Desktop, Tablet und Smartphone. Native App in der Roadmap.</div>
        </div>

      </div>'''

new_faq = '''      <div class="space-y-3 reveal">

        <div class="faq-item">
          <button class="faq-question" data-de="Wo werden meine Daten gespeichert?" data-en="Where is my data stored?">Wo werden meine Daten gespeichert?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="SchufaCleaner nutzt Supabase als Backend (Auth &amp; Datenbank). Die Datenspeicherung erfolgt ausschließlich auf EU-Servern. Die App ist vollständig DSGVO-konform entwickelt und in Deutschland gehostet." data-en="SchufaCleaner uses Supabase as backend (auth &amp; database). Data is stored exclusively on EU servers. The app is fully GDPR-compliant and hosted in Germany.">SchufaCleaner nutzt Supabase als Backend (Auth &amp; Datenbank). Datenspeicherung ausschließlich auf EU-Servern. Die App ist vollständig DSGVO-konform entwickelt.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Wie funktioniert die KI-Analyse meines SCHUFA-Berichts?" data-en="How does the AI analysis of my SCHUFA report work?">Wie funktioniert die KI-Analyse meines SCHUFA-Berichts?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Sie laden Ihren SCHUFA-Bericht (PDF) hoch oder geben die Einträge manuell ein. Unsere KI erkennt automatisch fehlerhafte, veraltete oder unzulässige Einträge und bewertet deren Bestreitbarkeit nach DSGVO Art. 16/17 und BDSG-Löschfristen." data-en="You upload your SCHUFA report (PDF) or enter entries manually. Our AI automatically detects incorrect, outdated or unlawful entries and assesses their contestability under GDPR Art. 16/17 and BDSG deletion deadlines.">SCHUFA-Bericht (PDF) hochladen oder Einträge manuell erfassen. Die KI erkennt fehlerhafte oder veraltete Einträge und bewertet deren Bestreitbarkeit nach DSGVO und BDSG.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Welche Eintragsarten kann SchufaCleaner anfechten?" data-en="Which types of entries can SchufaCleaner dispute?">Welche Eintragsarten kann SchufaCleaner anfechten?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="SchufaCleaner unterstützt Widersprüche bei: veralteten Einträgen (BDSG-Löschfristen überschritten), falschen Daten (Name, Adresse, Betrag), unzulässigen Anfragen, erledigten Forderungen, die noch als offen gelistet sind, und Einträgen ohne gültige Rechtsgrundlage." data-en="SchufaCleaner supports disputes for: outdated entries (BDSG deletion deadlines exceeded), incorrect data (name, address, amount), unlawful enquiries, settled debts still listed as open, and entries without a valid legal basis.">Unterstützt werden: veraltete Einträge, falsche Daten, unzulässige Anfragen, erledigte Forderungen und Einträge ohne Rechtsgrundlage.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Was unterscheidet Free von Pro?" data-en="What's the difference between Free and Pro?">Was unterscheidet Free von Pro?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Free enthält 1 SCHUFA-Analyse und 1 Widerspruchsschreiben – ideal zum Ausprobieren. Pro bietet unbegrenzte Analysen und Schreiben, KI-Prioritätserkennung, Fristenverfolgung mit Erinnerungen, direkten E-Mail-Versand an Auskunfteien, Verlaufsberichte und Unterstützung bei mehreren Auskunfteien (SCHUFA, Creditreform, Bürgel)." data-en="Free includes 1 SCHUFA analysis and 1 dispute letter – ideal for trying out. Pro offers unlimited analyses and letters, AI priority detection, deadline tracking with reminders, direct email dispatch to credit bureaus, history reports and support for multiple bureaus (SCHUFA, Creditreform, Bürgel).">Free: 1 Analyse + 1 Schreiben zum Testen. Pro: unbegrenzte Analysen, KI-Priorität, Fristenverfolgung, E-Mail-Versand, Verlaufsberichte, mehrere Auskunfteien.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Was ist das Legal Expert Package?" data-en="What is the Legal Expert Package?">Was ist das Legal Expert Package?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Das Legal Expert Package bündelt Pro mit persönlicher Rechtsberatung durch einen Fachanwalt, einem persönlichen Fallmanager, White-Label-Option für Unternehmenskunden und dediziertem Onboarding. Konditionen auf Anfrage." data-en="The Legal Expert Package bundles Pro with personal legal advice from a specialist lawyer, a personal case manager, white-label option for business clients and dedicated onboarding. Pricing on request.">Pro + Rechtsberatung durch Fachanwalt, persönlicher Fallmanager, White-Label-Option und dediziertes Onboarding. Konditionen auf Anfrage.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Wie lange dauert die Einrichtung?" data-en="How long does setup take?">Wie lange dauert die Einrichtung?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Konto anlegen und erste SCHUFA-Analyse starten dauert unter 5 Minuten. Das Widerspruchsschreiben wird innerhalb von Sekunden generiert und ist sofort versandfertig als PDF-Download verfügbar." data-en="Creating an account and starting your first SCHUFA analysis takes under 5 minutes. The dispute letter is generated within seconds and immediately available as a ready-to-send PDF download.">Konto anlegen und erste Analyse starten: unter 5 Minuten. Widerspruchsschreiben wird in Sekunden generiert und ist sofort als PDF verfügbar.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Kann ich das Abo jederzeit kündigen?" data-en="Can I cancel the subscription anytime?">Kann ich das Abo jederzeit kündigen?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="Ja. Pro-Abos können monatlich gekündigt werden – keine Mindestlaufzeit. Nach der Kündigung wird dein Account automatisch auf Free zurückgestuft." data-en="Yes. Pro subscriptions can be cancelled monthly – no minimum term. After cancellation, your account is automatically downgraded to Free.">Ja, monatlich kündbar ohne Mindestlaufzeit. Nach Kündigung automatische Rückstufung auf Free.</div>
        </div>

        <div class="faq-item">
          <button class="faq-question" data-de="Ist SchufaCleaner auf dem Smartphone nutzbar?" data-en="Is SchufaCleaner usable on smartphone?">Ist SchufaCleaner auf dem Smartphone nutzbar?
            <svg class="faq-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer" data-de="SchufaCleaner ist als responsive Web-App gebaut und auf Desktop, Tablet und Smartphone vollständig nutzbar. Eine native iOS- und Android-App ist in der Roadmap." data-en="SchufaCleaner is built as a responsive web app and fully usable on desktop, tablet and smartphone. A native iOS and Android app is on the roadmap.">SchufaCleaner ist eine responsive Web-App – vollständig nutzbar auf Desktop, Tablet und Smartphone. Native App in der Roadmap.</div>
        </div>

      </div>'''

replacements.append((old_faq, new_faq))

# ── 13. Final CTA heading + description ───────────────────────────────────
replacements.append((
    '<h2 class="text-4xl md:text-6xl font-black text-white font-display tracking-tight mb-6"><span data-de="Bereit für strukturierte Urlaubsplanung?" data-en="Ready for structured leave management?">Bereit für strukturierte Urlaubsplanung?</span></h2>\n      <p class="text-white/45 text-lg mb-10 max-w-xl mx-auto" data-de="Jetzt kostenlos starten – kein Excel, kein E-Mail-Chaos, kein manuelles Kalenderpflegen." data-en="Start free now – no Excel, no email chaos, no manual calendar maintenance.">Jetzt kostenlos starten – kein Excel, kein E-Mail-Chaos, kein manuelles Kalenderpflegen.</p>',
    '<h2 class="text-4xl md:text-6xl font-black text-white font-display tracking-tight mb-6"><span data-de="Bereit, Ihren SCHUFA-Score zu verbessern?" data-en="Ready to improve your SCHUFA score?">Bereit, Ihren SCHUFA-Score zu verbessern?</span></h2>\n      <p class="text-white/45 text-lg mb-10 max-w-xl mx-auto" data-de="Jetzt kostenlos starten – kein Anwalt nötig, kein Papierchaos, keine versteckten Kosten." data-en="Start free now – no lawyer needed, no paperwork chaos, no hidden costs.">Jetzt kostenlos starten – kein Anwalt nötig, kein Papierchaos, keine versteckten Kosten.</p>'
))

# ── 14. Final CTA link (away-alpha URL) ───────────────────────────────────
replacements.append((
    '        <a href="https://away-alpha.vercel.app/" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white px-8 py-4 rounded-2xl font-bold text-base transition-all shadow-xl shadow-indigo-900/40 active:scale-95" data-de="Kostenlos starten" data-en="Start free">',
    '        <a href="https://schufacleaner.vercel.app/" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white px-8 py-4 rounded-2xl font-bold text-base transition-all shadow-xl shadow-indigo-900/40 active:scale-95" data-de="Kostenlos starten" data-en="Start free">'
))

# ── 15. Footer: brand name + description ──────────────────────────────────
replacements.append((
    '            <span class="text-lg font-black text-white font-display tracking-tight">AWAY</span>',
    '            <span class="text-lg font-black text-white font-display tracking-tight">SchufaCleaner</span>'
))

replacements.append((
    '          <p class="text-white/30 text-sm leading-relaxed mb-5" data-de="Der intelligente Urlaubsplaner für moderne Teams. Entwickelt von WAMOCON." data-en="The intelligent leave planner for modern teams. Developed by WAMOCON.">Der intelligente Urlaubsplaner für moderne Teams. Entwickelt von WAMOCON.</p>',
    '          <p class="text-white/30 text-sm leading-relaxed mb-5" data-de="KI-gestützte SCHUFA-Bereinigung – rechtssichere Widerspruchsschreiben nach DSGVO Art. 16/17. Entwickelt von WAMOCON." data-en="AI-powered SCHUFA dispute tool – legally sound dispute letters under GDPR Art. 16/17. Developed by WAMOCON.">KI-gestützte SCHUFA-Bereinigung – rechtssichere Widerspruchsschreiben nach DSGVO Art. 16/17. Entwickelt von WAMOCON.</p>'
))

replacements.append((
    '              <span class="w-2 h-2 rounded-full bg-indigo-500"></span>AWAY\n              <span class="text-[10px] text-indigo-400/60 font-semibold ml-1" data-de="Urlaubsplaner" data-en="Leave planner">Urlaubsplaner</span>',
    '              <span class="w-2 h-2 rounded-full bg-indigo-500"></span>SchufaCleaner\n              <span class="text-[10px] text-indigo-400/60 font-semibold ml-1" data-de="SCHUFA-Bereinigung" data-en="Credit repair">SCHUFA-Bereinigung</span>'
))

replacements.append((
    '        <p class="text-white/20 text-xs" data-de="© 2026 AWAY. Ein Produkt der WAMOCON GmbH. Alle Rechte vorbehalten." data-en="© 2026 AWAY. A product of WAMOCON GmbH. All rights reserved.">© 2026 AWAY. Ein Produkt der WAMOCON GmbH. Alle Rechte vorbehalten.</p>',
    '        <p class="text-white/20 text-xs" data-de="© 2026 SchufaCleaner. Ein Produkt der WAMOCON GmbH. Alle Rechte vorbehalten." data-en="© 2026 SchufaCleaner. A product of WAMOCON GmbH. All rights reserved.">© 2026 SchufaCleaner. Ein Produkt der WAMOCON GmbH. Alle Rechte vorbehalten.</p>'
))

# ── 16. Contact modal: AWAY references ────────────────────────────────────
replacements.append((
    '            <span class="font-black text-slate-900 font-display tracking-tight">AWAY</span>',
    '            <span class="font-black text-slate-900 font-display tracking-tight">SchufaCleaner</span>'
))

replacements.append((
    '        <p class="text-slate-400 text-sm mb-7">AWAY Innovation Package oder allgemeine Produktanfrage</p>',
    '        <p class="text-slate-400 text-sm mb-7" data-de="Legal Expert Package oder allgemeine Produktanfrage" data-en="Legal Expert Package or general product enquiry">Legal Expert Package oder allgemeine Produktanfrage</p>'
))

replacements.append((
    '              <option value="AWAY Pro – Beratung">AWAY Pro – Beratung</option>',
    '              <option value="SchufaCleaner Pro – Beratung">SchufaCleaner Pro – Beratung</option>'
))

# Apply all replacements
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✓ Applied replacement (first 60 chars): {old[:60].strip()!r}")
    else:
        print(f"✗ NOT FOUND: {old[:60].strip()!r}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone. Verifying...")
away_count = html.count('AWAY')
away_alpha_count = html.count('away-alpha')
schufa_count = html.count('SchufaCleaner')
print(f"  'AWAY' occurrences: {away_count}")
print(f"  'away-alpha' occurrences: {away_alpha_count}")
print(f"  'SchufaCleaner' occurrences: {schufa_count}")
print(f"  Total lines: {html.count(chr(10))}")
