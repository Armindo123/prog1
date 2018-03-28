#indicar par ou impar

numero = int(input("Introduza um numero inteiro: "))

if numero%2 == 0:
    print("{} e par".format(numero))
else:
    print("{} e impar".format(numero))