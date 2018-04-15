#de 0 a z

def seq(num, z):
    
    if num > 0:
        
        print(z)
        z += 1
        num -= 1
        seq(num, z)
    elif num < 0:
        print(z)
        z -= 1
        num += 1
        seq(num, z)
        
    else: print(z)
    

z = 0

num = int(input("Numero desejado: "))
seq(num, z)