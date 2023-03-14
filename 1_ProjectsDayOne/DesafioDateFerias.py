#Desafio 1
from datetime import date


dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

def dateFerias(dia, mes, ano):

    data_atual = date.today()
    
    data_inicio_aulas = date(ano, mes, dia)
    
    dia_acabar_ferias = data_inicio_aulas - data_atual
    

    if dia_acabar_ferias != 0:
        return f'Faltam {dia_acabar_ferias} dias para acabarem as férias'
        
    else:
        return False
        
    
print(dateFerias(dia, mes, ano))