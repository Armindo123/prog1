#lista com 10 numeros ou ate -1

list = []
total = 0

for i in range(1, 11):
    num = int(input("Numero escolhido para a media: "))
    if num == -1 or i == 10:
        total += num
        media = total / (i)
        print(media)
        break
    else:
        total += num
        list.append(num)