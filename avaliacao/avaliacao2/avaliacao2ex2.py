#ordenar 3 valores do maior para o menor

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
valor3 = float(input("Valor 3: "))


if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("Introduza valores diferentes")
elif valor1 > valor2 and valor2 > valor3:
    print("{} > {} > {}".format(valor1, valor2, valor3))
elif valor1 > valor2 and valor3 > valor2:
    print("{} > {} > {}".format(valor1, valor3, valor2))
elif valor2 > valor3 and valor1 > valor3:
    print("{} > {} > {}".format(valor2, valor1, valor3))
elif valor2 > valor3 and valor3 > valor1:
    print("{} > {} > {}".format(valor2, valor3, valor1))
elif valor3 > valor1 and valor1 > valor2:
    print("{} > {} > {}".format(valor3, valor1, valor2))
else:
    print("{} > {} > {}".format(valor3, valor2, valor1))


