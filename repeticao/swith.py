from datetime import datetime
import calendar

def datas_do_dia(dia_semana,mes):
    
    datas = []
    dia_semana = dia_semana.lower()
    mes = mes.lower()

    dias_semana = {
        'segunda': 0,
        'terca': 1,
        'quarta': 2,
        'quinta': 3,
        'sexta': 4,
        'sabado': 5,
        'domingo': 6,
    }

    meses = {
        'janeiro': 1, 'fevereiro': 2, 'marco': 3, 'abril': 4,
        'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
        'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12,
    }

    if dia_semana not in dias_semana:
       raise ValueError(f"Dia da semana inválido '{dia_semana}'")
    
    if mes not in meses:
       raise ValueError(f"mês inválido '{mes}'")
    
    numero_dia = dias_semana[dia_semana]
    numero_mes = meses[mes]
    ano = datetime.now().year

    _,total_dias = calendar.monthrange(ano,numero_mes)
    
    for dia in range(1,total_dias + 1):
        if calendar.weekday(ano,numero_mes,dia) == numero_dia:
            datas.append(f'dia : {dia}')        

    return datas


resultado = datas_do_dia('sabado','janeiro')
print(resultado)
