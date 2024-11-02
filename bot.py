import telebot
from dotenv import load_dotenv
import os
import calculations


load_dotenv()
currencys = {}
exchange_rates = calculations.get_course_list()
token = os.getenv('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_source_currency(message):
    status = False
    while status == False:
        if message.text == 'start':
            source_currency = bot.send_message(message.chat.id, 'Введите код валюты(например JPY) из которой будет проводиться конвертация')
            currencys[message.chat.id] = {}
            status = True
            bot.register_next_step_handler(source_currency, get_converting_currency)
        else:
            message.text = 'start'



def get_converting_currency(message):
    source_currency = message.text
    if source_currency not in exchange_rates:
        bot.send_message(message.chat.id, 'Неверный или отстутствующий код валюты!')
        get_source_currency(message)
    currencys[message.chat.id]['source_currency'] = source_currency
    converting_currency = bot.send_message(message.chat.id, 'Введите код валюты в которую будет проходить конвертация')
    bot.register_next_step_handler(converting_currency, get_currency_amount)


def get_currency_amount(message):
    converting_currency = message.text
    currencys[message.chat.id]['converting_currency'] = converting_currency
    currency_amount = bot.send_message(message.chat.id, 'Введите количество валюты которое хотите конвертировать')
    bot.register_next_step_handler(currency_amount, convertating)


def convertating(message):
    currency_amount = message.text
    currencys[message.chat.id]['currency_amount'] = currency_amount
    bot.send_message(message.chat.id, f'Переводим {currencys[message.chat.id]['source_currency']} в {currencys[message.chat.id]['converting_currency']} в количестве {currencys[message.chat.id]['currency_amount']}...')


bot.infinity_polling()