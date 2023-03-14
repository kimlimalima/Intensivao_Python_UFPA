#Exercício 6
#Soma de 5 números inseridos pelo usuário
contador = 1
soma = 0
while contador <= 5:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
print(f'O total é: {soma}.')