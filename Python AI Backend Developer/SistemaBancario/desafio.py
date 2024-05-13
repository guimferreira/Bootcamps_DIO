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

while True:

    opcao = input(menu)

    match opcao:
        case "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        case "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        case "e":
            print(f"\n{'='*16} EXTRATO {'='*16}")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("="*42)

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")