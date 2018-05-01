class Analizar():
    
    def __init__(self, lista):
        self.len = len(lista)
        self.c1 = lista[0]
        self.c2 = lista[1]
        self.c3 = lista[2]
        self.c4 = lista[3]
        self.c5 = lista[4]
        self.c6 = lista[5]
        self.c7 = lista[6]
        self.c8 = lista[7]
        self.c9 = lista[8]
        self.c10 = lista[9]
        self.d1 = self.c1 * 2
        self.d2 = self.c3 * 2
        self.d3 = self.c3 * 2
        self.d4 = self.c4 * 2
        self.d5 = self.c5 * 2
        self.d6 = self.c6 * 2
        self.d7 = self.c7 * 2
        self.d8 = self.c8 * 2
        self.d9 = self.c9 * 2
        self.d10 = self.c10 * 2
        self.somatorio = (self.c1 + self.c2 + self.c3 + self.c4 + self.c5 + self.c6 + self.c7 + self.c8 + self.c9 + self.c10)
        self.med = self.somatorio / self.len
        self.maior = lista[9]
        self.menor = lista[0]

    def __str__(self):
        return "{}\n{}{}{}{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}{}{}{}\n{}{}\n{}{}".format(self.len, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10, self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.somatorio, self.med, self.maior, self.menor)

lista = []

for _ in range(10):
    lista.append(int(input("Introduza um numero para a lista de 10 elementos: ")))

lista = Analizar(lista)
print(lista)

#  
#    def double(self):
#        self.d1 = self.c1 * 2
#        self.d2 = self.c3 * 2
#        self.d3 = self.c3 * 2
#        self.d4 = self.c4 * 2
#        self.d5 = self.c5 * 2
#        self.d6 = self.c6 * 2
#        self.d7 = self.c7 * 2
#        self.d8 = self.c8 * 2
#        self.d9 = self.c9 * 2
#        self.d10 = self.c10 * 2
#
#    def media(self):
#        
#        
#
#    def maiorEmenor(self, lista):
#        lista.sort()
#        self.maior = lista[9]
#        self.menor = lista[0]
