class Data:
    def __init__(self, dia: int, mes: int, ano: int) -> None:
        if not 1 <= mes <= 12:
            raise ValueError(f'Mês inválido: {mes}')
        if not 1 <= dia <= 31:
            raise ValueError(f'Dia inválido: {dia}')
        
        self._validar_tipo(dia, 'dia')
        self._validar_tipo(mes, 'mes')
        self._validar_tipo(ano, 'ano')

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self) -> str:
        return f'{self.dia:02d}/{self.mes:02d}/{self.ano}'

    def _validar_tipo(self, valor, nome:str) ->None:
        if not isinstance(valor, int):
            raise ValueError(f'{nome} deve ser um número inteiro')


if __name__ == '__main__':
    data = Data(8, 6, 2026)
    print(data)
