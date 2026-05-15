from src.operacoes import validar_valor, calcular_total


def menu():
    gastos = []
    print("--- Gerenciador de Gastos Pessoais ---")
    while True:
        print("\n1. Adicionar Gasto")
        print("2. Ver Total")
        print("3. Sair")
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
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
