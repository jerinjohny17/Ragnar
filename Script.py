class script(object):
    START_TXT = """Hᴇʏ {},
I ᴀᴍ ᴀɴ Aᴜᴛᴏ - Mᴀɴᴜᴀʟ ғɪʟᴛᴇʀ ʙᴏᴛ ғᴏʀ sᴇᴀʀᴄʜɪɴɢ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs ɪɴ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴡɪᴛʜ ɪɴʟɪɴᴇ ᴍᴏᴅᴇ sᴇᴀʀᴄʜɪɴɢ sᴜᴘᴘᴏʀᴛ.

Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ & sᴇᴀʀᴄʜ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ᴍᴏᴠɪᴇs/sᴇʀɪᴇs."""
    HELP_TXT = """Hᴇʏ {}
Cʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ."""
    ABOUT_TXT = """<b>🤖 Mʏ Nᴀᴍᴇ:</b> <a href="tg://user?id=2071726557">{}</a>
<b>📔 Lɪʙʀᴀʀʏ:</b> <a href="https://docs.pyrogram.org">ᴘʏʀᴏɢʀᴀᴍ</a>
<b>✒️ Lᴀɴɢᴜᴀɢᴇ:</b> <a href="https://python.org">ᴘʏᴛʜᴏɴ3</a>
<b>💾 Dᴀᴛᴀʙᴀsᴇ:</b> <a href="https://mongodb.com">ᴍᴏɴɢᴏᴅʙ</a>
<b>📶 Bᴏᴛ Sᴇʀᴠᴇʀ:</b> <a href="https://heroku.com">ʜᴇʀᴏᴋᴜ</a>"""  
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Ragnar will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Ragnar should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Ragnar Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. Ragnar supports buttons with any telegram media type.
3. Buttons should be properly parsed in markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/RagnarFilterBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to your PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Ragnar

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the recent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📁 Tᴏᴛᴀʟ Fɪʟᴇs:</b> <code>{}</code>

<b>👥 Tᴏᴛᴀʟ Usᴇʀs:</b> <code>{}</code>

<b>🤘 Tᴏᴛᴀʟ Gʀᴏᴜᴘs:</b> <code>{}</code>

<b>📊 Usᴇᴅ Sᴛᴏʀᴀɢᴇ:</b> <code>{}</code>
<b>🆓 Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ:</b> <code>{}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
