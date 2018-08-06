import os
import csv
from pathlib import Path
from jogador import Jogador
from tabuleiro import Tabuleiro

def desistir(jogada):
    if jogada == "desisto" or jogada == "desistir":
        return True

def adicionar_jogador_default(caminho_ficheiro, data, delim = ","):
    with open(caminho_ficheiro, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def adicionar_jogador_novo(caminho_ficheiro, data, delim = ","):
    with open(caminho_ficheiro, "a", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def mostrar_jogadores(filepath, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        print("Jogadores existentes:\n")
        for row in data:
            print("\t".join(row))

def listar_info_jogadores(filepath, nomes, tokens, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            nome = row[0]
            token = row[1]
            nomes.append(nome)
            tokens.append(token)

def selecionar_jogador(filepath, nome, token, delim = ","):
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            if nome in row:
                return row[1]
                

def verificar_novo_jogador(jnome, jtoken):
    jnome = str(input("\nIntroduza o seu nome: "))
    if jnome in nomes:  #caso ja exista
        opcao_igual = True
        while opcao_igual:
            escolha = str(input("O jogador {} ja existe.\n\nDeseja usar esse jogador?(S/N) ".format(jnome)))
            if escolha == "S":  #e queira usar o que existe
                opcao_igual = False
                jtoken = selecionar_jogador(caminho_ficheiro, jnome, jtoken)
                return False, Jogador(jnome, jtoken)
                    
            elif escolha == "N":#se quiser criar um jogador novo
                jnome = str(input("\nIntroduza um nome diferente: "))
                if jnome not in nomes:  #quando acertar
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
                                opcao_igual = False
                                return jogador_novo, Jogador(jnome, jtoken)
            else:
                print("\nApenas sao aceites as letras S ou N como resposta")
    else:
        jtoken =str(input("\nIntroduza um token para o representar no jogo: "))
        if jtoken in tokens:
            opcao_igual = True
            while opcao_igual:
                escolha = str(input("\nO token {} ja esta a ser usado por outro jogador.\n\nPor favor escolha outro token: ".format(jtoken)))
                if escolha not in tokens:
                    jogador_novo = [
                        [jnome, jtoken, 0, 0]
                    ]
                    opcao_igual = False
                    return jogador_novo, Jogador(jnome, jtoken)
        else:
            jogador_novo = [
                    [jnome, jtoken, 0, 0]
            ]
            return jogador_novo, Jogador(jnome, jtoken)

JOGADASVALIDAS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

num_jogador = 0
ganhar = False
caminho_ficheiro = "data.csv"
jnome = "None"
jtoken = "None"
nomes = []
tokens = []
"""                     retirar as aspas na primeira vez que se executar o programa
jogadores_default = [
    ["Carlos", "C", 0, 0],
    ["Andre", "A", 0, 0],
    ["Armindo", "3", 0, 0],
    ["Jesue", "4", 0, 0]
]                     retirar as aspas na primeira vez que se executar o programa
"""
print("\nBem vindo ao jogo do galo!\nTodos os jogadores tem de ter um nome e um token diferente de todos os outros\n")

#adicionar_jogador_default(caminho_ficheiro, jogadores_default) fazer isto na primeira vez que o programa corre para criar jogadores default
print("Nomes e tokens ja registados:")
mostrar_jogadores(caminho_ficheiro)

listar_info_jogadores(caminho_ficheiro, nomes, tokens)



jogador_adicionar, jogador1 = verificar_novo_jogador(jnome, jtoken)     #verificar se estamos perante um novo jogador, mas constroi logo o jogador
if jogador_adicionar:                                                   #caso seja um novo jogador:
    adicionar_jogador_novo(caminho_ficheiro, jogador_adicionar)

jogador_adicionar, jogador2 = verificar_novo_jogador(jnome, jtoken)     #verificar se estamos perante um novo jogador, mas constroi logo o jogador
if jogador_adicionar:                                                   #caso seja um novo jogador:
    adicionar_jogador_novo(caminho_ficheiro, jogador_adicionar)

lista_jogadores = [jogador1, jogador2]      #apenas e possivel criar esta lista depois de definir o jogador1 e jogador2, dai nao estar perto das outras variaveis

jogador1.nome = str(jogador1.nome)
jogador1.token = str(jogador1.token)
jogador2.nome = str(jogador2.nome)
jogador2.token = str(jogador2.token)


print("\nA qualquer momento pode desistir ao escrever \"desisto\" como coordenada.\n")

tabuleiro = Tabuleiro()                 #construir o tabuleiro
print(tabuleiro)                        #mostrar o tabuleiro vazio

i = 0                                   #inicio do contador while (vai simular um ciclo for, explicado noutro comentario mais a baixo)

while i < 10:                           #foi necessario usar um ciclo while porque nao era possivel alterar o i do for i in... dentro do ciclo for
    num_jogador = abs(num_jogador)      #para ir alternando de jogadores
    validade = False
    while not validade:                 #determinar se a jogada pode acontecer para passar para o proximo jogador
        jogada = input("\nJogador {}: Escreva coordenadas (Ex: A1) > ".format(lista_jogadores[num_jogador].nome))
        if jogada in JOGADASVALIDAS:    #verificar se e uma coordenada
            coluna = jogada[0]
            linha = jogada[1]
            linha = int(linha)
            validade = tabuleiro.completar(coluna, linha, lista_jogadores[num_jogador])     #verificar se a jogada e valida
            tabuleiro.completar(coluna, linha, lista_jogadores[num_jogador])
            print(tabuleiro)
            if tabuleiro.ver_vitoria(coluna, linha, lista_jogadores[num_jogador]):
                print("\nO Jogador {} Venceu!\n".format(lista_jogadores[num_jogador].nome))
                ganhar = True
        if desistir(jogada):    #verificar se desistiu
            validade = True
            print("O Jogador {} ganhou.".format(lista_jogadores[abs(num_jogador-1)].nome))
            i = 10              #terminar o primeiro ciclo while uma vez que ja existe um vencedor

    if ganhar:
        break
    if i == 9:
        print("O jogo terminou num empate")
    
    num_jogador -= 1        #ir para o outro jogador
    i += 1                  #uma vez que este while esta a funcionar como um ciclo for, utilizou-se este contador