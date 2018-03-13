#duracao de um album com 5 cancoes
print("Introduza a duracao separando os minutos e os segundos por [:]")
tempo1m, tempo1s = input("Duracao da musica 1 (mm:ss)").split(":")
tempo2m, tempo2s = input("Duracao da musica 2 (mm:ss)").split(":")
tempo3m, tempo3s = input("Duracao da musica 3 (mm:ss)").split(":")
tempo4m, tempo4s = input("Duracao da musica 4 (mm:ss)").split(":")
tempo5m, tempo5s = input("Duracao da musica 5 (mm:ss)").split(":")

tempo1m = int(tempo1m)
tempo2m = int(tempo2m)
tempo3m = int(tempo3m)
tempo4m = int(tempo4m)
tempo5m = int(tempo5m)
tempo1s = int(tempo1s)
tempo2s = int(tempo2s)
tempo3s = int(tempo3s)
tempo4s = int(tempo4s)
tempo5s = int(tempo5s)

duracao_segundos = (tempo1m+tempo2m+tempo3m+tempo4m+tempo5m)*60
duracao_segundos += tempo1s + tempo2s + tempo3s + tempo4s + tempo5s


#print(duracao_minutos)
#print(duracao_segundos)
#print(duracao_total)


album_horas = duracao_segundos//3600
album_minutos = (duracao_segundos%3600)//60
album_segundos = (duracao_segundos%3600)%60



print(album_horas, ":", album_minutos, ":", album_segundos)