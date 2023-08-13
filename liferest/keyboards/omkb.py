from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#клавыатура яка дылиться номером телефону
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(KeyboardButton(text='поділитися номером', request_contact=True))
keyboard.add(KeyboardButton(text='/stop'))

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2 .add(KeyboardButton(text='/stop'))


keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard3 .add(KeyboardButton(text='/cart'))
