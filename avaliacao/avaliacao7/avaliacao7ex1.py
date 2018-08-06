#criar lista numeros random

from random import randint

INICIO = 1
FIM = 101
ALCANCE = 31

ficheiro = open("avaliacao/avaliacao7/rand_num.txt", "a")

for _ in range(ALCANCE):
    num_random = randint(INICIO, FIM)
    print(num_random)
    num_random = str(num_random) + "\n"
    ficheiro.write(num_random)

ficheiro.close()