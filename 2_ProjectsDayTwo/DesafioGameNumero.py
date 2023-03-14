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