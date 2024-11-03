import requests

def get_currency_list(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/codes'
    response = requests.get(url)
    response.raise_for_status()
    
    return {currency[0]: currency[1] for currency in response.json()['supported_codes']}

def convertation(original, converting_currency, amount, api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{original}/{converting_currency}/{amount}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['conversion_result']
