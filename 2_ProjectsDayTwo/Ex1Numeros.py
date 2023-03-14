#Exercício 1
#Antecessor, Sucessor, Dobro, Tripo e Quadrado de um número x

numero = int(input('Digite um número: '))

def numeros(numero):
    print(f'O Antecessor de {numero} é: {numero-1}')
    print(f'O Sucessor de {numero} é: {numero+1}')
    print(f'O Dobro de {numero} é: {numero*2}')
    print(f'O Triplo de {numero} é: {numero*3}')
    print(f'O Quadrado de {numero} é: {numero**2}')
    
    return "Programa finalizado."


print(numeros(numero))