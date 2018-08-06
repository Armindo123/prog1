import os
import csv
from pathlib import Path
from jogador import Jogador
from tabuleiro import Tabuleiro

def desistir(jogada):
    if jogada == "desisto" or jogada == "desistir":
        return exit()

def adicionar_jogador(caminho_ficheiro, data, delim = ","):
    with open(caminho_ficheiro, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def mostrar_jogadores(filepath, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        print("Jogadores existentes:\n")
        for row in data:
            print("\t".join(row))

def listar_jogadores_tokens(filepath, nomes, tokens, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            nome = row[0]
            token = row[1]

            nomes.append(nome)
            tokens.append(token)



JOGADASVALIDAS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "desisto", "desistir"]

num_jogador = 0
ganhar = False
caminho_ficheiro = "data.csv"
lista_jogadores = []
lista_jogadores.append(jogador1, jogador2)

jogadores_default = [
    ["Carlos", "C", 0, 0],
    ["Andre", "A", 0, 0],
    ["Armindo", "3", 0, 0],
    ["Jesue", "4", 0, 0]
]

print("\nBem vindo ao jogo do galo!\nTodos os jogadores tem de ter um nome e um token diferente de todos os outros\n")

adicionar_jogador(caminho_ficheiro, jogadores_default)
print("Nomes e tokens ja registados:")
mostrar_jogadores(caminho_ficheiro)

nomes = []
tokens = []

listar_jogadores_tokens(caminho_ficheiro, nomes, tokens)

for i in range(1,3):
    jnome = str(input("\nIntroduza o seu nome: "))
    if jnome in nomes:
        opcao_igual = True
        while opcao_igual:
            escolha = str(input("O jogador {} ja existe.\n\nDeseja usar esse jogador?(S/N) ".format(jnome)))
            if escolha == "S":
                opcao_igual = False
                
            elif escolha == "N":
                jnome = str(input("\nIntroduza um nome diferente: "))
                if jnome not in nomes:
                    opcao_igual = False
                    
                    jtoken =str(input("\nIntroduza um token para o representar no jogo: "))
                if jtoken in tokens:
                    opcao_igual = True
                    while opcao_igual:
                        escolha = str(input("\nO token {} ja esta a ser usado por outro jogador.\n\nPor favor escolha outro token: ".format(jtoken)))
                        if escolha not in tokens:
                            jogador_novo = [
                                [jnome, jtoken, 0, 0]
                            ]
                            adicionar_jogador(caminho_ficheiro, jogador_novo)
                            lista_jogadores[i] = Jogador(jnome, jtoken)
                            opcao_igual = False
            else:
                print("\nApenas sao aceites as letras S ou N como resposta")





j2nome = str(input("\nIntroduza o seu nome: "))
while True:
    j2token = str(input("\nIntroduza um token para o representar no jogo: "))
    if jtoken == j2token:
        print("Esse token ja esta a ser utilizado por outro jogador, escolha outro: ")
    else:
        break

jogador1 = Jogador(jnome, jtoken)
jogador2 = Jogador(j2nome, j2token)




jogador1.nome = str(jogador1.nome)
jogador1.token = str(jogador1.token)
jogador2.nome = str(jogador2.nome)
jogador2.token = str(jogador2.token)


print("\nA qualquer momento pode desistir ao escrever 'desisto' como coordenada.\n")

tabuleiro = Tabuleiro()
print(tabuleiro)

for i in range(1,10):
    num_jogador = abs(num_jogador)
    validade = False
    while not validade:
        jogada = input("\nJogador {}: Escreva coordenadas (Ex: A1) > ".format(lista_jogadores[num_jogador].nome))
        if jogada in JOGADASVALIDAS:
            desistir(jogada)
            coluna = jogada[0]
            linha = jogada[1]
            linha = int(linha)
            validade = tabuleiro.completar(coluna, linha, lista_jogadores[num_jogador])
            tabuleiro.completar(coluna, linha, lista_jogadores[num_jogador])
            print(tabuleiro)
            if tabuleiro.ver_vitoria(coluna, linha, lista_jogadores[num_jogador]):
                print("O Jogador {} Venceu!".format(lista_jogadores[num_jogador].nome))
                ganhar = True
    if ganhar:
        break
                
    num_jogador -= 1