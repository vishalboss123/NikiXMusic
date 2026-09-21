# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import asyncio
import importlib
import os
import threading
from flask import Flask

from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AlexaMusic import LOGGER, app, userbot
from AlexaMusic.core.call import Alexa
from AlexaMusic.misc import sudo
from AlexaMusic.plugins import ALL_MODULES
from AlexaMusic.utils.database import get_banned_users, get_gbanned
from AlexaMusic.core.cookies import save_cookies


async def init() -> None:
    # Check for at least one valid Pyrogram string session
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("AlexaMusic").error("Add Pyrogram string session and then try...")
        exit()
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    await save_cookies()
    for module in ALL_MODULES:
        importlib.import_module(f"AlexaMusic.plugins{module}")
    LOGGER("AlexaMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except NoActiveGroupCall:
        LOGGER("AlexaMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        exit()
    except Exception:
        pass
    await Alexa.decorators()
    LOGGER("AlexaMusic").info("Alexa Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AlexaMusic").info("Stopping Alexa Music Bot...")




# ============================================================
#                    HEALTH SERVER FOR UPTIMEROBOT
# ============================================================

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "🤖 Alexa Music Bot is running!", 200

@flask_app.route("/health")
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )

# Flask server ko background thread me chalao
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

print(f"✅ Health server started on port {os.environ.get('PORT', 10000)}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("AlexaMusic").info("Stopping Music Bot")
