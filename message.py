help_message = '''
Отправьте команду /buy, чтобы перейти к покупке.
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Привет! Сейчас ты увидишь работу платежей в Telegram!\n' + help_message

terms = '''
Правила!
'''

item_title = 'здесь место для покупок\n' \
             'тут бы могла быть ваша реклама, но вы предпочли РКСИ'
item_description = '''
Купить какие то товары'''

AU_error = '''
В данную страну доставка не оформляется'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''


MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}



    #                        title=MESSAGES['item_title'],
    #                        description=MESSAGES['item_description'],
    #                        provider_token=PAYMENTS_TOKEN,
    #                        currency='rub',
    #                        photo_url=item_url,
    #                        photo_height=512,
    #                        photo_width=512,
    #                        photo_size=512,
    #                        need_email=True,
    #                        need_phone_number=True,
    #                        is_flexible=True,
    #                        prices=PRICES,
    #                        start_parameter='example',
    #                        payload='some_invoice'