#grafico 2d

x, y = input("Introduza as coordenadas de um ponto (X-Y)").split("-")
x = int(x)
y = int(y)

if x == 0 and y == 0:
    print("O ponto localiza-se na origem do referencial")
elif x == 0:
    print("O ponto encontra-se no eixo das ordenadas")
elif  y == 0:
    print("O ponto encontra-se no eixo das abcissas")
elif x > 0 and y > 0:
    print("O ponto esta no primeiro quadrante")
elif x < 0 and y > 0:
    print("O ponto esta no segundo quadrante")
elif x < 0 and y < 0:
    print("O ponto esta no terceiro quadrante")
elif x > 0 and y < 0:
    print("o ponto ensta no quarto quadrante")
