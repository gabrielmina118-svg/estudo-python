from clientes import Cliente
from endereco import Endereco


class ClientePj(Cliente):
    def __init__(self, id: int, nome: str, cnpj: str, idade: int | None = None) -> None:
        super().__init__(id, nome, idade)
        self.cnpj = cnpj

    def __str__(self) -> str:
        return f'ClientePj(id={self.id}, nome={self.nome}, cnpj={self.cnpj}) \n'

    @classmethod
    def get_clientes_pj(cls) -> list['ClientePj']:
        return [cliente for cliente in Cliente.get_clientes() if isinstance(cliente, ClientePj)]