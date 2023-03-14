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




                    #Proposto por - IVAN - Web Scraping
                    #Em andamento irei aplicar algumas melhorias pra uma busca mais efetiva


#https://books.toscrape.com/catalogue/page-1.html
#CODKIM DO KIMA

from bs4 import BeautifulSoup
import requests,random
links = []
page = 1
# url = 'https://books.toscrape.com/catalogue/page-{page}.html'

page = 1
while True:
    if page:
        url = f'https://books.toscrape.com/catalogue/page-'+ str(page)+'.html'    
        pagina = requests.get(url)
        page += 1
        print(url)
    #raspagem dos links das imagens
    soup = BeautifulSoup(pagina.text, 'html.parser') 
    for item in soup.find_all('img'):
        links.append('https://books.toscrape.com/' + item['src']) 
    links = list(set(links))

    #download das imagens
    for item in links:
            try:
                img_data = requests.get(item).content
                with open('{}.jpg'.format(random.randint(1,100000)), 'wb') as handler:
                    handler.write(img_data)
            except:
                pass
    else: True
      
      
      
                                #Proposto por - IAN - Automação Download
                                #Em andamento


from pytube import YouTube

url = input('Digite a url do YouTube: ')

video = YouTube(url)

video.streams.get_highest_resolution().download(
    output_path=''
)

from tkinter import *
from tkinter import ttk
from pytube import YouTube

janela = Tk()
janela.geometry('720x300')
janela.title('TESTE DE JANELA')


texto = Label(
    janela,
    text ="Hello world",
    font = (
        'helvetica', 18, 'bold'
    )
)

texto.place(
    x = 40,
    y = 0,
    width = 300,
    height = 30
)

janela.mainloop()
# url = input('Digite a url do YouTube: ')
# video = YouTube(url)
# video.streams.get_highest_resolution().download()
