
from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.text & filters.group)
@admin_check
async def res_str(_, message: Message):
 if message.text == "استئناف" or message.text == "كمل" or message.text == "/resume":
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("**__◍ الموسيقي ليست موقفه √__**")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"**__◍ تم بدء الشتغيل__** \n│ \n **__بواسطة__**: {message.from_user.mention} ",
        reply_markup=close_key,
    )
