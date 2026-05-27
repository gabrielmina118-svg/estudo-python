import csv

with open('clientes.csv') as entrada:
    for cliente in csv.reader(entrada):
        print('Nome: {} , Idade :{}'.format(*cliente))