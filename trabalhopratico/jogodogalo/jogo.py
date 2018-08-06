#codigo do jogo separado

class Jogador():
    def __init__(self, jnome, jtoken):
        self.nome = jnome
        self.token = jtoken

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