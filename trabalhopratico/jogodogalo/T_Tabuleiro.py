#Classe Tabuleiro para o jogo do galo

class Tabuleiro():
    def __init__(self, token, jogada, lista):
        self.token = token
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
            listaA[0] = self.token
            self.a1 = self.token
        elif jogada == "A2":
            listaA[1] = self.token
            self.a2 = self.token
        elif jogada == "A3":
            listaA[2] = self.token
            self.a3 = self.token
        elif jogada == "B1":
            listaB[0] = self.token
            self.b1 = self.token
        elif jogada == "B2":
            listaB[1] = self.token
            self.b2 = self.token
        elif jogada == "B3":
            listaB[2] = self.token
            self.b3 = self.token
        elif jogada == "C1":
            listaC[0] = self.token
            self.c1 = self.token
        elif jogada == "C2":
            listaC[1] = self.token
            self.c2 = self.token
        elif jogada == "C3":
            listaC[2] = self.token
            self.c3 = self.token

    def __str__(self):
        return " |A|B|C|\n1|{}|{}|{}|\n2|{}|{}|{}|\n3|{}|{}|{}|".format(self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3)

listaA = [" "," "," "]
listaB = [" "," "," "]
listaC = [" "," "," "]
lista = [listaA, listaB, listaC]
token = "X"
jogada = "A1"
final = Tabuleiro(token, jogada, lista)
print(final)
final.completar(jogada, lista)
print(final)
token = "O"
jogada = "B2"
final = Tabuleiro(token, jogada, lista)
final.completar(jogada, lista)
print(final)