# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and modify
as you want or you can collaborate if you have new ideas.
"""

import config

from pyrogram.types import InlineKeyboardButton
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def btn(text, callback_data=None, emoji_name=None, url=None):
    button_args = {
        "text": stylish_button(text),
    }

    if callback_data is not None:
        button_args["callback_data"] = callback_data

    if url is not None:
        button_args["url"] = url

    emoji_id = EMOJI_IDS.get(emoji_name) if emoji_name else None

    if emoji_id:
        button_args["icon_custom_emoji_id"] = emoji_id

    try:
        return InlineKeyboardButton(**button_args)
    except TypeError:
        button_args.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**button_args)


def song_markup(_, vidid):
    return [
        [
            btn(
                _["SG_B_2"],
                f"song_helper audio|{vidid}",
                "audio",
            ),
            btn(
                _["SG_B_3"],
                f"song_helper video|{vidid}",
                "stream",
            ),
        ],
        [
            btn(
                "🌻 sᴜᴩᴩᴏʀᴛ 🌻",
                url=config.SUPPORT_GROUP,
                emoji_name="group",
            ),
            btn(
                _["CLOSE_BUTTON"],
                "close",
                "stop",
            ),
        ],
    ]
