from config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from keyboards import omkb
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from mysql_database import mysqldb
from sending_an_order import send_mail
from handlers.basket import Basket

class FSMOM(StatesGroup):
    # order = State()
    phone_number = State()
    table_number = State()


class OrderMachine:
    """
    КЛАС машина замовлень приймає:
    order - замовлення,
    phone_number - номер телефону,
    table_number - номер столу.
    Оброблює та записує значення до бази даних
    """

    # запускаємо машину і запитуємо замовлення
    async def on_start(self, message: types.Message) -> None:
        await FSMOM.phone_number.set()
        await bot.send_message(message.from_user.id, text='Введіть номер телефону', reply_markup=omkb.keyboard)

    #перериваємо (відключає) машину
    async def stop_fsm(self, message: types.Message, state: FSMContext) -> None:
        current_status = await state.get_state()
        if current_status is None:
            return
        await state.finish()
        await message.reply('OK', reply_markup=ReplyKeyboardRemove())

    #приймаємо замовлення та запитуємо номер телефону

    # async def load_order(self, message: types.Message, state: FSMContext) -> None:
    #     async with state.proxy() as data:
    #         data['order'] = message.text
    #     await FSMOM.next()
    #     await message.reply('Введіть номер телефону', reply_markup=omkb.keyboard)

    # приймаємо номер телефону та запитуємо номер столу
    async def load_phone_number(self, message: types.Message, state: FSMContext) -> None:
        contact = message.contact  # Доступ до контактної інформації з об’єкта повідомлення
        async with state.proxy() as data:
            data['phone_number'] = contact.phone_number
        await FSMOM.next()
        await message.reply('Введіть номер столу', reply_markup=omkb.keyboard2)

    # приймаємо номер столу та запитуємо дані в БД і пишемо людині що вона замовила

    async def load_table_number(self, message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['table_number'] = message.text

        res = list(data.values())  # дістаємо значення з словника "data" за записуемо в res
        ID = int(message.from_user.id)  # отримуємо телеграм_id замоника
        tel_name = message.from_user.full_name  # отримуємо телеграм імя

        order_names = str(Basket.Cart)
        phone_numbers = res[1]
        table_numbers = res[-1]
        print(order_names, phone_numbers, table_numbers, sep='\n')

        await bot.send_message(message.from_user.id, text=f'ваше замовлення: {res[0]}\nНомер столу: {res[-1]}', )
        await mysqldb.sql_add_command(ID=ID, tel_name=tel_name, order_name=order_names, phone_number=phone_numbers,
                                      table_number=table_numbers)  # записуемо дані в бд
        await message.answer('Замовлення прийняте\nСмачного',reply_markup=ReplyKeyboardRemove())
        await send_mail.send_email(state) #выдправляє заказ на пошту
        await state.finish()

    def run_handlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.on_start, commands=['order'], state=None)
        dp.register_message_handler(self.stop_fsm, state='*', commands=['stop'])
        dp.register_message_handler(self.stop_fsm, Text(equals=['stop'], ignore_case=True), state='*')
        # dp.register_message_handler(self.load_order, state=FSMOM.order)
        dp.register_message_handler(self.load_phone_number, state=FSMOM.phone_number,
                                    content_types=types.ContentTypes.CONTACT)
        dp.register_message_handler(self.load_table_number, state=FSMOM.table_number)
