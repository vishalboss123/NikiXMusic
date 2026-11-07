# ==================================================
#               PAGGLI X MUSIC
#          PREMIUM EMOJI + FONT SYSTEM
# ==================================================

# PREMIUM TELEGRAM EMOJI MAPPING
# Selected from Emoji_fan37_by_TgEmodziBot

EMOJI_IDS = {

    # GENERAL / WELCOME
    "welcome": "4956499161319998529",    # 🔥
    "hello": "4958832114540741368",      # 👋
    "star": "4958714479681471536",       # ⭐
    "love": "4956222745814762495",       # ❤️‍🔥
    "crown": "4956420911310832630",      # 👑

    # MUSIC
    "music": "4958562566688211974",      # 🎶
    "audio": "4956441587283395517",      # 🎤
    "microphone": "4958970970833421029", # 🎙
    "playlist": "4956247175588742152",   # 🪩
    "album": "4956739572114392015",      # 💎

    # PLAYER CONTROLS
    "play": "4956250031741993892",       # ▶️
    "pause": "4956442665320186933",      # ⏸
    "stop": "4958526153955476488",       # ❌
    "next": "4956282853882069908",       # ➡️
    "previous": "4956304191279596468",   # 👈
    "forward": "4958790109760587106",    # 🔼
    "backward": "4956720180337050608",   # 🔽
    "repeat": "4956371914323920049",     # 🔄

    # BOT FEATURES
    "download": "4958472587123360612",   # 💎
    "stream": "4958479549265347295",     # ⚡
    "ping": "4958479549265347295",       # ⚡
    "queue": "4958506272551863292",      # 📊
    "volume": "4958844999442629510",     # 💡
    "search": "4958587679361991667",     # 🔍
    "settings": "4958621433509970793",   # 🔖
    "help": "4958529074533238201",       # ℹ️

    # USER / DEVELOPER
    "owner": "4956420859771225351",      # 👑
    "developer": "4958725487682650920",  # 👑
    "users": "4958617898751886363",      # 👀
    "group": "4956475826762679249",      # 💬
    "channel": "4958686613933655185",    # 📣

    # STATUS
    "success": "4958610528588008305",    # ✅
    "done": "4956721670690702265",       # ✔️
    "error": "4958526153955476488",      # ❌
    "warning": "4956611513369494230",    # ⚠️
    "loading": "4956259055468282692",    # 💫
    "info": "4958529074533238201",       # ℹ️
    "notification": "4956290155326473271", # 🔔

    # EXTRA
    "gift": "4958699241137505132",       # 🎁
    "fire": "4956701046257746974",       # 🔥
    "diamond": "4956269706987177066",    # 💎
    "heart": "4956376789111800962",      # ❤️
    "flower": "4958597497657230624",     # 🌹
    "party": "4956596167451346576",      # 🎉
}


# ==================================================
#                    FONT STYLE
# ==================================================

FONT_MAP = str.maketrans({
    "a": "α", "b": "ʙ", "c": "ᴄ", "d": "ᴅ",
    "e": "є", "f": "ғ", "g": "ɢ", "h": "н",
    "i": "ɪ", "j": "נ", "k": "κ", "l": "ʟ",
    "m": "ϻ", "n": "η", "o": "σ", "p": "ᴘ",
    "q": "ǫ", "r": "ʀ", "s": "ѕ", "t": "ᴛ",
    "u": "υ", "v": "ᴠ", "w": "ᴡ", "x": "х",
    "y": "ʏ", "z": "ᴢ",
})


def font(text):
    return str(text).translate(FONT_MAP)


# ==================================================
#                PREMIUM EMOJI
# ==================================================

def emoji(name, fallback="✨"):
    emoji_id = EMOJI_IDS.get(name, "")

    if emoji_id:
        return (
            f'<tg-emoji emoji-id="{emoji_id}">'
            f'{fallback}</tg-emoji>'
        )

    return fallback


# ==================================================
#                 MESSAGE STYLE
# ==================================================

def stylish(text, emoji_name=None, fallback="✨"):
    text = font(text)

    if emoji_name:
        return f"{emoji(emoji_name, fallback)} {text}"

    return text


# ==================================================
#                  BUTTON STYLE
# ==================================================

def stylish_button(text):
    return f"˹˹{font(text)}˼˼"


def emoji_button(text, emoji_name, fallback="✨"):
    return f"{emoji(emoji_name, fallback)} {stylish_button(text)}"
