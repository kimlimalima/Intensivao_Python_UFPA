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