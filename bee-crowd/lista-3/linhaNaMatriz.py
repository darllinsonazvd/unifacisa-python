linha = int(input())
operacao = input()

matriz = []

for i in range(12):
    matriz.append([])

for i in range(12):
    for j in range(12):
        num = float(input())
        matriz[i].append(num)

if operacao == "S":
    soma = 0

    for elm in matriz[linha]:
        soma += elm

    print(soma)
elif operacao == "M":
    media = 0
    soma = 0

    for elm in matriz[linha]:
        soma += elm

    media = soma / 12
    print(media)
