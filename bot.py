import telebot
from telebot import types
from dotenv import load_dotenv
import os
import calculations

load_dotenv()
currencys = {}
exchange_rates = calculations.get_course_list()  # Предположим, что это словарь с поддерживаемыми валютами
token = os.getenv('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def get_source_currency(message):
    currencys[message.chat.id] = {}
    bot.send_message(message.chat.id, 'Введите код валюты (например, JPY), из которой будет проводиться конвертация')
    bot.register_next_step_handler(message, check_source_currency)

def check_source_currency(message):
    source_currency = message.text.strip().upper()  # Убираем лишние пробелы и приводим к верхнему регистру
    if source_currency not in exchange_rates:
        bot.send_message(message.chat.id, 'Неверный или отсутствующий код валюты! Попробуйте снова.')
        get_source_currency(message)  # Перезапускаем ввод кода валюты
    else:
        currencys[message.chat.id]['source_currency'] = source_currency
        converting_currency = bot.send_message(message.chat.id, 'Введите код валюты, в которую будет происходить конвертация')
        bot.register_next_step_handler(converting_currency, check_converting_currency)

def check_converting_currency(message):
    converting_currency = message.text.strip().upper()
    if converting_currency not in exchange_rates:
        bot.send_message(message.chat.id, 'Неверный или отсутствующий код валюты! Попробуйте снова.')
        get_source_currency(message)  # Возвращаемся к вводу начальной валюты
    else:
        currencys[message.chat.id]['converting_currency'] = converting_currency
        currency_amount = bot.send_message(message.chat.id, 'Введите количество валюты, которое хотите конвертировать')
        bot.register_next_step_handler(currency_amount, get_currency_amount)

def get_currency_amount(message):
    try:
        currency_amount = float(message.text.strip())
        currencys[message.chat.id]['currency_amount'] = currency_amount
        bot.send_message(message.chat.id, f'Переводим {currencys[message.chat.id]["source_currency"]} в {currencys[message.chat.id]["converting_currency"]} на сумму {currency_amount}.')
        convertating(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число!')
        get_currency_amount(message)

def convertating(message):
    source_currency = currencys[message.chat.id]['source_currency']
    converting_currency = currencys[message.chat.id]['converting_currency']
    currency_amount = currencys[message.chat.id]['currency_amount']
    converted_amount = calculations.convertation(source_currency, converting_currency, currency_amount)
    bot.send_message(message.chat.id, f'Результат конвертации: {currency_amount} {source_currency} = {converted_amount} {converting_currency}')

bot.infinity_polling()
