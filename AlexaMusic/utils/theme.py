# Copyright (C) 2025 by Alexa_Help @ Github
# Paggli X Music - Theme System

import random
from AlexaMusic.utils.database import get_theme

themes = [
    "alexa1",
    "alexa2",
    "alexa3",
    "alexa4",
    "alexa5",
    "alexa6",
    "alexa7",
    "alexa8",
]


async def check_theme(chat_id: int):
    """Get the selected theme or choose a random theme."""

    try:
        _theme = await get_theme(chat_id, "theme")

        if not _theme:
            return random.choice(themes)

        theme = _theme.get("theme", "Random")

        if theme == "Random":
            return random.choice(themes)

        if theme in themes:
            return theme

        return random.choice(themes)

    except Exception:
        return random.choice(themes)
