# technische datenschutz-dokumentation

stand: 18.11.2026 · gehört zu `site/datenschutz/index.html` (öffentlich unter `/datenschutz/`).
diese datei wird nicht deployt: vercel liefert nur `site/` aus (`.vercelignore` zusätzlich), github pages nimmt sie über `docs/_config.yml` (`exclude`) aus.

## hosting und auslieferung (ermittelt, nicht aus dem repo ableitbar)

| punkt | befund | beleg |
|---|---|---|
| hoster | vercel inc., projekt `ruwens-projekte/zerobot-site` (git-integration, `vercel[bot]`) | github commit-status von `web@82dac88` („Vercel – Deployment has completed“, `vercel.com/ruwens-projekte/zerobot-site/…`); antwort-header `server: Vercel`, `x-vercel-id` |
| produktiv-domain | `zerobot.bf0.by0.link` → CNAME `80aa868684f70bf9.vercel-dns-017.com` (A 216.198.79.1, 64.29.17.1) | dns-abfrage (dns.google) 18.11.2026 |
| proxy/cdn davor | keiner: dns zeigt direkt auf vercel, keine cloudflare-header. die zone `by0.link` liegt zwar bei cloudflare-dns (`chip`/`adaline.ns.cloudflare.com`), der eintrag ist aber nicht proxied | `curl -I`, dns 18.11.2026 |
| weiterleitungen | `http://` → 308 `https://zerobot.bf0.by0.link/` (vercel). `zerobot.by0.link` (alte adresse) antwortet 403, keine weiterleitung | `curl -I` 18.11.2026 |
| ausgeliefertes verzeichnis | nur `site/`: `/assets/…`, `/_headers` = 200; `/bot.py`, `/README.md`, `/site/index.html` = 404 | `curl` 18.11.2026 |
| konfiguration | keine `vercel.json`, keine functions (`api/`), keine middleware, kein build-schritt, keine `package.json` | repo-inhalt (branch `web`) |
| `site/_headers` | cloudflare-pages-format; **vercel wertet es nicht aus** und liefert es als datei aus. live gibt es daher kein `x-content-type-options`/`referrer-policy` aus dieser datei; der browser nutzt den default `strict-origin-when-cross-origin` | `curl -I` (nur `strict-transport-security`, `access-control-allow-origin: *`) |
| stand der produktion | live-html entspricht noch dem stand vor `82dac88` (links auf `zerobot.by0.link`); production-deploys aus `main` scheitern seit `d4ad498` (main hat kein `site/`). wie die aktuelle production entstanden ist, ist von außen nicht sichtbar | diff live-html vs. `site/index.html`; commit-status `main@d4ad498` = failure |
| previews | `*-ruwens-projekte.vercel.app` sind durch vercel authentication geschützt (302 auf `vercel.com/sso-api`). auf previews kann vercel die preview-/kommentar-toolbar (`vercel.live`) einblenden; betrifft nur angemeldete teammitglieder, nicht besucher der produktion | `curl` 18.11.2026 |
| altes vercel-projekt | `zerobot-website` (deploys 2021–2022 und 11/2026 aus `main`); alte deployment-urls 404/410 | github deployments-api |
| github pages | **zusätzlich aktiv**: `main:/docs` → `https://einfachruwen.github.io/ZeroBot/` (alte website von 2021). lädt beim aufruf `js.chargebee.com` (iframe + css), `us-east-1.tixte.net` (css), `zerobot.byzero.dev` (bild, nxdomain) und `shy.byzero.dev` (shynet-tracking, nxdomain). nicht teil dieser erklärung, siehe offene punkte | github pages-api, headless-chromium 18.11.2026 |

## website: verarbeitungen

zeilen beziehen sich auf `site/index.html` (branch `datenschutz`).

