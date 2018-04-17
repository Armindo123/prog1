#quadrilatero

def quadrilatero(linhas, caracter, colunas):
    print(caracter * colunas)
    baixo(linhas)
    if linhas == 1:
        exit
    else:
        print(caracter * colunas)

def baixo(linhas):
    igual = caracter + vazio * (colunas - 2) + caracter
    igual = str(igual)
    linhas -= 2
    for _ in range(linhas):
        print(igual)



vazio = str(" ")

caracter = str(input("Introduza o caracter desejada: "))
linhas = int(input("Introduza o numero de linhas desejado: "))
colunas = int(input("Introduza o numero de colunas desejado: "))


quadrilatero(linhas, caracter, colunas)