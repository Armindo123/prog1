#emails

from random import randint
import time
import re
def validaremail(stringlonga):
    if len(stringlonga) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", stringlonga) != None:
            return True
        return False
    if validaremail("my.email@gmail.com") == True :
        print("This is a valid email address")
    else:
        print("This is not a valid email address")

class User():
    def __init__(self, nome, email, password, identificador, bloqueador, secreta, criacao):
        self.nome = nome
        self.email = email
        self.password = password
        self.id = identificador
        self.blocker = bloqueador
        self.secret = secreta
        self.creationdate = criacao
    
    def loginsys(self):
        if self.blocker == False:
            if tryemail == self.email and trypassword == self.password:
                tries = 3
                return "Log in efetuado com sucesso."
            else:
                tries +=1
                return "E-mail ou palavra passe errada."
        else:
            if trysecreta == self.secret:
                self.blocker = False
                return "Conta desbloqueada"
            





a = str(input(print("Introduza o seu nome: ")))
b = str(input(print("Introduza o seu email: ")))
c = str(input(print("Introduza a sua palavra-passe: ")))
d = str("{}-{}".format(randint(100, 999),randint(1000, 9999)))
e = False
f = str(input(print("Introduza a sua resposta secreta: ")))
g = str(time.strftime("%d/%m/%Y"))


tries = 0
user1 = User(a, b, c, d, e, f, g)


while tries < 3:
    tryemail = str(input("E-mail: "))
    trypassword = str(input("Palavra passe: "))
    user1.loginsys()
    print(user1.loginsys())
else:
    e = True
    tries = 0
    trysecreta = str(input("Resposta secreta: "))
    user1.loginsys()
    print(user1.loginsys())

a = str(input(print("Introduza o seu nome")))
b = str(input(print("Introduza o seu email")))
c = str(input(print("Introduza a sua palavra-passe")))
d = str("{}-{}".format(randint(100, 999),randint(1000, 9999)))
e = False
f = str(input(print("Introduza a sua resposta secreta")))
g = str(time.strftime("%d/%m/%Y"))

user2 = User(a, b, c, d, e, f, g)