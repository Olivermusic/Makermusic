import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_TOKEN, OWNER, OWNER_NAME, DATABASE, CHANNEL, GROUP, LOGS, VIDEO

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "26165258"))
API_HASH = getenv("API_HASH", "f30075aa37a65af1f223d7968e2a0307")
BOT_TOKEN = BOT_TOKEN
MONGO_DB_URL = DATABASE
OWNER = OWNER
OWNER_NAME = OWNER_NAME
CHANNEL = CHANNEL
GROUP = GROUP
LOGS = LOGS
VIDEO = VIDEO
