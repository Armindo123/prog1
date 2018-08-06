#funcao para log in

def username():
    for a in range(1, 4):
        
        defaultusername = "defaultusername"                     #o input foi feito dentro da funcao para que seja possivel saber se o erro esta no username ou na password e para poder comecar por chamar a funcao
        username1 = input("Introduza o seu username: ")
        if username1 == defaultusername:
            password()
            break
        else:
            print("Username errado.")
            if a == 3:
                print("Tentativas esgotadas")

def password():
    for b in range(1,4): 
       
        defaultpassword = "defaultpassword"                     #o input foi feito dentro da funcao para que seja possivel saber se o erro esta no username ou na password e para poder comecar por chamar a funcao
        password1 = input("Introduza a sua password: ")
       
        if password1 == defaultpassword:
            print("Login efetuado com sucesso")
            break
        else:
            print("Password errada.")
            if b == 3:
                print("Tentativas esgotadas")

username()

