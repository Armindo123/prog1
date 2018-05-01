#lista com 10 caracteres e verificar

def localizar(lista, escolha):          #funcao para criar uma lista com as posicoes em que o caracter escolhido se repete
    for i in range(len(lista)):         #aproveitar a quantidade de dados em vez dos dados
        if lista[i] == escolha:
            listaEscolhida.append(i)

lista = []
listaEscolhida = []

for _ in range(10):                                     #input fora da funcao e utilizei "_" porque nao preciso da variavel
    lista.append(input("Introduza um caracter: "))      #criar a lista

escolha = input("Escolha um caracter para localizar: ") 

localizar(lista, escolha)                               #chamar a funcao

qnt = len(listaEscolhida)                               #criar uma variavel com o tamanho da lista para saber quantas vezes se repete o caracter

if qnt == 0:                                            #saber se o caracter apareceu e formatar o texto conforme o resultado
    print("Error 404: character not found.")
elif qnt == 1:
    print("O caracter \"{}\" apareceu {} vez nas posicoes: {}".format(escolha, qnt, listaEscolhida))
else:
    print("O caracter \"{}\" apareceu {} vezes nas posicoes: {}".format(escolha, qnt, listaEscolhida))