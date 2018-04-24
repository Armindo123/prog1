#gerir alunos

class Data():
    def __init__ (self, dia, mes, ano):
        self.valid = True
        self.dia = dia
        self.mes = mes
        self.ano = ano
        if isinstance(dia, str) or isinstance(mes, str) or isinstance(ano, str):
            self.valid = False
        elif dia < 0 or dia > 32 or mes < 0 or mes > 13 or ano < 1900 or ano > 2017:
            self.valid = False
    def __str__ (self):
        if self.valid == True:
            return "Data de aniversario {}/{}/{}".format(self.dia, self.mes, self.ano)
        return "Data invalida"

class Aluno():
    def __init__ (self, numero, nome, data):
        self.numero = numero
        self.nome = nome
        self.data = data
        self.nota = 0
        self.qnt = 0
        self.media = 0
    
    def addnota(self, nota):
        self.nota += nota
        self.qnt += 1
    def final(self):
        self.media = self.nota / self.qnt


    def __str__ (self):
        return "Numero: {}\nNome: {}\nData: {}".format(self.numero, self.nome, self.data)







d1 = Data(1, 1, 2000)
d2 = Data(5, 5, "199etrocaopasso")
aluno1 = Aluno(8170000, "Luis", d1)
aluno1.addnota(15)
aluno1.addnota(20)
aluno1.final()

print(aluno1.nota)
print(aluno1.media)

aluno2 = Aluno(8170201, "Antonio", d2)
print(d1)
print(aluno1)
print("\n")
print(d2)
print(aluno2)

