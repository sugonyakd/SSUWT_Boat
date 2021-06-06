from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Направления подготовки"),
        ],
        [
            KeyboardButton(text="Контакты приемной комиссии"),
        ],
        [
            KeyboardButton(text="Документы к поступлению"),
        ],
        [
            KeyboardButton(text="Лицей СГУВТ"),
            KeyboardButton(text="Тест"),
        ],
    ],
    resize_keyboard=True
)

