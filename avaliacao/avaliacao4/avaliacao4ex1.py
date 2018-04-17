#funcao para log in

def username(username1):
    for a in range(1, 4):
        
        defaultusername = "defaultusername"
        if username1 == defaultusername:
            password(password1)
            break
        else:
            print("Username errado.")
            if a == 3:
                print("Tentativas esgotadas")

def password(password1):
    for b in range(1,4):

        defaultpassword = "defaultpassword"
        if password1 == defaultpassword:
            print("Login efetuado com sucesso")
            break
        else:
            print("Password errada.")
            if b == 3:
                print("Tentativas esgotadas")

username1 = input("Introduza o seu username: ")
password1 = input("Introduza a sua password: ")


username(username1)

