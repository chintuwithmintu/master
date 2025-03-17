import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7704139198:AAGzSUJkbAIBlEPt2acAuN4noGmKlC-Ja9k"
    # Telegram API ki ID
    API_ID = 29940750
    # Telegram API ki hash key
    API_HASH = "33412ad3b366ca991309d1bcbb472c32"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7618270428'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mcacourse01:nEDXm37rW8u1VKUe@cluster0.dt5hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002416903653
    # Authentication log channel ki ID
    AUTH_LOG = -1002416903653
    # Hit log channel ki ID
    HIT_LOG = -1002416903653
    # DRM dump channel ki ID
    DRM_DUMP = -1002416903653
    # Main channel ki ID
    CHANNEL = -1002416903653
    # Channel ka link
    CH_URL = "https://t.me/+r5_1sjnU1ZNjYzE1"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/hello_oreo"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

