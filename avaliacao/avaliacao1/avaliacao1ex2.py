#converter de graus farhenheit para graus celsius

farhenheit = float(input("Introduza uma temperatura em graus Farhenheit: "))

celsius = (farhenheit - 32) * (5 / 9)

print("A conversao de {0} graus farhenheit para graus celsius corresponde a: {1:.3f}".format(farhenheit, celsius))
