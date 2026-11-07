# Copyright (C) 2025 by Alexa_Help @ Github
# Original project credits: Team Alexa © Yukki.

"""
Paggli X Music
Based on TheTeamAlexa Telegram Music Bot.
"""

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlexaMusic import app
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def btn(text, callback_data=None, emoji_name=None, url=None):
    button_args = {
        "text": stylish_button(text)
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


def back_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["BACK_BUTTON"],
                    callback_data="TOPMARKUPGET",
                    emoji_name="backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    callback_data="close",
                    emoji_name="stop",
                ),
            ],
        ]
    )


def overallback_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["BACK_BUTTON"],
                    callback_data="GlobalStats",
                    emoji_name="backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    callback_data="close",
                    emoji_name="stop",
                ),
            ],
        ]
    )


def get_stats_markup(_, status):
    not_sudo = [
        btn(
            _["CLOSEMENU_BUTTON"],
            callback_data="close",
            emoji_name="stop",
        )
    ]

    sudo = [
        btn(
            _["SA_B_8"],
            callback_data="bot_stats_sudo g",
            emoji_name="owner",
        ),
        btn(
            _["CLOSEMENU_BUTTON"],
            callback_data="close",
            emoji_name="stop",
        ),
    ]

    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                    emoji_name="users",
                )
            ],
            [
                btn(
                    _["SA_B_6"],
                    url=f"https://t.me/{app.username}?start=stats",
                    emoji_name="info",
                ),
                btn(
                    _["SA_B_5"],
                    callback_data="TopOverall g",
                    emoji_name="star",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )


def stats_buttons(_, status):
    not_sudo = [
        btn(
            _["SA_B_5"],
            callback_data="TopOverall s",
            emoji_name="star",
        )
    ]

    sudo = [
        btn(
            _["SA_B_8"],
            callback_data="bot_stats_sudo s",
            emoji_name="owner",
        ),
        btn(
            _["SA_B_5"],
            callback_data="TopOverall s",
            emoji_name="star",
        ),
    ]

    return InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                btn(
                    _["CLOSE_BUTTON"],
                    callback_data="close",
                    emoji_name="stop",
                ),
            ],
        ]
    )


def back_stats_buttons(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["BACK_BUTTON"],
                    callback_data="GETSTATS",
                    emoji_name="backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    callback_data="close",
                    emoji_name="stop",
                ),
            ],
        ]
    )


def top_ten_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                btn(
                    _["SA_B_2"],
                    callback_data="GetStatsNow Tracks",
                    emoji_name="music",
                ),
                btn(
                    _["SA_B_1"],
                    callback_data="GetStatsNow Chats",
                    emoji_name="group",
                ),
            ],
            [
                btn(
                    _["SA_B_3"],
                    callback_data="GetStatsNow Users",
                    emoji_name="users",
                ),
                btn(
                    _["SA_B_4"],
                    callback_data="GetStatsNow Here",
                    emoji_name="info",
                ),
            ],
            [
                btn(
                    _["BACK_BUTTON"],
                    callback_data="GlobalStats",
                    emoji_name="backward",
                ),
                btn(
                    _["CLOSE_BUTTON"],
                    callback_data="close",
                    emoji_name="stop",
                ),
            ],
        ]
    )
