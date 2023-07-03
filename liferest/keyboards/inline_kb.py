from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




#Інлайн клавіатура яка зизиваетьс командою /menu
kd_load = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('\U0001F382 Десерти', callback_data='dec '), InlineKeyboardButton('\U0001F363 Суші', callback_data='sush '),
    InlineKeyboardButton('\U0001F35D Паста', callback_data='paste '), InlineKeyboardButton('\U0001F957 Салати', callback_data='sal '),
    InlineKeyboardButton('\U0001F355 Піца', callback_data='piz '), InlineKeyboardButton('\U0001F357 Закуски', callback_data='appe '),
    InlineKeyboardButton('\U0001F372 Основні страви', callback_data='madi ')
)


'''
\U0001F382 - 🎂,
\U0001F363 - 🍣,
\U0001F355 - 🍕,
\U0001F957 - 🥗,
\U0001F35D - 🍝,
\U0001F372 - 🍲,
\U0001F357 - 🍗
'''