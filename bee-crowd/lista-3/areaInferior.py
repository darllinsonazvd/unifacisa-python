matriz = []
operacao = input()

for i in range(12):
    matriz.append([])

    for j in range(12):
        num = float(input())
        matriz[i].append(num)

soma = 0
inf = 5
sup = 7
cont = 0

for i in range(7, 12):
    for j in range(inf, sup):
        soma += matriz[i][j]
        cont += 1
    inf -= 1
    sup += 1

media = soma / cont

if operacao == "S":
    print("%.1f" % soma)
else:
    print("%.1f" % media)
