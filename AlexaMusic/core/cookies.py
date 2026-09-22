# Copyright (c) 2025 @KSKOP69. All rights reserved.
# Use of this source code is governed by a proprietary license.

# Made by @KSKOP69 with ❤️


import os
import aiohttp
import aiofiles
import asyncio

import config
from ..logging import LOGGER


async def fetch_content(session: aiohttp.ClientSession, url: str):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        LOGGER(__name__).error(f"Error fetching from {url}: {e}")
        return ""


async def save_file(content: str, file_path: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        async with aiofiles.open(file_path, "w") as file:
            await file.write(content)
        return file_path
    except Exception as e:
        LOGGER(__name__).error(f"Error saving file {file_path}: {e}")
        return ""


async def save_cookies():
    """Cookies file ko touch mat karo — manually upload ki gayi file use karo."""
    LOGGER(__name__).info("Skipping cookies save — using manually uploaded cookies.")
    return
