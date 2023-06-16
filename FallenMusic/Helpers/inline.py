
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="◞ مسح◜", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [[InlineKeyboardButton("◜ꪜꫀꪀ᥆ꪑ◞",user_id=5385770251)],
        [
            InlineKeyboardButton(text="◜▷◞", callback_data="resume_cb"),
            InlineKeyboardButton(text="◜II◞", callback_data="pause_cb"),
            InlineKeyboardButton(text="◜‣‣I◞", callback_data="skip_cb"),
            InlineKeyboardButton(text="◜▢◞", callback_data="end_cb"),
        ],
        [InlineKeyboardButton("◜𝚂𝙾𝚄𝚁𝙲𝙴◞",url="https://t.me/s_q_i")]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="◞ اضفني لمجموعتك◜",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="◞ الأوامر◜", callback_data="fallen_help"),InlineKeyboardButton("◞ الاستعمال◜",callback_data="how_to_use")],
    [
        InlineKeyboardButton(text="◜ꪜꫀꪀ᥆ꪑ◞", user_id=5385770251),
        InlineKeyboardButton(text="◜𝚂𝙾𝚄𝚁𝙲𝙴◞", url="https://t.me/s_q_i"),
    ]
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="◞ اضفني لمجموعتك◜",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="◞ الأوامر◜", callback_data="fallen_help"),InlineKeyboardButton("◞ الاستعمال◜",callback_data="how_to_use")],
    [
        InlineKeyboardButton(text="◜ꪜꫀꪀ᥆ꪑ◞", user_id=5385770251),
        InlineKeyboardButton(text="◜𝚂𝙾𝚄𝚁𝙲𝙴◞", url="https://t.me/s_q_i"),
    ]
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="◞ الاعضاء◜",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="◞ المطورين◜", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="◞ المبرمج◜", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="◞ رجوع◜", callback_data="fallen_home"),
        InlineKeyboardButton(text="◞ مسح◜", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="◜ꪜꫀꪀ᥆ꪑ◞", user_id=5385770251)],
    [
        InlineKeyboardButton(text="◞ ررجوع", callback_data="fallen_help"),
        InlineKeyboardButton(text="◞ مسح◜", callback_data="close"),
    ],
]