| # | verarbeitung | daten | fundstelle | auslöser | rechtsgrundlage | speicherdauer | belegt |
|---|---|---|---|---|---|---|---|
| 1 | auslieferung durch vercel, request-logs | ip, zeit, host, pfad, status, referrer, user-agent, aus ip abgeleiteter ort | hosting (s. o.) | jeder aufruf | art. 6 abs. 1 lit. f | dashboard: hobby 1 h, pro 1 tag (runtime logs). vercel-intern: „minimum necessary“, keine frist | header/dns live; vercel-doku |
| 2 | drittland usa (vercel) | wie 1 | – | – | art. 45 (dpf: vercel inc. eu/swiss/uk „active“) | – | dpf-liste 18.11.2026 |
| 3 | google fonts | ip, url, user-agent, referrer an `fonts.googleapis.com`/`fonts.gstatic.com` | `site/index.html:14-16` | **jeder aufruf der startseite** | art. 6 abs. 1 lit. f (angreifbar, s. offene punkte); art. 45 (google llc dpf „active“) | bei google | headless-chromium: 1 css + 4 woff2 von google beim laden |
| 4 | `/weather` | ort (freitext), dann lat/lon | `:1283`, `:1286` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `geocoding-api.open-meteo.com`, `api.open-meteo.com` |
| 5 | `/define` | suchbegriff | `:1302` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `api.urbandictionary.com` |
| 6 | `/whois` | minecraft-name, uuid; bilder von crafatar | `:1314`, `:1318-1320` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `playerdb.co`, `crafatar.com` |
| 7 | `/meme`, `/image aww` | anfrage; bild-url aus antwort (meist `i.redd.it`) | `:1327`, `:1340`, bild: `:956` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `meme-api.com`, `i.redd.it` |
| 8 | `/image floof` (katze) | anfrage, bild | `:1338` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `api.thecatapi.com`, `cdn2.thecatapi.com` |
| 9 | `/image hug` | anfrage, gif | `:1339` | befehl | art. 6 abs. 1 lit. f | beim anbieter | chromium: `api.otakugifs.xyz`, `cdn.otakugifs.xyz` |
| 10 | `/short`, `/avatar` | zu kürzende url (bei `/avatar` nur asset-url dieser site) | `:1242`, `:1234`, `shorten()` `:1406-1410` | befehl | art. 6 abs. 1 lit. f | is.gd: url dauerhaft, ip zur missbrauchsabwehr (is.gd/privacy.php) | chromium: `is.gd` |
| 11 | tenor-iframe bei „hallo/moin/servus/hi“ (4 von 6 fällen, husky-gif nur link) | ip, user-agent, referrer; tenor lädt eigene skripte inkl. `www.google-analytics.com` | `:1578-1598` (`handlePlain`), iframe `:1595` | nachricht | art. 6 abs. 1 lit. f; **§ 25 tdddg offen** (s. u.) | bei google | chromium: `tenor.com` (document/script/css/font/image), `media.tenor.com`, `www.google-analytics.com` (script) |
| 12 | localStorage `zb-pets` | zahl | store `:751-754`, lesen `:818`, schreiben `:822` (nur bei klick auf donut) | klick | § 25 abs. 2 nr. 2 tdddg | bis browserdaten gelöscht | chromium: `{"zb-pets":"1"}` nach klick, vorher leer |
| 13 | `/stats` liest gerätewerte | `navigator.hardwareConcurrency`, `navigator.deviceMemory`, `location.hostname` | `:1248-1254` | befehl | lokal, keine speicherung/übertragung (§ 25 abs. 2 nr. 2) | – | code |
| 14 | externe links | nur `<a href>`: github (`:361`, `:1265`, `:1556`), github-issue vorausgefüllt mit eingabe (`:1563`), youtube (`:1224`), google-suche (`:1554`), namemc (`:1318`), tenor (`:1594-1595`), impressum (`:362`) | – | klick | – | – | code |
| 15 | e-mail-kontakt | mailto auf der datenschutzseite | `site/datenschutz/index.html` (abschnitte 01, 10) | nutzer | art. 6 abs. 1 lit. f | bis erledigt | – |

befehle mit netzzugriff sind in der befehlstabelle mit `net: 1` markiert (`site/index.html:1069-1080`: avatar, weather, define, whois, meme, image, short); neue befehle mit `net: 1` gehören in tabelle #4–#10 und in abschnitt 04 der erklärung.

nicht vorhanden (grep + headless-chromium geprüft): cookies (auch nach allen befehlen: `ctx.cookies()` leer), sessionStorage, indexeddb, service worker, sendBeacon/xhr, formulare mit serverversand (das `<form id="composer">` wird nur lokal ausgewertet), analytics auf der seite selbst (kein umami, keine vercel web analytics/speed insights), discord-widgets/-invites/-embeds, verbindungen zu discord.

die datenschutzseite selbst lädt nur same-origin-ressourcen (`/assets/zerobot-avatar.webp`), keine google fonts.

## bot: was der code verarbeiten würde

**status: wird nicht betrieben (stand 18.11.2026, soweit von außen prüfbar).**

