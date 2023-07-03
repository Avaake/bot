from aiogram import Dispatcher, types
from config import bot, dp
from mysql_database import mysqldb
from keyboards import inline_kb
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Menu:

    # реагує на кнопку "Десерти" і визиває функцію menu_desserts яка виводе меню десертів
    async def menu_desserts_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_desserts(callback.from_user.id)
        await callback.answer()

    # реагує на кнопку "Суші" і визиває функцію menu_sushi яка виводе меню  сушів
    async def menu_sushi_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_sushi(callback.from_user.id)
        await callback.answer()


    # реагує на кнопку "Паста" і визиває функцію menu_paste яка виводе меню паст
    async def menu_paste_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_paste(callback.from_user.id)
        await callback.answer()

    # реагує на кнопку "Салати" і визиває функцію menu_salads яка виводе меню салатів
    async def menu_salads_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_salads(callback.from_user.id)
        await callback.answer()

    # реагує на кнопку "Піца" і визиває функцію menu_pizza яка виводе меню піц
    async def menu_pizza_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_pizza(callback.from_user.id)
        await callback.answer()

    # реагує на кнопку "Закуски" і визиває функцію menu_appetizer яка виводе меню закусок
    async def menu_appetizer_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_appetizer(callback.from_user.id)
        await callback.answer()

    # реагує на кнопку "Основіні страви" і визиває функцію menu_main_dishes яка виводе меню основних страв
    async def menu_main_dishes_callback(self, callback: types.CallbackQuery) -> None:
        await mysqldb.menu_main_dishes(callback.from_user.id)
        await callback.answer()

    # МЕНЮ видовить інлайн клавіатуру з назвою всіх доступніх варінтов їжі
    async def menu(self, message: types.Message) -> None:
        await bot.send_message(message.from_user.id, text='\U0001F374 menu', reply_markup=inline_kb.kd_load)


    def run_handlers(self, dp: Dispatcher) -> None:
        dp.register_callback_query_handler(self.menu_desserts_callback, Text(startswith='dec '))
        dp.register_callback_query_handler(self.menu_sushi_callback, Text(startswith='sush '))
        dp.register_callback_query_handler(self.menu_paste_callback, Text(startswith='paste '))
        dp.register_callback_query_handler(self.menu_salads_callback, Text(startswith='sal '))
        dp.register_callback_query_handler(self.menu_pizza_callback, Text(startswith='piz '))
        dp.register_callback_query_handler(self.menu_appetizer_callback, Text(startswith='appe '))
        dp.register_callback_query_handler(self.menu_main_dishes_callback, Text(startswith='madi '))
        dp.register_message_handler(self.menu, commands=['menu'])
