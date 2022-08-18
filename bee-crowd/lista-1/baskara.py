from math import sqrt

valores = input().split()

a, b, c = float(valores[0]), float(valores[1]), float(valores[2])

delta = b**2 - 4 * a * c

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
