# Copyright (C) 2025 by Alexa_Help @ Github
# Paggli X Music - Theme Database

from typing import Dict, Union
from AlexaMusic.core.mongo import mongodb

themedb = mongodb.notes


async def _get_theme(chat_id: int) -> Dict:
    _notes = await themedb.find_one({"chat_id": chat_id})

    if not _notes:
        return {}

    return _notes.get("notes", {})


async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)

    if name in _notes:
        return _notes[name]

    return False


async def save_theme(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)
    _notes[name] = note

    await themedb.update_one(
        {"chat_id": chat_id},
        {"$set": {"notes": _notes}},
        upsert=True
  )
