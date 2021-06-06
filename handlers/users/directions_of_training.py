import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, \
    InlineKeyboardButton

from data.config import PHONE_NUMBER_GTF
from keyboards.inline.choice_training import choice, contacts_GTF
from loader import dp


@dp.message_handler(Text(equals=['Направления подготовки']))
async def nap(message: Message):
    await message.answer(text='Выбери факультет', reply_markup=choice)


# фабрика callback data
@dp.callback_query_handler(text_contains="Hydraulic")
async def hydraulic(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(
        "На факультете <b>ГТФ</b> ведется подготовка бакалавров техники и технологии по следующим направлениям и профилям:\n"
        '• Строительство\n''• Техносферная безопасность\n''• Природообустройство и водопользование\n'
        "А также специалистов в направлении <b>Пожарной безопасности</b>.\n"
        "Выпускники факультета сегодня работают во всех бассейнах +79954990435 внутренних водных путей "
        "России, в строительных и проектных организациях, в структурах МЧС и пожарной безопасности.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                    [InlineKeyboardButton(text="+79954990435", url="https://ya.com")],
                    [InlineKeyboardButton(text="Электронная почта",
                                          url="https://mail.google.com/gtf@nsawt.ru")],
                    [InlineKeyboardButton(text="Показать на карте",
                                          venue=("55.029486893037024", "82.91459704564168",
                                                 "Главный корпус", "ул. Щетинкина, 33, "
                                                                   "Новосибирск, Новосибирская обл."))],
                    [InlineKeyboardButton(text='Выход', callback_data='cancel'), ],
                ],
        ),
    )


@dp.callback_query_handler(text="cancel")
async def cancel_GTF(call: CallbackQuery):
    await call.answer("Ты можешь выбрать другой факультет и почитать про него!", show_alert=True)
    await call.message.delete()
#     await call.message.edit_reply_markup()
