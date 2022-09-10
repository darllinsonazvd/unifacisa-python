matriz = []
operacao = input()

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

soma = 0
cont1 = 0
cont2 = 0

for i in range(11, 0, -1):
    cont1 += 1

    for j in range(cont1, 12):
        soma += matriz[i][j]
        cont2 += 1

if operacao == "S":
    print("%.1f" % soma)
elif operacao == "M":
    media = soma / cont2
    print("%.1f" % media)
