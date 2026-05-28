def criar_html(texto,classe = 'sucesso'):
    return f'<div class="{classe}">{texto}</div>'

def soma_n(*numeros):
    return sum(numeros)

print(soma_n(1,2,3,4,5))