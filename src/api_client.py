import requests


def get_usd_quotation():
    """Busca a cotação atual do USD para BRL via AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data['USDBRL']['bid'])
    return None
