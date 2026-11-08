# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Modified Branding: Paggli X Music.
# Original project credits belong to their respective authors.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa.

Paggli X Music Custom Branding.
"""

import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PLAYLIST_IMG_URL, PRIVATE_BOT_MODE, adminlist
from AlexaMusic.misc import db
from strings import get_string
from AlexaMusic import YouTube, app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.stylish import stylish_button, EMOJI_IDS
from AlexaMusic.utils.database import (
    get_cmode,
    get_lang,
    get_playmode,
    get_assistant,
    get_playtype,
    is_active_chat,
    is_commanddelete_on,
    is_served_private_chat,
)
from AlexaMusic.utils.database.memorydatabase import is_maintenance
from AlexaMusic.utils.inline.playlist import botplaylist_markup

links = {}


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
        f'ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.\n'
        f'ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ sᴏᴍᴇ ᴛɪᴍᴇ...'
    )


# ==========================================
#              PLAY WRAPPER
# ==========================================

def PlayWrapper(command):

    async def wrapper(client, message):

        if (
            await is_maintenance() is False
            and message.from_user.id not in SUDOERS
        ):
            return await message.reply_text(
                maintenance_text(),
                parse_mode="html",
            )

        if PRIVATE_BOT_MODE == str(True) and not await is_served_private_chat(
            message.chat.id
        ):
            await message.reply_text(
                (
                    f'{premium_emoji("warning", "⚠️")} '
                    f'<b>ᴘʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ</b>\n\n'
                    f'ᴛʜɪs ʙᴏᴛ ɪs ᴏɴʟʏ ғᴏʀ '
                    f'ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀᴛs.\n\n'
                    f'ᴀsᴋ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ᴀʟʟᴏᴡ '
                    f'ʏᴏᴜʀ ᴄʜᴀᴛ ғɪʀsᴛ.'
                ),
                parse_mode="html",
            )
            return await app.leave_chat(message.chat.id)

        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except Exception:
                pass

        language = await get_lang(message.chat.id)
        _ = get_string(language)

        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )

        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )

        url = await YouTube.url(message)

        if (
            audio_telegram is None
            and video_telegram is None
            and url is None
            and len(message.command) < 2
        ):
            if "stream" in message.command:
                return await message.reply_text(_["str_1"])

            buttons = botplaylist_markup(_)

            return await message.reply_photo(
                photo=PLAYLIST_IMG_URL,
                caption=_["playlist_1"],
                reply_markup=InlineKeyboardMarkup(buttons),
            )

        if message.sender_chat:

            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"✨ {stylish_text('How To Fix This?')} ✨",
                            callback_data="AnonymousAdmin",
                            style="success",
                        ),
                    ]
                ]
            )

            return await message.reply_text(
                _["general_4"],
                reply_markup=upl,
            )

        if message.command[0][0] == "c":

            chat_id = await get_cmode(message.chat.id)

            if chat_id is None:
                return await message.reply_text(_["setting_12"])

            try:
                chat = await app.get_chat(chat_id)
            except Exception:
                return await message.reply_text(_["cplay_4"])

            channel = chat.title

        else:
            chat_id = message.chat.id
            channel = None

        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)

        if playty != "Everyone" and message.from_user.id not in SUDOERS:

            admins = adminlist.get(message.chat.id)

            if not admins:
                return await message.reply_text(_["admin_18"])

            if message.from_user.id not in admins:
                return await message.reply_text(_["play_4"])

        if message.command[0][0] == "v":
            video = True
        else:
            if message.text and "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None

        if message.command[0][-1] == "e":

            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])

            fplay = True

        else:
            fplay = None

        if not await is_active_chat(chat_id):

            userbot = await get_assistant(chat_id)

            try:

                try:
                    get = await app.get_chat_member(chat_id, userbot.id)

                except ChatAdminRequired:
                    return await message.reply_text(_["call_12"])

                if get.status in [
                    ChatMemberStatus.BANNED,
                    ChatMemberStatus.RESTRICTED,
                ]:
                    return await message.reply_text(
                        _["call_13"].format(
                            app.mention,
                            userbot.id,
                            userbot.name,
                            userbot.username,
                        )
                    )

            except UserNotParticipant:

                if chat_id in links:
                    invitelink = links[chat_id]

                else:

                    if message.chat.username:

                        invitelink = message.chat.username

                        try:
                            await userbot.resolve_peer(invitelink)
                        except Exception:
                            pass

                    else:

                        try:
                            invitelink = await app.export_chat_invite_link(
                                chat_id
                            )

                        except ChatAdminRequired:
                            return await message.reply_text(_["call_12"])

                        except Exception as e:
                            return await message.reply_text(
                                _["call_14"].format(
                                    app.mention,
                                    type(e).__name__,
                                )
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+",
                        "https://t.me/joinchat/",
                    )

                myu = await message.reply_text(
                    _["call_15"].format(app.mention)
                )

                try:

                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)

                except InviteRequestSent:

                    try:
                        await app.approve_chat_join_request(
                            chat_id,
                            userbot.id,
                        )

                    except Exception as e:
                        return await message.reply_text(
                            _["call_14"].format(
                                app.mention,
                                type(e).__name__,
                            )
                        )

                    await asyncio.sleep(3)
                    await myu.edit(
                        _["call_16"].format(app.mention)
                    )

                except UserAlreadyParticipant:
                    pass

                except Exception as e:
                    return await message.reply_text(
                        _["call_14"].format(
                            app.mention,
                            type(e).__name__,
                        )
                    )

                links[chat_id] = invitelink

                try:
                    await userbot.resolve_peer(chat_id)
                except Exception:
                    pass

        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
