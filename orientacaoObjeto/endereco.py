class Endereco:
    _enderecos: list['Endereco'] = []
    def __init__(self, id:int, rua: str, bairro: str, cidade: str, cep: str) -> None:
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        Endereco._enderecos.append(self)

    def __str__(self) -> str:
        return f'Endereco(id={self.id}, rua={self.rua}, bairro={self.bairro}, cidade={self.cidade}, cep={self.cep})'

    @classmethod
    def get_enderecos(self) -> list['Endereco']:
        return list(self._enderecos)
    
    @classmethod
    def get_enderecos_by_id(self, id: int) -> list['Endereco']:
        return [endereco for endereco in self._enderecos if endereco.id == id]