import requests


def get_usd_quotation():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        # User-Agent ajuda a não ser bloqueado como bot
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'USDBRL' in data:
                return float(data['USDBRL']['bid'])
        print(f"API indisponível (Status {response.status_code}). Usando valor padrão.")
        return 5.50  # Valor de fallback (contingência)
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return 5.50
