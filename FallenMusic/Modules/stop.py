

from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import _clear_, admin_check, close_key


@app.on_message(filters.text & filters.group,group=8)
@admin_check
async def stop_str(_, message: Message):
 if message.text == "ايقاف" or message.text == "/stop":
    try:
        await message.delete()
    except:
        pass
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass

    return await message.reply_text(
        text=f"**__◍ تم ايقاف التشغيل __** \n│ \n└ʙʏ : {message.from_user.mention} ",
        reply_markup=close_key,
    )
