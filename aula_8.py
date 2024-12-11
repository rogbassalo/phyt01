# minha_lista = []
#
# print(minha_lista)
# print(type(minha_lista))

#
# minha_lista = [10, 1.4, "OI", True]
#
# for elemento in minha_lista:
#     print(elemento)
#
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Índice
#
# print(numeros)
# print(numeros[0])
# print(numeros[5])
# print(numeros[-1])
#
# # Slicing
#
# print(numeros[::-1])
# print(numeros[2:8])
# print(numeros[2:8:2])
#
# numeros_2 = [10, 11, 12, 13, 14]
#
# lista_todos_os_numeros = numeros + numeros_2
#
# print(lista_todos_os_numeros)

# lista = list(range(500))
#
# print(lista)
#
# palavra = "paralelepipedo"
# #
# soletrando = list(palavra)
#
# outra_forma = ' - '.join(soletrando)
#
# print(soletrando)
# print(outra_forma)
#
# nome = input("Nome: ").split()
#
# print(nome)
#
# import time
#
# palavra = "paralelepipedo"
# l1 = 0
# l2 = 1
#
# for i in (range(len(palavra)//2)):
#     print(palavra[l1] + palavra[l2])
#     l1 += 2
#     l2 += 2
#     time.sleep(1)

#
# frutas = ['laranja', 'uva']
# print(len(frutas))
# # Métodos para inserção de elementos na lista
# nova_fruta = 'melancia'
# frutas.append(nova_fruta)
# print(frutas)
# print(len(frutas))
# # Mais itens de por vez
# frutas.extend(['banana', 'maçã', 'maçã',  'uva'])
# print(frutas)
# print(len(frutas))
# for fruta in frutas:
#     print(f"{frutas.count(fruta)}: {fruta}")
# frutas.insert(0, 'pêra')
# print(frutas)
# frutas[2] = 'abacaxi'
# print(frutas)
# # Remover itens de uma lista
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
# print(len(frutas))
# frutas.remove('maçã')
# print(frutas)
# print(len(frutas))
# del frutas[2]
# print(frutas)
# while 'maçã' in frutas:
#     frutas.remove('maçã')
# print(frutas)
# # frutas.clear()
# # print(frutas)
# # Ordenação de listas
# frutas.sort()
# print(frutas)
# frutas = sorted(frutas, reverse=True)
# print(frutas)
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matriz)
#
# numeros = []
#
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))


#
# lista_alunos = ['joão', 'maria', 'ana', 'raul',]
# notas_alunos = [5, 7, 8, 9]
# print(list(enumerate(lista_alunos)))
#
# for posicao, nome in enumerate(lista_alunos):
#     if nome == 'joão':
#         notas_alunos[posicao] = 7.5
#
# print(notas_alunos)

meu_dicionario = {'a':1, 'b':2, 'c': 3}
print( )