from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from message import MESSAGES, teh_message
from configure import BOT_TOKEN

storage = MemoryStorage()
chatbot = Bot(token='6089974069:AAGslyieQbUFasP9VyuEAmFLAXcR-vknG9g')
dp = Dispatcher(chatbot, storage=storage)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

catalog_button = KeyboardButton('Каталог')
teh_button = KeyboardButton('Тех.поддержка')
stocks_button = KeyboardButton('Акции')
delivery_button = KeyboardButton('Информация о доставке')
keyboard.add(catalog_button, teh_button, stocks_button, delivery_button)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'], reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])

@dp.message_handler(lambda message: message.text == 'Каталог')
async def buy_process(message: Message):
    await message.answer(MESSAGES['item_title'])

@dp.message_handler(lambda message: message.text == 'Акции')
async def buy_process(message: Message):
    await message.answer(MESSAGES['stocks'])

@dp.message_handler(lambda message: message.text == 'Тех.поддержка')
async def start_cmd(message: Message):
    try:
        cid = message.chat.id
        uid = message.from_user.id
        await message.answer(MESSAGES['teh'])
        msg = await message.answer("*📨 | Введите текст который хотите отправить тех.поддержке*", parse_mode='Markdown')
        dp.register_message_handler(teh_message, lambda message: message.text, state='*')
    except Exception as e:
        await message.answer(f'🚫 | Ошибка при выполнении команды: {str(e)}')

@dp.message_handler()
async def teh_message(message: Message):
    pass

@dp.message_handler(lambda message: message.text == 'Информация о доставке')
async def buy_process(message: Message):
    await message.answer(MESSAGES['delivery'])


@dp.shipping_query_handler(lambda q: True)
async def shipping_process(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.country_code == 'AU':
        return await bot.answer_shipping_query(
            shipping_query.id,
            ok=False,
            error_message=MESSAGES['AU_error']
        )

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.total_amount // 100,
                                              currency=message.successful_payment.currency)
    )

if __name__ == "__main__":
    executor.start_polling(dp)