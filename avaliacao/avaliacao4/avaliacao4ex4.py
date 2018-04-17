#de 0 a z

def seq(num):
    
    if num > 0:
        
        seq(num - 1)
        
    if num >= 0:  
        print(num)

num = int(input("Numero desejado: "))
seq(num)