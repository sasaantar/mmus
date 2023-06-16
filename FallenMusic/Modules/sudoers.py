
from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import SUDOERS, app


@app.on_message(filters.command(["addsudo"]) & filters.user(OWNER_ID))
async def sudoadd(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "**__◍ قم بالرد على المستخدم √__**"
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) in SUDOERS:
            return await message.reply_text(f"**__◍ {user.mention} هو مطور بالفعل √__**")
        try:
            SUDOERS.add(int(user.id))
            await message.reply_text(f"**__◍ تم اضافه {user.mention} الي مطورين البوت √__**")
        except:
            return await message.reply_text("**__◍ فشل في رفعه مطور في البوت √__**")

    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"**__◍ {message.reply_to_message.from_user.mention} هو مطور بالفعل √__**"
        )
    try:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"**__◍ تم اضافه {message.reply_to_message.from_user.mention} الي مطورين البوت __**"
        )
    except:
        return await message.reply_text("**__◍ فشل في رفعه مطور في البوت √__**")


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user(OWNER_ID))
async def sudodel(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "**__◍ قم بالرد على المستخدم √__**"
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) not in SUDOERS:
            return await message.reply_text(
                f"**__◍ هو ليس مطور في البوت ، {user.mention} √"
            )
        try:
            SUDOERS.remove(int(user.id))
            return await message.reply_text(
                f"**__◍ تم تنزيل {user.mention} من مطورين البوت √__**."
            )
        except:
            return await message.reply_text(f"**__◍ فشل في تنزيله من مطورين البوت √__**")
    else:
        user_id = message.reply_to_message.from_user.id
        if int(user_id) not in SUDOERS:
            return await message.reply_text(
                f"**__◍ هو ليس مطور في البوت {message.reply_to_message.from_user.mention} . √__**"
            )
        try:
            SUDOERS.remove(int(user_id))
            return await message.reply_text(
                f"**__◍ تم تنزيل {message.reply_to_message.from_user.mention} من مطورين البوت √ __**"
            )
        except:
            return await message.reply_text(f"**__◍ فشل في تنزيله من مطورين البوت √__**")


@app.on_message(filters.command(["sudolist", "sudoers", "sudo"]))
async def sudoers_list(_, message: Message):
    hehe = await message.reply_text("**__◍ يتم جلب مطورين البوت... √__**")
    text = "<u> **ᴏᴡɴᴇʀ :**</u>\n"
    count = 0
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    count += 1
    text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n<u> **sᴜᴅᴏᴇʀs :**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("**__◍ لا يوجد مطورين في البوت √__**")
    else:
        await hehe.edit_text(text)
