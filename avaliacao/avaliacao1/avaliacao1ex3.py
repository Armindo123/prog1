#calcular imc

massa = float(input("Massa (Kg): "))
altura = float(input("Altura (cm): "))

alturametros = altura / 100

imc = massa / (alturametros ** 2)
print("O seu IMC corresponde a: {0:.2f}".format(imc))