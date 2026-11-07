# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and modify
as you want or collaborate if you have new ideas.
"""

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def btn(text, callback_data, emoji_name=None):
    button_args = {
        "text": stylish_button(text),
        "callback_data": callback_data,
    }

    emoji_id = EMOJI_IDS.get(emoji_name) if emoji_name else None

    if emoji_id:
        button_args["icon_custom_emoji_id"] = emoji_id

    try:
        return InlineKeyboardButton(**button_args)
    except TypeError:
        button_args.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**button_args)


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            btn(
                _["QU_B_1"],
                f"GetQueued {CPLAY}|{videoid}",
                "queue",
            ),
            btn(
                _["CLOSEMENU_BUTTON"],
                "close",
                "stop",
            ),
        ]
    ]

    dur = [
        [
            btn(
                _["QU_B_2"].format(played, dur),
                "GetTimer",
                "loading",
            )
        ],
        [
            btn(
                _["QU_B_1"],
                f"GetQueued {CPLAY}|{videoid}",
                "queue",
            ),
            btn(
                _["CLOSEMENU_BUTTON"],
                "close",
                "stop",
            ),
        ],
    ]

    return InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)


def queue_back_markup(_, CPLAY):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["BACK_BUTTON"],
                    f"queue_back_timer {CPLAY}",
                    "backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    "close",
                    "stop",
                ),
            ]
        ]
)
