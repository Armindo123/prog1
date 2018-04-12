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
    linhas -= 2
    if linhas > 0:
        
        print(igual) 
        linhas -= 1
        baixo(linhas)
        print(igual)
    elif linhas <= 0:
        exit



vazio = str(" ")

caracter = str(input("Introduza o caracter desejada: "))
linhas = int(input("Introduza o numero de linhas desejado: "))
colunas = int(input("Introduza o numero de colunas desejado: "))


quadrilatero(linhas, caracter, colunas)