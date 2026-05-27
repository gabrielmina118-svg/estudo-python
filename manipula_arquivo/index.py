with open('clientes.csv','r',encoding='utf-8-sig') as arquivo:

   for registro in arquivo:
    print('Nome: {}, Idade: {}, CPF: {}, Email: {}, Telefone: {}, Celular: {}, Data de Nascimento: {}, Gênero: {}, Estado Civil: {}, CEP: {}, Endereço: {}, Número: {}, Bairro: {}, Cidade: {}, Estado: {}'
          .format(*registro.split(',')),end='\n\n')