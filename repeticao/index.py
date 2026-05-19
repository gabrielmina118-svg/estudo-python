# from random import randint

# numero_informado = -1
# numero_secreto = randint(0, 9)

# while numero_informado != numero_secreto:
#     print("Número informado é diferente do número secreto")
#     numero_informado = int(input("Informe um número entre 0 e 9: "))

# print(f"O numero secreto {numero_secreto} foi encontrado")

# ----------------------------------------------------------------------------------
# for i in range(10):
#     print(i)

# palavra = "Python"
# for letra in palavra:
#     print(letra)

# ----------------------------------------------------------------------------------

produtos = [
            {'nome': 'Notebook', 'preco': 2500 , 'importada':True , 'estoque': 10} ,
            {'nome': 'Mouse', 'preco': 150 , 'importada':False , 'estoque': 50} ,
            {'nome': 'Teclado', 'preco': 300 , 'importada':True , 'estoque': 20},
            {'nome': 'Monitor', 'preco': 800 , 'importada':False , 'estoque': 15},
            {'nome': 'Impressora', 'preco': 600 , 'importada':True , 'estoque': 5}   
            ]

# for produto in produtos:
#     print(produto.get('nome'))

# list comprehension
# nomes = [produto['nome'] for produto in produtos]
# print(nomes)

# for produto in produtos:
#     print(f"O produto {produto['nome']} custa R${produto['preco']} e tem estoque de {produto['estoque']} unidades")

# list comprehension trazendo nome e estoque
nomes_estoque = [(produto['nome'], produto['estoque']) for produto in produtos]
print(nomes_estoque)