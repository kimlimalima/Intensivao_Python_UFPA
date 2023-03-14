#Exercise 1
nome = input('Escreva seu nome completo: ')
nome_split = nome.split()
quantidade_letras_primeiro_nome = len(nome_split[0])
quantidade_letras_nome_completo = len(''.join(nome_split))

print(f'Olá, {nome}')
print(f'Seu nome completo com letras maiusulas é: {nome.upper()}')
print(f'Seu nome completo com letras minusculas é: {nome.lower()}')
print(f'Seu nome sem espaços tem {quantidade_letras_nome_completo} letras')
print(f'Seu primeiro nome tem {quantidade_letras_primeiro_nome} letras')