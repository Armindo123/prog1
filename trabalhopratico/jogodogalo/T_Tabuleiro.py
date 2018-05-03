#Classe Tabuleiro para o jogo do galo

class Tabuleiro():
    def __init__(self, tokenjogador, jogada, lista):
        self.token = tokenjogador
        self.jogada = jogada
        self.a1 = listaA[0]
        self.a2 = listaA[1]
        self.a3 = listaA[2]
        self.b1 = listaB[0]
        self.b2 = listaB[1]
        self.b3 = listaB[2]
        self.c1 = listaC[0]
        self.c2 = listaC[1]
        self.c3 = listaC[2]
    
    def completar(self, jogada, lista):
        if jogada == "A1":
            lista[listaA[0]] = self.token
        elif jogada == "A2":
            lista[listaA[1]] = self.token
        elif jogada == "A3":
            lista[listaA[2]] = self.token
        elif jogada == "B1":
            lista[listaB[0]] = self.token
        elif jogada == "B2":
            lista[listaB[1]] = self.token
        elif jogada == "B3":
            lista[listaB[2]] = self.token
        elif jogada == "C1":
            lista[listaC[0]] = self.token
        elif jogada == "C2":
            lista[listaC[1]] = self.token
        elif jogada == "C3":
            lista[listaC[2]] = self.token

    def __str__(self):
        return " |A|B|C|\n1|{}|{}|{}|\n2|{}|{}|{}|\n3|{}|{}|{}|".format(self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3)

listaA = [" "," "," "]
listaB = [" "," "," "]
listaC = [" "," "," "]
lista = [listaA, listaB, listaC]
tokenjogador = "X"
jogada = "A2"
final = Tabuleiro(tokenjogador, jogada, lista)
print(final)