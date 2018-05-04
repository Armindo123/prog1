#Classe Tabuleiro para o jogo do galo

class Tabuleiro():
    def __init__(self): #criar campos para colocar os tokens
        self.A = [None, None, None]
        self.B = [None, None, None]
        self.C = [None, None, None]
        self.lista = [self.A, self.B, self.C]

    def devolvernumero(self, jogada1): #transformar A B ou C em numero para servir de indice para as listas
        if jogada1 == "A":
            return 0
        elif jogada1 == "B":
            return 1
        elif jogada1 == "C":
            return 2 

    def completar(self, jogada1, jogada2, token): #preencher com o token de cada jogador
        v = self.devolvernumero(jogada1)
        if self.lista[v][jogada2] == None:
            self.lista[v][jogada2] = token
            return True
        else:
            return False

    def __str__(self): #Mostrar o tabuleiro
        stroutput = "  A|B|C|"
        for i in range(0, 3):
            stroutput += "\n" + str(i+1) + "|"
            for j in range(0, 3):
                if self.lista[i][j] == None:
                    stroutput += " |"
                else:
                    stroutput += self.lista[i][j] + "|"
        return stroutput

    def ver(self, token):
        if (self.lista[0][0]== token and self.lista[0][1] == token and self.lista[0][2] == token) or \
            (self.lista[1][0] == token and self.lista[1][1] == token and self.lista[1][2] == token) or \
            (self.lista[2][0] == token and self.lista[2][1] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][0] == token and self.lista[2][0] == token) or \
            (self.lista[0][1] == token and self.lista[1][1] == token and self.lista[2][1] == token) or \
            (self.lista[0][2] == token and self.lista[1][2] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][1] == token and self.lista[2][2] == token) or \
            (self.lista[0][2] == token and self.lista[1][1] == token and self.lista[2][0] == token):
            global play
            print("Vencedor")
            play = False



play = True
token = "X"
jogada1 = "A"
jogada2 = 1
jogada1 = str(jogada1)
jogada2 = int(jogada2)
final = Tabuleiro()
print(final)
final.completar(jogada1, jogada2, token)
print(final)
