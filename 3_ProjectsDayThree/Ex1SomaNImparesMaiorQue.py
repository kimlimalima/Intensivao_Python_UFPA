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