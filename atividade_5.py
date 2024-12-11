# # exercicio 1
#
# frutas = ["maçã", "uva", "laranja", "banana", "morango"]
# print(frutas)
#
# frutas.extend(["manga", "abacaxi", "pera"])
# print("Lista de frutas:", frutas)
#
# print{'primeira', frutas(0)}
# print{'ultima', frutas(-1)}

# frutas.pop(1)
# #print com a fruta removida
# print("Lista de frutas:", frutas)
#
# frutas.sort()
#
# contagem_banana = frutas.count("banana")
#
# print("Número de bananas na lista:", contagem_banana)

#exercicio 2

# # Criando uma tupla
# nome = ("Rogério", 57, "São Paulo")
#
#
# print("Nome:", nome[0])
# print("Idade:", nome[1])
# print("Cidade Natal:", nome[2])
#
# #Não é possíve mudar uma tupla, são Imutáveis.
#
#
# hobbies = ("leitura", "ciclismo", 'ouvir música')
# nome_com_hobbies = nome + hobbies
#
# print("\nMeus Hobbies:", nome_com_hobbies)

# Exercicio 3

# Lista de contatos
# contatos = {
#     "Felipe": "97456-7890",
#     "Giovanna": "98754-3210",
#     "Carlos": "96322-5455",
#     "Ana": "95368-9653",
#     "Rogerio": "98744-9874"
# }
# print(contatos)

# contatos["Pedro"] = "95123-4567"

# del contatos["Giovanna"]


# contatos["Felipe"] = "91222-6973"
# print("novo numero de Felipe é: ", contatos)
#

# print("Nomes dos contatos:")
# for nome in contatos:
#     print(nome)


#Exercício 4

# produtos = []
#
# def cadastrar_produto():
#     nome = input("Nome do produto: ")
#     preco = float(input("Preço: "))
#     quantidade = int(input("Quantidade em estoque: "))
#     produto = [nome, preco, quantidade]
#     produtos.append(produto)
#     print("Produto cadastrado com sucesso!")
#
# def pesquisar_produto():
#     nome = input("Nome do produto a pesquisar: ")
#     for produto in produtos:
#         if produto[0] == nome:
#             print("Nome:", produto[0])
#             print("Preço:", produto[1])
#             print("Quantidade em estoque:", produto[2])
#             return
#     print("Produto não encontrado.")
#
# def alterar_preco():
#     nome = input("Nome do produto a alterar o preço: ")
#     for produto in produtos:
#         if produto[0] == nome:
#             novo_preco = float(input("Novo preço: "))
#             produto[1] = novo_preco
#             print("Preço alterado com sucesso!")
#             return
#     print("Produto não encontrado.")
#
# def remover_produto():
#     nome = input("Nome do produto a remover: ")
#     for produto in produtos:
#         if produto[0] == nome:
#             produtos.remove(produto)
#             print("Produto removido com sucesso!")
#             return
#     print("Produto não encontrado.")
#
# def exibir_produtos():
#     print("\nLista de Produtos Cadastrados:")
#     if not produtos:
#         print("Nenhum produto cadastrado.")
#     else:
#         for produto in produtos:
#             print("Nome:", produto[0])
#             print("Preço:", produto[1])
#             print("Quantidade em estoque:", produto[2])
#             print("-" * 20)
#
# while True:
#     print("\nOpções:")
#     print("1. Cadastrar produto")
#     print("2. Pesquisar produto")
#     print("3. Alterar preço de um produto")
#     print("4. Remover produto")
#     print("5. Exibir produtos cadastrados")
#     print("6. Sair")
#
#     opcao = input("Escolha uma opção: ")
#
#     if opcao == "1":
#         cadastrar_produto()
#     elif opcao == "2":
#         pesquisar_produto()
#     elif opcao == "3":
#         alterar_preco()
#     elif opcao == "4":
#         remover_produto()
#     elif opcao == "5":
#         exibir_produtos()
#     elif opcao == "6":
#         break
#     else:
#         print("Opção inválida.")


#Exercicio 5

alunos = [
    {"nome": "Rogerio", "idade": 57, "notas": [8.5, 7.0, 9.0]},
    {"nome": "Felipe", "idade": 37, "notas": [9.5, 9.5, 10.0]},
    {"nome": "Giovanna", "idade": 19, "notas": [9.0, 8.5, 9.5]},
    {"nome": "Barbara", "idade": 21, "notas": [6.0, 7.0, 7.5]},
    {"nome": "Thiago", "idade": 26, "notas": [9.0, 7.0, 9.5]}
]

for aluno in alunos:
    aluno["media"] = sum(aluno["notas"]) / len(aluno["notas"])
aluno_maior_media = max(alunos, key=lambda aluno: aluno["media"])
alunos.sort(key=lambda aluno: aluno["idade"])
alunos_media_acima_7 = [aluno["nome"] for aluno in alunos if aluno["media"] > 7]
print("Média dos alunos:")
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['media']:.2f}")
print(f"\nAluno com a maior média: {aluno_maior_media['nome']} ({aluno_maior_media['media']:.2f})")
print("\nAlunos ordenados por idade:")
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['idade']}")
print(f"\nAlunos com média acima de 7: {alunos_media_acima_7}")
