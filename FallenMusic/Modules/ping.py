
import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from FallenMusic import BOT_NAME, StartTime, app,SUDOERS
from FallenMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping") & SUDOERS)
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ɪs ᴘɪɴɢɪɴɢ..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""➻ ᴩᴏɴɢ : `{resp}ᴍs`

<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :</u></b>

๏ **ᴜᴩᴛɪᴍᴇ :** {uptime}
๏ **ʀᴀᴍ :** {mem}
๏ **ᴄᴩᴜ :** {cpu}
๏ **ᴅɪsᴋ :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("◜ꪜꫀꪀ᥆ꪑ◞", user_id=5385770251),
                    InlineKeyboardButton(
                        "◜ 𝚂𝙾𝚄𝚁𝙲𝙴 ◞",
                        url="https://t.me/s_q_i",
                    ),
                ],
            ]
        ),
    )
