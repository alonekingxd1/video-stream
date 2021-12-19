import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "ALONE_KING")
ALIVE_NAME = getenv("ALIVE_NAME", "ALONE")
BOT_USERNAME = getenv("BOT_USERNAME", "ALONE_vc_player_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ALONE_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "welcomefriendclub")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! P .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://https://telegra.ph/file/7a34a97effda25f9fbff4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://https://telegra.ph/file/db2ef276b01387cffca00.jpg")
IMG_2 = getenv("IMG_2", "https://https://telegra.ph/file/db2ef276b01387cffca00.jpg")
IMG_3 = getenv("IMG_3", "https://https://telegra.ph/file/7a34a97effda25f9fbff4.jpg")
