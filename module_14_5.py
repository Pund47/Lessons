from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from keyboards import *
from crud_functions import *

import asyncio

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())
start_menu = ReplyKeyboardMarkup()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    id = State()
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Бу', reply_markup=kb2)


@dp.callback_query_handler(text='calories')  # запуск расчётов!
async def strt_of_calc(call):
    message = call.message
    await set_growth(message)


@dp.callback_query_handler(text='formulas')  # запуск формул!
async def infor(call):
    await call.message.answer('https://www.calc.ru/Formula-Mifflinasan-Zheora.html')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await  message.answer('Выберите действие:', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте, нетути)))')


@dp.message_handler(text='Рассчитать')
async def nachalo_rascheta(message):
    await set_growth(message)


@dp.message_handler(text='Calories')
async def set_growth(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def fsm_handler(message, state):
    await state.update_data(age=message.text)
    date = await state.get_data()

    await message.answer(f"Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def fsm_handler(message, state):
    await state.update_data(growth=message.text)
    date = await state.get_data()

    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def fsm_handler(message, state):
    await state.update_data(weight=message.text)
    date = await state.get_data()
    await send_calories(message, date, state)


@dp.message_handler()
async def send_calories(message, date, state):
    callories = int(10 * int(date["weight"]) + 6.25 * int(date["growth"]) + 5 * int(date["age"]))
    await message.answer(f"Необходимое количество килокалорий (ккал) в сутки: {callories}")
    await state.finish()


@dp.callback_query_handler(text='buy_this_shit')
async def get_buying_list(call):
    products = get_all_products
    for prod in products():
        with open(f"{prod[0]}.png", "rb") as img1:
            tekopis = list_of_overview[prod[0] - 1]
            await call.message.answer_photo(img1, f"Название: {prod[1]} | Описание:{tekopis} | Цена: {prod[3]}")

    await call.message.answer("Выберите продукт для покупки: ", reply_markup=kb3)
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


######################################################################################Дополнения14_5

@dp.callback_query_handler(text='registration')
async def sing_up(call):
    message = call.message
    await set_name(message)


@dp.message_handler()
async def set_name(message):
    await message.answer("Введите имя пользователя(только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def fsm_handler(message, state):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя")
        await set_name(message)
    else:
        await state.update_data(username=message.text)
    # Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя"
    # и запрашивать новое состояние для RegistrationState.username.

        date = await state.get_data()
        await message.answer(f"Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def fsm_handler(message, state):
    await state.update_data(email=message.text)
    await message.answer(f"Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def fsm_handler(message, state):
    await state.update_data(age=message.text)
    date = await state.get_data()
    await add_new_user(message, date, state)

@dp.message_handler()
async def add_new_user(message, date, state):
    add_user(date["username"], date["email"], date["age"])
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
