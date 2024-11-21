from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')

kb.add(button, button2)

kb2 = InlineKeyboardMarkup()
but1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
but3 = InlineKeyboardButton(text='Купить', callback_data='buy_this_shit')

kb2.add(but1, but2, but3)

kb3 = InlineKeyboardMarkup()
b_but1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
b_but2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
b_but3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
b_but4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')

kb3.add(b_but1, b_but2, b_but3, b_but4)