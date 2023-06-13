from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram import types

but_start = KeyboardButton('start')

catalog_list = InlineKeyboardMarkup(row_width=2)

#ряд с одной кнопкой    
row1_button = types.InlineKeyboardButton(text='⚡️Купить⚡️', callback_data="button_pressed")
catalog_list.add(row1_button)

# Второй ряд с двумя кнопками
row2_button1 = types.InlineKeyboardButton(text='🏆Хочу Заработать!🏆', callback_data='earnings')
row2_button2 = types.InlineKeyboardButton(text='👨‍💻Помощь [ЛС]👨‍💻', url='https://app.leadteh.ru/w/rXrc?k=FM7fI05E')
catalog_list.add(row2_button1, row2_button2)

# Третий ряд с одной кнопкой
row3_button = types.InlineKeyboardButton(text='🔥Наш Сайт[Можно купить, Есть тех.поддержка]🔥', url='https://app.leadteh.ru/w/rXrd?k=rPvgw4ib')
catalog_list.add(row3_button)

# buy_list = InlineKeyboardMarkup(row_width=2)

# row2_button1 = types.InlineKeyboardButton(text='💜Nitro FULL [1 год]💜', url='https://www.youtube.com/watch?v=H9yVRqPixS4')
# row2_button2 = types.InlineKeyboardButton(text='💜Nitro Basic [1месяц]💜', url='https://www.youtube.com/watch?v=H9yVRqPixS4')
# buy_list.add(row2_button1, row2_button2)

# row2_button1 = types.InlineKeyboardButton(text='💚Бейдж"Активный Разработчик"💚', url='https://www.youtube.com/watch?v=H9yVRqPixS4')
# row2_button2 = types.InlineKeyboardButton(text='Помощь [ЛС]', url='https://www.youtube.com/watch?v=H9yVRqPixS4')
# buy_list.add(row2_button1, row2_button2)

earnings_list = InlineKeyboardMarkup(row_width=2)

earnings_button1 = types.InlineKeyboardButton(text='Читать в Дискорде', url='https://app.leadteh.ru/w/r5Ms?k=CxnJGQS6')
earnings_button2 = types.InlineKeyboardButton(text='Читать в ВК', url='https://app.leadteh.ru/w/r5Mt?k=mmURbDLQ')
earnings_list.add(earnings_button1, earnings_button2)