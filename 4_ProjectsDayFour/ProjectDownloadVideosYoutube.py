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