# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and modify
as you want or collaborate if you have new ideas.
"""

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def btn(text, callback_data, emoji_name=None):
    """Create stylish button with optional Premium custom emoji icon."""

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
        # Compatibility fallback for Pyrogram forks
        button_args.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**button_args)


def botplaylist_markup(_):
    return [
        [
            btn(_["PL_B_1"], "get_playlist_playmode", "playlist"),
            btn(_["PL_B_8"], "get_top_playlists", "star"),
        ],
        [
            btn(_["PL_B_4"], "PM", "settings"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def top_play_markup(_):
    return [
        [btn(_["PL_B_9"], "SERVERTOP global", "users")],
        [btn(_["PL_B_10"], "SERVERTOP chat", "group")],
        [btn(_["PL_B_11"], "SERVERTOP user", "owner")],
        [
            btn(_["BACK_BUTTON"], "get_playmarkup", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def get_playlist_markup(_):
    return [
        [
            btn(_["P_B_1"], "play_playlist a", "play"),
            btn(_["P_B_2"], "play_playlist b", "playlist"),
        ],
        [
            btn(_["BACK_BUTTON"], "home_play", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def top_play_markup(_):
    return [
        [btn(_["PL_B_9"], "SERVERTOP Global", "users")],
        [btn(_["PL_B_10"], "SERVERTOP Group", "group")],
        [btn(_["PL_B_11"], "SERVERTOP Personal", "owner")],
        [
            btn(_["BACK_BUTTON"], "get_playmarkup", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def failed_top_markup(_):
    return [
        [
            btn(_["BACK_BUTTON"], "get_top_playlists", "backward"),
            btn(_["CLOSE_BUTTON"], "close", "stop"),
        ],
    ]


def warning_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["PL_B_7"],
                    "delete_whole_playlist",
                    "error",
                ),
            ],
            [
                btn(
                    _["BACK_BUTTON"],
                    "del_back_playlist",
                    "backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    "close",
                    "stop",
                ),
            ],
        ]
    )


def close_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["CLOSE_BUTTON"],
                    "close",
                    "stop",
                ),
            ]
        ]
    )
