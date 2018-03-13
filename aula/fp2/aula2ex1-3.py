#calculadora de dois numeros

num1 = int(input("Introduza um numero: "))
operacao = input("Introduza que operacao deseja fazer (+ - * ou /): ").strip()
num2 = int(input("Introduza outro numero: "))


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
