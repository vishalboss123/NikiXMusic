# Copyright (C) 2025 by Alexa_Help @ Github
# Original project credits: Team Alexa © Yukki.

"""
Paggli X Music
Based on TheTeamAlexa Telegram Music Bot.
"""

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


def get_emoji(name):
    return EMOJI_IDS.get(name, "")


answer = [
    InlineQueryResultArticle(
        title=f"{get_emoji('pause')} {stylish_button('Pause')}",
        description=stylish_button(
            "Pause the current playing stream on videochat."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title=f"{get_emoji('play')} {stylish_button('Resume')}",
        description=stylish_button(
            "Resume the paused stream on videochat."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title=f"{get_emoji('next')} {stylish_button('Skip')}",
        description=stylish_button(
            "Skip the current playing stream on videochat and move to the next stream."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title=f"{get_emoji('stop')} {stylish_button('End')}",
        description=stylish_button(
            "End the current playing stream on videochat."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title=f"{get_emoji('repeat')} {stylish_button('Shuffle')}",
        description=stylish_button(
            "Shuffle the queued songs in playlist."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title=f"{get_emoji('repeat')} {stylish_button('Loop')}",
        description=stylish_button(
            "Loop the current playing track on videochat."
        ),
        thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
]
