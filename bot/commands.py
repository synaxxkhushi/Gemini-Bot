from .admin import auth, add_user
from .database import db
from .gemini import check_api
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """ʜᴇʟʟᴏ {},
ɪ ᴀᴍ ᴀ ɢᴇᴍɪɴɪ ᴀɪ ʙᴏᴛ 🧸❤️

ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ( ᴛᴇxᴛ ᴛʏᴘᴇ ) ᴀɴsᴡᴇʀs ᴜsɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ ( ǫᴜᴇsᴛɪᴏɴ /ǫᴜᴇʀʏ ) ᴀɴᴅ ɪᴍᴀɢᴇs ᴜsɪɴɢ ᴛʜᴇ ɢᴇᴍɪɴɪ ᴀᴘɪ 🐰.

ᴄʟɪᴄᴋ ʜᴇʟᴘ ғᴏʀ ᴍᴏʀᴇ 🌸"""

HELP_TEXT = """--**𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩**--

**In Private (text only):**
- Just send me question as text
- I will reply in text form

**In Private (photo only):**
- Just send me photo
- Then reply /ai command to the photo
- I will reply with generated text

**In Private (photo and text):**
- Send me a photo
- Reply text to the photo
- I will reply with generated text


**In Group (text only):**
- Just send me question as text with /ai command
- I will reply with generated text

**In Group (photo only):**
- Just send me photo
- Then reply /ai command to the photo
- I will reply with generated text

**In Group (photo and text):**
- Send me a photo
- Reply /ai command with text to the photo
- I will reply with generated text

--**Other Commands**--

/api: To add your Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
/my_api: To get your Gemini API Key
/delete_api: To delete your Gemini API Key
"""

ABOUT_TEXT = """**𝐀𝐛𝐨𝐮𝐭 𝐌𝐞**

➩ **𝐁𝐨𝐭 🇮🇳 :** `ʀᴇᴍɪɴɪ ᴀɪ sʏɴᴀx 🦄`
➩ **𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ☘️ :** [ɪɴsᴛᴀɢʀᴀᴍ ](https://instagram.com/sanatanisynax) | [ᴛᴇʟᴇɢʀᴀᴍ ](https://telegram.me/synaxbots)
➩ **𝐒𝐨𝐮𝐫𝐜𝐞 :** [ᴄʟɪᴄᴋ ᴋʀ 🐰](https://t.me/synaxnetwork)
➩ **𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :** [ᴘʏᴛʜᴏɴ 3 🦜](https://python.org)
➩ **𝐋𝐢𝐛𝐫𝐚𝐫𝐲 :** [ᴘʏʀᴏɢʀᴀᴍ 🌸](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🌷ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🧸 ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('♨️ ᴄʟᴏsᴇ', callback_data='close')
        ],
        [
            InlineKeyboardButton('💬 ғᴇᴇᴅʙᴀᴄᴋ', url='https://telegram.me/synaxnetwork')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('☣️ ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🧸 ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('♨️ ᴄʟᴏsᴇ', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('☣️ ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🌷ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('♨️ ᴄʟᴏsᴇ', callback_data='close')
        ]
    ]
)


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message, cb=False):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    text=START_TEXT.format(message.from_user.mention)
    if cb:
        await message.message.edit_text(
            text=text,
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
            quote=True
        )


@Client.on_message(filters.private & filters.command(["help"]))
async def help(bot, message, cb=False):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    if cb:
        await message.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Client.on_message(filters.private & filters.command(["about"]))
async def about(bot, message, cb=False):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    if cb:
        await message.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.reply_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Client.on_message(filters.private & filters.command(["api", "add_api"]))
async def add_api(bot, message):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    if (" " not in message.text):
        await message.reply_text("Send your Gemini API Key")
        return
    
    api = message.text.split(" ", 1)[1]
    m = await message.reply_text("Checking API Key...")
    if check_api(api):
        await db.update_api(id=message.from_user.id, api=api)
        if await db.get_api(message.from_user.id):
            text = "API Key updated successfully"
        else:
            text = "API Key added successfully"
        await m.edit_text(text)
    else:
        await m.edit_text("Invalid API Key")


@Client.on_message(filters.private & filters.command(["my_api", "get_api"]))
async def get_api(bot, message):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    api = await db.get_api(message.from_user.id)
    if api:
        await message.reply_text(f"Your Gemini API Key is\n`{api}`")
    else:
        await message.reply_text("You haven't added your Gemini API Key")


@Client.on_message(filters.private & filters.command(["delete_api", "remove_api"]))
async def delete_api(bot, message):
    
    # authorising
    if not auth(message.from_user.id):
        return
    
    # adding user to database
    await add_user(message)
    
    text = "Are you sure to delete your Gemini API Key?"
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Yes', callback_data='confirm_delete_api'),
                InlineKeyboardButton('No', callback_data='cancel_delete_api')
            ]
        ]
    )
    await message.reply_text(
        text=text,
        reply_markup=buttons,
        quote=True
    )


# Callbacks
async def delete_api_cb(bot, message, confirm):
    m = message.message
    if confirm:
        await m.edit_text("Deleting your Gemini API Key...")
        if await db.get_api(message.from_user.id):
            await db.update_api(message.from_user.id, None)
            await m.edit_text("API Key removed successfully")
        else:
            await m.edit_text("You haven't added your Gemini API Key")
    else:
        await m.edit_text("Cancelled the process")
