from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot,storage= MemoryStorage())

class UserState(StatesGroup):
    age    = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Calories')
async def set_growth(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def fsm_handler(message,state):
    await state.update_data(age = message.text)
    date = await state.get_data()

    await message.answer(f"Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def fsm_handler(message,state):
    await state.update_data(growth = message.text)
    date = await state.get_data()

    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def fsm_handler(message,state):
    await state.update_data(weight = message.text)
    date = await state.get_data()
    await send_calories(message,date,state)

@dp.message_handler()
async def  send_calories(message,date,state):
    callories = int(10*int(date["weight"]) + 6.25 * int(date["growth"]) + 5 * int(date["age"]))
    #bot.send_message(message.chat.id, (f"Необходимое количество килокалорий (ккал) в сутки",callories))
    await message.answer(f"Необходимое количество килокалорий (ккал) в сутки: {callories}")
    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
