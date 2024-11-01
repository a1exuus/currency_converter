import requests


def get_exchange_rates():
    url = 'https://api.nbrb.by/exrates/rates?periodicity=0'
    response = requests.get(url)
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