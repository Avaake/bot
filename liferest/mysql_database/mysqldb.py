import mysql.connector
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_db_start() -> None:
    global mydb, mycursor

    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        passwd='22lolka8833',
        database='lifrrests'
    )
    mycursor = mydb.cursor()
    if mydb:
        print('Data base connected OK!')


# діситая всі десерти які є в БД  і виводить їх
async def menu_desserts(from_user_id):
    mycursor.execute("SELECT * FROM desserts")
    results = mycursor.fetchall()
    await bot.send_message(chat_id=from_user_id, text='Десерти')
    for i in results:
        await bot.send_photo(from_user_id, i[1],
                             f'Назва: {i[2]}.\nОпис: {i[3]}.\nВага: {i[4]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2]}')))
        # await bot.send_message(from_user_id, text='^^^', reply_markup=InlineKeyboardMarkup().add(
        #     InlineKeyboardButton(f'Удалить {i[2]}', callback_data=f'del {i[2]}')))
    # for i in results:
    #     await bot.send_photo(from_user_id, i[1], f'Назва: {i[2]}.\nОпис: {i[3]}.\nВага: {i[4]}.\nЦіна: {i[-1]} \u20B4.')


# діситая всі суші які є в БД  і виводить їх
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def menu_sushi(from_user_id):
    mycursor.execute("SELECT * FROM sushi")
    results = mycursor.fetchall()
    await bot.send_message(chat_id=from_user_id, text='Суші')
    for i in results:
        await bot.send_photo(from_user_id, i[1],
                             f'Назва: {i[2]}.\nОпис: {i[3]}.\nВага: {i[4]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2][:20]}')))


# діситая всю пасту яка є в БД і виводить її
async def menu_paste(from_user_id):
    mycursor.execute('SELECT * FROM paste')
    results = mycursor.fetchall()
    await bot.send_message(chat_id=from_user_id, text='Паста')
    for i in results:
        await bot.send_photo(from_user_id, i[1],
                             f'Назва: {i[2]}.\nОпис: {i[3]}.\nВага: {i[4]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2][6:33]}')))


# діситая всі салати які є в БД  і виводить їх
async def menu_salads(from_user_id):
    mycursor.execute("SELECT * FROM salads")
    results = mycursor.fetchall()
    await bot.send_message(chat_id=from_user_id, text='Салати')
    for i in results:
        await bot.send_photo(from_user_id, i[1], f'Назва: {i[2]}.\nОпис: {i[4]}.\nВага: {i[3]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2][6:33]}')))


# діситая всю піцу які є в БД  і виводить їх
async def menu_pizza(from_user_id):
    mycursor.execute("SELECT * FROM pizza")
    results = mycursor.fetchall()
    await bot.send_message(chat_id=from_user_id, text='Піца')
    for i in results:
        await bot.send_photo(from_user_id, i[1],
                             f'Назва: {i[2]}.\nОпис: {i[4]}.\nРозмір: {i[3]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2]}')))


# діситая всі закуски які є в БД  і виводить їх
async def menu_appetizer(from_user_id):
    mycursor.execute("SELECT * FROM appetizer")
    await bot.send_message(chat_id=from_user_id, text='Закуски')
    results = mycursor.fetchall()
    for i in results:
        await bot.send_photo(from_user_id, i[1], f'Назва: {i[2]}.\nОпис: {i[4]}.\nВага: {i[3]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додити у кошик {i[2]}', callback_data=f'add {i[2][:20]}')))


# діситая всі основні страви які є в БД  і виводить їх
async def menu_main_dishes(from_user_id):
    mycursor.execute("SELECT * FROM maindishes")
    await bot.send_message(chat_id=from_user_id, text='Основні страви')
    results = mycursor.fetchall()
    for i in results:
        await bot.send_photo(from_user_id, i[1], f'Назва: {i[2]}.\nОпис: {i[4]}.\nВага: {i[3]}.\nЦіна: {i[-1]} \u20B4.',
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f'Додати у кошик {i[2]}', callback_data=f'add {i[2][:20]}')))





async def sql_add_command(ID, tel_name,order_name, phone_number, table_number):
    # async with state.proxy() as data:
    mycursor.execute(
        'INSERT INTO customer_order (telegram_ID, telegram_name, order_name, phone_number, table_number) VALUES (%s, %s, %s, %s, %s)',
        (ID, tel_name, order_name, phone_number, table_number)
    )
    mydb.commit()
