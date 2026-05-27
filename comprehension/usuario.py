usuarios = {
    1: {"nome": "Ana", "idade": 25},
    2: {"nome": "Bruno", "idade": 30},
    3: {"nome": "Carlos", "idade": 22},
    4: {"nome": "Daniela", "idade": 28},
    5: {"nome": "Eduardo", "idade": 35},
    6: {"nome": "Fernanda", "idade": 19},
    7: {"nome": "Gabriel", "idade": 41},
    8: {"nome": "Helena", "idade": 27},
    9: {"nome": "Igor", "idade": 33},
    10: {"nome": "Juliana", "idade": 24}
}

#  Essa busca é hash table
def buscar_usuario(id):
    return usuarios.get(id,"Usuario inválido")

print(buscar_usuario(2))