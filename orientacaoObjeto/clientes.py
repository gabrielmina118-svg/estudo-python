from endereco import Endereco

class Cliente:
    _clientes: list['Cliente'] = []
    
    def __init__(self,id: int,nome: str,idade: int | None = None) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        Cliente._clientes.append(self)

    def __str__(self) -> str:
        return f'Cliente(id={self.id}, nome={self.nome}, idade={self.idade}) \n'

    @classmethod
    def get_clientes(self) -> list['Cliente']:
        return list(self._clientes)


