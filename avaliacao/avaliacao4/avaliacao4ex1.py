#funcao para log in

def username():
    for a in range(1, 4):
        
        defaultusername = "defaultusername"
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

        defaultpassword = "defaultpassword"
        password1 = input("Introduza a sua password: ")
        if password1 == defaultpassword:
            print("Login efetuado com sucesso")
            break
        else:
            print("Password errada.")
            if b == 3:
                print("Tentativas esgotadas")



username()

