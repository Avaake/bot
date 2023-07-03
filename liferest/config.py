from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '6226602014:AAHes51aNViJTIX0I65Bc2D5PSInUy0cQNc'

storage = MemoryStorage()

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, storage=storage)