- belege dafür: readme 2022 („I will no longer host / maintain it“), startseite („Kein Server, kein Token“); vercel liefert nur `site/` (statisch, `bot.py` = 404, keine functions); `bot.py` braucht nicht eingecheckte dateien `tokens/*.txt` (`.gitignore`: `tokens/`, `logs/`); tote abhängigkeiten (`evergene.io` nicht erreichbar, short.io-domain `zero.byzero.dev` und `zerobot.byzero.dev` nxdomain); `discord.py==1.7.1`, `discord-py-slash-command==1.1.2` (`requirements.txt`).
- discord: anwendung `817092531874693131` „ZeroBot“ existiert noch (`bot_public: true`), flags `8429568` = presence- und guild-members-intent (limited) aktiviert, **message-content-intent nicht aktiviert** → prefix-befehle/`on_message`-inhalt würden heute ohne anpassung nicht funktionieren (`GET discord.com/api/v10/applications/817092531874693131/rpc`, 18.11.2026). server-widget von `728308958682415175` zeigt den bot nicht online (`/api/guilds/728308958682415175/widget.json`, 18.11.2026; nur momentaufnahme).
- **nicht belegbar:** ob irgendwo noch ein prozess mit dem token läuft, wo der bot früher gehostet war (kommentar `bot.py:1180`: `/root/Bots/ZeroBot/…`, also ein root-server unbekannten anbieters; `tokens/stats/hoster.txt` nicht im repo) und ob die alten logdateien noch existieren. → nutzer muss bestätigen.
- kein `/privacy`-befehl oder ähnliche datenschutz-ausgabe im bot. `/developer` und `/credits` geben nur infos zum entwickler aus.
- `python -m py_compile` für alle `.py`-dateien: ok (nicht gestartet).

falls der bot wieder eingeschaltet wird, verarbeitet er laut code (zeilen `bot.py`):

| # | verarbeitung | daten | fundstelle | empfänger/ort |
|---|---|---|---|---|
| b1 | gateway-intents | nachrichten, server, reaktionen, **mitgliederlisten, presence (status/aktivität) aller mitglieder** | `:38` | discord (plattform), arbeitsspeicher des bots |
| b2 | statcord | nutzungsstatistik (befehlsnutzung über `api.command_run`, server-/nutzerzahlen; genaue felder der bibliothek nicht geprüft) | `:36`, `:44-52` | statcord.com |
| b3 | join/leave-log | `name#discriminator` + „has joined/left“ aller server | `:119-145` | datei `logs/joinsandleaves.txt`, **unbefristet** |
| b4 | befehlslog (prefix) | nutzer-tag, mention/id, avatar-url, befehlstext, kanal, zeit, servername/-id/-owner/-mitgliederzahl/-icon | `:202-226` | datei `logs/commandlogs.txt`, **unbefristet** |
| b5 | befehlslog (slash) | wie b4 inkl. argumente | `:261-283` | `logs/commandlogs.txt` |
| b6 | log-kanal | dieselben daten + nachrichten-link als embed | `:225-235`, `:284-294` | discord-kanal `879054620838748192` |
| b7 | konsole | `"<nutzer> used <befehl>"`, lösung des ratespiels | `:236`, `:247`, `:295` | stdout des hosts |
| b8 | alle server-nachrichten | inhalt wird gelesen (mention, „hallo“, prefix, ratespiel `wait_for`) | `:166-258` | – |
| b9 | server beitreten/verlassen | name, id, owner, region, mitgliederzahl, icon | `:87-107` | log-kanal |
| b10 | moderation | kick/ban/unban mit ziel, grund, server | `:331-368`, `:546-562` | discord, log-kanal |
| b11 | fehler | fehlermeldung | `:761-784` | log-kanal |
| b12 | `/avatar` | avatar-url des mitglieds | `:516-536` | short.io (api-token) |
| b13 | `/short` | eingegebene url | `:939-958` | short.io |
| b14 | `/define` | suchbegriff | `:839-857` | urbandictionary.com (scraping) |
| b15 | `/whois` | minecraft-name | `:1069-1081` | api.mojang.com, bilder crafatar.com |
| b16 | `/image`, `/meme` | – | `:1108-1134` | evergene.io (tot) |
| b17 | `/weather` | ort | `:1146-1174` | api.openweathermap.org (api-key) |
| b18 | `/rickroll`, `/sendmsg` | dm an mitglied bzw. server-owner | `:750-757`, `:1046-1057` | discord |
| b19 | giveaway | nutzer, die reagiert haben | `:691-720` | discord |
| b20 | `/whereami`, `/howgay`, `/rps` usw. | autor, avatar, server-daten im kanal | `:993-1008` u. a. | discord-kanal |

statusbot (`status.py` = `statusbot/status.py`): liest alle 20 s den presence-status des bots auf server `728308958682415175`, schreibt `/www/index.html` auf dem host, meldet „offline“ in kanal `847777027885236235`. `Versions/` = archiv, nicht deployt.

**vor einer reaktivierung nötig:** eigener abschnitt in der erklärung mit verantwortlichem, discord als plattform (discord netherlands bv / discord inc., dpf eu-us „active – re-certification under review“ am 18.11.2026), hosting des bots (anbieter, ort, avv), statcord, short.io, openweathermap, mojang, logdateien mit löschfrist, log-kanal, rechtsgrundlagen (art. 6 abs. 1 lit. f), art. 21; besser die logs b3–b7 stark kürzen oder streichen.

