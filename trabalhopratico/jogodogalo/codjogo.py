#codigo do jogo

from jogador import Jogador
from tabuleiro import Tabuleiro

def desistir(jogada):
    if jogada == "desisto":
        return exit()

def jogar(jogada, final, jtoken, jnome):
    desistir(jogada)
    coluna = jogada[0]
    linha = jogada[1]
    linha = int(linha)
    final.completar(coluna, linha, jtoken)
    print(final)
    final.ver_vitoria(coluna, linha, jtoken, jnome)

playsvalidas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "desisto"]
"""
j1nome = #str(input("Introduza o seu nome: "))
j1token =str(input("Introduza um token para o representar no jogo: "))
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
"""


jogador1 = Jogador("a", "a")
jogador2 = Jogador("b", "b")

final = Tabuleiro()             #vai fazer o tabuleiro pela primeira vez
print(final)                    #e imprimi-lo
for i in range(1,10):           #ciclo for que nos vai facilitar a descobrir empates
    if i != 9:                 #serve para saber se nao estamos na jogada 10(ou seja, se tivermos a certeza que ainda nao houve empate)
        validade = False
        while validade == False:#com este ciclo vamos introduzindo as coordenadas ate colocarmos uma correta
            if i % 2 != 0:      #para verificar se quem vai jogar é o jogador 1
                jogada = input("\nJogador 1: Escreva coordenadas (Ex: A1) > ")
                if jogada in playsvalidas:
                    jogar(jogada, final, jogador1.token, jogador1.nome)
            else:               #se não for o jogador1, só pode ser o jogador 2
                jogada = input("\nJogador 2: Escreva coordenadas (Ex: A1) > ")
                if jogada in playsvalidas:
                    jogar(jogada, final, jogador2.token, jogador2.nome)
    else:                       #caso o jogo chegue à 10ª jogada, o programa acaba
        print("O jogo terminou num empate.")
        play = False            #se chegar as 10 jogadas isto funciona bem e acaba o programa direito