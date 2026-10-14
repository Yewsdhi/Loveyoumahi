# -----------------------------------------------
# AarumiMusic Project
# Colored Inline Buttons
# -----------------------------------------------

import math

from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from AarumiMusic import app
import config
from AarumiMusic.utils.formatters import time_to_seconds

# Requires a Telegram Bot API/library version
# that supports InlineKeyboardButton.style.
try:
    from pyrogram.types import ButtonStyle
except ImportError:
    ButtonStyle = None


def make_button(text, callback_data, color="PRIMARY"):
    """Create a colored inline button when supported."""
    if ButtonStyle is None:
        return InlineKeyboardButton(
            text=text,
            callback_data=callback_data,
        )

    return InlineKeyboardButton(
        text=text,
        callback_data=callback_data,
        style=getattr(ButtonStyle, color),
    )


def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            make_button(
                _["P_B_1"],
                f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                "SUCCESS",
            ),
            make_button(
                _["P_B_2"],
                f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                "PRIMARY",
            ),
        ],
        [
            make_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "DANGER",
            )
        ],
    ]


def _progress_bar(percentage):
    percentage = max(0, min(100, percentage))
    position = min(9, int(percentage // 10))
    return "━" * position + "●" + "━" * (9 - position)


def _control_buttons(chat_id):
    return [
        make_button("▶️", f"ADMIN Resume|{chat_id}", "SUCCESS"),
        make_button("⏸️", f"ADMIN Pause|{chat_id}", "PRIMARY"),
        make_button("🔁", f"ADMIN Replay|{chat_id}", "PRIMARY"),
        make_button("⏭️", f"ADMIN Skip|{chat_id}", "SUCCESS"),
        make_button("⏹️", f"ADMIN Stop|{chat_id}", "DANGER"),
    ]


def _seek_buttons():
    return [
        make_button("⏪ 20s", "seek_backward_20", "PRIMARY"),
        make_button("📊 STATUS", "api_status", "SUCCESS"),
        make_button("20s ⏩", "seek_forward_20", "PRIMARY"),
    ]


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    percentage = (
        (played_sec / duration_sec) * 100
        if duration_sec > 0 else 0
    )

    bar = _progress_bar(percentage)

    return [
        [
            InlineKeyboardButton(
                text=f"🎧 {played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        _control_buttons(chat_id),
        _seek_buttons(),
        [
            make_button(
                _["CLOSE_BUTTON"],
                "close",
                "DANGER",
            )
        ],
    ]


def stream_markup(_, chat_id):
    return [
        _control_buttons(chat_id),
        _seek_buttons(),
        [
            make_button(
                _["CLOSE_BUTTON"],
                "close",
                "DANGER",
            )
        ],
    ]


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            make_button(
                _["P_B_1"],
                f"AarumiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                "SUCCESS",
            ),
            make_button(
                _["P_B_2"],
                f"AarumiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                "PRIMARY",
            ),
        ],
        [
            make_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "DANGER",
            )
        ],
    ]


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            make_button(
                _["P_B_3"],
                f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                "SUCCESS",
            )
        ],
        [
            make_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "DANGER",
            )
        ],
    ]


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = str(query)[:20]

    return [
        [
            make_button(
                _["P_B_1"],
                f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                "SUCCESS",
            ),
            make_button(
                _["P_B_2"],
                f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                "PRIMARY",
            ),
        ],
        [
            make_button(
                "◁",
                f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                "PRIMARY",
            ),
            make_button(
                _["CLOSE_BUTTON"],
                f"forceclose {query}|{user_id}",
                "DANGER",
            ),
            make_button(
                "▷",
                f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                "PRIMARY",
            ),
        ],
    ]
