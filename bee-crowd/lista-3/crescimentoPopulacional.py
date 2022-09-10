qtdTestes = int(input())
lista = []

for i in range(qtdTestes):
    cont = 0

    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    porcentoA = ((PA * G1) // 100) + PA
    porcentoB = ((PB * G2) // 100) + PB
    porcentoA = int(porcentoA)
    porcentoB = int(porcentoB)

    while porcentoA <= porcentoB:
        porcentoA = ((porcentoA * G1) // 100) + porcentoA
        porcentoB = ((porcentoB * G2) // 100) + porcentoB
        cont += 1

        if cont > 100:
            break

    cont += 1
    lista.append(cont)

for i in range(qtdTestes):
    if lista[i] > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % lista[i])
