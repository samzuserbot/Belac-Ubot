# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# iSan-PyroBot

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚙️")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/4cef468dc46606b252835.mp4")
HELP_LOGO = getenv("HELP_LOGO", "https://telegra.ph/file/30d92c74e7579ab0281a6.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hi,Saya San-Ubot🤖")
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001687155877]
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOT_VER = "1.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "fortwentyvibes")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX3R2ZE8yWmw4Y3V2cG1uTjFvaEpEMTFjTEtCdGJKUTBzZkZyaw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "cariteman_only")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "True")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
