operacao = input()

soma = 0
cOut = 12
cIn = 0
mudar = False

qtd = 0
naoEntra = cOut
entra = cIn

for i in range(144):
    valor = float(input())

    if mudar:
        if naoEntra + entra == 0:
            cOut += 1
            cIn -= 1
            naoEntra = cOut
            entra = cIn

        if entra > 0:
            entra -= 1
            soma += valor
            qtd += 1
            continue

        if naoEntra > 0:
            naoEntra -= 1
            continue
    else:
        if naoEntra + entra == 0:
            cOut -= 1
            cIn += 1
            naoEntra = cOut
            entra = cIn

        if entra > 0:
            if entra == 6:
                mudar = True
                entra -= 1
                naoEntra += 1
                cIn -= 1
                cOut += 1

            entra -= 1
            soma += valor
            qtd += 1
            continue

        if naoEntra > 0:
            naoEntra -= 1
            continue

if operacao == "S":
    print("%.1f" % soma)
elif operacao == "M":
    print("%.1f" % (soma / float(qtd)))
