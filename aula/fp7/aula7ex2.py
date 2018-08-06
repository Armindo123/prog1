#class Turma
from aula7ex1 import Aluno

class Turma():
    def __init__(self, nome, anoLetivo):
        self.turma_nome = nome
        self.ano = anoLetivo
        self.lista_alunos = []
        self.quantidade_alunos = 0
    
    def existe_aluno(self, aluno):
        for i in range(self.quantidade_alunos):
            if self.lista_alunos[i].e_igual(aluno):
                return True
        return False

    def adicionar_aluno(self, aluno):
        if not self.existe_aluno(aluno):
            self.lista_alunos.append(aluno)
            self.quantidade_alunos += 1
            return True
        return False
    
    def mostrar_alunos(self):
        listarAlunos = ""
        for aluno in self.lista_alunos:
            listarAlunos += str(aluno) + "\n"
        return listarAlunos
    
    def __str__(self):
        return "Nome da turma: {}\nAno letivo: {}\nNumero de alunos: {}\nLista de alunos: {}".format(self.turma_nome, self.ano, self.quantidade_alunos, self.mostrar_alunos())

            


if __name__ == "__main__":
    turma1 = Turma("CRSI1", 2018)
    A1 = Aluno(1, "teste A")
    B2 = Aluno(2, "teste B")
    print("\nAdicionar aluno A1")
    existe = turma1.adicionar_aluno(A1)
    if existe == False:
        print("O aluno ja existe na turma")
    else:
        print("Aluno adicionado")

    print("\nAdicionar aluno A1")
    existe = turma1.adicionar_aluno(A1)
    if existe == False:
        print("O aluno ja existe na turma")
    else:
        print("Aluno adicionado")

    print("\nAdicionar aluno B2")
    existe = turma1.adicionar_aluno(B2)
    if existe == False:
        print("O aluno ja existe na turma")
    else:
        print("Aluno adicionado")

    turma1.mostrar_alunos()
    print(turma1.mostrar_alunos())
    print(turma1)