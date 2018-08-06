import os
import csv
from pathlib import Path
from jogador import Jogador
from tabuleiro import Tabuleiro

def menu(mensagem_personalizada):
    print("{}".format(mensagem_personalizada))
    selecao = input("\n(1/2/3)->")
    if selecao == "1":
        print_ranking()
        return  menu(mensagem_personalizada)
    if selecao == "2":
        return True
    return False

def desistir(jogada):
    if jogada == "desisto" or jogada == "desistir":
        return True
    return False

def verificar_ficheiro(caminho_ficheiro):
    caminho_ficheiro = str(caminho_ficheiro)
    ficheiro = Path(caminho_ficheiro)
    if ficheiro.is_file():
        return True
    return False

def escrever_data_csv(caminho_ficheiro, data, delim = ","):
    with open(caminho_ficheiro, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def lista_jogadores_csv(filepath, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        data = list(data)
        return data
    return None

def editar_jogador(caminho_ficheiro, lista_jogadores_completa, delim = ","):
    with open(caminho_ficheiro, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in lista_jogadores_completa:
            writer.writerow(line)

def listar_info_jogadores(filepath, nomes, tokens, delim = ",") :
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            nome = row[0]
            token = row[1]
            nomes.append(nome)
            tokens.append(token)

def selecionar_jogador(filepath, nome, delim = ","):
    with open(caminho_ficheiro, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            if nome in row:
                return row[1], row[2], row[3]
    return None

def ordenar_pontos(data):
    for i in range(len(data)):
        data[i][2] = int(data[i][2])
    data.sort(key=lambda data: data[2], reverse = True) #trocar por algoritmo da aula
    return data
               
def verificar_novo_jogador():
    jnome = str(input("\nIntroduza o seu nome: "))
    if jnome in nomes:  #caso ja exista
        opcao_igual = True
        while opcao_igual:
            escolha = str(input("O jogador {} ja existe.\n\nDeseja usar esse jogador?(S/N) ".format(jnome)))
            if escolha == "S":  #e queira usar o que existe
                opcao_igual = False
                jtoken, jpontos, jjogos = selecionar_jogador(caminho_ficheiro, jnome)
                return False, jnome, jtoken, jpontos, jjogos       
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
                                jogador_novo =  [jnome, jtoken, 0, 0]
                                opcao_igual = False
                                return jogador_novo, jnome, jtoken, 0, 0
                    else:
                        return False, jnome, jtoken
            else:
                print("\nApenas sao aceites as letras S ou N como resposta")
    else:
        jtoken =str(input("\nIntroduza um token para o representar no jogo: "))
        if jtoken in tokens:
            opcao_igual = True
            while opcao_igual:
                escolha = str(input("\nO token {} ja esta a ser usado por outro jogador.\n\nPor favor escolha outro token: ".format(jtoken)))
                if escolha not in tokens:
                    jogador_novo = [jnome, jtoken, 0, 0]
                    opcao_igual = False
                    return jogador_novo, jnome, jtoken, 0, 0
        else:
            jogador_novo = [jnome, jtoken, 0, 0]
            return jogador_novo, jnome, jtoken, 0, 0

def print_ranking():
        print("\n Ranking atual:\n")
        ranking = ordenar_pontos(lista_jogadores_completa)              #criar o ranking
        for k in range(len(ranking)):
            print("{}-{}".format(k + 1, ranking[k]))



JOGADASVALIDAS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
JOGADORES_DEFAULT = [
    ["Carlos", "C", 0, 0],
    ["Andre", "A", 0, 0]
]

num_jogador = 0
ganhar = False
caminho_ficheiro = "data.csv"
nomes = []
tokens = []
mensagem_menu = "\nPara visualizar o ranking, prima 1\nPara comecar outro jogo, prima 2\nPara sair do jogo prima outra tecla qualquer" #mensagem personalizada para o menu(comecar)

if verificar_ficheiro(caminho_ficheiro) == False:
    escrever_data_csv(caminho_ficheiro, JOGADORES_DEFAULT) #fazer isto na primeira vez que o programa corre para criar jogadores default

lista_jogadores_completa = lista_jogadores_csv(caminho_ficheiro)    #criar uma lista com toda a info dos jogadores presentes em data.csv

print("\nBem vindo ao jogo do galo!\nTodos os jogadores tem de ter um nome e um token diferente de todos os outros")

jogar = menu(mensagem_menu)

while jogar:
    print("\nNomes e tokens ja registados:\n")
    for linha in lista_jogadores_completa:
        print(linha)

    listar_info_jogadores(caminho_ficheiro, nomes, tokens)

    jogador_adicionar, jnome, jtoken, jpontos, jjogos = verificar_novo_jogador()     #verificar se estamos perante um novo jogador, mas constroi logo o jogador
    if jogador_adicionar:                                                   #caso seja um novo jogador:
        lista_jogadores_completa.append(jogador_adicionar)
        escrever_data_csv(caminho_ficheiro, lista_jogadores_completa)
    jogador1 = Jogador(jnome, jtoken, jpontos, jjogos)
    
    jogador_adicionar, jnome, jtoken, jpontos, jjogos = verificar_novo_jogador()     #verificar se estamos perante um novo jogador, mas constroi logo o jogador
    if jogador_adicionar:                                                   #caso seja um novo jogador:
        lista_jogadores_completa.append(jogador_adicionar)
        escrever_data_csv(caminho_ficheiro, lista_jogadores_completa)
    jogador2 = Jogador(jnome, jtoken, jpontos, jjogos)

    lista_jogadores_completa = lista_jogadores_csv(caminho_ficheiro)

    lista_jogadores = [jogador1, jogador2]      #apenas e possivel criar esta lista depois de definir o jogador1 e jogador2, dai nao estar perto das outras variaveis

    jogador1.nome = str(jogador1.nome)
    jogador1.token = str(jogador1.token)
    jogador1.pontos = int(jogador1.pontos)
    jogador1.jogos = int(jogador1.jogos)
    jogador2.nome = str(jogador2.nome)
    jogador2.token = str(jogador2.token)
    jogador2.pontos = int(jogador2.pontos)
    jogador2.jogos = int(jogador2.jogos)

    print("\nA qualquer momento pode desistir ao escrever \"desisto\" como coordenada.\n")
    tabuleiro = Tabuleiro()                 #construir o tabuleiro
    print(tabuleiro)                        #mostrar o tabuleiro vazio
    
    quantidade_jogadores = len(lista_jogadores_completa)

    i = 0                                   #inicio do contador while (vai simular um ciclo for, explicado noutro comentario mais a baixo)
    while i < 9:                           #foi necessario usar um ciclo while porque nao era possivel alterar o i do for i in... dentro do ciclo for
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
            elif desistir(jogada):    #verificar se desistiu
                validade = True
                lista_jogadores[num_jogador].pontos += 1
                lista_jogadores[num_jogador].jogos += 1
                lista_jogadores[abs(num_jogador - 1)].pontos += 3
                lista_jogadores[abs(num_jogador - 1)].jogos += 1
                print("O Jogador {} ganhou.".format(lista_jogadores[abs(num_jogador-1)].nome))
                i = 10              #terminar o primeiro ciclo while uma vez que ja existe um vencedor
        i += 1                  #uma vez que este while esta a funcionar como um ciclo for, utilizou-se este contador      

        if ganhar:
            lista_jogadores[num_jogador].pontos += 3
            lista_jogadores[num_jogador].jogos += 1
            info_vencedor = [lista_jogadores[num_jogador].nome, lista_jogadores[num_jogador].token,lista_jogadores[num_jogador].pontos, lista_jogadores[num_jogador].jogos]
            lista_jogadores[abs(num_jogador - 1)].pontos += 1
            lista_jogadores[abs(num_jogador - 1)].jogos += 1
            info_perdedor = [lista_jogadores[abs(num_jogador - 1)].nome, lista_jogadores[abs(num_jogador - 1)].token, lista_jogadores[abs(num_jogador - 1)].pontos, lista_jogadores[abs(num_jogador - 1)].jogos]

            for j in range(quantidade_jogadores):                  #alterar os dados do vencedor na lista do programa
                if info_vencedor[0] in lista_jogadores_completa[j]:
                    lista_jogadores_completa[j] = info_vencedor  

            for j in range(quantidade_jogadores):                  #alterar os dados do perdedor na lista do programa
                if info_perdedor[0] in lista_jogadores_completa[j]:
                    lista_jogadores_completa[j] = info_perdedor
            i = 10

        if i == 9:
            lista_jogadores[num_jogador].pontos += 1
            lista_jogadores[num_jogador].jogos += 1
            info_empate = [lista_jogadores[num_jogador].nome, lista_jogadores[num_jogador].token,lista_jogadores[num_jogador].pontos, lista_jogadores[num_jogador].jogos]

            for j in range(quantidade_jogadores):
                if lista_jogadores[num_jogador].nome in lista_jogadores_completa[j]:
                     lista_jogadores_completa[j] = info_empate
            lista_jogadores[abs(num_jogador - 1)].pontos += 1
            lista_jogadores[abs(num_jogador - 1)].jogos += 1
            info_empate = [lista_jogadores[abs(num_jogador - 1)].nome, lista_jogadores[abs(num_jogador - 1)].token, lista_jogadores[abs(num_jogador - 1)].pontos, lista_jogadores[abs(num_jogador - 1)].jogos]

            for j in range(quantidade_jogadores):
                if lista_jogadores[abs(num_jogador - 1)].nome in lista_jogadores_completa[j]:
                     lista_jogadores_completa[j] = info_empate
            print("O jogo terminou num empate")

        num_jogador -= 1        #ir para o outro jogador    

    editar_jogador(caminho_ficheiro, lista_jogadores_completa)      #alterar os dados do vencedor no ficheiro data.csv

    lista_jogadores_completa = lista_jogadores_csv(caminho_ficheiro)    #atualizar a lista de jogadores completa

    mensagem_menu = "\nPara visualizar o ranking, prima 1\nPara recomecar outro jogo, prima 2\nPara sair do jogo, prima 3"   #mensagem personalizada para o menu(recomecar)
    jogar = menu(mensagem_menu)