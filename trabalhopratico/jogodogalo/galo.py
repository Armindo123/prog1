__author__ = 'André'

class Tabuleiro():
    def __init__(self): #Todos os campos possiveis de jogar no tabuleiro
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self): #Basicamente o que estou a fazer é criar os espaços onde poderemos jogar
        print (" %s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, jogador):
        if self.cells[cell_no] == " ":
           self.cells[cell_no] = jogador
        else:
            print("Campo ja ocupado.")

tabuleiro = Tabuleiro()

def print_header(): # O print_header é para dar um título inicial ao jogo (Introdução)
    print (" Bem-Vindos ao jogo do galo \n")

def refresh_screen():
    #preciso de uma especie de clear para apagar o que esta antes
    tabuleiro.display() # Mostrar o Tabuleiro

def ver(choice):
    if (tabuleiro.cells[1] == choice and tabuleiro.cells[2] == choice and tabuleiro.cells[3] == choice) or \
        (tabuleiro.cells[4] == choice and tabuleiro.cells[5] == choice and tabuleiro.cells[6] == choice) or \
        (tabuleiro.cells[7] == choice and tabuleiro.cells[8] == choice and tabuleiro.cells[9] == choice) or \
        (tabuleiro.cells[1] == choice and tabuleiro.cells[4] == choice and tabuleiro.cells[7] == choice) or \
        (tabuleiro.cells[2] == choice and tabuleiro.cells[5] == choice and tabuleiro.cells[8] == choice) or \
        (tabuleiro.cells[3] == choice and tabuleiro.cells[6] == choice and tabuleiro.cells[9] == choice) or \
        (tabuleiro.cells[1] == choice and tabuleiro.cells[5] == choice and tabuleiro.cells[9] == choice) or \
        (tabuleiro.cells[3] == choice and tabuleiro.cells[5] == choice and tabuleiro.cells[7] == choice):
        print("O jogador {} ganhou".format(choice))
        global play
        play = False

print_header() # dar print "chamar" a  função header

play = True

while play: # criar um loop para dar seguimento ao jogo
    refresh_screen()
    #Inserir X
    x_choice = int(input("\nX) Escolha o campo de 1 - 9. > "))
    #Atualizar Tabuleiro
    tabuleiro.update_cell(x_choice, "X")
    refresh_screen()
    ver("X")
    #Inserir O
    o_choice = int(input("\nO) Escolha o campo de  1 - 9. > "))
    #Atualizar Tabuleiro
    tabuleiro.update_cell(o_choice, "O")
    refresh_screen()
    ver("O")
