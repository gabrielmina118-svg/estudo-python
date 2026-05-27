# Criação com comprehension - o valor do array é completo
# dobro = [i * 2 for i in range(10) if i % 2 == 0]
# print(dobro)

# Generator cria array por demanda - Melhor devido ao uso de memoria
# generator = (i * 2 for i in range(10) if i % 2 == 0)
# print(next(generator,"fim do generator"))

# dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}

# for numero , valor in dicionario.items():
#     print(f'{numero} x 2 = {valor}')

