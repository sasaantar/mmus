# MIT License


from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch
import re
from FallenMusic import app


@app.on_message(filters.text,group=9)
async def ytsearch(_, message: Message):
 if re.match("^بحث (.*?)$",message.text) or re.match("^/search (.*?)$",message.text) or message.text == "بحث" or message.text == "/search":
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.text.split()) == 1:
            return await message.reply_text("**__◍ قم بكتابه اي شئ للبحث √__**")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"✨ الاسم : {results[i]['title']}\n"
            text += f"⏱ الوقت : `{results[i]['duration']}`\n"
            text += f"👀 المشاهدات : `{results[i]['views']}`\n"
            text += f"📣 القناه : {results[i]['channel']}\n"
            text += f"🔗 الرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="◞ مسح◜",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
