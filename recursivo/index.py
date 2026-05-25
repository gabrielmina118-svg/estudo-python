def imprimir(maximo , atual):
    if(atual < maximo):        
        print(atual , end=',')
        imprimir(maximo , atual + 1)

# imprimir(10,0)
def fibonnaci(quantidade, sequencia=(0,1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonnaci(quantidade , sequencia + (sum(sequencia[-2:]), ))

for fib in fibonnaci(10):
    print(fib , end=',')