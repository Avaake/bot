from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.dispatcher.filters import Text



class Basket:
    Cart = None
    async def add_to_cart_via_button(self, callback: types.CallbackQuery):
        item = callback.data.replace("add ", "")
        user_data = await dp.storage.get_data(chat=callback.message.chat.id)
        cart = user_data.get('cart', [])
        cart.append(item)
        user_data['cart'] = cart
        await dp.storage.set_data(chat=callback.message.chat.id, data=user_data)
        await callback.answer(text=f'{item} Додане у кошик.')

    async def remove_from_cart(self, message: types.Message):
        item = message.text.split('/remove ')[1]
        user_data = await dp.storage.get_data(chat=message.chat.id)
        cart = user_data.get('cart', [])
        if item in cart:
            cart.remove(item)
            user_data['cart'] = cart
            await dp.storage.set_data(chat=message.chat.id, data=user_data)
            await message.reply(f'Товар "{item}" удален из корзины.')
        else:
            await message.reply(f'Товар "{item}" не найден в корзине.')

    messages = None

    async def show_cart(self, message: types.Message):
        user_data = await dp.storage.get_data(chat=message.chat.id)
        Basket.Cart = ','.join(user_data.get('cart', []))
        print(Basket.Cart)
        print(type(Basket.Cart))
        if Basket.Cart:
            await message.answer(Basket.Cart)
        else:
            await message.answer('Корзина пуста.')

    def run_handlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.show_cart, commands=['cart'])
        dp.register_message_handler(self.show_cart, commands=['cart'])
        dp.register_message_handler(self.remove_from_cart, commands=['remove'])
        dp.register_callback_query_handler(self.add_to_cart_via_button, Text(startswith='add '))

