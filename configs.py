import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "28019550"))
    API_HASH = os.getenv("API_HASH", "b76bea8b932e73732d625491687e6c45")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5938687682:AAFgFbLIf7_AwdANXJ_6y1A-vyjbtDbQkhY")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "starcinemahub")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BAGri14Avc2AZky0-tGtpAILfYoBrXs_iMAhNA0eNKrHoTuvNr3FuwCT5_AOZxh2n-miei_aGKOH5q9n48gGSjPdqRUwyFhBNdPBhkBZ6VamXjPFJb4BG0ri6WtUxifO_YfVpYJZCVn9o1ED_8zHzn13GrtklX6AnJ-oZ46FKPquxlo48gswq9Ub1LiKl5bz9VmnS02WF2RroaaZfTxV63-7O6kcRZ7wa-GlxxDSV3MQCyZvkaMglyk5e6RddRRS7uL3xQufg9JHtyNFpMTSh8tVjTs5V3y2l7yrXT13ISUcmh_f0X4mARMZKxUAHRXHMuhViK08mQYhxhAar9NuVikeSqz-zQAAAAAdTbxkAA")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001846061385")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "starcinemahubbot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "491633764"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Plyer456")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "starcinemabackup")
#    GROUP_USERNAME = os.getenv("starcinemabackup")
    START_MSG = os.getenv("START_MSG", """**Hᴇʏ {}, 

I ᴀᴍ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ ʙᴏᴛ 🔍 powered by star cinema hub.

I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Eᴠᴇʀʏ Mᴏᴠɪᴇ Iɴ Mᴅɪsᴋ Lɪɴᴋ 🔗

Jᴜsᴛ Tʏᴘᴇ ᴀ Mᴏᴠɪᴇ Nᴀᴍᴇ 🎬**""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/7d357b72c29a6aa21fb78.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001881532555")
    DATABASE_URL = os.getenv("mongodb+srv://Madmax:CJrUvWXt-ab#Hd6@cluster0.jfdp37g.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001503061670"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "starcinemahub")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 400))
    MDISK_API = os.getenv("MDISK_API", "Qu7jX9V0Sn3q1JHdxjPp")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @Plyer496 🤖""" )
    ABOUT_WATCH_TEXT = """
    Hello
"""
    ABOUT_MDISK_TEXT = """
Hello You Can Search and download Movies for free 
"""
    ABOUT_HELP_TEXT = """
Please contact us for questions @Plyer496

"""

