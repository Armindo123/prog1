#calculo da media ponderada

nota1 = float(input("Nota numero 1: "))
nota2 = float(input("Nota numero 2: "))
nota3 = float(input("Nota numero 3: "))


#print(nota1)
#print(nota2)
#print(nota3)


if nota1 > 20 or nota2 > 20 or nota3 >20:
    print("Por favor introduza numeros entre 0 e 20")
elif nota1 < 0 or nota2 < 0 or nota3 < 0:
    print("Por favor introduza numeros entre 0 e 20")
else:
    nota1final = nota1 * 0.25
    nota2final = nota2 * 0.35
    nota3final = nota3 * 0.40
    media = nota1final + nota2final + nota3final
    print("A media corresponde a: {}".format(media))





