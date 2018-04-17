#conversao E-D D-E

def currency(a, b):
    
    a = float(a)
    b = str(b)
    if b == "D":
        convertorDE(a)
        print("{} Dolars correspondem a {} Euros".format(a, convertorDE(a)))
    elif b == "E":
        convertorED(a)
        print("{} Euros correspondem a {} Dolars".format(a, convertorED(a)))


def convertorDE(a):
            return a / 1.23785


def convertorED(a):
            return a / 0.807852325

a = input("Introduza uma quantia : ")
b = input("Introduza D ou E (Dolar ou Euro):  ")
currency(a, b)