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