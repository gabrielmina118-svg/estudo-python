def get_tipo_dia(dia):

    dias = {
        (1,7):"Fim de semana",
        tuple(range(2,7)): "Dia de semana"
    }

    dia_escolhido = (tipo for numeros , tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, "Dia inválido")

print(get_tipo_dia(10))
    