
def mostrar_menu():
    print("\n===== MENU =====")
    print("1 - Ver Cardapio")
    print("2 - Fazer Pedido")
    print("3 - Ver Conta")
    print("4 - Sair")

conta = 0

while True:

    mostrar_menu()

    opcao = input("Escolha: ")

    match opcao:

        case '1':
            print("\nCARDAPIO")
            print("1 - pizza $35")
            print("2 - hamburguer $20")
            print("3 - refrigerante $10")

        case '2':
            pedido = input("Escolha o item: ")

            match pedido:

                case '1':
                    conta += 35
                    print("pizza adicionada")

                case '2':
                    conta += 20
                    print("hamburguer adicionado")

                case '3':
                    conta += 10
                    print("refrigerante adicionado")

                case _:
                    print("opcao invalida")

        case '3':
            print(f"\nValor da conta: {conta}")

        case '4':
            print("obrigado por nos visitar!!!")
            break

        case _:
            print("volte ao menu!!!")