import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from yookassa import Payment as YooPayment, Configuration
import requests

# Установка идентификатора магазина и секретного ключа Юkassa
Configuration.account_id = 'your_account_id'
Configuration.secret_key = 'your_secret_key'

# Установка ключа API amoCRM
amo_crm_api_key = 'your_api_key'

# Создание объектов бота и диспетчера
bot = Bot(token='6089974069:AAGslyieQbUFasP9VyuEAmFLAXcR-vknG9g')
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # Отправка пользователю сообщения с приветствием и инструкцией
    await message.answer('Добро пожаловать в РКСИ! Чтобы сделать заказ, нажмите /buy.')

# Обработчик команды /order
@dp.message_handler(commands=['order'])
async def order_handler(message: types.Message):
    # Создание сообщения с предложением оформить заказ
    text = 'Оформлениреп заказа'
    await message.answer(text)

# Обработчик текстового сообщения с информацией о заказе
@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    # Получение информации о заказе
    order_data = message.text.split(' ')
    product_name = order_data[0]
    product_price = order_data[1]

    # Создание объекта платежа Юkassa
    payment = YooPayment.create({
        'amount': {
            'value': product_price,
            'currency': 'RUB'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://example.com/return'
        },
        'description': product_name
    })

    # Получение ссылки на оплату и отправка ее пользователю
    payment_url = payment.confirmation.confirmation_url
    text = f'Для оплаты товара "{product_name}" перейдите по ссылке: {payment_url}'
    await message.answer