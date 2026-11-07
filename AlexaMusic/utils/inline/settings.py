# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and modify
as you want or you can collaborate if you have new ideas.
"""

import config
from typing import Union

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


def setting_markup(_):
    return [
        [
            btn(_["ST_B_1"], "AQ", "audio"),
            btn(_["ST_B_2"], "VQ", "stream"),
        ],
        [
            btn(_["ST_B_3"], "AU", "users"),
            btn(_["ST_B_6"], "LG", "info"),
        ],
        [
            btn(_["ST_B_5"], "PM", "play"),
            btn(_["ST_B_7"], "CM", "settings"),
        ],
        [
            btn(
                "𝖲𝗎𝗉𝗉𝗈𝗋𝗍",
                url=config.SUPPORT_GROUP,
                emoji_name="group",
            ),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            btn(
                _["ST_B_8"].format("✅") if low == True else _["ST_B_8"].format(""),
                "LQA",
                "audio",
            )
        ],
        [
            btn(
                _["ST_B_9"].format("✅") if medium == True else _["ST_B_9"].format(""),
                "MQA",
                "audio",
            )
        ],
        [
            btn(
                _["ST_B_10"].format("✅") if high == True else _["ST_B_10"].format(""),
                "HQA",
                "audio",
            )
        ],
        [
            btn(_["BACK_BUTTON"], "settingsback_helper", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            btn(
                _["ST_B_11"].format("✅") if low == True else _["ST_B_11"].format(""),
                "LQV",
                "stream",
            )
        ],
        [
            btn(
                _["ST_B_12"].format("✅") if medium == True else _["ST_B_12"].format(""),
                "MQV",
                "stream",
            )
        ],
        [
            btn(
                _["ST_B_13"].format("✅") if high == True else _["ST_B_13"].format(""),
                "HQV",
                "stream",
            )
        ],
        [
            btn(_["BACK_BUTTON"], "settingsback_helper", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    return [
        [
            btn(_["ST_B_7"], "CMANSWER", "settings"),
            btn(_["ST_B_14"] if status == True else _["ST_B_15"], "CLEANMODE", "success"),
        ],
        [
            btn(_["ST_B_26"], "COMMANDANSWER", "info"),
            btn(_["ST_B_14"] if dels == True else _["ST_B_15"], "COMMANDELMODE", "success"),
        ],
        [
            btn(_["ST_B_27"], "SUGGANSWER", "notification"),
            btn(_["ST_B_14"] if sug == True else _["ST_B_15"], "SUGGESTIONCHANGE", "success"),
        ],
        [
            btn(_["BACK_BUTTON"], "settingsback_helper", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def auth_users_markup(_, status: Union[bool, str] = None):
    return [
        [
            btn(_["ST_B_3"], "AUTHANSWER", "users"),
            btn(_["ST_B_16"] if status == True else _["ST_B_17"], "AUTH", "owner"),
        ],
        [
            btn(_["ST_B_18"], "AUTHLIST", "group"),
        ],
        [
            btn(_["BACK_BUTTON"], "settingsback_helper", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    return [
        [
            btn(_["ST_B_19"], "SEARCHANSWER", "search"),
            btn(_["ST_B_20"] if Direct == True else _["ST_B_21"], "MODECHANGE", "music"),
        ],
        [
            btn(_["ST_B_22"], "AUTHANSWER", "group"),
            btn(_["ST_B_16"] if Group == True else _["ST_B_17"], "CHANNELMODECHANGE", "success"),
        ],
        [
            btn(_["ST_B_25"], "PLAYTYPEANSWER", "play"),
            btn(_["ST_B_16"] if Playtype == True else _["ST_B_17"], "PLAYTYPECHANGE", "success"),
        ],
        [
            btn(_["BACK_BUTTON"], "settingsback_helper", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
]
