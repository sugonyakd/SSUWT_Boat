from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from states.test import Test


@dp.message_handler(Text(equals=['Тест']), state=None)
async def enter_test(message: types.Message):
    await message.answer("Сейчас мы с тобой выберем подходящее направление обучения для тебя:\n"
                         "Вопрос №1. \n \n"
                         "Тебе нравится заниматься точными науками?")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Вопрос №2. \n \n"
                         "Любишь ли ты рисовать и заниматься черчением?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Вопрос №3. \n \n"
                         "Ты любишь путешествовать?")
    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Вопрос №4. \n \n"
                         "Ты любишь путешествовать?")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Вопрос №3. \n \n"
                         "Ты любишь путешествовать?")
    await Test.next()


@dp.message_handler(state=Test.Q8)
async def answer_q3(message: types.Message, state: FSMContext):
    answer8 = message.text
    data = await state.get_data()
    answer7 = data.get("answer7")
    answer8 = message.text

    await message.answer("Спасибо, ты прошел тест!")

    await state.finish()
