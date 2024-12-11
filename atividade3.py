# n1 = float(input('digite a nota 1: \n'))
# n2 = float(input('digite a nota 2: \n'))
#
# media_notas = ((n1 + n2) / 2)
# print(f'a media das notas é: {media_notas:.2f}')
#
# if media_notas ==10:
#     print('Aluno aprovado com destinção')
# elif media_notas >= 7 and media_notas <10:
#     print('Aluno aprovado')
# elif media_notas < 7 and media_notas >=0:
#     print('Aluno reprovado')
#
# else:
#     print('valor da media esta fora do intervalo de 0 - 10')

#Exercicio triangulo

# lado_A = float(input('digite a medida de A: \n'))
# lado_B = float(input('digite a medida de B: \n'))
# lado_C = float(input('digite a medida de C: \n'))
#
# print('tamanho do lado_A:', lado_A)
# print('tamanho do lado_B:', lado_B)
# print('tamanho do lado_C:', lado_C)
#
#
# if (lado_A + lado_B > lado_C) and (lado_A + lado_C > lado_B) and (lado_B + lado_C > lado_A):
#     if lado_A == lado_B and lado_B == lado_C:
#         print('É um triangulo equilatero')
#     elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
#         print('É um triangulo isosceles')
#     else:
#         print('É um triangulo escaleno')
# else: print("os valores informados não formam um triangulo")



#Exercicio salário

# ate 2k isento
# de 2001 a 3500 10%
# de 3501 a 5000 15%
# acima de 5k 20%

# salario_bruto = float(input('digite o valor do salario bruto: R$ \n'))
# valor_imposto = 0
#
#
# if salario_bruto <= 2000:
#     print('salario isento de imposto')
#     salario_liquido = salario_bruto
# elif salario_bruto >= 2001 and salario_bruto <= 3500:
#     salario_liquido = (salario_bruto - (salario_bruto * 0.1))
#     valor_imposto = salario_bruto * 0.1
# elif salario_bruto >= 3501 and salario_bruto <= 5000:
#     salario_liquido = (salario_bruto - (salario_bruto * 0.15))
#     valor_imposto = salario_bruto * 0.15
# elif salario_bruto > 5000:
#     salario_liquido = (salario_bruto - (salario_bruto * 0.2))
#     valor_imposto = salario_bruto * 0.2
#
#
# print(f'o salario bruto é de: R$ {salario_bruto:.2f}')
# print(f'o salario liquido é de: R$ {salario_liquido:.2f}')
# print(f'o valor do imposto é de: R$ {valor_imposto:.2f}')

# numero = int(input('Informe o numero que se deve apresentar a tabuada: '))
#
# print(f'vamos ver a tabuada do {numero}')
#
# for num in range(1, 11, 1):
#     print(num * numero)

#
# import time
#
# tempo = 240
#
# for i in range (tempo, -1, -1):
#     print('\r',end = f'{i//60}:{i%60}')
#     time.sleep(1)






















