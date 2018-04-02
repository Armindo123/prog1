#imprimir 5 numeros anteriores e seguintes

numero = int(input("Introduza um numero inteiro: "))

for n in range(numero - 5, numero + 6):
    print(n)