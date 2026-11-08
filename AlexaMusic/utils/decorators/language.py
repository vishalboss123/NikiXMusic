# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Modified Branding: Paggli X Music.
# Original project credits belong to their respective authors.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa.

Paggli X Music Custom Branding.
"""

from strings import get_string
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.stylish import stylish_button, EMOJI_IDS
from AlexaMusic.utils.database import (
    get_lang,
    is_commanddelete_on,
    is_maintenance,
)


# ==========================================
#          PAGGLI X MUSIC EMOJI
# ==========================================

def premium_emoji(name, fallback="✨"):
    emoji_id = EMOJI_IDS.get(name)

    if not emoji_id:
        return fallback

    return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>'


def stylish_text(text):
    return stylish_button(text)


def maintenance_text():
    return (
        f'{premium_emoji("warning", "⚠️")} '
        f'<b>ᴘᴀɢɢʟɪ x ᴍᴜsɪᴄ</b>\n\n'
        f'ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ғᴏʀ sᴏᴍᴇ ᴛɪᴍᴇ.\n\n'
        f'{premium_emoji("info", "ℹ️")} '
        f'ᴩʟᴇᴀsᴇ ᴠɪsɪᴛ ᴏᴜʀ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ '
        f'ᴛᴏ ᴋɴᴏᴡ ᴛʜᴇ ʀᴇᴀsᴏɴ.'
    )


# ==========================================
#             LANGUAGE DECORATOR
# ==========================================

def language(mystic):

    async def wrapper(_, message, **kwargs):

        if (
            await is_maintenance() is False
            and message.from_user.id not in SUDOERS
        ):
            return await message.reply_text(
                maintenance_text(),
                parse_mode="html",
            )

        if await is_commanddelete_on(message.chat.id):

            try:
                await message.delete()
            except Exception:
                pass

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)

        except Exception:
            language = get_string("en")

        return await mystic(_, message, language)

    return wrapper


# ==========================================
#          LANGUAGE CALLBACK DECORATOR
# ==========================================

def languageCB(mystic):

    async def wrapper(_, CallbackQuery, **kwargs):

        if (
            await is_maintenance() is False
            and CallbackQuery.from_user.id not in SUDOERS
        ):
            return await CallbackQuery.answer(
                "⚠️ Paggli X Music is under maintenance. "
                "Please visit our support chat.",
                show_alert=True,
            )

        try:
            language = await get_lang(
                CallbackQuery.message.chat.id
            )
            language = get_string(language)

        except Exception:
            language = get_string("en")

        return await mystic(_, CallbackQuery, language)

    return wrapper


# ==========================================
#             LANGUAGE START
# ==========================================

def LanguageStart(mystic):

    async def wrapper(_, message, **kwargs):

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)

        except Exception:
            language = get_string("en")

        return await mystic(_, message, language)

    return wrapper
