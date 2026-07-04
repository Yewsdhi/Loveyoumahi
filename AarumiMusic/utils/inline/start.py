# -----------------------------------------------
# 🔸 AarumiMusic Project
# 🔹 Developed & Maintained by: Aarumi Bots (https://github.com/itsAarumi)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItsAarumi
# -----------------------------------------------


from pyrogram.types import InlineKeyboardButton
import config
from AarumiMusic import app

# ── Premium emoji IDs (Emoji_fan37_by_TgEmodziBot pack) ──
_E_SPARK   = 4958489311726011319   # ✨
_E_STAR    = 4958714479681471536   # ⭐️
_E_CROWN   = 4956420911310832630   # 👑
_E_SUPPORT = 4956475826762679249   # 💬
_E_BULB    = 4958665796227171144   # 💡
_E_UPDATE  = 4956214478002717877   # 🔝
_E_DIAMOND = 4956739572114392015   # 💎
_E_BELL    = 4956290155326473271   # 🔔


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], callback_data="shiv_Aarumi"),
            InlineKeyboardButton(
                text="💌 ʏᴛ-ᴀᴘɪ",
                callback_data="api_status"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper"
            ),
        ],
    ]
    return buttons
