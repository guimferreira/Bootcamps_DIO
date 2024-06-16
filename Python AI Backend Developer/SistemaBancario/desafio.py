def depositar(valor):
    if valor > 0:
        global saldo
        saldo += valor
        global extrato
        extrato += f'Depósito: R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido.')


def efetuar_saque(valor):
    global saldo
    global extrato
    global numero_saques
    saldo -= valor
    extrato += f'Saque: R$ {valor:.2f}\n'
    numero_saques += 1


def sacar(valor):
    global saldo
    global extrato
    global limite
    global numero_saques
    global LIMITE_SAQUES

    if valor > saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif valor > limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        efetuar_saque(valor)
    else:
        print('Operação falhou! O valor informado é inválido.')


def emitir_extrato():
    global saldo
    global extrato

    print(f"\n{'=' * 16} EXTRATO {'=' * 16}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 42)


def menu_index(op):
    while True:
        opcao = input(op)
        match opcao:
            case "d":
                value = float(input("Informe o valor do depósito: "))
                depositar(value)
            case "s":
                value = float(input("Informe o valor do saque: "))
                sacar(value)
            case "e":
                emitir_extrato()
            case "q":
                break
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 300
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

opcao = input()
menu_index(opcao)
