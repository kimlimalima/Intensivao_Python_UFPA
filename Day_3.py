#Exercício 1
#Soma dos 10 primeiros números ímpares maiores do que 5

lista = []
teste = 0

for numero in range(1,100):
    if numero % 2 != 0 and numero > 5:
        lista.append(numero)

for numero_impar in range(10):
    teste += lista[numero_impar]
print(f'A soma dos 10 primeiros números ímpares maiores do que 5 é: {teste}')
    



#Exercício 2
#Apresentar o 20 número de uma lista com 30 elementos

lista = []
for numero in range(0,30):
    lista.append(numero)
print(lista[20])




# Exercício 3
# Apresentar 5 elementos contidos em uma lista

numeros = [1,2,3,4,5]
for numeros_inteiros in numeros:
    print(numeros_inteiros)





#Exercício 4
#Receber 4 notas do usuário e apresentar a média das mesmas usando dicionário

nota1 = float(input('Digite a 1º nota: ')); nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: ')); nota4 = float(input('Digite a 4º nota: '))

notas_gerais = {
    'nota1':nota1,
    'nota2':nota2,
    'nota3':nota3,
    'nota4':nota4
    }

todas_notas = [notas_gerais['nota1'], notas_gerais['nota2'],notas_gerais['nota3'],notas_gerais['nota4']]
nota_geral = 0

for nota in todas_notas:
    nota_geral += nota
    media = nota_geral/len(notas_gerais)
print(media)





# Exercício 5
# Calculadora

import os

def operador_soma(numero1,numero2):
    return numero1 + numero2

def operador_subtração(numero1,numero2):
    return numero1 - numero2

def operador_multiplicação(numero1,numero2):
    return numero1 * numero2

def operador_divisão(numero1,numero2):
    return numero1 - numero2

while True:
    opção = input('''   
    Calculadora que calcula !!!
    Soma            [1]
    Subtração       [2]
    Multiplicação   [3]
    Divisão         [4]
    Escolha uma opção: ''')
    
    numero1 = float(input('Digite o primeiro operador: '))
    numero2 = float(input('Digite o segundo operador: '))

    if opção == '1':
        print(operador_soma(numero1,numero2))

    elif opção == '2':
        print(operador_subtração(numero1,numero2))

    elif opção == '3':
        print(operador_multiplicação(numero1,numero2))

    elif opção == '4':
        print(operador_divisão(numero1,numero2))

    else:
        print('Opção inválida!!!')
        True
        os.system("clear")
