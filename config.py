# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "22620068")
    API_HASH = environ.get("API_HASH", "11e2c113078324f7e36688baa86c3911")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7276231385:AAG7PYYPmwl_q73J-Asz-FIHK8U8zlxQ-Z4") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6062527012').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://e6si4kxfhr:<db_password>@cluster0.j26ea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002050604893'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/+bnmbjw-mkckyNTc1") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
