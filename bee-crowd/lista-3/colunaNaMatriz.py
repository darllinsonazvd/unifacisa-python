col = int(input())
operacao = input()

matriz = []

for i in range(12):
    matriz.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

if operacao == "S":
    soma = 0

    for linha in range(12):
        soma += matriz[linha][col]
    print(soma)
elif operacao == "M":
    med = 0
    soma = 0

    for linha in range(12):
        soma += matriz[linha][col]
    med = soma / 12
    print("{:.1f}".format(med))
