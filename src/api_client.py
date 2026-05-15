import requests


def get_usd_quotation():
    """Busca a cotação atual do USD para BRL via AwesomeAPI."""
    # Usando a URL padrão sem hífens desnecessários para garantir a chave 'USDBRL'
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        # Adicionamos um timeout e um header de User-Agent simples
        # Isso evita que o GitHub Actions seja bloqueado por parecer um "bot"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            # Verificamos se a chave existe antes de acessar
            if 'USDBRL' in data:
                return float(data['USDBRL']['bid'])
        # Se chegar aqui, printamos o status para você ver no log do GitHub o que houve
        print(f"Status inesperado da API: {response.status_code}")
        return None
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return None
