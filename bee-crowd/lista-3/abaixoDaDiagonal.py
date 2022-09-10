matriz = []
operacao = input()

for i in range(12):
    matriz.append([])

    for j in range(12):
        x = float(input())
        matriz[i].append(x)

if operacao == "S":
    soma = 0
    cont = 11
    for i in range(11, 0, -1):
        for j in range(0, cont):
            soma += matriz[i][j]
        cont -= 1
    print("%.1f" % soma)
elif operacao == "M":
    soma = 0
    cont = 11
    cont2 = 0
    for i in range(11, 0, -1):
        for j in range(0, cont):
            soma += matriz[i][j]
            cont2 += 1
        cont -= 1

    media = soma / (cont2)
    print("%.1f" % media)
