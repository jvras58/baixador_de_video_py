#inport do pytube
from pytube import YouTube, streams
from pytube.cli import on_progress

#inserir link do video do youtube
link = input ("link: ")

#progesso do download
yt= YouTube(link, on_progress_callback = on_progress)

#mostra o titulo do video:
print("Titulo = ", yt.title)

#mostrar se iniciou o download
print("baixando...")

#maior resolução disponivel 
ys = yt.streams.get_highest_resolution()
ys.download()