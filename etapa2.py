listaCliente = []
listaConta = []
proximaConta = 1

print("--------Sistema Bancário--------")

operacao = input(
    "Digite qual operação você deseja realizar:\n"
    "1- Cadastrar cliente\n"
    "2- Cadastrar conta\n"
    "3- Listar contas\n"
    "4- Procurar conta\n"
    "5- Consultar saldo\n"
    "6- Realizar depósito\n"
    "7- Realizar saque\n"
    "8- Sair\n"
).upper()

while operacao != "8":

    print("\n--------Sistema Bancário--------")

    if operacao == "1" or operacao == "CADASTRAR CLIENTE":

        nome = input("Digite o nome do cliente: ")
        listaCliente.append([nome])

        print("Cliente cadastrado")

    elif operacao == "2" or operacao == "CADASTRAR CONTA":

        nome = input("Digite o nome do cliente: ")
        for cliente in listaCliente:

            if cliente[0] == nome:

                listaConta.append([proximaConta, nome, 0])

                print("Conta criada")
                print("Número da conta:", proximaConta)

                proximaConta = proximaConta + 1
                break

        else:
            print("Cliente não encontrado")

    elif operacao == "3" or operacao == "LISTAR CONTAS":

        if len(listaConta) > 0:
            print(f"O total de contas cadastradas são: {len(listaConta)}")

            for conta in listaConta:
                print("--------------------")
                print("Número da conta:", conta[0])
                print("Nome do cliente:", conta[1])
                print("Saldo: R$", conta[2])

        else:
            print("Nenhuma conta cadastrada")

    elif operacao == "4" or operacao == "PROCURAR CONTA":

        numeroConta = int(input("Digite o número da conta: "))

        for conta in listaConta:

            if conta[0] == numeroConta:

                print("Conta encontrada")
                print("Número da conta:", conta[0])
                print("Nome do cliente:", conta[1])
                print("Saldo: R$", conta[2])
                break

        else:
            print("Conta não encontrada")

    elif operacao == "5" or operacao == "CONSULTAR SALDO":

        numeroConta = int(input("Digite o número da conta: "))

        for conta in listaConta:

            if conta[0] == numeroConta:

                print("Seu saldo é: R$", conta[2])
                break

        else:
            print("Conta não encontrada")

    elif operacao == "6" or operacao == "REALIZAR DEPOSITO":

        numeroConta = int(input("Digite o número da conta: "))

        for conta in listaConta:

            if conta[0] == numeroConta:

                deposito = float(input("Digite o valor do depósito: R$ "))

                if deposito > 0:
                    conta[2] = conta[2] + deposito
                    print("Depósito realizado")
                    print("Novo saldo: R$", conta[2])
                else:
                    print("Valor inválido")

                break

        else:
            print("Conta não encontrada")

    elif operacao == "7" or operacao == "REALIZAR SAQUE":

        numeroConta = int(input("Digite o número da conta: "))

        for conta in listaConta:

            if conta[0] == numeroConta:

                saque = float(input("Digite o valor do saque: R$ "))

                if saque > 0 and saque <= conta[2]:

                    conta[2] = conta[2] - saque

                    print("Saque realizado")
                    print("Novo saldo: R$", conta[2])

                elif saque > conta[2]:
                    print("Saldo insuficiente")

                else:
                    print("Valor inválido")

                break

        else:
            print("Conta não encontrada")

    else:
        print("Operação inválida")

    operacao = input(
        "\nDigite a próxima operação:\n"
        "1- Cadastrar cliente\n"
        "2- Cadastrar conta\n"
        "3- Listar contas\n"
        "4- Procurar conta\n"
        "5- Consultar saldo\n"
        "6- Realizar depósito\n"
        "7- Realizar saque\n"
        "8- Sair\n"
    ).upper()

print("--------Sistema Bancário--------")
print("Sistema encerrado")
