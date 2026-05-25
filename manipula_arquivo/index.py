with open('clientes.csv','r',encoding='utf-8-sig') as arquivo:
   dados = arquivo.read()

for registro in dados.splitlines():
#    print(registro.split(','))
    print('Nome: {}, Idade: {}, CPF: {}, Email: {}, Telefone: {}, Celular: {}, Data de Nascimento: {}, Gênero: {}, Estado Civil: {}, CEP: {}, Endereço: {}, Número: {}, Bairro: {}, Cidade: {}, Estado: {}'
          .format(*registro.split(',')),end='\n\n')