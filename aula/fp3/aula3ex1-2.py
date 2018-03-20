#apresentar valores num intervalo introduzido

inicio = int(input("Introduza o primeiro valor: "))
fim = int(input("Introduza o ultimo valor: "))
fim += 1

for i in range(inicio, fim, 1):
    print(i, end=" ")