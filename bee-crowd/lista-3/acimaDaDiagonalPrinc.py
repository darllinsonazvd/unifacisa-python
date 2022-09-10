operacao = input()
matriz = []

for i in range(12):
    matriz.append([])

    for j in range(12):
        num = float(input())
        matriz[i].append(num)

if operacao == "S":
    soma = 0
    cont = 1

    for i in range(0, 11):
        for j in range(cont, 12):
            soma += matriz[i][j]
        cont += 1
    print("%.1f" % soma)
elif operacao == "M":
    soma = 0
    cont = 1
    cont2 = 0

    for i in range(0, 11):
        for j in range(cont, 12):
            soma += matriz[i][j]
            cont2 += 1
        cont += 1

    media = soma / cont2
    print("%.1f" % media)
