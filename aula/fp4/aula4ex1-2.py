#calculadora

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

x = float(input("Introduza o primeiro valor: "))
operacao = input("Introduza uma operacao (+ - * /)")
y = float(input("Introduza o segundo valor: "))


if operacao == "+":
    resultado = soma(x, y)
    print(resultado)
elif operacao == "-":
    resultado = subtracao(x, y)
    print(resultado)
elif operacao == "*":
    resultado = multiplicacao(x, y)
    print(resultado)
elif operacao == "/":
    resultado = divisao(x, y)
    print(resultado)
else:
    print("Introduza uma das operacoes apresentadas.")