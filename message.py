help_message = '''
'''

start_message = 'Здравствуйте! \n' \
                'Рады приветствовать вас в боте магазина Alice&Cat.' \
                'Здесь вы можете приобрести наши домики'+ help_message

item_title = '''
Тут позже будет переход на сайт
'''

stocks_title = '''
Ддя вас есть несколько домиков по специальной цене 💕
'''

item_description = '''
Купить какие то товары
'''

teh_message = '''
Связь с тех.поддержкой
'''

inf_delivery = '''
Доставку можно оформить во все страны и в Ркси
'''

AU_error = '''
В данную страну доставка не оформляется
'''

admin_message = '''
Получен уровень доступа: администратор
'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''

MESSAGES = {
    'start': start_message,
    'admin': admin_message,
    'help': help_message,
    'teh': teh_message,
    'item_title': item_title,
    'stocks': stocks_title,
    'delivery': inf_delivery,
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