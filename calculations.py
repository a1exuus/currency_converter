import requests


def get_course_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['Valute']


def convertation(original, converting_currency, amount):
    if original == 'BYN':
        url = f'https://api.nbrb.by/exrates/rates/{converting_currency}?periodicity=0'
        response = requests.get(url)
        response.raise_for_status()
        cource = response.json
    else:
        url = ''