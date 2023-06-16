from pyrogram import filters
from FallenMusic import app,SUDOERS
from db import db
from pyrogram.types import Message


@app.on_message((filters.text | filters.photo) & SUDOERS ,group=10)
async def features(app,m:Message):
    if m.text == "ضع صوره البوت" or m.text == "/setpicbot":
        db.set("taggpic","on")
        await m.reply_text("**__◍ ارسل صوره البوت √__**")
    elif m.photo and db.get("taggpic") == "on":
        db.delete("taggpic")
        db.set("botpic",m.photo.file_id)
        await m.reply_text("**__◍ تم وضع صوره البوت √__**")
