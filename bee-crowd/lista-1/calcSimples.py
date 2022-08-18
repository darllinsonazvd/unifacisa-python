entrada1 = input().split()
entrada2 = input().split()

codP1, qtdP1, valP1 = int(entrada1[0]), int(entrada1[1]), float(entrada1[2])
codP2, qtdP2, valP2 = int(entrada2[0]), int(entrada2[1]), float(entrada2[2])

precoP1 = qtdP1 * valP1
precoP2 = qtdP2 * valP2

valorTotal = precoP1 + precoP2

print("VALOR A PAGAR: R$ %.2f" % valorTotal)
