from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ""

bot = Bot(token=api)
dp = Dispatcher(bot,storage= MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
#button3 = KeyboardButton(text='Купить')

kb.add(button,button2)


kb3 = InlineKeyboardMarkup()
b_but1 = InlineKeyboardButton(text='Продукт 1' , callback_data='product_buying')
b_but2 = InlineKeyboardButton(text='Продукт 2' , callback_data='product_buying')
b_but3 = InlineKeyboardButton(text='Продукт 3' , callback_data='product_buying')
b_but4 = InlineKeyboardButton(text='Продукт 4' , callback_data='product_buying')

kb3.add(b_but1,b_but2,b_but3,b_but4)

kb2 = InlineKeyboardMarkup()
but1 = InlineKeyboardButton(text='Рассчитать норму калорий' , callback_data='calories')
but2 = InlineKeyboardButton(text='Формулы расчёта' , callback_data='formulas')
but3 = InlineKeyboardButton(text='Купить' , callback_data='buy_this_shit')

kb2.add(but1,but2,but3)





start_menu =ReplyKeyboardMarkup()



class UserState(StatesGroup):
    age    = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Бу',reply_markup=kb2)

@dp.callback_query_handler(text = 'calories')    #запуск расчётов!
async def strt_of_calc(call):
    message = call.message
    await set_growth(message)

@dp.callback_query_handler(text = 'formulas')    #запуск формул!
async def infor(call):
    await call.message.answer('https://www.calc.ru/Formula-Mifflinasan-Zheora.html')
    await call.answer()




@dp.message_handler(commands=['start'])
async def start(message):
    await  message.answer('Выберите действие:',reply_markup= kb)

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
    await message.answer(f"Необходимое количество килокалорий (ккал) в сутки: {callories}")
    await state.finish()


@dp.callback_query_handler(text = 'buy_this_shit')
async def get_buying_list(call):
#Добавить Четыре Картинки
    with open('1.png',"rb") as img1:
        await call.message.answer_photo(img1,f"Название: Продукт{1} | Описание: Описание {1}| Цена: {1*100}")
    with open('2.png',"rb") as img2:
        await call.message.answer_photo(img2,f"Название: Продукт{2} | Описание: Описание {2}| Цена: {2*100}")
    with open('3.png',"rb") as img3:
        await call.message.answer_photo(img3,f"Название: Продукт{3} | Описание: Описание {3}| Цена: {3*100}")
    with open('4.png',"rb") as img4:
        await call.message.answer_photo(img4,f"Название: Продукт{4} | Описание: Описание {4}| Цена: {4*100}")

    await call.message.answer("Выберите продукт для покупки: ",reply_markup=kb3)
    await call.answer()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
   await call.message.answer("Вы успешно приобрели продукт!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)