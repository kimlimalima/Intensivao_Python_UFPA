# Hello World
print('Hello World !!!')

#Exercício 1
nome = input('Escreva seu nome completo: ')
nome_split = nome.split()
quantidade_letras_primeiro_nome = len(nome_split[0])
quantidade_letras_nome_completo = len(''.join(nome_split))

print(f'Olá, {nome}')
print(f'Seu nome completo com letras maiusulas é: {nome.upper()}')
print(f'Seu nome completo com letras minusculas é: {nome.lower()}')
print(f'Seu nome sem espaços tem {quantidade_letras_nome_completo} letras')
print(f'Seu primeiro nome tem {quantidade_letras_primeiro_nome} letras')


# Exercício 2
# CPF formato: 000.000.000-00
cpf_extenso = input('''
Digite os 11 números do seu CPF sem formato extenso: (Ex: 00000000000)
''')

print(f'''
Seu CPF no formato 000.000.000-00:
{cpf_extenso[0:3]}.{cpf_extenso[3:6]}.{cpf_extenso[6:9]}-{cpf_extenso[9:11]}
''')


#Exercício 3

from datetime import date

ano_atual = date.today().year
idade_atual = int(input('Digite sua idade atual: '))
idade_aposentadoria = int(input('Digite a idade que você gostaria de se aposentar: '))

anos_restantes_para_aposentadoria = idade_aposentadoria - idade_atual
ano_aposentadoria = ano_atual + anos_restantes_para_aposentadoria

aniversario_ano_atual = input('''
Você já fez anisário este ano?
Se sim digite [S]
Se não digite [N]\n
''').upper()

print(f'Ainda faltam {anos_restantes_para_aposentadoria} anos para se aposentar.')

if aniversario_ano_atual == 'S':
    print(f'É {ano_atual}, então você pode se aposentar em {ano_aposentadoria}.')
elif aniversario_ano_atual == 'N':
    print(f'É {ano_atual}, então você pode se aposentar em {ano_aposentadoria-1}.')
else:
    print('Resposta Inválida!!!')


#Desafios
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
