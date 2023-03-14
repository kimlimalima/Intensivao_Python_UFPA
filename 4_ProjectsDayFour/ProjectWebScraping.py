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