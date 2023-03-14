#Desafio 1
from datetime import date
data_atual = date.today()
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))
data_inicio_aulas = date(ano, mes, dia)
dia_acabar_ferias = data_inicio_aulas - data_atual

if dia_acabar_ferias > 0:
    print(f'Faltam {dia_acabar_ferias} dias para acabarem as férias')