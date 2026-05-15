from src.api_client import get_usd_quotation


def test_api_connection():
    """Valida se a aplicação consegue buscar dados da API externa."""
    quotation = get_usd_quotation()
    assert quotation is not None
    assert isinstance(quotation, float)
    assert quotation > 0
