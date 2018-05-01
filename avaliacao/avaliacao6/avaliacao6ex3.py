class Analizar():
    
    def __init__(self):             #criar o necessario para todas as funcoes
        self.len = len(lista)
        self.l1 = []
        self.l2 = []
        self.somatorio = 0
        self.med = 0
        self.maior = 0
        self.menor = 0
    
    def content(self, lista):
        for num in lista:
            self.l1.append(num)
    
    def double(self, lista):
        for num in lista:
            dobro = num * 2
            self.l2.append(dobro)
    
    def soma(self, lista):
        for num in lista:
            self.somatorio += num
           
    def media(self):
        med = self.somatorio / 10
        self.med += med
    
    def maiorEmenor(self, lista):
        lista.sort()
        self.maior = lista[9]
        self.menor = lista[0]
    
    def __str__(self):              #transformar em string
        return "Conteudo da lista: {}\nDobro de cada elemento: {}\nSomatorio de todos os elementos: {}\nMedia: {}\nMaior elemento: {}\nMenor elemento: {}".format(self.l1, self.l2, self.somatorio, self.med, self.maior, self.menor)
    

lista = []

for _ in range(10):             #fazer a lista
    lista.append(int(input("Introduza um numero para a lista de 10 elementos: ")))

resultado = Analizar()          #garantir que constroi tudo
resultado.content(lista)        #garantir que constroi tudo
resultado.double(lista)         #garantir que constroi tudo
resultado.soma(lista)           #garantir que constroi tudo
resultado.media()               #garantir que constroi tudo
resultado.maiorEmenor(lista)    #garantir que constroi tudo
print(resultado)                #garantir que constroi tudo