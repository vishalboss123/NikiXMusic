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

from AlexaMusic import app
from AlexaMusic.utils.stylish import font, stylish_button


def button(text, fallback):
    return f"{fallback} {stylish_button(font(text))}"


def help_pannel(_, START: Union[bool, int] = None):

    first = [
        InlineKeyboardButton(
            text=button("Close", "❌"),
            callback_data="close",
        )
    ]

    second = [
        InlineKeyboardButton(
            text=button("Back", "⬅️"),
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=button("Close", "❌"),
            callback_data="close",
        ),
    ]

    mark = second if START else first

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=button(_["H_B_2"], "🎶"),
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=button(_["H_B_1"], "📚"),
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=button(_["H_B_3"], "🎤"),
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text=button(_["H_B_4"], "⚙️"),
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=button(_["H_B_7"], "👑"),
                    callback_data="help_callback hb7",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=button(_["H_B_8"], "🎧"),
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=button(_["H_B_6"], "ℹ️"),
                    callback_data="help_callback hb5",
                ),
            ],
            mark,
        ]
    )


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=button(_["BACK_BUTTON"], "⬅️"),
                    callback_data="settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=button(_["CLOSE_BUTTON"], "❌"),
                    callback_data="close",
                ),
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=button(_["S_B_1"], "📚"),
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
