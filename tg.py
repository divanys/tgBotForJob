from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from message import MESSAGES
from configure import BOT_TOKEN

storage = MemoryStorage()
chatbot = Bot(token=BOT_TOKEN)
dp = Dispatcher(chatbot, storage=storage)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'])

@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])

@dp.message_handler(commands=['terms'])
async def terms_cmd(message: Message):
    await message.answer(MESSAGES['terms'])

@dp.message_handler(commands=['buy'])
async def buy_process(message: Message):
    await message.answer(MESSAGES['item_title'])

@dp.message_handler(commands=['order'])
async def order_handler(message: Message):
    await message.answer('text')

    @dp.message_handler(content_types=['text'])
    async def text_handler(message: types.Message):
        # Получение информации о заказе
        order_data = message.text.split(' ')
        product_name = order_data[0]
        product_price = order_data[1]


@dp.message_handler(lambda message: message.text)
async def wtf_text(message: Message):
    await message.answer(MESSAGES['something_text'])

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