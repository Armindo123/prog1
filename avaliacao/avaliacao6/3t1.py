#analizar lista de 10 numeros

def content(lista):
    for num in lista:
        print(num)

def double(lista):
    for num in lista:
        print("Dobro dos elementos: {}".format(2 * num))

def soma(lista, somatorio):
    for num in lista:
        somatorio += num
    print("Somatorio: {}".format(somatorio))

def media(lista, somatorio):
    med = somatorio / 10
    print("Media: {}".format(med))

def maiorEmenor(lista):
    lista.sort()
    print("Maior elemento: {}".format(lista[9]))
    print("Menor elemento: {}".format(lista[0]))

lista = []
somatorio = 0

for _ in range(10):
    lista.append(int(input("Introduza um numero para a lista de 10 elementos: ")))

content(lista)
double(lista)
soma(lista, somatorio)
media(lista, somatorio)
maiorEmenor(lista)