from aiogram import Dispatcher, types
from config import bot
from mysql_database import mysqldb


class UserHandlers:

    async def cmd_start(self, message: types.Message) -> None:
        await bot.send_message(message.from_user.id, text='Смачного,\n'
                                                          '/work - Час прийому гостей,\n'
                                                          '/local - Місце знаходження закладу,\n'
                                                          '/menu - Меню,\n'
                                                          '/order - зробити заказ,\n'
                                                          '/stop - скасовує прийом замовлення')

    # Час роботи закладу
    async def cmd_work_rest(self, message: types.Message) -> None:
        await bot.send_message(message.from_user.id,
                               text="Час прийому гостей\n"
                                    "Пн - з 11:00 до 21:00\n"
                                    "Вт - з 11:00 до 21:00\n"
                                    "Ср - з 11:00 до 21:00\n"
                                    "Чт - з 11:00 до 21:00\n"
                                    "Пт - з 11:00 до 21:00\n"
                                    "Сб - з 11:00 до 21:00\n"
                                    "Нд - з 11:00 до 21:00")

    # місце розташування закладу
    async def cmd_local(self, message: types.Message) -> None:
        await bot.send_message(message.from_user.id, text='вул. Вовчинецька, 196')

    def run_handlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.cmd_start, commands=['start'])
        dp.register_message_handler(self.cmd_work_rest, commands=['work'])
        dp.register_message_handler(self.cmd_local, commands=['local'])
