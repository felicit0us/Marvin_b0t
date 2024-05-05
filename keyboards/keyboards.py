from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/prof')
button3 = types.KeyboardButton(text='Покажи лису')
button4 = types.KeyboardButton(text='Случайное число')
button5 = types.KeyboardButton(text='/stop')


keyboard1 = [
    [button1, button2, button5],
    [button4, button3]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
