class Analizar():
    
    def __init__(self):
        self.len = len(lista)
    
    def content(self, lista):
        for num in lista:
            print(num)
    
    def double(self, lista):
        for num in lista:
            print(num * 2)
    
    def soma(self, lista, somatorio = 0):
        for num in lista:
            somatorio += num
           
    def media(self, somatorio):
        med = somatorio / 10
        print(med)
    
    def maiorEmenor(self, lista):
        lista.sort()
        print(lista[9])
        print(lista[0])

lista = []

for _ in range(10):
    lista.append(int(input("Introduza um numero para a lista de 10 elementos: ")))

lista = Analizar()