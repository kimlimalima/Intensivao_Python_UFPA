# Exercício 2
# CPF formato: 000.000.000-00
cpf_extenso = input('''
Digite os 11 números do seu CPF sem formato extenso: (Ex: 00000000000)
''')

print(f'''
Seu CPF no formato 000.000.000-00:
{cpf_extenso[0:3]}.{cpf_extenso[3:6]}.{cpf_extenso[6:9]}-{cpf_extenso[9:11]}
''')