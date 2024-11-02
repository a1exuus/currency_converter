import requests


def get_currency_list(token):
    url = 'https://currate.ru/api/'
    response = requests.get(url, params={'get': 'currency_list', 'key': token})
    response.raise_for_status()
    return response.json()


def convertation(original, converting_currency, amount):
    if original == 'BYN':
        url = f'https://api.nbrb.by/exrates/rates/{converting_currency}?periodicity=0'
        response = requests.get(url)
        response.raise_for_status()
        cource = response.json
    else:
        url = ''