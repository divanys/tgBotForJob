from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import yandex_checkout
from pyamocrm import AmoCRM
from configure import BOT_TOKEN

bot = Bot(token= BOT_TOKEN)
dp = Dispatcher(bot)

yandex_checkout.configure('your_yandex_checkout_api_key')
amocrm = AmoCRM('your_domain', 'your_user_login', 'your_user_hash')

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply('Добро пожаловать!')

@dp.message_handler(commands=['buy'])
async def buy_handler(message: types.Message):
    payment = yandex_checkout.Payment.create({
        "amount": {
            "value": 1000.00,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://your.return.url"
        },
        "description": "Описание заказа",
        "metadata": {
            "customer_id": message.from_user.id
        }
    })
    payment_url = payment.confirmation.confirmation_url
    # создаем сделку в amoCRM
    lead_id = create_lead(payment_id=payment.id, user_id=message.from_user.id, amount=1000.00)
    await message.reply(f'Перейдите по ссылке для оплаты: {payment_url}')

@dp.message_handler(commands=['payment'])
async def payment_handler(message: types.Message):
    payment_id = 'your_payment_id'
    payment = yandex_checkout.Payment.find_one(payment_id)
    # обновляем статус оплаты в amoCRM
    update_lead(lead_id=get_lead_by_payment_id(payment_id), status=payment.status)
    await message.reply(f'Статус оплаты: {payment.status}')

def create_lead(payment_id, user_id, amount):
    lead_data = {
        'name': f'Оплата заказа {payment_id}',
        'responsible_user_id': 'your_user_id',
        'sale': amount,
        'custom_fields_values': [
            {
                'field_id': 'your_payment_id_field_id',
                'values': [
                    {
                        'value': payment_id
                    }
                ]
            },
            {
                'field_id': 'your_user_id_field_id',
                'values': [
                    {
                        'value': user_id
                    }
                ]
            }
        ]
    }
    lead = amocrm.lead.create(lead_data)
    return lead['id']

def get_lead_by_payment_id(payment_id):
    leads = amocrm.lead.get({'query': payment_id})
    for lead in leads:
        for field in lead['custom_fields_values']:
            if field['field_id'] == 'your_payment_id_field_id' and field['values'][0]['value'] == payment_id:
                return lead['id']
    return None

def update_lead(lead_id, status):
    if lead_id:
        lead_data = {
            'status_id': 'your_status_id'
        }