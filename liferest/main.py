from config import dp, bot
from aiogram.utils import executor
from handlers import user, menu, order_machine, basket
from mysql_database import mysqldb


def main():
    async def on_startup(_):
        print('start bot')
        mysqldb.get_db_start()


    users = user.UserHandlers()
    menus = menu.Menu()
    order_machines = order_machine.OrderMachine()
    baskets = basket.Basket()

    users.run_handlers(dp)
    menus.run_handlers(dp)
    order_machines.run_handlers(dp)
    baskets.run_handlers(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    main()
