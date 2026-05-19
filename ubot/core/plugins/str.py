import asyncio
from datetime import datetime
from gc import get_objects
from time import time
from random import randint

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ubot import *


async def send_msg_to_owner(client, message):
    if message.from_user.id == OWNER_ID:
        return
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "👤 Profil", callback_data=f"profil {message.from_user.id}"
                ),
                InlineKeyboardButton(
                    "Jawab 💬", callback_data=f"jawab_pesan {message.from_user.id}"
                ),
            ],
        ]
        await client.send_message(
            OWNER_ID,
            f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>\n\n<code>{message.text}</code>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

async def reak(client, message):
    await client.send_reaction(message.chat.id, message.id, "⚡")

async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id

async def load_ping_messages(user_id):
    ping_message = {}

    ping_message["pong"] = await get_ping_pong(user_id) or "ᴘᴏɴɢ:"
    ping_message["uptime"] = await get_ping_uptime(user_id) or "ᴜᴘᴛɪᴍᴇ:"
    ping_message["mention"] = await get_ping_mention(user_id) or "ᴍᴇɴᴛɪᴏɴ:"

    return ping_message

async def ping_cmd(client, message):
    user_id = message.from_user.id
    ub_uptime = await get_uptime(client.me.id)
    uptime = await get_time((time() - ub_uptime))
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    ping_msg = await load_ping_messages(user_id)
    delta_ping = (end - start).microseconds / 10000
    emot_1 = await get_vars(client.me.id, "EMOJI_PING_PONG")
    emot_2 = await get_vars(client.me.id, "EMOJI_UPTIME")
    emot_3 = await get_vars(client.me.id, "EMOJI_MENTION")
    emot_pong = emot_1 if emot_1 else "5269563867305879894"
    emot_uptime = emot_2 if emot_2 else "5316615057939897832"
    emot_mention = emot_3 if emot_3 else "6226371543065167427"
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_pong}>🏓</emoji> {ping_msg["pong"]}</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={emot_uptime}>⏰</emoji> {ping_msg["uptime"]}</b> <code>{uptime}</code>
<b><emoji id={emot_mention}>👑</emoji> {ping_msg["mention"]}:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    else:
        _ping = f"""
<b>🏓 {ping_msg["pong"]}</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b>⏰{ping_msg["uptime"]}</b> <code>{uptime}</code>
<b>👑{ping_msg["mention"]}:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    await message.reply(_ping)


async def set_pong_message(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) >= 2:
        new_message = args[1]
        await set_ping_pong(user_id, new_message)
        await message.reply_text("ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ᴘᴇsᴀɴ ᴘᴏɴɢ..")
    else:
        await message.reply_text("ғᴏʀᴍᴀᴛ sᴀʟᴀʜ, ɢᴜɴᴀᴋᴀɴ '.setpong <kata kata>'.")

async def set_uptime_message(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) >= 2:
        new_message = args[1]
        await set_ping_uptime(user_id, new_message)
        await message.reply_text("ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ᴘᴇsᴀɴ ᴜᴘᴛɪᴍᴇ..")
    else:
        await message.reply_text("ғᴏʀᴍᴀᴛ sᴀʟᴀʜ, ɢᴜɴᴀᴋᴀɴ '.setupime <kata kata>'.")

async def set_mention_message(client: Client, message: Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) >= 2:
        new_message = args[1]
        await set_ping_mention(user_id, new_message)
        await message.reply_text("ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ᴘᴇsᴀɴ ᴍᴇɴᴛɪᴏɴ..")
    else:
        await message.reply_text("ғᴏʀᴍᴀᴛ sᴀʟᴀʜ, ɢᴜɴᴀᴋᴀɴ '.setmention <kata kata>'.")


async def start_cmd(client, message):
    await add_served_user(message.from_user.id)
    await send_msg_to_owner(client, message)
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>Tunggu Sebentar...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ Eror:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>Mau ngapain sayangku gk boleh loh ini<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ Eror:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)


