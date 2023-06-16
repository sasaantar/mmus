
from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.text & SUDOERS,group=2)
async def set_pfp(_, message: Message):
    if message.text == "ضع صوره المساعد" or message.text == "/setpic":
        if message.reply_to_message.photo:
            fuk = await message.reply_text("**__◍ يتم ضع صوره حساب المساعد √__**")
            img = await message.reply_to_message.download()
            try:
                await app2.set_profile_photo(photo=img)
                return await fuk.edit_text(
                    f"» {ASS_MENTION} **__◍ تم تغيير صوره حساب المساعد √__**."
            )
            except:
                return await fuk.edit_text("**__◍ فشل تغيير صوره حساب المساعد √__**")
    else:
            await message.reply_text(
            "**__◍ قم بالرد على الصوره √__**"
        )


@app.on_message(filters.text & SUDOERS,group=4)
async def set_pfp(_, message: Message):
    if message.text == "حذف صوره المساعد" or message.text == "/delpic":
        try:
            pfp = [p async for p in app2.get_chat_photos("me")]
            await app2.delete_profile_photos(pfp[0].file_id)
            return await message.reply_text(
            "**__◍ تم حذف صوره المساعد √__**"
        )
        except Exception as ex:
            LOGGER.error(ex)
            await message.reply_text("**__◍ فشل في حذف صوره المساعد √__**")


@app.on_message(filters.text & SUDOERS,group=3)
async def set_bio(_, message: Message):
    if message.text == "ضع بايو المساعد" or message.text == "/setbio":
        msg = message.reply_to_message
        if msg:
            if msg.text:
                newbio = msg.text
                await app2.update_profile(bio=newbio)
                return await message.reply_text(
                    f"» {ASS_MENTION} **__◍ تم وضع بايو المساعد √__**"
            )
        else:
            return await message.reply_text(
            "**__◍ قم بالرد على الرساله √__**"
        )


@app.on_message(filters.text & SUDOERS,group=5)
async def set_name(_, message: Message):
    if message.text == "ضع اسم المساعد" or message.text == "/setname":
        msg = message.reply_to_message
        if msg:
            if msg.text:
                name = msg.text
                await app2.update_profile(first_name=name)
                return await message.reply_text(
                f"» {ASS_MENTION} **__◍ تم تغير اسم المساعد √__**."
            )
        else:
            return await message.reply_text(
            "**__◍ قم بالرد على الرساله √__**"
        )
