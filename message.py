help_message = '''
Для связи с техподдержкой можно воспользоваться командой /support
'''

start_message = 'Здравствуйте! \n' \
                'Рады приветствовать вас в боте магазина Alice&Cat.' \
                'Здесь вы можете приобрести наши домики'+ help_message


item_title = '''
Готовые домики по Гарри Поттеру
'''
support = '''
ИИ для техподдержки
'''

stocks_title = '''
Для вас есть несколько домиков по специальной цене 💕
'''

item_description = '''
Купить какие то товары
'''

teh_message = '''
Здесь вы можете написать о своей проблеме, наш специалист попробует решить ее и связажется с вами
'''

AU_error = '''
В данную страну доставка не оформляется
'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'support': support,
    'teh': teh_message,
    'item_title': item_title,
    'stocks': stocks_title,
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