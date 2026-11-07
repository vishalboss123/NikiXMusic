# Copyright (C) 2025 by Alexa_Help @ Github
# Subscribe On YT < Jankari Ki Duniya >.
# Original project credits: Team Alexa © Yukki.

"""
Paggli X Music
Based on TheTeamAlexa Telegram Music Bot.
"""

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID
from AlexaMusic import app
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def btn(
    text,
    callback_data=None,
    emoji_name=None,
    url=None,
    user_id=None,
):
    button_args = {
        "text": stylish_button(text)
    }

    if callback_data is not None:
        button_args["callback_data"] = callback_data

    if url is not None:
        button_args["url"] = url

    if user_id is not None:
        button_args["user_id"] = user_id

    emoji_id = EMOJI_IDS.get(emoji_name) if emoji_name else None

    if emoji_id:
        button_args["icon_custom_emoji_id"] = emoji_id

    try:
        return InlineKeyboardButton(**button_args)
    except TypeError:
        button_args.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**button_args)


def start_pannel(_):
    buttons = [
        [
            btn(
                _["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
                emoji_name="help",
            ),
            btn(
                _["S_B_2"],
                callback_data="settings_helper",
                emoji_name="settings",
            ),
        ],
    ]

    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                btn(
                    _["S_B_4"],
                    url=SUPPORT_CHANNEL,
                    emoji_name="channel",
                ),
                btn(
                    _["S_B_3"],
                    url=SUPPORT_GROUP,
                    emoji_name="group",
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    btn(
                        _["S_B_4"],
                        url=SUPPORT_CHANNEL,
                        emoji_name="channel",
                    )
                ]
            )

        if SUPPORT_GROUP:
            buttons.append(
                [
                    btn(
                        _["S_B_3"],
                        url=SUPPORT_GROUP,
                        emoji_name="group",
                    )
                ]
            )

    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            btn(
                _["S_B_8"],
                callback_data="settings_back_helper",
                emoji_name="backward",
            )
        ]
    ]

    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                btn(
                    _["S_B_4"],
                    url=SUPPORT_CHANNEL,
                    emoji_name="channel",
                ),
                btn(
                    _["S_B_3"],
                    url=SUPPORT_GROUP,
                    emoji_name="group",
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    btn(
                        _["S_B_4"],
                        url=SUPPORT_CHANNEL,
                        emoji_name="channel",
                    )
                ]
            )

        if SUPPORT_GROUP:
            buttons.append(
                [
                    btn(
                        _["S_B_3"],
                        url=SUPPORT_GROUP,
                        emoji_name="group",
                    )
                ]
            )

    buttons.append(
        [
            btn(
                _["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                emoji_name="users",
            )
        ]
    )

    if GITHUB_REPO and OWNER_ID:
        buttons.append(
            [
                btn(
                    _["S_B_7"],
                    user_id=OWNER_ID,
                    emoji_name="owner",
                ),
                btn(
                    _["S_B_6"],
                    url=GITHUB_REPO,
                    emoji_name="developer",
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    btn(
                        _["S_B_6"],
                        url=GITHUB_REPO,
                        emoji_name="developer",
                    )
                ]
            )

        if OWNER:
            buttons.append(
                [
                    btn(
                        _["S_B_7"],
                        user_id=OWNER_ID,
                        emoji_name="owner",
                    )
                ]
            )

    return buttons
