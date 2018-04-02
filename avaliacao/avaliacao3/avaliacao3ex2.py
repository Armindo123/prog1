#Descobrir se e numero primo

numero = int(input("Introduza um numero inteiro: "))

for n in range(2, numero, 1):
    if numero % n == 0:
        print("O numero {} nao e primo".format(numero))
        break
else:
    print("O numero {} e primo".format(numero))