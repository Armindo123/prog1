#Sistema de votos


menos1= False
branco = 0
numerovoto1 = 0
numerovoto2 = 0
numerovoto3 = 0
numerovoto4 = 0
nulo = 0

while not menos1:
    codigo = int(input("Codigo do voto: "))
    if codigo != -1:
        if  codigo == 0:
            branco += 1
        if codigo == 1:
            numerovoto1 += 1
        if codigo == 2:
            numerovoto2 += 1
        if codigo == 3:
            numerovoto3 += 1
        if codigo == 4:
            numerovoto4 += 1
        if codigo == 9:
            nulo += 1
    else:
        numerovotos = numerovoto1 + numerovoto2 + numerovoto3 + numerovoto4 + branco + nulo
        print("Numero de votos: {}".format(numerovotos))
        print("Numero de votos do candidato 1: {}".format(numerovoto1))
        print("Numero de votos do candidato 2: {}".format(numerovoto2))
        print("Numero de votos do candidato 3: {}".format(numerovoto3))
        print("Numero de votos do candidato 4: {}".format(numerovoto4))
        print("Votos nulos: {}".format(nulo))
        print("Votos branco: {}".format(branco))
        percentagem1 = (numerovoto1 / numerovotos)*100 
        print("Percentagem de votos do candidato 1: {}%".format(percentagem1))
        percentagem2 = (numerovoto2 / numerovotos)*100 
        print("Percentagem de votos do candidato 2: {}%".format(percentagem2))
        percentagem3 = (numerovoto3 / numerovotos)*100 
        print("Percentagem de votos do candidato 3: {}%".format(percentagem3))
        percentagem4 = (numerovoto4 / numerovotos)*100 
        print("Percentagem de votos do candidato 4: {}%".format(percentagem4))
        percentagembranco = (branco / numerovotos)*100 
        print("Percentagem de votos do candidato branco: {}%".format(percentagembranco))
        percentagemnulo = (nulo / numerovotos)*100 
        print("Percentagem de votos do candidato nulo: {}%".format(percentagemnulo))
        menos1 = True

