#par ou impar numa lista

def lista():
    for _ in range(1,11):
        num = int(input("Introduza um numero: "))
        numeros.append(num)
    escolha = str(input("Apresentar apenas Pares ou Impares(P ou I): "))
    if escolha == "P":
        par()
    elif escolha == "I":
        impar()
    else:
        print("Introduziu mal a escolha")

def par():
    for i in numeros:
        if i % 2 == 0:
            print(i)

def impar():
    for i in numeros:
        if i % 2 != 0:
            print(i)


numeros = []
lista()