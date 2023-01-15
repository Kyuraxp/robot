# Copyright (c) 2022 Shiinobu Project

from datetime import datetime

from pyrogram import filters

from pyrogram.types import (

    InlineKeyboardButton,

    InlineKeyboardMarkup,

    CallbackQuery,

    Message,

)

from EmikoRobot import pbot as Client

from EmikoRobot import (

    OWNER_ID as owner,

    SUPPORT_CHAT as log,

)

from EmikoRobot.utils.errors import capture_err

def content(msg: Message) -> [None, str]:

    text_to_return = msg.text

    if msg.text is None:

        return None

    if " " in text_to_return:

        try:

            return msg.text.split(None, 1)[1]

        except IndexError:

            return None

    else:

        return None

@Client.on_message(filters.command("bug"))

@capture_err

async def bug(_, msg: Message):

    if msg.chat.username:

        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")

    else:

        chat_username = (f"ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ/ `{msg.chat.id}`")

    bugs = content(msg)

    user_id = msg.from_user.id

    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"

    datetimes_fmt = "%d-%m-%Y"

    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/6896aefa314491ca5a3a8.jpg"

    

    bug_report = f"""

**#BUG : ** **[@Hisoka69](https://t.me/hisoka69)**

**ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ: ** **{mention}**

**ɪᴅ ᴘᴇɴɢɢᴜɴᴀ: ** **{user_id}**

**ɢʀᴏᴜᴘ : ** **{chat_username}**

**ʟᴀᴘᴏʀᴀɴ ᴋᴇsᴀʟᴀʜᴀɴ: ** **{bugs}**

**ᴛᴀɴɢɢᴀʟ ʟᴀᴘᴏʀᴀɴ: ** **{datetimes}**"""

    

    if msg.chat.type == "private":

        await msg.reply_text("❎ <b>ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ʜᴀɴʏᴀ ʙᴇʀʟᴀᴋᴜ ᴅɪ ɢʀᴏᴜᴘ.</b>")

        return

    if user_id == owner:

        if bugs:

            await msg.reply_text(

                f"❎ <b>ᴀᴘᴀ ʏᴀɴɢ ʜᴀʀᴜs ᴅɪ ʟᴀᴘᴏʀᴋᴀɴ? ᴅᴀsᴀʀ ʙᴏᴅᴏʜ??</b>",

            )

            return

        else:

            await msg.reply_text(

                f"❎ <b>ᴏᴡɴᴇʀ ʙᴏᴅᴏʜ</b>",

            )

    elif user_id != owner:

        if bugs:

            await msg.reply_text(

                f"<b>Bug Report : {bugs}</b>\n\n"

                "✅ <b>ʙᴜɢ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴀᴍᴘᴀɪ ᴋᴀɴ ᴋᴇᴘᴀᴅᴀ ᴘᴇᴍɪʟɪᴋ ʙᴏᴛ ɪɴɪ</b>",

                reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton(

                                "ᴛᴜᴛᴜᴘ", callback_data=f"close_reply")

                        ]

                    ]

                )

            )

            await Client.send_photo(

                log,

                photo=thumb,

                caption=f"{bug_report}",

                reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton(

                                "➡ ʟɪʜᴀᴛ ʙᴜɢ", url=f"{msg.link}")

                        ],

                        [

                            InlineKeyboardButton(

                                "ᴛᴜᴛᴜᴘ", callback_data=f"close_send_photo")

                        ]

                    ]

                )

            )

        else:

            await msg.reply_text(

                f"❎ <b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ʏᴀɴɢ ᴅɪ ʟᴀᴘᴏʀᴋᴀɴ</b>",

            )

        

    

@Client.on_callback_query(filters.regex("close_reply"))

async def close_reply(msg, CallbackQuery):

    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))

async def close_send_photo(Client, CallbackQuery):

    await CallbackQuery.message.delete()

__mod_name__ = "Bug"
