from handlers.users.directions_of_training import nap
from keyboards.inline import choice
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Пожалуйста, выбери интересующий тебя пункт", reply_markup=menu)

