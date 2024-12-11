# i = 0
# unidade = 1
#
#
# while i <= 100:
#
#     print(i)
#
#     i = i + 2
#     i += unidade

# somador = 0
#
# while somador < 100:
#     somador += int(input('digite o numero a ser somado: '))
#     print(somador)


# import time
#
# tempo = 3600
#
# while tempo > -1:
#     print('\r', end=f'{tempo// 3600}:{tempo// 60}:{tempo % 60}')
#     time.sleep(1)
#     tempo -= 1

# while True:
#     email = input('email: ')
#     #if '.com' not in email:
#     if email[-4:] != '.com':
#         print('falta o .com')
#         continue
#     else:
#         print('bem vindo')
#         break


# acesso = 'thiago_001'
# controle_acesso = False
# contador = 0
#
# while not controle_acesso:
#     if contador < 3:
#         chave_acesso = input('Informe sua credencial: ')
#         contador  +=1
#         if chave_acesso == acesso:
#             chave_acesso = True
#             controle_acesso = True
#             print('acesso autorizado')
#             break
#         else:
#             continue
#     else:
#         print('não autorizado')
#         break



# numero = int(input("Para saber a tabuada, insira um número qualquer: "))
#
# a=1
# while a <= 10:
#     mult = numero * a
#     print(f"{numero} * {a} = {int(mult)}")
#     a += 1
# print("\nFim do programa\n")


saldo = 1000

while True:

    oque = input("\n1- Saldo\n2- Saque\n3- Deposito\ns- Sair\n\nDigite a alternativa desejada (1-3 ou 's'):").lower()

    if oque.isdigit():
        if oque == "1":
            print(f"\nSeu saldo é de: R$ {saldo:.2f}")
        elif oque == "2":
            if saldo == 0:
                print(f"\nO saldo da conta é de R$ {saldo:.2f}, por gentileza deposite antes de sacar.\n")
                continue
            saque = float(input("Insira o valor que deseja sacar: "))
            if saque > saldo:
                print("\nO valor solicitado excede o limite disponível.\nREPITA A OPERAÇÃO\n")
                continue
            else:
                saldo -= saque
                print(f"\nRetire seu dinheiro.\n\nSaldo remanescente: R$ {saldo:.2f}\n")
        elif oque == "3":
            deposito = float(input("Insira o valor que deseja depositar: "))

            if deposito < 0:
                print("\nO valor informado é inválido.\nREPITA A OPERAÇÃO\n")
                continue

            else:
                saldo += deposito
                print(f"\nSaldo atualidado: R$ {saldo:.2f}\n")

    elif oque == "s":
        break
    else:
        print(f"\nOpção inválida.\nDigite um número de 1 a 3 ou 's' para sair.\n")
        continue

print(f"\nObrigado pela preferência.\nSISTEMA ENCERRADO.\n")


# quantidade_despesas = int(input('insira a quantidade de despesas: '))
# total = 0
# for i in range(quantidade_despesas):
#     nota = int(input(f'Insira o valor da nota_{i+1}: '))
#     total += nota
# print(f'foram inseridos os valores de {quantidade_despesas} notas, e o somatorio total foi de R$: {total:.2f}')





# c = 0
# total = 0
#
# while True:
#     nota = input(f'Insira o valor da nota_{c+1}: e digite "sair" para somar o total do valor e sair ').lower()
#     if nota.isdigit():
#        total += int(nota)
#        c += 1
#
#     if nota == 'sair':
#
#        print(f'foram inseridos os valores de {c} notas, e o somatorio total foi de R$: {total:.2f}')
#        break

