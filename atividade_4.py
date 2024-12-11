# Tabuada

# numero = int(input("Para saber a tabuada, insira um número qualquer: "))
#
# a=1
# while a <= 10:
#     mult = numero * a
#     print(f"{numero} * {a} = {mult}")
#     a += 1
# print("\nFim do programa\n")


# Somador de despesas

# c = 0
# total = 0
#
# while True:
#     nota = input(f'Insira o valor da nota_{c+1}: e digite "sair" para somar o total do valor e sair ').lower()
#     if nota.isdigit():
#        total += float(nota)
#        c += 1
#
#     if nota == 'sair':
#
#        print(f'foram inseridos os valores de {c} notas, e o somatorio total foi de R$: {total:.2f}')
#        break


#Sistema de banco

# saldo = 1000
#
# while True:
#
#     oque = input("\n1- Saldo\n2- Saque\n3- Deposito\ns- Sair\n\nDigite a alternativa desejada (1-3 ou 's'):").lower()
#
#     if oque.isdigit():
#         if oque == "1":
#             print(f"\nSeu saldo é de: R$ {saldo:.2f}")
#         elif oque == "2":
#             if saldo == 0:
#                 print(f"\nO saldo da conta é de R$ {saldo:.2f}, por gentileza deposite antes de sacar.\n")
#                 continue
#             saque = float(input("Insira o valor que deseja sacar: "))
#             if saque > saldo:
#                 print("\nO valor solicitado excede o limite disponível.\nREPITA A OPERAÇÃO\n")
#                 continue
#             else:
#                 saldo -= saque
#                 print(f"\nRetire seu dinheiro.\n\nSaldo remanescente: R$ {saldo:.2f}\n")
#         elif oque == "3":
#             deposito = float(input("Insira o valor que deseja depositar: "))
#
#             if deposito < 0:
#                 print("\nO valor informado é inválido.\nREPITA A OPERAÇÃO\n")
#                 continue
#
#             else:
#                 saldo += deposito
#                 print(f"\nSaldo atualidado: R$ {saldo:.2f}\n")
#
#     elif oque == "s":
#         break
#     else:
#         print(f"\nOpção inválida.\nDigite um número de 1 a 3 ou 's' para sair.\n")
#         continue
#
# print(f"\nObrigado pela preferência.\nSISTEMA ENCERRADO.\n")
