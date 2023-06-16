from telebot import types

earbut_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton("Доллар $")
btn2 = types.KeyboardButton("Фунт Стерлингов £")
btn3 = types.KeyboardButton("Евро €")
btn4 = types.KeyboardButton("Йены ¥")
btn5 = types.KeyboardButton("Рубли ₽")
earbut_markup.add(btn1, btn2, btn3, btn4, btn5)
