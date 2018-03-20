#apresentar os valores num intervalo escolhido com saltos escolhidos

fim = int(input("Valor final do intervalo: "))
incremento = int(input("Incremento escolhido: "))

fim += 1
for i in range(0, fim, incremento):
    print(i, end=" ")