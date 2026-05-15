def validar_valor(valor):
    """Verifica se o valor é numérico e positivo."""
    if not isinstance(valor, (int, float)):
        raise ValueError("O valor deve ser um número.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return True


def calcular_total(lista_gastos):
    """Soma todos os valores de uma lista de dicionários."""
    return sum(gasto['valor'] for gasto in lista_gastos)
