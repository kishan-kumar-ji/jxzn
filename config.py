#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6974767086:AAF_ABkOhpxjldqj5SCByhQLPnDfzKIrffc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24646671"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f10705d9cc4dde81ea47b72e402d32b7")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002019428322"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6669835291"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URI","mongodb+srv://kxzn980:kishan@cluster0.tu0fpes.mongodb.net")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "link2paisa.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "d34145ea300249d435b463ce8c81818bb25d1080")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86399)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","japanese_live_actionz/19")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002117448248"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
ADMINS=[6949736066,6986912824]

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

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
