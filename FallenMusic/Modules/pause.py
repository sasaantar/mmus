
from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import admin_check, close_key, is_streaming, stream_off


@app.on_message(filters.text & filters.group,group=6)
@admin_check
async def pause_str(_, message: Message):
    if message.text == "مؤقتا" or message.text == "/puase":
        try:
            await message.delete()
        except:
            pass

        if not await is_streaming(message.chat.id):
            return await message.reply_text(
            "**__◍ الموسيقي واقفه مؤقتا بالفعل__**"
        )

        await pytgcalls.pause_stream(message.chat.id)
        await stream_off(message.chat.id)
        return await message.reply_text(
            text=f"➻ **__تم أيقاف الموسيقي مؤقتا__** √\n│ \n└**__بواسطة__** : {message.from_user.mention} √",
        reply_markup=close_key,
    )
