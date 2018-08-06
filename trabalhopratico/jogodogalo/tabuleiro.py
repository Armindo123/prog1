#class tabuleiro
from jogador import Jogador
class Tabuleiro():
    def __init__(self): #criar campos para colocar os jogador.tokens
        self.A = [None, None, None]
        self.B = [None, None, None]
        self.C = [None, None, None]
        self.lista = [self.A, self.B, self.C]

    def devolvernumero(self, coluna): #transformar A B ou C em numero para servir de índice para as listas
        if coluna == "A":
            return 0
        if coluna == "B":
            return 1
        return 2 # jodada1 == C

    def completar(self, coluna, linha, jogador): #preencher com o jogador.token de cada jogador
        v = self.devolvernumero(coluna)
        linha -= 1        #tenho de fazer isto para a pessoa poder por A 1 e isso se referir à lista[A][0] corretamente
        if self.lista[v][linha] == None:
            self.lista[v][linha] = jogador.token
            return True #isto faz com que o ciclo continue para o proximo jogador

    def ver_vitoria(self, coluna, linha, jogador):   #verificar se ganhou            
        v = self.devolvernumero(coluna)
        linha -= 1
        if (self.lista[v][0] == jogador.token and self.lista[v][1] == jogador.token and self.lista[v][2] == jogador.token) or \
            (self.lista[0][linha] == jogador.token and self.lista[1][linha] == jogador.token and self.lista[2][linha] == jogador.token) or \
            (self.lista[0][0] == jogador.token and self.lista[1][1] == jogador.token and self.lista[2][2] == jogador.token) or \
            (self.lista[0][2] == jogador.token and self.lista[1][1] == jogador.token and self.lista[2][0] == jogador.token):#condicão especial
            return True

    def __str__(self): #Mostrar o tabuleiro
        stroutput = "\n  A|B|C|"
        for i in range(0, 3):
            stroutput += "\n" + str(i+1) + "|"
            for j in range(0, 3):
                if self.lista[j][i] == None:
                    stroutput += " |"
                else:
                    stroutput += self.lista[j][i] + "|"
        return stroutput