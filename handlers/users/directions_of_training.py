import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.choice_training import choice
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
                                      url="https://www.google.com/maps/place/@55.048578,82.9184433,17z/data=!3m1!4b1!4m5!3m4!1s0x42dfe5ba22b0a237:0x2af710589870ad29!8m2!3d55.048578!4d82.920632")],
                [InlineKeyboardButton(text='Выход', callback_data='cancel'), ],
            ],
        ),
    )


@dp.callback_query_handler(text="cancel")
async def cancel_GTF(call: CallbackQuery):
    await call.answer("Ты можешь выбрать другой факультет и почитать про него!", show_alert=True)
    await call.message.delete()


@dp.callback_query_handler(text_contains="ship")
async def ship(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(
        "Факультет <b>Судмеха</b> ведет обучение по направлению подготовки «Кораблестроение, "
        "океанотехника и "
        "системотехника объектов морской инфраструктуры». Получив образование по этому "
        "направлению, ты найдешь ответы на вопросы: как устроены морские и речные суда, "
        "чем они отличаются от военных кораблей, какие механизмы приводят их в движение и т.д., "
        "станешь востребованным специалистом в области строительства и ремонта морских и речных "
        "судов.\n\n"
        "С дипломом бакалавра по профилю «Кораблестроение» ты сможешь заниматься любой "
        "профессиональной деятельностью, связанной с проектированием, постройкой, техническим обслуживанием и ремонтом речных и морских судов и средств речной и морской техники, а также в других областях техники.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Позвонить", url="http://onmap.uz/tel/+73832213486")],
                [InlineKeyboardButton(text="Электронная почта",
                                      url="https://mail.google.com/smf@nsawt.ru")],
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


@dp.callback_query_handler(text_contains="Water")
async def Water(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(
        "На факультете <b>УВТ</b> готовят квалифицированных специалистов по следующим"
        "направлениям и профилям:\n"
        '• Экономика\n''• Менеджмент\n''• Технология транспортных процессов\n'
        "А также специалистов в направлении <b>Управление водным транспортом и гидрографическое обеспечение судоходства</b>.\n"
        "Поступая на данный факультет СГУВТа, ты выбираешь специальности, связанные с управлением "
        "на транспорте, современными логистическими технологиями а, следовательно, облегчаете себе трудоустройство после окончания вуза.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Позвонить", url="http://onmap.uz/tel/+73832246800")],
                [InlineKeyboardButton(text="Вконтакте",
                                      url="https://vk.com/dekanat_uwt")],
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


@dp.callback_query_handler(text_contains="Electromechanical")
async def Electromechanical(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(
        "<b>ЭМФ - ЭЛИТА</b> так называют все студенты свой любимый факультет! "
        "На нем готовят настоящих профессионалов своего дела. Студенты обучаются по направлениям:\n"
        '• Информационные системы и технологии\n''• Электроэнергетика и электротехника\n''• '
        'Эксплуатация транспортных технологических машин и комплексов\n'
        "Сегодня выпускники Электромеханического факультета работают по всей России и за рубежом, нередко занимая "
        "ключевые руководящие должности, а это значит, что преподаватели всех кафедр нашего Университета работают не зря! Традиционно высокое качество подготовки наших выпускников отмечают многие предприятия, некоторые из которых являются постоянными базами практик для наших студентов.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Позвонить", url="http://onmap.uz/tel/73832223183")],
                [InlineKeyboardButton(text="Сайт",
                                      url="http://ssuwt.tw1.ru/")],
                [InlineKeyboardButton(text="Показать на карте",
                                      url="https://www.google.ru/maps/place/@55.028392,82.9125063,17z/data=!3m1!4b1!4m5!3m4!1s0x42dfe5d24af4351b:0xdf828793aa57afaa!8m2!3d55.028392!4d82.914695?hl=ru&authuser=0")],
                [InlineKeyboardButton(text='Выход', callback_data='cancel'), ],
            ],
        ),
    )


@dp.callback_query_handler(text="cancel")
async def cancel_GTF(call: CallbackQuery):
    await call.answer("Ты можешь выбрать другой факультет и почитать про него!", show_alert=True)
    await call.message.delete()
