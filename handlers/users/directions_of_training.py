import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, venue

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
        "Выпускники факультета сегодня работают во всех бассейнах внутренних водных путей "
        "России, в строительных и проектных организациях, в структурах МЧС и пожарной безопасности.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Позвонить", url="http://onmap.uz/tel/73832111191")],
                [InlineKeyboardButton(text="Электронная почта",
                                      url="https://mail.google.com/gtf@nsawt.ru")],
                [InlineKeyboardButton(text="Показать на карте",
                                      url="https://www.google.ru/maps/place/%D0%A1%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9+%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82+%D0%B2%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%B0/@55.0283951,82.9125063,17z/data=!3m1!4b1!4m5!3m4!1s0x42dfe5d24af4351b:0xdf828793aa57afaa!8m2!3d55.028392!4d82.914695?hl=ru&authuser=0")],
                [InlineKeyboardButton(text='Выход', callback_data='cancel'), ],
            ],
        ),
    )


@dp.callback_query_handler(text="cancel")
async def cancel_GTF(call: CallbackQuery):
    await call.answer("Ты можешь выбрать другой факультет и почитать про него!", show_alert=True)
    await call.message.delete()
#     await call.message.edit_reply_markup()
