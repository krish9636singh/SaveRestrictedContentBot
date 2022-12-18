#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=11008248, cast=int)
API_HASH = config("API_HASH", default="355877e5f8d9c0294432230aa98b9038")
BOT_TOKEN = config("BOT_TOKEN", default="5452506536:AAFbmp2u9WIw4eMzycJxQdBCkfni7jwduKI")
SESSION = config("SESSION", default="BQB1zSLsKlQDn11-D3CMANay03O2yHnAy-x_9hEFBORi4liEwMTuo-uhkDl1etz09FPyWefKIQxWE_hY5MbGPLWJhppgJqcmLfDKD3UxAMeJfKJOaEE3ft85N6E9DFgggXMr-ySP4S8cVbYVeBWFgcJ162HvZ7I2M2Q4XliKX9MyoQEmocGQlCbKQfp938gJXH_0kMjt3NKk9ZiTpoVt7_ssO1LmTk9921NPTQIBdNz-BeBJ6eqd3V2-mhVZkQpDDnZI26xdNoADMgEotPanrNryoRYYGOZUJ0CLhnLFw2TQIuM7OZzWpx3594oLoy2A66T5nY-IUum66w97DZf5HXcIUHqL3AA")
FORCESUB = config("FORCESUB", default="allmovieslinkhindi")
AUTH = config("AUTH", default=1300886114, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
