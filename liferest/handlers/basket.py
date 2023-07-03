from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.dispatcher.filters import Text



class Basket:

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

    async def show_cart(self, message: types.Message):
        user_data = await dp.storage.get_data(chat=message.chat.id)
        cart = user_data.get('cart', [])
        print(type(cart))
        if cart:
            await message.answer('\n'.join(cart))
        else:
            await message.answer('Корзина пуста.')

    async def show_carts(self, message: types.Message):
        user_data = await dp.storage.get_data(chat=message.chat.id)
        cart = user_data.get('cart', [])
        print(type(cart))
        if cart:
            return  ' '.join(cart)

    def run_handlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.show_cart, commands=['cart'])
        dp.register_message_handler(self.show_carts, commands=['cartt'])
        dp.register_message_handler(self.remove_from_cart, commands=['remove'])
        dp.register_callback_query_handler(self.add_to_cart_via_button, Text(startswith='add '))

