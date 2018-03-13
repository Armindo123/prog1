#maior de dois numeros inteiros
print("Indique dois numeros separados por um espaco")
num1, num2 = input("Escreva os dois numeros escolhidos: ").split()

num1 = int(num1)
num2 = int(num2)

if num1 == num2:
    print("Os numeros introduzidos sao iguais; logo, nao e possivel indicar o maior.")
elif num1 > num2:
    print("O maior numero e: ", num1)
else:
    print("O maior numero e: ", num2)