from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Чат-бот Boat разработан студентами кафедры <b>ИТ СГУВТ</b> для будущих студентов",
            "Поступай к нам - мы будем рады видеть тебя в наших рядах",
            )

    await message.answer("\n".join(text))
