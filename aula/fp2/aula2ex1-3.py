#calculadora de dois numeros

num1 = int(input("Introduza um numero: "))
num2 = int(input("Introduza outro numero: "))
operacao = input("Introduza que operacao deseja fazer (+ - * ou /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Nao introduziu a operacao de forma correta")
