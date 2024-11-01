import telebot
from telebot import types
from dotenv import load_dotenv
import os
import calculations


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TG_BOT_TOKEN')
    exchange_rates = calculations.get_exchange_rates()
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])


    def get_source_currency(message):
        bot.send_message(message.chat.id, "Введите исходную валюту(краткий код, например BYN) из которой будет выполняться конвертирование")

    @bot.message_handler(content_types='text')


    def get_converting_currency(message):
        for index in range(len(exchange_rates)):
            if exchange_rates[index]['Cur_Abbreviation'] == message.text:
                message.text = None
                break
            else:
                bot.send_message(message.chat.id, 'Вы ввели неверный или несуществующий код!')
                get_source_currency(message)
        bot.send_message(message.chat.id, 'Введите валюту в которую хотите конвертировать')
        source_currency = message.text
        return source_currency


    @bot.message_handler(content_types='text')


    def currency_amount(message):
        bot.send_message(message.chat.id, 'Введите количество конвертируемой валюты')
        converting_curency = message.text
        return converting_curency

    
    @bot.message_handler(content_types='text')


    def convertating(message):
        currency_amount = message.text
        


    bot.infinity_polling()
