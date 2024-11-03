import telebot
from dotenv import load_dotenv
import os
import re
import calculations

load_dotenv()
currencys = {}
api_key = os.getenv('API_KEY')
token = os.getenv('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)

supported_currencies = calculations.get_currency_list(api_key)

@bot.message_handler(commands=['start'])
def get_source_currency(message):
    currencys[message.chat.id] = {}
    bot.send_message(message.chat.id, 'Введите код валюты (например, JPY), из которой будет проводиться конвертация')
    bot.register_next_step_handler(message, check_source_currency)

def check_source_currency(message):
    source_currency = message.text.strip().upper()
    if not re.match(r'^[A-Z]{3}$', source_currency):
        bot.send_message(message.chat.id, 'Код валюты должен содержать три буквы! Попробуйте снова.')
        bot.register_next_step_handler(message, check_source_currency)
    elif source_currency not in supported_currencies:
        bot.send_message(message.chat.id, 'Неверный код валюты! Пожалуйста, попробуйте снова.')
        bot.register_next_step_handler(message, check_source_currency)
    else:
        currencys[message.chat.id]['source_currency'] = source_currency
        bot.send_message(message.chat.id, 'Введите код валюты, в которую будет происходить конвертация')
        bot.register_next_step_handler(message, check_converting_currency)

def check_converting_currency(message):
    converting_currency = message.text.strip().upper()
    if not re.match(r'^[A-Z]{3}$', converting_currency):
        bot.send_message(message.chat.id, 'Код валюты должен содержать три буквы! Попробуйте снова.')
        bot.register_next_step_handler(message, check_converting_currency)
    elif converting_currency not in supported_currencies:
        bot.send_message(message.chat.id, 'Неверный код валюты! Пожалуйста, попробуйте снова.')
        bot.register_next_step_handler(message, check_converting_currency)
    else:
        currencys[message.chat.id]['converting_currency'] = converting_currency
        bot.send_message(message.chat.id, 'Введите количество валюты, которое хотите конвертировать')
        bot.register_next_step_handler(message, get_currency_amount)

def get_currency_amount(message):
    try:
        currency_amount = float(message.text.strip())
        currencys[message.chat.id]['currency_amount'] = currency_amount
        bot.send_message(message.chat.id, f'Переводим {currencys[message.chat.id]["source_currency"]} в {currencys[message.chat.id]["converting_currency"]} на сумму {currency_amount}...')
        convertating(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число!')
        bot.register_next_step_handler(message, get_currency_amount)

def convertating(message):
    source_currency = currencys[message.chat.id]['source_currency']
    converting_currency = currencys[message.chat.id]['converting_currency']
    currency_amount = currencys[message.chat.id]['currency_amount']
    
    converted_amount = calculations.convertation(source_currency, converting_currency, currency_amount, api_key)
    bot.send_message(message.chat.id, f'Результат конвертации: {currency_amount} {source_currency} = {converted_amount} {converting_currency}')
    bot.send_message(message.chat.id, 'Если хотите провести ещё конвертацию, введите команду /start')

bot.infinity_polling()
