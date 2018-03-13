#media de 5 valores
valor1 = float(input("Introduza o valor 1: "))
valor2 = float(input("Introduza o valor 2: "))
valor3 = float(input("Introduza o valor 3: "))
valor4 = float(input("Introduza o valor 4: "))
valor5 = float(input("Introduza o valor 5: "))

media = (valor1+valor2+valor3+valor4+valor5)/5
modulo = (valor1+valor2+valor3+valor4+valor5)%5
print("A media é: ", media)
print("O modulo é: ", modulo)