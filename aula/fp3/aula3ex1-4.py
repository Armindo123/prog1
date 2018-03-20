#tabuada de um numero introduzido

tabuadanumero = int(input("Tabuada do numero: "))
for i in range(1, 11):
    resultado = tabuadanumero * i
    print("{} x {} = {}".format(tabuadanumero, i, resultado))