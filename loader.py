from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# отвечает за отправку запроса с помощью бота к Telegram
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# отвечает за хранилище состояний
storage = MemoryStorage()
# отвечает за доставку и обработку всех update
dp = Dispatcher(bot, storage=storage)
