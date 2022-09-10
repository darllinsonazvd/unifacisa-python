operacao = input()

soma = 0
cOut = 0
cIn = 11
qtd = 0

naoEntra = cOut
entra = cIn

for i in range(144):
    num = float(input())

    if entra > 0:
        entra -= 1
        soma += num
        qtd += 1
        continue

    if naoEntra > 0:
        naoEntra -= 1
        continue

    if naoEntra + entra == 0:
        cOut += 1
        cIn -= 1
        naoEntra = cOut
        entra = cIn

if operacao == "S":
    print("%.1f" % soma)
elif operacao == "M":
    print("%.1f" % (soma / float(qtd)))
