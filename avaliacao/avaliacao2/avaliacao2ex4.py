#verificar se o numero e divisivel por 3 e 5 ao mesmo tempo

numero = int(input("Introduza um numero inteiro: "))

if numero%3 == 0 and numero%5 == 0:
    print("{} e simultaneamente divisivel por 3 e 5".format(numero))
else:
    print("{} nao e simultaneamente divisivel por 3 e 5".format(numero))