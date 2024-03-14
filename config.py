#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6610385824:AAGk35zGKu2mP8JoFAtpEplVXawdw_Tly0s")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "18102551"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7c51c14ac28592debd5a45a3fdd376eb")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002142552072"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6669835291"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URI","mongodb+srv://timeshorts77:kishan@cluster0.ctsvnka.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "kingurl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "56f1ce381624036f60fd477786ffaf965f82fe07")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86399)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","japanese_live_actionz/20")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002024429534"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
ADMINS=[6986912824,6669835291]

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel @preview_X to use me\n\nKindly Please join Channel </b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
