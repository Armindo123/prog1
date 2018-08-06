#ler e organizar numeros de um ficheiro random

def sort(numeros):          #ordenar crescentemente
    if len(numeros) > 1:
        mid = int(len(numeros)/2)
        left = numeros[:mid]
        right = numeros[mid:]
        # Split
        sort(left)
        sort(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numeros[k] = left[i]
                i += 1
            else:
                numeros[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            numeros[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            numeros[k] = right[j]
            j += 1
            k += 1

ficheiro = open("rand_num.txt", "r")   #apenas e preciso ler o ficheiro

numeros = []                #lista que vai conter os numeros do ficheiro rand_num.txt

for linha in ficheiro.readlines():    #Este ciclo encontra-se antes de uma funcao apenas para poder fechar o ficheiro "rand_num.txt" o mais cedo possivel
    #print(linha)            caso seja preciso verificar imprimir lista original linha a linha
    numeros.append(int(linha))   #adicionar cada linha à lista de numeros

ficheiro.close()

total = len(numeros)        #criou-se esta variavel para nao diminuir a quantidade de operacoes necessarias
indice_maximo = total - 1   #criou-se esta variavel para nao diminuir a quantidade de operacoes necessarias

sort(numeros)               #ordenar crescente

for i in numeros:           #imprimir cada numero numa linha diferente
    print(i)

print("")

for i in range(indice_maximo, -1, -1):      #trocar a ordem para decrescente
    print(numeros[i])