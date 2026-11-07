# Copyright (C) 2025 by Alexa_Help @ Github
# Original project credits: Team Alexa © Yukki.

"""
Paggli X Music
System Statistics Utility
"""

import time
import psutil

from AlexaMusic.misc import _boot_
from AlexaMusic.utils.stylish import EMOJI_IDS, stylish_button
from .formatters import get_readable_time


def premium_emoji(name, fallback="✨"):
    emoji_id = EMOJI_IDS.get(name)

    if emoji_id:
        return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>'

    return fallback


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)

    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    UP = get_readable_time(bot_uptime)
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"

    return UP, CPU, RAM, DISK


def get_sys_stats_text(UP, CPU, RAM, DISK):
    return f"""
<b>{premium_emoji("settings", "⚙️")} {stylish_button("Paggli X Music System Stats")}</b>

{premium_emoji("loading", "⏱️")} <b>{stylish_button("Uptime")}:</b> {UP}
{premium_emoji("developer", "💻")} <b>{stylish_button("CPU Usage")}:</b> {CPU}
{premium_emoji("users", "🧠")} <b>{stylish_button("RAM Usage")}:</b> {RAM}
{premium_emoji("info", "💾")} <b>{stylish_button("Disk Usage")}:</b> {DISK}
"""
