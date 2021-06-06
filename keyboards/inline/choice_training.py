from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_dates import faculty_callback


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Гидротехнический факультет', callback_data='faculty_name:Hydraulic engineering faculty'),
        ],
        [
            InlineKeyboardButton(text='Судомеханический факультет', callback_data='faculty_name:Faculty of ship mechanics'),

        ],
        [
            InlineKeyboardButton(text='Факультет управления водным транспортом', callback_data='faculty_name:Faculty of Water Transport Management'),

        ],
        [
            InlineKeyboardButton(text='Электромеханический факультет', callback_data='faculty_name:Electromechanical Faculty')

        ],
    ]
)
