#ordenar dois valores do maior para menor

num1, num2 = input("Indique dois numeros separados por um espaco: ").split()

num1 = int(num1)
num2 = int(num2)

if num1 == num2:
    print("Os numeros ssao iguais; nao e possivel apresentar ordem do maior para o menor")
elif num1 > num2:
    print(num1, num2)
else:
    print(num2, num1)
