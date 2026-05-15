from unittest.mock import patch
from src.api_client import get_usd_quotation


def test_api_connection():
    """Valida a busca de dados, simulando a API para evitar erro 429."""
    # O 'patch' intercepta a chamada do requests.get dentro do seu src.api_client
    with patch('src.api_client.requests.get') as mock_get:
        # Configuramos o que o 'mock' deve retornar
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'USDBRL': {'bid': '5.50'}
        }

        quotation = get_usd_quotation()
        assert quotation is not None
        assert isinstance(quotation, float)
        assert quotation > 0
