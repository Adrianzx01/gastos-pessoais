from src.operacoes import validar_valor, calcular_total
from src.api_client import get_usd_quotation


def menu():
    gastos = []
    print("--- Gerenciador de Gastos Pessoais ---")

    while True:
        print("\n1. Adicionar Gasto")
        print("2. Ver Total")
        # Passo 2: Adicionar a opção no visual do menu
        print("3. Ver Cotação do Dólar (USD)")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            desc = input("Descrição do gasto: ")
            try:
                valor = float(input("Valor: R$ "))
                if validar_valor(valor):
                    gastos.append({"descricao": desc, "valor": valor})
                    print("Gasto adicionado!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            total = calcular_total(gastos)
            print(f"\nTotal acumulado: R$ {total:.2f}")

        # Passo 3: Criar a lógica para a nova opção
        elif opcao == "3":
            print("Buscando cotação atual...")
            cotacao = get_usd_quotation()
            if cotacao:
                print(f"\nCotação atual do Dólar (USD): R$ {cotacao:.2f}")
            else:
                print("\nErro ao buscar cotação. Verifique sua conexão com a internet.")

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
