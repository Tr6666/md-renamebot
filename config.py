import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 4546803))
    API_HASH = os.environ.get("API_HASH" "08ad181fba3b05e1141db96175cab60e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5975207762:AAEC_F5hp5cis2EBiqab2Buh26FDIPowtxM")
    OWNER_ID = int(os.environ.get("OWNER_ID", 5117106150))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://karnan:karnan@cluster0.5npe8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
