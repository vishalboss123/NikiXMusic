# Copyright (C) 2025 by Alexa_Help @ Github
# Paggli X Music

"""
Paggli X Music - Broadcast Manager
"""

import asyncio
import datetime
import os
import random
import string
import time
import traceback

import aiofiles

from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

from protector.brdb import db, dcmdb

from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button


# BR Tools

broadcast_ids = {}


def premium_emoji(name, fallback):
    emoji_id = EMOJI_IDS.get(name)
    if emoji_id:
        return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>'
    return fallback


async def main_broadcast_handler(m, db):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message

    while True:
        broadcast_id = "".join(
            random.choice(string.ascii_letters) for _ in range(3)
        )
        if not broadcast_ids.get(broadcast_id):
            break

    out = await m.reply_text(
        text=(
            f"{premium_emoji('notification', '📢')} "
            f"**{stylish_button('Paggli X Music Broadcast')}**\n\n"
            f"{premium_emoji('loading', '⏳')} "
            f"**{stylish_button('Broadcast Started')}...**\n\n"
            f"**» {stylish_button('When it is done, you will be notified here')}...!**"
        ),
        parse_mode="html",
    )

    start_time = time.time()
    total_users = await db.total_users_count()

    done = 0
    failed = 0
    success = 0

    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success,
    )

    async with aiofiles.open(
        "broadcast-logs.txt", "w"
    ) as broadcast_log_file:

        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user["id"]),
                message=broadcast_msg,
            )

            if msg is not None:
                await broadcast_log_file.write(msg)

            if sts == 200:
                success += 1
            else:
                failed += 1

            if sts == 400:
                await db.delete_user(user["id"])

            done += 1

            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success,
                    )
                )

    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)

    completed_in = datetime.timedelta(
        seconds=int(time.time() - start_time)
    )

    await asyncio.sleep(3)
    await out.delete()

    result_text = (
        f"{premium_emoji('success', '✅')} "
        f"**{stylish_button('Paggli X Music Broadcast Completed')}!**\n\n"
        f"{premium_emoji('info', '⏱')} "
        f"**{stylish_button('Completed In')}:** `{completed_in}`\n\n"
        f"{premium_emoji('users', '👥')} "
        f"**{stylish_button('Total Users')}:** `{total_users}`\n"
        f"**{stylish_button('Total Done')}:** `{done}`\n"
        f"{premium_emoji('success', '✅')} "
        f"**{stylish_button('Total Success')}:** `{success}`\n"
        f"{premium_emoji('error', '❌')} "
        f"**{stylish_button('Total Failed')}:** `{failed}`"
    )

    if failed == 0:
        await m.reply_text(
            text=result_text,
            quote=True,
            parse_mode="html",
        )
    else:
        await m.reply_document(
            document="broadcast-logs.txt",
            caption=result_text,
            quote=True,
            parse_mode="html",
        )

    os.remove("broadcast-logs.txt")
