#Exercício 1
#Antecessor, Sucessor, Dobro, Tripo e Quadrado de um número x

numero = int(input('Digite um número: '))

print(f'O Antecessor de {numero} é: {numero-1}')
print(f'O Sucessor de {numero} é: {numero+1}')
print(f'O Dobro de {numero} é: {numero*2}')
print(f'O Triplo de {numero} é: {numero*3}')
print(f'O Quadrado de {numero} é: {numero**2}')


#Exerrcício 2
#Questionário CNH

try:
    idade = int(input('Digite sua idade: '))

    if idade < 18:
        print('É preciso ser maior de idade para participar dos cursos')
    elif idade >= 18:
        cnh = int(input('''
        Você já possui CNH?

        Se sim digite [1]
        Se não digite [2]

        Digite sua opção: '''))
        if cnh == 1:
            print('Você pode partcipar dos cursos de: Direção Defensiva e Defesa Pessoal.')
        elif cnh == 2:
                print('Você pode participar dos cursos de: Defesa Pessoal.')
        else :
                print('Resposta inválida!!!')
except:
    print('Idade inválida!!!')



#Exercício 3
#Login

nome_criada_login = input('Digite um nome de usuário: ')
senha_criada_login = input('Digite uma senha: ')

nome_inserida = input('Nome de Usuário: ')
senha_inserida = input('Senha do usuário: ')

if nome_inserida == nome_criada_login and senha_inserida == senha_criada_login:
    print('Seja Bem Vindo!')
else:
    print('Acesso Negado!')




#Exercício 4
#Imposto
valor_pedido = float(input('Qual é o Valor do pedido? '))
estado = input('Qual o Estado: ').upper()
imposto = 0.055*valor_pedido

if estado == 'PA':
    print(f'O subtotal é de R${valor_pedido}')
    print(f'O imposto é de R${imposto:.2f}')
    print(f'O total é de R${valor_pedido+imposto:.2f}')
else:
    print(f'O total é de R${valor_pedido}')



#Exercício 5
#Converter Celsius - Fahrenheit

print('Digite C para converter de Fahrenheit para Celsius.')
print('Digite F para converter de Celsius para Fahrenheit.')

operacao = input('Sua escolha: ').upper()

if operacao == 'C':
    tempF = input('Temperatura em Fahrenheit: ')
    if tempF.isnumeric():
        tempC = (float(tempF) - 32) * 5/9
        print(f'A temperatura em C é {tempC}')
    else:
        print('Temperatura inválida!')
elif operacao == 'F':
    tempC = input('Temperatura em Celsius: ')
    if tempC.isnumeric():
        tempF = (float(tempC) * 9/5) + 32
        print(f'A temperatura em C é {tempF:.2f}')
    else:
        print('Temperatura inválida!')
else:
    print('Comando inválido!')


#Exercício 6
#Soma de 5 números inseridos pelo usuário
contador = 1
soma = 0
while contador <= 5:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
print(f'O total é: {soma}.')



# Exercício 7
# Game acertar número aleatório

import random

resposta = random.randrange(1, 10)
tentativas = 1
chute = int(input('Digite um número: '))

while chute != resposta:
    if chute > resposta:
        print(f'Errou! É um valor menor que {chute}')
    if chute < resposta:
        print(f'Errou! É um valor maior que {chute}')
    tentativas += 1
    chute = int(input('Digite um número: '))
    
print(f'Resposta correta! Você utilizou {tentativas} tentativas o número sorteado foi {chute}.')
