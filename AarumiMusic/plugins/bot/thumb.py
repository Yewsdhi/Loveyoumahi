from pyrogram import filters
from pyrogram.types import CallbackQuery

from AarumiMusic import app
from AarumiMusic.utils.database import is_thumb_on, set_thumb
from AarumiMusic.utils.decorators import language
from config import BANNED_USERS


@app.on_callback_query(filters.regex("THUMBNAILCHANGE") & ~filters.user(BANNED_USERS))
@language
async def thumbnail_toggle(client, query: CallbackQuery, _):
    try:
        chat_id = query.message.chat.id

        # current state check karo
        current = await is_thumb_on(chat_id)

        # toggle karo
        new_state = not current
        await set_thumb(chat_id, new_state)

        # text update
        status = "ᴇɴᴀʙʟᴇᴅ ✅" if new_state else "ᴅɪsᴀʙʟᴇᴅ ❌"

        # button update
        button_text = "ᴇɴᴀʙʟᴇ" if not new_state else "ᴅɪsᴀʙʟᴇ"

        buttons = [
            [
                InlineKeyboardButton(
                    text=button_text,
                    callback_data="THUMBNAILCHANGE"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data="close"
                )
            ]
        ]

        await query.message.edit_text(
            f"{_['thumb_1']}\n\n**Status:** {status}",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

        await query.answer("Thumbnail setting updated!")

    except Exception as e:
        await query.answer("Error occurred!", show_alert=True)
