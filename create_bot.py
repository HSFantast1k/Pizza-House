from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '1234332:FKKEKF34KFK3KKZF3'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