## rechtliches gerüst der erklärung

- verantwortlicher wie impressum (`https://fcrw.cc/imprint` → 302 → `https://focusonruwen.com/impressum/`) und zentrale erklärung `https://focusonruwen.com/datenschutz/` (stand 15.11.2026); beide stimmen überein (c/o autorenglück #45094, hoyerswerda).
- betroffenenrechte art. 15–18, 20; art. 21 hervorgehoben (callout); beschwerde art. 77 ohne konkrete behörde.
- keine automatisierte entscheidung (art. 22); keine bereitstellungspflicht.
- keine einwilligungen eingeholt → kein widerruf nach art. 7 abs. 3, kein cookie-banner.
- quellen: vercel privacy notice (stand 01.06.2026) `https://vercel.com/legal/privacy-notice`; vercel dpa („for customers who are on enterprise and pro plans“) `https://vercel.com/legal/dpa`; runtime-log-aufbewahrung `https://vercel.com/docs/observability/runtime-logs`; dpf-liste `https://www.dataprivacyframework.gov/list` (abfrage 18.11.2026: vercel inc., google llc, reddit inc., cloudflare inc., github „active“; discord inc. „active – re-certification under review“); google fonts faq `https://developers.google.com/fonts/faq/privacy`; google-verantwortlicher eu `https://policies.google.com/privacy?hl=de`; discord privacy policy (stand 29.08.2025) `https://discord.com/privacy`; is.gd `https://is.gd/privacy.php`.

## offene punkte

1. **google fonts (größtes risiko):** die startseite lädt google fonts bei jedem aufruf ohne einwilligung. lg münchen i (urt. v. 20.01.2022, 3 o 17493/20) hielt das für unzulässig. die erklärung stützt es auf art. 6 abs. 1 lit. f, das ist angreifbar. empfehlung: die vier schriften selbst hosten (ofl), dann abschnitt 03 streichen.
2. **tenor-iframe:** lädt google-inhalte inkl. google-analytics-skript, sobald die zufallsantwort auf „hallo“ kommt. für mögliche cookies/zugriffe durch google gibt es keine einwilligung (§ 25 abs. 1 tdddg). empfehlung: nur link oder click-to-load statt iframe.
3. **drittländer der api-dienste:** für open-meteo, urban dictionary, playerdb (nodecraft), crafatar, meme-api.com, thecatapi, otakugifs, is.gd keinen dpf-eintrag/angemessenheitsbeschluss belegt (sitz/server teils unbekannt). erklärung sagt das offen; ein übermittlungsinstrument nach art. 46/49 gibt es nicht.
4. **`zb-pets`:** § 25 abs. 2 nr. 2 ist vertretbar (vom nutzer ausgelöste zählfunktion), aber nicht zwingend; alternative: `sessionStorage` oder gar nicht speichern.
5. **vercel-tarif / avv:** das dpa gilt nur für pro/enterprise. im hobby-tarif kein avv nach art. 28 → erklärung formuliert neutral („verarbeitet vercel“). tarif im dashboard prüfen.
6. **aufsichtsbehörde:** zentrale erklärung nennt lfd niedersachsen; nutzer entscheidet noch zwischen lfd niedersachsen und ldi nrw → hier nur art. 77 allgemein.
7. **bot-betrieb:** „betreibe ich derzeit nicht“ stützt sich auf repo-aussagen und eine momentaufnahme; nutzer muss bestätigen, dass kein prozess mit dem token mehr läuft und alte logs (`logs/*.txt`, log-kanal `879054620838748192`) gelöscht sind. bot-token ggf. im developer-portal zurücksetzen.
8. **github pages (`einfachruwen.github.io/ZeroBot/`):** alte seite aus `main:/docs` ist weiter öffentlich und lädt chargebee/tixte; tracking-domain tot. keine datenschutzerklärung, nicht durch diese abgedeckt. empfehlung: pages abschalten oder seite bereinigen.
9. **production-stand:** live läuft ein älterer stand; production-branch des vercel-projekts ist offenbar `main` (ohne `site/`). nach dem merge in `web` erreicht die datenschutzseite die produktion nur, wenn vercel `web` als production deployt oder `site/` auf `main` landet.
10. **`site/_headers`:** wirkt auf vercel nicht und ist öffentlich abrufbar. wenn die header gewünscht sind: `vercel.json` mit `headers` im root-verzeichnis des vercel-projekts.
11. **zentrale erklärung** auf focusonruwen.com nennt zerobot.bf0.by0.link nicht; ggf. dort verweisen.

## pflege

bei jeder änderung, die daten berührt, diese datei **und** `site/datenschutz/index.html` (inkl. stand-datum und zeilenangaben) prüfen und anpassen. siehe `CLAUDE.md`.
