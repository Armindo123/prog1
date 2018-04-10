#funcao para log in

def username():
    for a in range(1, 4):
        
        default1 = "abc"
        username1 = input("Introduza o seu username: ")
        if username1 == default1:
            print("Parabens")
        else:
            
            if a == 3:
                print("Tentativas esgotadas")


username()

