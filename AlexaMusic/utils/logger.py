# Copyright (C) 2025 by Alexa_Help @ Github
# Original project credits: Team Alexa © Yukki.

"""
Paggli X Music
Activity Logging System
Based on TheTeamAlexa Telegram Music Bot.
"""

from html import escape

from pyrogram.enums import ParseMode

from config import LOG_GROUP_ID
from AlexaMusic.utils.database import is_on_off
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button
from AlexaMusic import app


# ==========================================
# PREMIUM EMOJI
# ==========================================

def premium_emoji(name, fallback="✨"):
    emoji_id = EMOJI_IDS.get(name)

    if emoji_id:
        return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>'

    return fallback


# ==========================================
# HTML SAFE USER DETAILS
# ==========================================

def get_user_name(user):
    if not user:
        return "Unknown"

    return escape(user.first_name or "Unknown")


def get_username(user):
    if not user:
        return "None"

    return f"@{escape(user.username)}" if user.username else "None"


def get_user_mention(user):
    if not user:
        return "Unknown"

    name = escape(user.first_name or "User")
    return f'<a href="tg://user?id={user.id}">{name}</a>'


def get_chat_name(chat):
    if not chat:
        return "Unknown"

    return escape(chat.title or chat.first_name or "Private Chat")


# ==========================================
# MAIN LOG SENDER
# ==========================================

