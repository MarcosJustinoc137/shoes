from clientes import cadastrar_cliente,consultar_clientes
from costuras import cadastrar_costura, consultar_costuras
from pedidos import registrar_pedido, consultar_pedidos
from relatorios import calcular_valores, relatorio_mensal

# ==========================================
# MENU
# ==========================================


while True:
    print("\n===== MENU DA BANCA DE SAPATOS =====")
    print("1 - Cadastrar cliente")
    print("2 - Consultar clientes")
    print("3 - Cadastrar costura")
    print("4 - Consultar costuras")
    print("5 - Registrar pedido")
    print("6 - Consultar pedidos")
    print("7 - Calcular valores")
    print("8 - Relatório mensal")
    print("0 - Sair")

    opcao = input("\nDigite uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        consultar_clientes()

    elif opcao == "3":
        cadastrar_costura()

    elif opcao == "4":
        consultar_costuras()

    elif opcao == "5":
        registrar_pedido()

    elif opcao == "6":
        consultar_pedidos()

    elif opcao == "7":
        calcular_valores()

    elif opcao == "8":
        relatorio_mensal()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")