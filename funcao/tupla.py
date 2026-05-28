# def podio_olimpiada(**podio):
#     for posicao , atleta in podio.items():
#         print(f"{posicao} lugar: {atleta}")

# podio_olimpiada(primeiro="joao",
#                 segundo="maria",
#                 terceiro="pedro")


def calcular_preco_final(preco_bruto,calculo_imposto,*params):
    return preco_bruto + calculo_imposto(*params)

def imposto_sp(importado):
    return 0.15 if importado else 0.05

def imposto_explosivo(explosivo , fator = 1):
    return 0.11 * fator if explosivo else 0


if __name__ == "__main__":
    preco_bruto = 150
    preco_medio = calcular_preco_final(preco_bruto, imposto_sp, True)
    preco_final = calcular_preco_final(preco_medio, imposto_explosivo, True, 2)

    print(preco_medio)
    print(preco_final)
