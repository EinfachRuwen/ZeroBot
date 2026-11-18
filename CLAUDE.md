# CLAUDE.md

two things live in this repo:

- **the revival website** (`site/`): plain html, css and js in one `site/index.html`, no build step, no `vercel.json`. deployed as static files on vercel (project `zerobot-site`, domain `zerobot.bf0.by0.link`); only `site/` is served. the readme's "cloudflare pages" note and `site/_headers` are leftovers: vercel does not apply `_headers`.
- **the original discord bot** (`bot.py`, `status.py`, `statusbot/`, `Versions/`): python, discord.py 1.7, from 2021. archived and not running. keep it as the historical record; do not modernise it unless asked.

commit messages: short, imperative, capitalised (e.g. "Add a privacy page and link it with the impressum in the footer").

## datenschutz

- the privacy policy lives at `site/datenschutz/index.html` (served at `/datenschutz/`); the technical record is `docs/PRIVACY-TECHNICAL.md`.
- **whenever a change touches personal data, the browser or the bot**, check both files and update them in the same change, including the "stand" date and the file:line references. that covers:
  - website: new external resource, script, font, image, iframe or embed; new command that calls an api; analytics; cookies, localStorage, sessionStorage, indexeddb, service worker; fetch/beacon; forms or mailto; response headers; hosting, domains, redirects or rewrites; vercel analytics/speed insights/functions/middleware.
  - bot: switching it back on or hosting it anywhere; intents; anything it logs, prints, stores or posts to a log channel; new external apis (short.io, openweathermap, mojang, statcord, …); dms; any new `/privacy`-style output.
- the bot section of the policy currently says the bot is not operated. **before the bot runs again**, extend the policy first (see "bot: was der code verarbeiten würde" in `docs/PRIVACY-TECHNICAL.md`).
- `/datenschutz/` must stay directly reachable: no catch-all rewrite or 404 handling may swallow it.
- the footer of `site/index.html` and of `site/datenschutz/index.html` must keep links to the impressum (`https://fcrw.cc/imprint`) and to `/datenschutz/`.
- the privacy page loads nothing from other servers (no google fonts); keep it that way.
- `docs/` and this file are not part of the deployment (`.vercelignore`; vercel only serves `site/`). `docs/PRIVACY-TECHNICAL.md` is also excluded from github pages in `docs/_config.yml`.
