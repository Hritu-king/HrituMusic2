# © Cyril C Thomas
# https://t.me/cyril_c_10

import os

class Config(object):
    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6356388726:AAGNT3VwYvMQ55KGndcUfQ9uQ-Cz-Dw7Yvg")
    API_ID = int(os.environ.get("APP_ID", 21203142))
    API_HASH = os.environ.get("API_HASH", "64d92910619503d54fdb9d89ccb805a6")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001924268233))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ronoxe1308:nulcnaRvqNC5uty@rename-telegram-bot-log.clbv64f.mongodb.net/?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("SESSION_NAME", "xenon")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5190902724))
