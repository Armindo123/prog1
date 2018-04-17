#de 0 a z

def seq(num, ordem):
    
    if num >= 0: #criterio de paragem
        if ordem == "crescente":
            seq(num - 1, ordem)    
        
            print(num)
        elif ordem == "decrescente":
            print(num)
            seq(num - 1, ordem)

num = int(input("Numero desejado: "))
ordem = str(input("Ordem (crescente ou decrescente): "))
seq(num, ordem)