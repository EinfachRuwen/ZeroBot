<p align="center">
  <img src="media/ZeroBot%20Banner.png" alt="ZeroBot: a hand-drawn pink donut with sprinkles on dripping teal glaze" width="720">
</p>

<h1 align="center">ZeroBot 🍩</h1>

<p align="center">
  <b>“Meet ZeroBot, the best bot for your server!”</b><br>
  A Discord bot from 2021, written by byZero at the age of 13. Switched back on in 2026.
</p>

<p align="center">
  <a href="https://zerobot.by0.link"><img alt="Revival: zerobot.by0.link" src="https://img.shields.io/badge/revival-zerobot.by0.link-f59fc2?style=for-the-badge&labelColor=131517"></a>
  <img alt="Version 3.0" src="https://img.shields.io/badge/bot-v3.0-1f4a5b?style=for-the-badge&labelColor=131517">
  <a href="LICENSE"><img alt="License: GPL-3.0" src="https://img.shields.io/badge/license-GPL--3.0-f1ab45?style=for-the-badge&labelColor=131517"></a>
</p>

---

## 🔁 The ZeroBot Revival

**➜ [zerobot.by0.link](https://zerobot.by0.link)**

ZeroBot is back, as a playable time capsule in your browser. There is no Discord server to join, no token to set up and nothing to install. You type `/` and he answers the way he did in 2021.

- **Every slash command** from the last version, with the original replies: *“Seriously? You want to see all commands? … Shut up. GET OUTTA HERE”*
- **The original code** is on the back of every answer. Flip any reply and you see the Python that produced it.
- **The original bugs are still in.** `/rps` stays silent one time in four, and `/clear 3` deletes four messages. A small 2026 note explains each one.
- **Hidden extras from the old days:** say `hallo`, start the guessing game with `_start`, or try `/calc`. That command was added and removed again on the same day in July 2021, *“cause of Security”*.
- **A `#logs` channel, the StatusBot and owner mode** for the commands that only byZero was allowed to use.
- **A time capsule of all commit messages**, from *“Initial commit”* to *“YEAHHHHHHHHHH FINALLY”*.

APIs that no longer exist were swapped for free ones that need no key: is.gd, the Urban Dictionary API, playerdb.co, meme-api.com, TheCatAPI, OtakuGIFs and Open-Meteo. The behaviour stayed the same.

<p align="center"><img src="media/PetTheZeroBot.gif" alt="A hand petting the ZeroBot donut" width="112"><br><sub>Yes, you can pet him.</sub></p>

## 📖 The story

ZeroBot started in March 2021 as a small Python bot for one Discord server, ZeroNetwork. byZero was 13 and taught himself as he went, with StackOverflow, YouTube and GitHub, as the bot’s own `/credits` command says. The bot grew into one of his biggest and longest projects.

| When | What happened |
|---|---|
| **6 Mar 2021** | *Initial commit.* Prefix commands like `_help`, `_dice` and `_kick`, with a help menu that lived on GitHub. |
| **11 Mar 2021** | **v1.0**, the first release. |
| **14 May 2021** | **v2.0: ZeroBot goes public.** The commit message says it all: *“I made the bot public :D — YEAHHHHHHHHHH FINALLY”* |
| **18 May 2021** | First outside help: [jcw05](https://github.com/joseywoermann) fixes spelling and grammar and optimizes the “hello” feature ([pull request 21](https://github.com/EinfachRuwen/ZeroBot/pull/21)). byZero’s next commit: *“just fixed a few mistakes and made more mistakes xD”* |
| **27 May 2021** | **Slash commands.** *“You don’t need a help menu anymore, and everything is a lot easier.”* |
| **June 2021** | A website, `/meme` and `/image`, a separate StatusBot that watches ZeroBot, and giveaways with several winners. |
| **17 Jul 2021** | `/weather` and a calculator arrive. The calculator used `eval()` and was gone again the same day. |
| **2022** | The bot goes offline, and the repository is archived with a goodbye (below). |
| **Nov 2026** | **The Revival.** ZeroBot runs again, this time in the browser. |

> ### ZeroBot is now archived!
> The ZeroBot, which has been offline for quite some time now, will now have to come to an end. I hereby announce that I will no longer host / maintain it. Whoever wants to, is welcome to take care of it, the repository will remain online.
>
> Thanks to all! Thanks for letting the ZeroBot be one of my biggest and longest projects.
>
> ~byZero, 2022

## 🧰 What ZeroBot can do

| | Commands |
|---|---|
| **Fun** | `/dice` `/rps` `/howgay` `/pickrandom` `/rickroll` `/meme` `/image` `/define` |
| **Moderation** | `/clear` `/commandclear` `/kick` `/ban` `/unban` `/giveaway` |
| **General** | `/help` `/ping` `/stats` `/whereami` `/avatar` `/short` `/weather` `/whois` `/developer` `/credits` `/invite` |
| **Owner only** | `/presence` `/spam` `/sendmsg` `_s` |
| **Easter eggs** | `hallo` `moin` `servus` `hi` · `@ZeroBot` · `_start` (guess the number) |
| **From v1/v2** | `_crash` `_question` `_google` `_makeissue` `_feature` `_updates` |

## 🗂 What’s in this repository

| Path | Content |
|---|---|
| [`bot.py`](bot.py) | ZeroBot v3, the last version that ran on Discord (discord.py + discord-py-slash-command) |
| [`Versions/`](Versions) | v1.0, v2.0 and v2.1 with their prefix commands |
| [`statusbot/`](statusbot) | The StatusBot that reported whether ZeroBot was online |
| [`media/`](media) | ZeroBot and Testbot, drawn by byZero, as PNG and PSD |
| [`docs/`](docs) | The old website from 2021/22 |
| Branch [`web`](../../tree/web) | The Revival: a static site in `site/`, deployed on Cloudflare Pages |

To run the Revival locally, check out the `web` branch, start `python3 -m http.server -d site` and open `http://localhost:8000`.

The original Discord bot still needs its `tokens/` folder (bot token, API keys), which was never part of this repository. Several of the APIs it used have shut down since. That’s why the Revival exists.

## 📝 License

Copyright © 2021 [byZero](https://github.com/EinfachRuwen).
This project is licensed under the [GPL-3.0](LICENSE).
