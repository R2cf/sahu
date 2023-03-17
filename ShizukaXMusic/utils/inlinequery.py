from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄ᴠɪᴊᴀʏ💕ᴊɪʏᴀ ᴩᴀᴜsᴇ 🙄",
            description=f"ʀᴏᴋ ᴅɪʏᴀ ʙᴇ ᴠɪᴅᴇᴏ.",
            thumb_url="https://te.legra.ph/file/036135523034b99f44f79.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋ᴠɪᴊᴀʏ💕ᴊɪʏᴀ ʀᴇsᴜᴍᴇ 😋",
            description=f"ᴄʜᴀʟᴜ ʜᴏ ɢʏᴇ ᴍᴏᴊ ᴋᴀʀᴏ.",
            thumb_url="https://te.legra.ph/file/036135523034b99f44f79.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂ᴠɪᴊᴀʏ💕ᴊɪʏᴀ sᴋɪᴩ 🙂",
            description=f"sᴀʙᴀʀ ᴋᴀʀ ᴅᴜsʀᴀ ᴘʟᴀʏ ᴋᴀʀ ʀʜᴀ ʜᴜ.",
            thumb_url="https://te.legra.ph/file/036135523034b99f44f79.jpg.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺ᴠɪᴊᴀʏ💕ᴊɪʏᴀ ᴇɴᴅ 🥺",
            description="ᴋʜᴀᴛᴀᴍ ᴛᴀᴛᴀ ʙʏ.",
            thumb_url="https://te.legra.ph/file/036135523034b99f44f79.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 sʜᴜғғʟᴇ 🥴",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 ʟᴏᴏᴩ 🥱",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
