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