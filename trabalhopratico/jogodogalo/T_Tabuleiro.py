#Classe Tabuleiro para o jogo do galo

class Tabuleiro():
    def __init__(self): #criar campos para colocar os tokens
        self.A = [None, None, None]
        self.B = [None, None, None]
        self.C = [None, None, None]
        self.lista = [self.A, self.B, self.C]

    def devolvernumero(self, jogada1): #transformar A B ou C em numero para servir de índice para as listas
        if jogada1 == "A":
            return 0
        if jogada1 == "B":
            return 1
        return 2 

    def completar(self, jogada1, jogada2, token): #preencher com o token de cada jogador
        v = self.devolvernumero(jogada1)
        jogada2 -= 1        #tenho de fazer isto para a pessoa poder por A 1 e isso se referir à lista[A][0] corretamente
        global validade
        if self.lista[v][jogada2] == None:
            self.lista[v][jogada2] = token
            validade = True #isto faz com que o ciclo continue para o proximo jogador

    def ver_vitoria(self, jogada1, jogada2, token, nome):   #verificar se ganhou            
        v = self.devolvernumero(jogada1)
        jogada2 -= 1
        if (self.lista[v][0] == token and self.lista[v][1] == token and self.lista[v][2] == token) or \
            (self.lista[0][jogada2] == token and self.lista[1][jogada2] == token and self.lista[2][jogada2] == token):  #condicão mais básica
            print("Parabens! {} venceu!".format(nome))
            return exit()
        elif (self.lista[0][0] == token and self.lista[1][1] == token and self.lista[2][2] == token) or \
            (self.lista[0][2] == token and self.lista[1][1] == token and self.lista[2][0] == token):#condicão especial
            print("Parabens! {} venceu!".format(nome))
            return exit()


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

class Jogador():
    def __init__(self, jnome, jtoken):
        self.nome = jnome
        self.token = jtoken

def desistir(jogada):
    if jogada == "desisto":
        return exit()

def jogar(jogada, final, jtoken, jnome):
    desistir(jogada)
    jogada1 = jogada[0]
    jogada2 = jogada[1]
    jogada2 = int(jogada2)
    final.completar(jogada1, jogada2, jtoken)
    print(final)
    final.ver_vitoria(jogada1, jogada2, jtoken, jnome)

playsvalidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "desisto"]

j1nome = str(input("Introduza o seu nome: "))
j1token = str(input("Introduza um token para o representar no jogo: "))
j2nome = str(input("introduza o seu nome: "))
while True:
    j2token = str(input("Introduza um token para o representar no jogo: "))
    if j1token == j2token:
        print("Esse token ja esta a ser utilizado por outro jogador, escolha outro: ")
    else:
        break
jogador1 = Jogador(j1nome, j1token)
jogador2 = Jogador(j2nome, j2token)
print("\nA qualquer momento pode desistir ao escrever 'desisto' como coordenada.\n")

final = Tabuleiro()             #vai fazer o tabuleiro pela primeira vez
print(final)                    #e imprimi-lo
for i in range(1,11):           #ciclo for que nos vai facilitar a descobrir empates
    if i != 10:                 #serve para saber se nao estamos na jogada 10(ou seja, se tivermos a certeza que ainda nao houve empate)
        validade = False
        while validade == False:#com este ciclo vamos introduzindo as coordenadas ate colocarmos uma correta
            if i % 2 != 0:      #para verificar se quem vai jogar é o jogador 1
                jogada =input("\nJogador 1: Escreva coordenadas (Ex: A1) > ")
                if jogada in playsvalidas:
                    jogar(jogada, final, j1token, j1nome)
            else:               #se não for o jogador1, só pode ser o jogador 2
                jogada = input("\nJogador 2: Escreva coordenadas (Ex: A1) > ")
                if jogada in playsvalidas:
                    jogar(jogada, final, j2token, j2nome)
    else:                       #caso o jogo chegue à 10ª jogada, o programa acaba
        print("O jogo terminou num empate.")
        play = False            #se chegar as 10 jogadas isto funciona bem e acaba o programa direito