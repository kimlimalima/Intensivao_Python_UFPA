                    # Proposto por - ERICK - API Cotação

#Projetinho 1
#Capturar a cotação de determinadaas moedas e apresentar ao usuário

import requests

req = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')

req_json = req.json()

cotação_dolar = float(req_json['USDBRL']['bid'])

valor_real = float(input('Digite um valor em reais: '))
real_dolar = valor_real/cotação_dolar
print(f'Valor em dólar: {real_dolar:.2f}')


cotação_euro = float(req_json['EURBRL']['bid'])
print(f'Valor EUR-BRL: {cotação_euro:.2f}')