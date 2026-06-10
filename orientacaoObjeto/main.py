from dataclasses import dataclass

from clientes import Cliente
from clientesPj import ClientePj
from endereco import Endereco


@dataclass
class ClienteComEnderecos:
    cliente: Cliente
    enderecos: list[Endereco]
def criar_clientes() -> None:
    Cliente(
        id=1,
        nome='Ana Silva',
        idade=28
    )

    Cliente(
        id=2,
        nome='Bruno Santos',
        idade=35
    )

    Cliente(
        id=3,
        nome='Carla Oliveira',
        idade=22
    )

    Cliente(
        id=4,
        nome='Diego Costa',
        idade=41
    )
    
    ClientePj(
        id=5,
        nome='Empresa XYZ',
        cnpj='12345678901234'
    )

def criar_enderecos() -> None:
    Endereco(
        id=1,
        rua='Rua das Flores, 100',
        bairro='Centro',
        cidade='São Paulo',
        cep='01310-100',
    )
    Endereco(
        id=2,
        rua='Av. Paulista, 500',
        bairro='Bela Vista',
        cidade='São Paulo',
        cep='01310-200',
    )
    Endereco(
        id=3,
        rua='Rua do Sol, 45',
        bairro='Jardins',
        cidade='Rio de Janeiro',
        cep='22460-010',
    )
    Endereco(
        id=4,
        rua='Rua das Palmeiras, 12',
        bairro='Aldeota',
        cidade='Fortaleza',
        cep='60150-060',
    )

def Clientes() -> list[ClienteComEnderecos]:
    criar_clientes()
    criar_enderecos()

    return [
        ClienteComEnderecos(
            cliente=cliente,
            enderecos=Endereco.get_enderecos_by_id(cliente.id),
        )
        for cliente in Cliente.get_clientes()
    ]

if __name__ == '__main__':
    for item in Clientes():
        print(item.cliente, end='')
        for endereco in item.enderecos:
            print(f'  -> {endereco}')