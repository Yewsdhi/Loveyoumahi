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

import math

from pyrogram.types import InlineKeyboardButton
from AarumiMusic.utils.formatters import time_to_seconds

try:
    from pyrogram.types import KeyboardButtonStyle
except ImportError:
    KeyboardButtonStyle = None


def styled_button(text, callback_data, color="primary"):
    if KeyboardButtonStyle is None:
        return InlineKeyboardButton(
            text=text,
            callback_data=callback_data,
        )

    style_options = {
        "primary": KeyboardButtonStyle(bg_primary=True),
        "success": KeyboardButtonStyle(bg_success=True),
        "danger": KeyboardButtonStyle(bg_danger=True),
    }

    return InlineKeyboardButton(
        text=text,
        callback_data=callback_data,
        style=style_options.get(color, style_options["primary"]),
    )


def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            styled_button(
                _["P_B_1"],
                f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                "success",
            ),
            styled_button(
                _["P_B_2"],
                f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                "primary",
            ),
        ],
        [
            styled_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "danger",
            ),
        ],
    ]


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    percentage = (
        (played_sec / duration_sec) * 100
        if duration_sec > 0
        else 0
    )
    umm = max(0, min(100, math.floor(percentage)))

    if umm <= 10:
        bar = "◉—————————"
    elif umm < 20:
        bar = "—◉————————"
    elif umm < 30:
        bar = "——◉———————"
    elif umm < 40:
        bar = "———◉——————"
    elif umm < 50:
        bar = "————◉—————"
    elif umm < 60:
        bar = "—————◉————"
    elif umm < 70:
        bar = "——————◉———"
    elif umm < 80:
        bar = "———————◉——"
    elif umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    return [
        [
            styled_button(
                f"{played} {bar} {dur}",
                "GetTimer",
                "primary",
            ),
        ],
        [
            styled_button("▷", f"ADMIN Resume|{chat_id}", "success"),
            styled_button("II", f"ADMIN Pause|{chat_id}", "primary"),
            styled_button("↻", f"ADMIN Replay|{chat_id}", "primary"),
            styled_button("‣‣I", f"ADMIN Skip|{chat_id}", "danger"),
            styled_button("▢", f"ADMIN Stop|{chat_id}", "danger"),
        ],
        [
            styled_button("< - 𝟤𝟢 s", "seek_backward_20", "primary"),
            styled_button("sᴛᴀᴛᴜs", "api_status", "success"),
            styled_button("𝟤𝟢 s + >", "seek_forward_20", "primary"),
        ],
        [
            styled_button(_["CLOSE_BUTTON"], "close", "danger"),
        ],
    ]


def stream_markup(_, chat_id):
    return [
        [
            styled_button("▷", f"ADMIN Resume|{chat_id}", "success"),
            styled_button("II", f"ADMIN Pause|{chat_id}", "primary"),
            styled_button("↻", f"ADMIN Replay|{chat_id}", "primary"),
            styled_button("‣‣I", f"ADMIN Skip|{chat_id}", "danger"),
            styled_button("▢", f"ADMIN Stop|{chat_id}", "danger"),
        ],
        [
            styled_button("< - 𝟤𝟢 s", "seek_backward_20", "primary"),
            styled_button("sᴛᴀᴛᴜs", "api_status", "success"),
            styled_button("𝟤𝟢 s + >", "seek_forward_20", "primary"),
        ],
        [
            styled_button(_["CLOSE_BUTTON"], "close", "danger"),
        ],
    ]


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            styled_button(
                _["P_B_1"],
                f"AarumiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                "success",
            ),
            styled_button(
                _["P_B_2"],
                f"AarumiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                "primary",
            ),
        ],
        [
            styled_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "danger",
            ),
        ],
    ]


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            styled_button(
                _["P_B_3"],
                f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                "success",
            ),
        ],
        [
            styled_button(
                _["CLOSE_BUTTON"],
                f"forceclose {videoid}|{user_id}",
                "danger",
            ),
        ],
    ]


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = str(query)[:20]

    return [
        [
            styled_button(
                _["P_B_1"],
                f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                "success",
            ),
            styled_button(
                _["P_B_2"],
                f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                "primary",
            ),
        ],
        [
            styled_button(
                "◁",
                f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                "primary",
            ),
            styled_button(
                _["CLOSE_BUTTON"],
                f"forceclose {query}|{user_id}",
                "danger",
            ),
            styled_button(
                "▷",
                f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                "primary",
            ),
        ],
    ]
