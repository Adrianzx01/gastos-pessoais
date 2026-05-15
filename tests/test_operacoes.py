import pytest
from src.operacoes import validar_valor, calcular_total


# TESTE 1: Caminho Feliz (Sucesso)
# Verifica se a soma de vários gastos está correta.
def test_calcular_total_sucesso():
    gastos = [
        {"descricao": "Almoço", "valor": 30.0},
        {"descricao": "Transporte", "valor": 20.0}
    ]
    assert calcular_total(gastos) == 50.0


# TESTE 2: Entrada Inválida (Erro esperado)
# Verifica se o sistema trava valores negativos ou zero.
def test_validar_valor_negativo_erro():
    with pytest.raises(ValueError, match="O valor deve ser maior que zero."):
        validar_valor(-5)


# TESTE 3: Caso Limite (Vazio)
# Verifica se o sistema se comporta bem quando não há gastos ainda.
def test_calcular_total_lista_vazia():
    assert calcular_total([]) == 0
