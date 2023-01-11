# ⚠️ © @Hisoka69
# ⚠️ Don't Remove Credits

import os
import random
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from BagaskaraRobot.events import register
from BagaskaraRobot import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@asupankyura", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Ini Asupan nya 🥵", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupan Tidak Di Temukan")  


@register(pattern="^/ayang ?(.*)")
async def _(event):
    bubur = await event.reply("**Mencari Ayang...🔍**") 
    try:
        ayangnya = [
            ayang
            async for ayang in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        termos = random.choice(ayangnya)
        kompor = await ubot2.download_media(termos)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Ayang nya ♥️💘💝💖💗💞🙀", 
            file=kompor
            )
        await bubur.delete()
    except Exception:
        await bubur.edit("Ayang nya kamu sedang missing")  


@register(pattern="^/pp ?(.*)")
async def _(event):
    liong = await event.reply("**Mencari PP Couple...🔍**") 
    try:
        couplenya = [
            couple
            async for couple in ubot2.iter_messages(
            "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        kopi = random.choice(couplenya)
        roko = await ubot2.download_media(kopi)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Kak PP Couplenya😍", 
            file=roko
            )
        await liong.delete()
    except Exception:
        await liong.edit("PP Couple Ny Gada Yang Bagus _-")


@register(pattern="^/wibu ?(.*)")
async def _(event):
    liong = await event.reply("**Mencari PP Anime...🔍**") 
    try:
        couplenya = [
            couple
            async for couple in ubot2.iter_messages(
            "@animekyura", filter=InputMessagesFilterPhotos
            )
        ]
        kopi = random.choice(couplenya)
        roko = await ubot2.download_media(kopi)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Kak Photo Anime nya", 
            file=roko
            )
        await liong.delete()
    except Exception:
        await liong.edit("Photo Anime Nya Gada Yang Bagus _-")
       


__mod_name__ = "Asupan"

        
