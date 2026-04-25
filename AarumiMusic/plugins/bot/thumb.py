#
# Copyright (C) 2021-2022 by TheAloneteam@Github
#

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from AarumiMusic import app
from AarumiMusic.utils.database import is_thumb_on
from AarumiMusic.utils.decorators import language
from config import BANNED_USERS


@app.on_message(filters.command(["thumb", "thumbnail"]) & filters.group & ~filters.user(BANNED_USERS))
@language
async def thumb_command(client, message: Message, _):
    try:
        thumb_state = await is_thumb_on(message.chat.id)

        button_text = "ᴇɴᴀʙʟᴇ" if not thumb_state else "ᴅɪsᴀʙʟᴇ"

        buttons = [
            [
                InlineKeyboardButton(
                    text=button_text,
                    callback_data="THUMBNAILCHANGE"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data="close"
                ),
            ],
        ]

        await message.reply_text(
            _["thumb_1"],
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