async def send_activity_log(text):
    try:
        if not LOG_GROUP_ID:
            return False

        await app.send_message(
            chat_id=LOG_GROUP_ID,
            text=text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

        return True

    except Exception as e:
        print(f"[PAGGLI LOG ERROR] {e}")
        return False


# ==========================================
# PLAY LOGS
# ==========================================

async def play_logs(message, streamtype):
    if not await is_on_off(2):
        return

    chat = message.chat
    user = message.from_user

    query = (
        message.text.split(None, 1)[1]
        if message.text and len(message.text.split(None, 1)) > 1
        else "No query provided"
    )

    logger_text = f"""
<b>{premium_emoji("music", "🎵")} {stylish_button("Paggli X Music")} {premium_emoji("info", "📋")}</b>

<b>{premium_emoji("group", "👥")} {stylish_button("Chat ID")}:</b> <code>{chat.id}</code>
<b>{premium_emoji("group", "💬")} {stylish_button("Chat Name")}:</b> {get_chat_name(chat)}
<b>{premium_emoji("users", "🔗")} {stylish_button("Chat Username")}:</b> {f"@{escape(chat.username)}" if chat.username else "None"}

<b>{premium_emoji("owner", "👤")} {stylish_button("User ID")}:</b> <code>{user.id if user else "Unknown"}</code>
<b>{premium_emoji("users", "👤")} {stylish_button("User Name")}:</b> {get_user_mention(user)}
<b>{premium_emoji("info", "🔗")} {stylish_button("Username")}:</b> {get_username(user)}

<b>{premium_emoji("search", "🔎")} {stylish_button("Query")}:</b> {escape(query)}
<b>{premium_emoji("stream", "🎧")} {stylish_button("Stream Type")}:</b> {escape(str(streamtype))}
"""

    if chat.id != LOG_GROUP_ID:
        await send_activity_log(logger_text)


# ==========================================
# USER START LOGS
# Call this from your /start handler.
# ==========================================

async def user_start_logs(message):
    user = message.from_user

    if not user:
        return

    text = f"""
<b>{premium_emoji("success", "🚀")} {stylish_button("New User Started Bot")}</b>

<b>{premium_emoji("owner", "👤")} {stylish_button("User Name")}:</b> {get_user_mention(user)}
<b>{premium_emoji("users", "🔗")} {stylish_button("Username")}:</b> {get_username(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id}</code>

<b>{premium_emoji("notification", "📢")} {stylish_button("Activity")}:</b> Started Paggli X Music
"""

    await send_activity_log(text)


# ==========================================
# USER BLOCK / UNBLOCK LOGS
# Call from my_chat_member handler.
# ==========================================

async def user_status_logs(user, status):
    if not user:
        return

    status = str(status).lower()

    if "kicked" in status or "blocked" in status:
        title = "User Blocked Bot"
        emoji = premium_emoji("error", "🚫")

    elif "member" in status or "left" in status:
        title = "User Unblocked / Returned"
        emoji = premium_emoji("success", "✅")

    else:
        return

    text = f"""
<b>{emoji} {stylish_button(title)}</b>

<b>{premium_emoji("owner", "👤")} {stylish_button("User Name")}:</b> {get_user_mention(user)}
<b>{premium_emoji("users", "🔗")} {stylish_button("Username")}:</b> {get_username(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id}</code>
"""

    await send_activity_log(text)


# ==========================================
# GROUP JOIN / LEAVE LOGS
# Call from chat_member handler.
# ==========================================

async def group_member_logs(chat, user, action):
    if not chat or not user:
        return

    action = action.lower()

    if action == "join":
        title = "New Member Joined"
        emoji = premium_emoji("success", "➕")

    elif action == "leave":
        title = "Member Left Group"
        emoji = premium_emoji("warning", "👋")

    else:
        return

    text = f"""
<b>{emoji} {stylish_button(title)}</b>

<b>{premium_emoji("group", "👥")} {stylish_button("Group Name")}:</b> {get_chat_name(chat)}
<b>{premium_emoji("info", "🆔")} {stylish_button("Group ID")}:</b> <code>{chat.id}</code>

<b>{premium_emoji("owner", "👤")} {stylish_button("User Name")}:</b> {get_user_mention(user)}
<b>{premium_emoji("users", "🔗")} {stylish_button("Username")}:</b> {get_username(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id}</code>
"""

    await send_activity_log(text)


# ==========================================
# BOT ADDED / REMOVED FROM GROUP
# ==========================================

async def bot_group_logs(chat, action):
    if not chat:
        return

    action = action.lower()

    if action == "added":
        title = "Bot Added To Group"
        emoji = premium_emoji("success", "➕")

    elif action == "removed":
        title = "Bot Removed From Group"
        emoji = premium_emoji("error", "➖")

    else:
        return

    text = f"""
<b>{emoji} {stylish_button(title)}</b>

<b>{premium_emoji("group", "👥")} {stylish_button("Group Name")}:</b> {get_chat_name(chat)}
<b>{premium_emoji("info", "🆔")} {stylish_button("Group ID")}:</b> <code>{chat.id}</code>
<b>{premium_emoji("info", "🔗")} {stylish_button("Group Username")}:</b> {f"@{escape(chat.username)}" if chat.username else "None"}
"""

    await send_activity_log(text)


# ==========================================
# SEARCH LOGS
# ==========================================

async def search_logs(message, query):
    user = message.from_user
    chat = message.chat

    text = f"""
<b>{premium_emoji("search", "🔎")} {stylish_button("New Search")}</b>

<b>{premium_emoji("owner", "👤")} {stylish_button("User")}:</b> {get_user_mention(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id if user else "Unknown"}</code>
<b>{premium_emoji("group", "👥")} {stylish_button("Chat")}:</b> {get_chat_name(chat)}
<b>{premium_emoji("info", "🔎")} {stylish_button("Query")}:</b> {escape(str(query))}
"""

    await send_activity_log(text)


# ==========================================
# DOWNLOAD LOGS
# ==========================================

async def download_logs(message, filename):
    user = message.from_user
    chat = message.chat

    text = f"""
<b>{premium_emoji("download", "📥")} {stylish_button("New Download")}</b>

<b>{premium_emoji("owner", "👤")} {stylish_button("User")}:</b> {get_user_mention(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id if user else "Unknown"}</code>
<b>{premium_emoji("group", "👥")} {stylish_button("Chat")}:</b> {get_chat_name(chat)}
<b>{premium_emoji("audio", "🎵")} {stylish_button("File Name")}:</b> {escape(str(filename))}
"""

    await send_activity_log(text)


# ==========================================
# ERROR LOGS
# ==========================================

async def error_logs(error, message=None):
    user = message.from_user if message else None
    chat = message.chat if message else None

    text = f"""
<b>{premium_emoji("error", "⚠️")} {stylish_button("Bot Error")}</b>

<b>{premium_emoji("info", "📋")} {stylish_button("Error")}:</b>
<code>{escape(str(error)[:3000])}</code>

<b>{premium_emoji("owner", "👤")} {stylish_button("User")}:</b> {get_user_mention(user)}
<b>{premium_emoji("info", "🆔")} {stylish_button("User ID")}:</b> <code>{user.id if user else "Unknown"}</code>
<b>{premium_emoji("group", "👥")} {stylish_button("Chat")}:</b> {get_chat_name(chat)}
"""

    await send_activity_log(text)
