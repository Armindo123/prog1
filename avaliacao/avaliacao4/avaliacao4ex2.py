#conversao E-D D-E

def currency():
    a, b = input("Introduza uma quantia e D ou E separando com um espaco: ").split()
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


currency()