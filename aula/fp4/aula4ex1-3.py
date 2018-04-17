

def lerinteiro(min, max):
    valor = min - 1
    while valor < min or valor > max:
        valor = int(input("insira um valor"))
    return valor

num = lerinteiro(0, 20)

print(num)