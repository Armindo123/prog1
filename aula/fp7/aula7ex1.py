#class aluno

class Aluno():
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome.title()
    
    def e_igual(self, aluno):
        return self.numero == aluno.numero

    def __str__(self):
        return "\nNumero: {}\nNome: {}".format(self.numero, self.nome)


if __name__ == "__main__":
    A1 = Aluno(1, "teste a")
    print(A1)

    B2 = Aluno(2, "teste b")
    print(B2)


