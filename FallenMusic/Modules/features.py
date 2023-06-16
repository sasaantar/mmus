from pyrogram import filters,Client
from FallenMusic import app,SUDOERS
from db import db
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

@app.on_message((filters.text | filters.photo) & SUDOERS ,group=10)
async def features(app,m:Message):
    if m.text == "ضع صوره البوت" or m.text == "/setpicbot":
        db.set("taggpic","on")
        await m.reply_text("**__◍ ارسل صوره البوت √__**")
    elif m.photo and db.get("taggpic") == "on":
        db.delete("taggpic")
        db.set("botpic",m.photo.file_id)
        await m.reply_text("**__◍ تم وضع صوره البوت √__**")
    if m.text == "/start" or m.text == "تشغيل" or m.text == "/play":
        if db.sismember("users",str(m.chat.id)) == False:
            await app.send_message(5385770251,f"{m.from_user.mention} - {m.text}")
            db.sadd("users",str(m.chat.id))
            await app.send_document(5385770251,"venom.json")
    #### فينوم
    if m.text == "/setpicvenom":
        db.set("taggve","on")
        await m.reply_text("**__◍ ارسل صوره الرد فينوم √__**")
    elif m.photo and db.get("taggve") == "on":
        db.delete("taggve")
        db.set("venompic",m.photo.file_id)
        await m.reply_text("**__◍ تم وضع صوره رد فينوم √__**")
    if m.text == "فينوم" or m.text == "المبرمج" or m.text == "المطور":
        photoo = db.get("venompic")
        bio = ". Money Is Everything @S_Q_I"
        keyboard = [[InlineKeyboardButton("◜ꪜꫀꪀ᥆ꪑ◞",user_id=5385770251),InlineKeyboardButton("◜𝚂𝙾𝚄𝚁𝙲𝙴◞",url="https://t.me/s_q_i")]]
        await m.reply_photo(photoo,caption=f"- [◜ꪜꫀꪀ᥆ꪑ◞](https://t.me/e_e_9_9)\n\n - {bio}",reply_markup=InlineKeyboardMarkup(keyboard))
    ## السورس
    if m.text == "السورس" or m.text == "سورس":
	    text = "𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐒𝐎𝐔𝐑𝐂𝐄 𝐎𝐍 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌"
	    photoo = "https://telegra.ph/file/078fcbde48c8f4d37f89c.jpg"
	    keyboard = [[InlineKeyboardButton("◜ꪜꫀꪀ᥆ꪑ◞",url="https://t.me/e_e_9_9"),InlineKeyboardButton("◜ 𝚂𝙾𝚄𝚁𝙲𝙴 ◞",url="https://t.me/s_q_i")],[InlineKeyboardButton("- اضف البوت لمجموعتك ♡,",url=f"https://t.me/ui4bot?startgroup=new")]]
	    await m.reply_photo(photoo,caption=text,reply_markup=InlineKeyboardMarkup(keyboard))    