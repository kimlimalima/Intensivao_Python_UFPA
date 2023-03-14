#Exercise 3
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