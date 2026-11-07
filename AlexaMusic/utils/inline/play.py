# Copyright (C) 2025 by Alexa_Help @ Github

"""
PAGGLI X MUSIC
Premium Animated Emoji + Stylish Button System
"""

import random

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_GROUP, SUPPORT_CHANNEL

from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


OWNER_URL = "https://t.me/YTT_BISHAL"


# ==================================================
# PREMIUM EMOJI BUTTON HELPER
# ==================================================

def btn(text, emoji_name, **kwargs):
    emoji_id = EMOJI_IDS.get(emoji_name)

    button_args = {
        "text": stylish_button(text),
        **kwargs
    }

    if emoji_id:
        button_args["icon_custom_emoji_id"] = emoji_id

    return InlineKeyboardButton(**button_args)


# ==================================================
# TIMER BAR
# ==================================================

selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]


# ==================================================
# STREAM MARKUP WITH TIMER
# ==================================================

def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)

    return [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            btn(
                _["PL_B_2"],
                "playlist",
                callback_data=f"add_playlist {videoid}",
            ),
            btn(
                "Owner",
                "owner",
                url=OWNER_URL,
            ),
        ],
        [
            btn(
                _["PL_B_3"],
                "settings",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
            btn(
                "Support",
                "group",
                url=SUPPORT_GROUP,
            ),
        ],
        [
            btn(
                "Updates",
                "channel",
                url=SUPPORT_CHANNEL,
            )
        ],
    ]


def telegram_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)

    return [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            btn(
                _["PL_B_2"],
                "playlist",
                callback_data=f"add_playlist {videoid}",
            ),
            btn(
                "Owner",
                "owner",
                url=OWNER_URL,
            ),
        ],
        [
            btn(
                _["PL_B_3"],
                "settings",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            btn(
                "Support",
                "group",
                url=SUPPORT_GROUP,
            ),
        ],
    ]


# ==================================================
# INLINE WITHOUT TIMER BAR
# ==================================================

def stream_markup(_, videoid, chat_id):
    return [
        [
            btn(
                _["PL_B_2"],
                "playlist",
                callback_data=f"add_playlist {videoid}",
            ),
            btn(
                "Owner",
                "owner",
                url=OWNER_URL,
            ),
        ],
        [
            btn(
                _["PL_B_3"],
                "settings",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            btn(
                "Support",
                "group",
                url=SUPPORT_GROUP,
            ),
        ],
    ]


def telegram_markup(_, chat_id):
    return [
        [
            btn(
                _["PL_B_3"],
                "settings",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            btn(
                _["CLOSEMENU_BUTTON"],
                "stop",
                callback_data="close",
            ),
        ],
    ]


# ==================================================
# CLOSE KEYBOARD
# ==================================================

close_keyboard = InlineKeyboardMarkup(
    [
        [
            btn(
                "Close",
                "stop",
                callback_data="close",
            )
        ]
    ]
)


# ==================================================
# SEARCH QUERY INLINE
# ==================================================

def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            btn(
                _["P_B_1"],
                "music",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            btn(
                _["P_B_2"],
                "audio",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            btn(
                _["CLOSE_BUTTON"],
                "stop",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            btn(
                _["P_B_1"],
                "music",
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            btn(
                _["P_B_2"],
                "audio",
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            btn(
                _["S_B_3"],
                "group",
                url=SUPPORT_GROUP,
            ),
            btn(
                _["CLOSE_BUTTON"],
                "stop",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]


# ==================================================
# LIVE STREAM MARKUP
# ==================================================

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            btn(
                _["P_B_3"],
                "stream",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            btn(
                _["S_B_3"],
                "group",
                url=SUPPORT_GROUP,
            ),
            btn(
                _["CLOSEMENU_BUTTON"],
                "stop",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]


# ==================================================
# SLIDER QUERY MARKUP
# ==================================================

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"

    return [
        [
            btn(
                _["P_B_1"],
                "music",
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            btn(
                _["P_B_2"],
                "audio",
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            btn(
                "Previous",
                "previous",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            btn(
                _["CLOSE_BUTTON"],
                "stop",
                callback_data=f"forceclose {query}|{user_id}",
            ),
            btn(
                "Next",
                "next",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]


# ==================================================
# CPANEL MARKUP
# ==================================================

def panel_markup_1(_, videoid, chat_id):
    return [
        [
            btn(
                "Resume",
                "play",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            btn(
                "Pause",
                "pause",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            btn(
                "Skip",
                "next",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            btn(
                "Stop",
                "stop",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            btn(
                _["PL_B_2"],
                "playlist",
                callback_data=f"add_playlist {videoid}",
            ),
            btn(
                _["S_B_3"],
                "group",
                url=SUPPORT_GROUP,
            ),
        ],
        [
            btn(
                "Shuffle",
                "repeat",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            btn(
                "Loop",
                "repeat",
                callback_data=f"ADMIN Loop|{chat_id}",
            ),
        ],
        [
            btn(
                "10 Seconds Back",
                "backward",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            btn(
                "10 Seconds Forward",
                "forward",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            btn(
                "30 Seconds Back",
                "backward",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            btn(
                "30 Seconds Forward",
                "forward",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            btn(
                "Back",
                "previous",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]


# ==================================================
# QUEUE MARKUP
# ==================================================

def queue_markup(_, videoid, chat_id):
    return [
        [
            btn(
                "Resume",
                "play",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            btn(
                "Pause",
                "pause",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            btn(
                "Add Playlist",
                "playlist",
                callback_data=f"add_playlist {videoid}",
            ),
            btn(
                "Skip",
                "next",
                callback_data=f"ADMIN Skip|{chat_id}",
            ),
            btn(
                "Stop",
                "stop",
                callback_data=f"ADMIN Stop|{chat_id}",
            ),
        ],
        [
            btn(
                "Close",
                "stop",
                callback_data=f"ADMIN CloseA|{chat_id}",
            )
        ],
]
