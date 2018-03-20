#introduzir numeros ate -1 e depois calcular a media



hit = False
mediabruta = 0
divisor = 0
tentativa = 0
while not hit:
    tentativa = int(input("Numero: "))
    if tentativa != -1:
        mediabruta += tentativa
        divisor += 1
    else:
        media = mediabruta / divisor 
        print(media)
        hit = True