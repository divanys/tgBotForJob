from distutils.command.config import config

from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from message import MESSAGES, teh_message
from configure import BOT_TOKEN

storage = MemoryStorage()
chatbot = Bot(token='6089974069:AAGslyieQbUFasP9VyuEAmFLAXcR-vknG9g')
dp = Dispatcher(chatbot, storage=storage)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

website_url = 'https://aliceandcat.ru/gotovye-domiki//'
website_button = InlineKeyboardButton('Домики по Гарри Поттеру', url=website_url)
inline_keyboard = InlineKeyboardMarkup().add(website_button)

@dp.message_handler(lambda message: message.text == 'Каталог')
async def buy_process(message: Message):
    await message.answer(MESSAGES['item_title'], reply_markup=inline_keyboard)

catalog_button = KeyboardButton('Каталог')
teh_button = KeyboardButton('Тех.поддержка')
stocks_button = KeyboardButton('Акции')
keyboard.add(catalog_button, teh_button, stocks_button )

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'], reply_markup=keyboard)
@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])

class SupportStates(StatesGroup):
    waiting_for_text = State()

@dp.message_handler(commands=['support'])
async def process_support_command(message: Message):
    await message.reply("Какой у вас вопрос или проблема? Опишите в свободной форме.",
                        reply_markup=ReplyKeyboardRemove())
    await SupportStates.waiting_for_text.set()

@dp.message_handler(state=SupportStates.waiting_for_text, content_types=types.ContentType.TEXT)
async def process_support_text(message: Message, state: FSMContext):
    await message.reply("Ваш запрос принят, оператор свяжется с вами в ближайшее время.")
    user_text = message.text
    await chatbot.send_message(867798233, f"Новый запрос от пользователя {message.from_user.id}:\n\n{user_text}")
    await state.finish()


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

@dp.shipping_query_handler(lambda q: True)
async def shipping_process(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.country_code == 'AU':
        return await dp.answer_shipping_query(
            shipping_query.id,
            ok=False,
            error_message=MESSAGES['AU_error']
        )

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await dp.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await dp.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.total_amount // 100,
                                              currency=message.successful_payment.currency)
    )

if __name__ == "__main__":
    executor.start_polling(dp)